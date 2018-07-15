import pyautogui
from PIL import Image
import sys
import cv2
import os
import datetime

now = datetime.datetime.now()
year = now.year
month = now.month
day = now.day
logfile = str(month) + "-" + str(day) + "-" + str(year) + "-log.txt"


exepath = os.path.dirname(sys.executable)
config = open(exepath + "/resources/config.txt", "r")
folder = config.read()
path = exepath + "/resources/" + folder + "/"
logpath = exepath + "/resources/" + logfile


bloodicon = Image.open(path + "BloodIcon.png")
bloodpost = Image.open(path + "BloodPost.png")
dragonicon = Image.open(path + "DragonIcon.png")
dragonpost = Image.open(path + "DragonPost.png")
foresticon = Image.open(path + "ForestIcon.png")
forestpost = Image.open(path + "ForestPost.png")
havenicon = Image.open(path + "HavenIcon.png")
havenpost = Image.open(path + "HavenPost.png")
portalicon = Image.open(path + "PortalIcon.png")
portalpost = Image.open(path + "PortalPost.png")
runeicon = Image.open(path + "RuneIcon.png")
runepost = Image.open(path + "RunePost.png")
shadowicon = Image.open(path + "ShadowIcon.png")
shadowpost = Image.open(path + "ShadowPost.png")
swordicon = Image.open(path + "SwordIcon.png")
swordpost = Image.open(path + "SwordPost.png")
yourClass = ""
oppoClass = ""
icons = [foresticon, swordicon, havenicon, runeicon, shadowicon, dragonicon, bloodicon, portalicon]
posts = [forestpost, swordpost, havenpost, runepost, shadowpost, dragonpost, bloodpost, portalpost]
crafts = ["Forestcraft", "Swordcraft", "Havencraft", "Runecraft", "Shadowcraft", "Dragoncraft", "Bloodcraft", "Portalcraft"]
img1 = Image.open(path + "1st.png")
img2 = Image.open(path + "2nd.png")
imgV = Image.open(path + "Victory.png")
imgD = Image.open(path + "Defeat.png")
first = True
win = True
mullTaken = False
turnSet = False
oppoSet = False
resultSet = False
yourSet = False

print("Hi there! My name is Nio and I will be assisting you with automatically logging your matches! Fighting!" +
      "\nTo leave me alone and make me sad, just hit ctrl c on this window.")
try:
    while True:
        screen = pyautogui.screenshot()
        if not mullTaken:
            if not pyautogui.locate(img1, screen, grayscale=True, confidence=0.9) is None:
                first = True
                turnSet = True
            elif not pyautogui.locate(img2, screen, grayscale=True, confidence=0.9) is None:
                first = False
                turnSet = True
            if turnSet:
                for icon in icons:
                    if not pyautogui.locate(icon, screen, grayscale=True, confidence=0.9) is None:
                        oppoClass = crafts[icons.index(icon)]
                        oppoSet = True
                        break
            mullTaken = turnSet and oppoSet
            if mullTaken:
                print("Okay, I've got your mulligan screen. Good luck!")
        else:
            if not pyautogui.locate(imgD, screen, grayscale=False, confidence=0.9) is None:
                win = False
                resultSet = True
            elif not pyautogui.locate(imgV, screen, grayscale=False, confidence=0.9) is None:
                win = True
                resultSet = True
            if resultSet:
                for post in posts:
                    if not pyautogui.locate(post, screen, grayscale=True, confidence=0.9) is None:
                        yourClass = crafts[posts.index(post)]
                        yourSet = True
                        break
            if resultSet and yourSet:
                with open(logpath, "a") as log:
                    log.write(yourClass + " " + oppoClass + " " + str(first) + " " + str(win) + "\n")
                print("Your class: " + yourClass + "\nOpponent class: " + oppoClass + "\nFirst: " + str(
                    first) + "\nWon: " + str(win))
                first = True
                win = True
                mullTaken = False
                turnSet = False
                oppoSet = False
                resultSet = False
                yourSet = False
                yourClass = ""
                oppoClass = ""
except KeyboardInterrupt:
    print("Bye bye! Will you come back soon?")
