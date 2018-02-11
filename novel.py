#!/usr/bin/python3

import sys

assert sys.version_info >= (3, 4), 'This script requires at least Python 3.4'


def read_script(loc):
    print(script[loc]["des"])
    not_num = True
    while not_num:
        print(script[loc]["choices"])
        check = input("please input the number of your chosen route")
        if check.isdigit():
            if int(check) <= len(script[loc]["choices"]):
                not_num = False
        else:
            print("invalid input")
    return script[loc]["results"][int(check) - 1]


location = "start"
script = {
    "start": {
        "des": "you find yourself in a barren wasteland.\nAs you start your normal training to defeat the man who "
               "killed your father, \nyou sense an unbelievably powerful person approach you",
        "choices": ["stand your ground: 1", "run away: 2"],
        "results": ["fight", "run"]
    },
    "fight": {
        "des": "you take a defensive stance as a man with long black hair and a tail flies over to you. he says he is\n"
               "looking for his brother and thought you might be him since you appear to be the strongest thing on \n"
               "the planet. you take pride in that until he says he feels someone stronger and takes off",
        "choices": ["follow him: 1", "ignore him: 2"],
        "results": ["follow", "ending1"]
    },
    "run": {
        "des": "you start running away.\nwait a second you remember you can fly\n"
               "you start flying away from whoever it is that has this much power."
               "\nit's faster than you. as it is just about to reach you you feel it stop and go in the opposite "
               "direction, weird.",
        "choices": ["follow him: 1", "be thankful he's not your problem anymore: 2"],
        "results": ["follow", "ending1"]
    },
    "follow": {
        "des": "He is a lot faster than you. You eventually reach the last spot you he stopped at."
               "\nit's an island with a house on it. you see an old man, a woman, a short bald man who obviouly was\n"
               "knocked into the house through a wall and you old enemy is prone on the ground.",
        "choices": ["laugh at his enemy and his friend: 1", "attack the man who killed your father: 2"],
        "results": ["laugh", "ending2"]
    },
    "ending1": "you ignore whoever it was with the great power and keep training. Bad call.\n"
               "you see an incredible blast of energy right before it destroys the planet.\n"
               "Bad End",
    "laugh": {
        "des": "you laugh at the sight of your rival and his friend being beat up. \nAs you strart claming down the "
               "woman tells you that that guy with insane power came here and said he was going to destroy the world"
               "\n you can't let that happen you live on the world!",
        "choices": ["team up with your rival to defeat him: 1", "fight alone: 2"],
        "results": ["team", "alone"]
    },
    "ending2": "you attack the man who killed your father and easily defeat him since he was hurt.\n"
               "you leave the island since you have completed your life's goal and return to training.\n"
               "on a night when the moon is full a gaint monkey appears out of nowhere and kills you\n"
               "Bad End",
    "team": {
        "des": "eh, your father was an evil overlord anyways and besides the help will most likely be needed.\n"
               "you both go to where you can feel the man had gone. you find him in an open field next to a large hole "
               "with a big metal ball in it.\nyour rival rushes to attack head on.",
        "choices": ["go with him: 1", "go for a sneak attack: 2"],
        "results": ["ending3", "ending4"]
    },
    "alone": {
        "des": "you can beat anyone by yourself. you arrive at where the man is waiting.\n"
               "he is in an open field next to a large hole with a large metal orb in it.",
        "choices": ["attack him head on: 1", "surprise attack: 2"],
        "results": ["ending5", "ending6"]
    },
    "ending3": "you both fight as hard as possible but he beats both of you back.\n"
               "As he is gloating over his ability to beat you both so easily your rival gets him in a full nelson.\n"
               "you strike him with your most powerful attack and accidentally kill both him and your rival.\n"
               "Good End?",
    "ending4": "ok wow, he completely destroyed your rival in seconds.\n"
               "As you try to think of what to do he notices you and kills you before you could do anything.\n"
               "Bad End",
    "ending5": " you get in a few good hits because he is surprised you found him, but he was way too powerful for you."
               "\n you died.\nBad End",
    "ending6": "you charge your strongest attack and surprise him with it. He can't avoid it and dies.\n"
               "Now no one can stop you from taking over the world.\n"
               "Evil End"
}
while not location.startswith("end"):
    location = read_script(location)
print(script[location])
