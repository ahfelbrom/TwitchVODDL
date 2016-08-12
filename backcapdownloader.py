## Notes
""" 
    This is Backcap's downloader for Twitch highlights.
    Made by nei (@neistuff), with great help from shounic (@shounic_).
    
    Usage:
        - Install youtube-dl.
            You can do it with pip, by typing "python pip install yourube-dl".
            YOU ONLY NEED TO DO IT THE FIRST TIME THOUGH.
        - Put the URL, the start time and the end time of the highlights in highlights.txt.
            This must suit the following format: "url h:m:s h:m:s". Example: https://www.twitch.tv/teamfortresstv/v/78990145 0:49:52 0:50:11
            You can put more than one highlight, just put them in seperate lines.
        - Start backcapdownloader.py in a Python interpreter
        - The script does the rest, so "????"
        - Profit!
        
    Enjoy!
"""

## Libraries import
from __future__ import unicode_literals
import youtube_dl

## Reading the txt file
# Console information
print("Backcap dowloader started! Reading the highlights file...")

# File opening
try:
    highlightsFile = open("highlights.txt","r")
except:
    print("Error while reading the file. Perhaps it does not exist?")
# Getting all the highlights and putting them in a list
highlights = highlightsFile.readlines()

print("File successfully read!")

## Begin fun stuff
# Function used for converting timecodes in seconds.
def convert_to_s(timecode):
    listTime = timecode.split(":")
    return int(listTime[0]) * 3600 + int(listTime[1]) * 60 + int(listTime[2])

# Now we begin doing important stuff.
for highlight in highlights:
    highlight.rstrip() # Removes the \n
    highlightList = highlight.split() # Separates the url and the timestamps
    highlightStartTime = convert_to_s(highlightList[1]) # Gets the start time in seconds
    print(highlightStartTime)
    highlightEndTime = convert_to_s(highlightList[2]) # Gets the end time in seconds
    print(highlightEndTime)
    if highlightStartTime >= highlightEndTime:
        choice = a
        while choice != i or choice != s:
            print("WARNING: Timecodes incorrectly entered for this highlight: "+highlightList[0]+". Type i to invert them or s to ignore and skip.")
            choice = str(input().lower())
        if choice == s:
            print("The following highlight has been ignored: "+highlightList[0]+".")
            continue
        elif choice == i:
            stamp = highlightStartTime
            highlightStartTime = highlightEndTime
            highlightEndTime = stamp
            print("Values successfully inverted.")
    else:
        # yt-dl function goes here
        # ydl_opts = {}
        # with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        #     ydl.download(highlightList[0])
        print("ok")