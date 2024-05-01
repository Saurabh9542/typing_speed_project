from time import *
import random as rd


def mistake(sentece, userInp):
    mistakes = 0

    for i in range(len(sentece)):
        try:
            if sentece[i] != userInp[i]:
                mistakes += 1
        except:
            mistakes += 1
    return mistakes


def speed_time(time_strt, time_end, userInp):
    time_delay = time_end - time_strt
    time_r = round(time_delay, 2)
    speed = len(userInp)/time_r
    return round(speed)



sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Tomorrow is another day.",
    "The sun sets in the west.",
    "Time flies when you're having fun.",
    "Practice makes perfect.",
    "Life is like a box of chocolates, you never know what you're gonna get.",
    "Beauty is in the eye of the beholder.",
    "All that glitters is not gold.",
    "Two wrongs don't make a right.",
    "Actions speak louder than words.",
    "A journey of a thousand miles begins with a single step.",
    "The early bird catches the worm.",
    "Laughter is the best medicine.",
    "Love conquers all.",
    "Rome wasn't built in a day."
]

display = rd.choice(sentences)

print(" CHECK YOUR TYPING SPEED HERE!")

print(display)
print()
print()

starting_time = time()
inp = input("Enter your sentence : ")
ending_time = time()

print("number of errors ", mistake(display, inp))
print("Speed : ", speed_time(starting_time, ending_time, inp), "w/s")
