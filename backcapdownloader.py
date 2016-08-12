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

## Libraries import + variables setup
import os
fileNumber = 1

## Reading the txt file
# Console information
print("Backcap dowloader started! Reading the highlights file...")

# Highlights file opening
try:
    highlightsFile = open("highlights.txt","r")
except:
    print("Error while reading the file. Perhaps it does not exist?")
# Getting all the highlights and putting them in a list
highlights = highlightsFile.readlines()

print("Highlights file successfully read!")

## Begin fun stuff
# Function used for converting timecodes in seconds.
def convert_to_s(timecode):
    listTime = timecode.split(":")
    return int(listTime[0]) * 3600 + int(listTime[1]) * 60 + int(listTime[2])

# Now we begin doing important stuff.
for highlight in highlights:
    
    # Opening the batch file
    print("Opening the batch file...")
    batchFile = open("backcapdownloader.bat","w+")
    print("Batch file successfully opened!")
    
    # This is for renaming the files
    filesInDirBefore = os.listdir(".")
    print(filesInDirBefore)
    
    #Reading the highlights file
    highlight.rstrip() # Removes the \n
    highlightList = highlight.split() # Separates the url and the timestamps
    highlightStartTime = convert_to_s(highlightList[1]) # Gets the start time in seconds
    highlightEndTime = convert_to_s(highlightList[2]) # Gets the end time in seconds
    
    # If start time > end time, we have to warn the user.
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
    
    # Now we write the batch file
    else:
        # We need the duration to input in ffmpeg
        duration = highlightEndTime - highlightStartTime
        
        # Now we write in the file all this stuff.
        batchFile.write("@ECHO off\n\n")
        batchFile.write("SET url="+ highlightList[0] + "\n")
        batchFile.write("IF \"%url%\" EQU \"\" GOTO End\n")
        batchFile.write("IF \"%url: =%\" NEQ \"%url%\" GOTO Input\n")
        batchFile.write("SET start=" + highlightList[1] + "\n")
        batchFile.write("SET dur=" + str(duration) + "\n")
        batchFile.write("ECHO.\nFOR /F \"delims==\" %%A IN ('youtube-dl.exe --no-warnings --get-filename \"%url%\"') DO SET filename=%%A\n")
        batchFile.write("FOR /F %%B IN ('youtube-dl.exe -g \"%url%\"') DO (\n")
        batchFile.write("ffmpeg.exe -hide_banner -ss \"%start%\" -i \"%%B\" -c copy -t \"%dur%\" -bsf aac_adtstoasc \"%filename%\"\n")
        batchFile.write(")\n")
        batchFile.write(":End\n\n")
        batchFile.close()
        print("\nBatch file successfully configured! It will now start automatically!")
        
        # The Python script runs the batch file automatically. Isn't it wonderful?
        os.system("backcapdownloader.bat")
        
        # Now we look at what files are in the directory after the download.
        filesInDirAfter = os.listdir(".")
        print(filesInDirAfter)
        
        # And we compare the two lists of files.
        for file in filesInDirAfter:
            
            # If it finds one file that differs from the other list,
            if file not in filesInDirBefore:
                # We make a file out of its name
                fileList = list(file)
                # Get the index of it before the extension (here, .mp4 so 4 characters)
                beforeFormat = len(fileList) - 4
                # We initialize a list in order to put every letter of the name of the file without the extension in it.
                woFormat = list()
                index = 0
                for letter in range(beforeFormat):
                    woFormat.append(fileList[index])
                    index += 1
                
                # So woFormat now contains the name of the file without .mp4
                # afterFormat will fusion the list and add "-[fileNumber].mp4" to it.
                afterFormat = ''.join(woFormat) + "-" + str(fileNumber) + ".mp4"
                os.rename(file,afterFormat)
                fileNumber += 1
            else:
                continue

print("All files downloaded!")
os.system("pause")

'''
@ECHO off

:Input
ECHO.
SET url=
ECHO Enter Youtube-url:
SET /P url=
IF "%url%" EQU "" GOTO End
IF "%url: =%" NEQ "%url%" GOTO Input
ECHO Enter start time (in seconds, or in hh:mm:ss[.xxx] form):
SET /P start=
ECHO Enter duration (in seconds, or in hh:mm:ss[.xxx] form):
SET /P dur=
ECHO.
FOR /F "delims==" %%A IN ('youtube-dl.exe --no-warnings --get-filename "%url%"') DO SET filename=%%A
FOR /F %%B IN ('youtube-dl.exe -g "%url%"') DO (
ffmpeg.exe -hide_banner -ss "%start%" -i "%%B" -c copy -t "%dur%" -bsf aac_adtstoasc "%filename%"
)
GOTO Input

:End
'''