from pygame import mixer
from datetime import datetime
import time
def time_stamp():
    return datetime.now().strftime("%Y-%m-%d [%H:%M:%S]")

def logBook(user_input,time_stamp):
    with open("Programer.txt","a") as f:
        f.write(f"{time_stamp}: {user_input}\n")
        f.close()

def music_player(file_name, stopper):
    mixer.init()
    mixer.music.load(file_name)
    mixer.music.play()
    while True:
        user = input(f"Enter \"{stopper}\" to stop the music: ")
        if user == stopper:
            mixer.music.stop()
            stamp=time_stamp()
            logBook(user,stamp)
            break


if __name__ == '__main__':
    working_time=int(datetime.now().strftime('%H'))
    drinking = 60 * 30
    eyes = 60 * 40
    exercise = 60 * 50
    drinking_now=time.time()
    eyes_now=time.time()
    exercise_now=time.time()
    while 9<working_time<24:
        if time.time()-drinking_now>5:
            music_player('song_name.mp3',"drinking done" )
            drinking_now=time.time()

        elif time.time()-eyes_now>10:
            music_player('song_name.mp3',"eyes done" )
            eyes_now=time.time()

        elif time.time()-exercise_now>exercise:
            music_player('song_name.mp3',"exercise done" )
            exercise_now=time.time()