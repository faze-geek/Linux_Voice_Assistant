from recog import recog
from say import say
from search_package import searchpac
from install_package import install
import os
import datetime
import wikipedia
import webbrowser as wb
import subprocess
import pyautogui
import screen_brightness_control as sbc
from AppOpener import run
from lxml import html
import requests
import time


# Function to Greet the user based on time
def Greeting():
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        say("Good Morning !!")
    elif hour>=12 and hour<18:
        say("Good Afternoon!!")
    else:
        say("Good Evening !!")
    print("I am Thor, How may I help you?")
    say("I am Thor, How may I help you?")



if __name__ == "__main__":
    Greeting() 
    while True:
        query  = recog().lower() # converting the query to all lowercase
        # searching for keywords inside the text query
        if "wikipedia" in query: # if we get a keyword as wikipedia
            say("Searching Wikipedia")
            # replacing wikipedia with ""
            query = query.replace("wikipedia","") 
            # searching the new query directly on wikipedia using the wikipedia library
            results  = wikipedia.summary(query,sentences = 2)
            say("According to Wikipedia")
            print(results)
            say(results)
        elif "increase volume by" in query: # if we get a keyword as increase volume by
            say("Increasing Volume")
            # replacing increase volume by with ""
            query = query.replace("increase volume by","")
            # converting left query to integer
            query =  int(query)
            # loop for query times
            for i in range(query):
                # pressing the volume up button query times
                pyautogui.press('volumeup')
        elif "decrease volume by" in query:# if we get a keyword as decrease volume by
            say("Decreasing Volume")
            # replacing decrease volume by with ""
            query = query.replace("decrease volume by","")
            # converting left query to integer
            query =  int(query)
            # loop for query times
            for i in range(query):
                # pressing the volume down button query times
                pyautogui.press('volumedown')
        
        elif "open youtube" in query:# if we get a keyword as open youtube
            # opeaning youtube.com using webbrowser library
            wb.open("youtube.com")
        elif "open google" in query:# if we get a keyword as open google
            # opeaning google.com using webbrowser library
            wb.open("google.com")
        elif "open chess" in query:# if we get a keyword as open chess
            # opeaning chess.com using webbrowser library
            wb.open("chess.com")
        elif "play music" in query:# if we get a keyword as play music
            # address of the direcotory where the music is 
            music_Dir = ""
            songs = os.listdir(music_Dir)
            # playing the first song in the directory
            os.startfile(os.path.join(music_Dir,songs[0]))
        elif "the time" in query:# if we get a keyword as the time
            # Time in H M S format
            Time  = datetime.datetime.now().strftime("%H:%M:%S")
            say("The time is")
            say(Time) 
        elif "open" in query:# if we get a keyword as open
            # replacing open with ""
            query = query.replace("open ","")
            run(query)
        elif "set brightness to" in query:# if we get a keyword as set brightness to
            say("setting brightness")
            # replacing set brightness to with ""
            query = query.replace("set brightness to","")
            # converting left query to integer
            query =  int(query)
            # using the screen_brightness_control to set the brightness to query
            sbc.set_brightness(query)
        elif "click" in query:# if we get a keyword as click
            # holding down the win button
            pyautogui.keyDown("win")
            # pressing the prtscn button
            pyautogui.press("printscreen")
            # releasing up the win button
            pyautogui.keyUp("win")
        elif "search on youtube" in query:# if we get a keyword as search as youtube
            # replacing search on youtube with ""
            query = query.replace("search on youtube","")
            # appending the query to the youtube url
            query = 'https://www.youtube.com/results?search_query='+query
            print(query)
            # opeaning the new formed url 
            wb.open(query)
        elif "search on google" in query:# if we get a keyword as search on google
            # replacing search on google with ""
            query = query.replace("search on google","")
            # appending the query to the google url
            query = 'https://www.google.com/search?q='+query
            print(query)
            # opeaning the new formed url 
            wb.open(query)
        else:
            print("I did not recognize that")   
            say("I did not recognize that!!")