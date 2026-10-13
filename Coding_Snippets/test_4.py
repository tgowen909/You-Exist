from threading import Thread
from time import sleep
from pydub import AudioSegment
from pydub.playback import play


def threaded_function():
    sfx = AudioSegment.from_mp3("Audio/Crazy_Dave.mp3")
    play(sfx)


#if __name__ == "__main__": -> dunno what this shit does
thread = Thread(target = threaded_function)
thread.start()
#thread.join() -> .join makes it wait until the thread is finished (BAD)
print("thread finished...exiting")