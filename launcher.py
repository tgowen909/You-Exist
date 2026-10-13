# ============================================================
#  You Exist launcher
#  1. Checks GitHub for the latest version of the game.
#  2. Downloads only the files that have changed since last time.
#  3. Runs the game.
#  If there's no internet, it runs the last version it downloaded
#  (or, on the very first launch, the copy packed inside the app).
# ============================================================

GITHUB_USER = "tgowen909"
GITHUB_REPO = "You-Exist"
BRANCH = "main"

import os
import sys
import ssl
import json
import shutil
import hashlib
import tempfile
import runpy
import urllib.request
import urllib.parse

# ---- Libraries the game uses ----
# The launcher doesn't use these itself. Importing them here is what makes
# PyInstaller pack them into the app, so the downloaded game code can use them.
# If the game ever starts using a NEW library, add it here and rebuild the app.
import __future__
import subprocess, time, random, signal, readline, math, textwrap
import re, builtins, platform, threading
import termcolor
import pynput.keyboard
from aquaui.notification.native_notification import Notification
try:
    import certifi   # lets the app make secure connections on any Mac
except ImportError:
    certifi = None

# Where downloaded game files are kept on each player's Mac
SAVE_FOLDER = os.path.expanduser("~/Library/Application Support/You Exist")
GAME_FOLDER = os.path.join(SAVE_FOLDER, "game")
VERSION_FILE = os.path.join(SAVE_FOLDER, "version.txt")   # remembers which version is installed

API = f"https://api.github.com/repos/{GITHUB_USER}/{GITHUB_REPO}"
SSL_CONTEXT = ssl.create_default_context(cafile=certifi.where() if certifi else None)
SKIP = {"__pycache__", ".DS_Store"}   # files the launcher never touches


def fetch(url, timeout=8):
    request = urllib.request.Request(url, headers={"User-Agent": "You-Exist-launcher"})
    with urllib.request.urlopen(request, timeout=timeout, context=SSL_CONTEXT) as response:
        return response.read()


def git_hash(data):
    # The same fingerprint GitHub uses for every file, so files can be compared without downloading them
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def local_hash(path):
    try:
        with open(path, "rb") as f:
            return git_hash(f.read())
    except OSError:
        return None


def read_installed_version():
    try:
        with open(VERSION_FILE) as f:
            return f.read().strip()
    except OSError:
        return None


def copy_bundled_game():
    """First launch of the built app: start from the copy packed inside it,
    so only files changed since the app was built need downloading."""
    if getattr(sys, "frozen", False) and not os.path.exists(GAME_FOLDER):
        shutil.copytree(os.path.join(sys._MEIPASS, "game"), GAME_FOLDER)


def update_game():
    """Bring GAME_FOLDER up to date with GitHub. Returns True if it's now up to date."""
    print("Checking for updates...")
    try:
        os.makedirs(SAVE_FOLDER, exist_ok=True)
        copy_bundled_game()

        # 1. What's the latest version on GitHub? (one small request)
        latest = json.loads(fetch(f"{API}/commits/{BRANCH}"))
        version = latest["sha"]
        if version == read_installed_version() and os.path.exists(os.path.join(GAME_FOLDER, "You_Exist.py")):
            return True   # already up to date, nothing to download

        # 2. Get the list of every file in that version, with its fingerprint
        tree_sha = latest["commit"]["tree"]["sha"]
        tree = json.loads(fetch(f"{API}/git/trees/{tree_sha}?recursive=1"))
        remote_files = {item["path"]: item["sha"] for item in tree["tree"] if item["type"] == "blob"}
        if "You_Exist.py" not in remote_files:
            return False   # something's wrong on GitHub's end, so keep the current version

        # 3. Download only the files that are new or different, into a temporary folder first
        os.makedirs(GAME_FOLDER, exist_ok=True)
        staging = tempfile.mkdtemp(dir=SAVE_FOLDER)
        try:
            changed = [path for path, sha in remote_files.items()
                       if local_hash(os.path.join(GAME_FOLDER, path)) != sha]
            for path in changed:
                url = f"https://raw.githubusercontent.com/{GITHUB_USER}/{GITHUB_REPO}/{version}/{urllib.parse.quote(path)}"
                data = fetch(url, timeout=30)
                if git_hash(data) != remote_files[path]:
                    return False   # download got corrupted, try again next launch
                staged = os.path.join(staging, path)
                os.makedirs(os.path.dirname(staged), exist_ok=True)
                with open(staged, "wb") as f:
                    f.write(data)

            # 4. Everything downloaded fine, so move the new files into place
            for path in changed:
                target = os.path.join(GAME_FOLDER, path)
                os.makedirs(os.path.dirname(target), exist_ok=True)
                os.replace(os.path.join(staging, path), target)
        finally:
            shutil.rmtree(staging, ignore_errors=True)

        # 5. Remove files that have been deleted from GitHub
        for root, folders, files in os.walk(GAME_FOLDER):
            folders[:] = [f for f in folders if f not in SKIP]
            for name in files:
                path = os.path.relpath(os.path.join(root, name), GAME_FOLDER).replace(os.sep, "/")
                if name not in SKIP and path not in remote_files:
                    os.remove(os.path.join(root, name))

        with open(VERSION_FILE, "w") as f:
            f.write(version)
        return True

    except Exception:
        return False   # no internet, GitHub down, etc.: just use what we already have


def choose_game_folder():
    """Use the downloaded game if there is one, otherwise the copy packed in the app."""
    if os.path.exists(os.path.join(GAME_FOLDER, "You_Exist.py")):
        return GAME_FOLDER
    if getattr(sys, "frozen", False):
        return os.path.join(sys._MEIPASS, "game")        # inside the built app
    return os.path.dirname(os.path.abspath(__file__))   # running launcher.py in VS Code


update_game()
folder = choose_game_folder()
sys.path.insert(0, folder)
os.chdir(folder)
main_file = os.path.join(folder, "You_Exist.py")
sys.argv = [main_file]
runpy.run_path(main_file, run_name="__main__")
