@ECHO off

SET url=https://www.twitch.tv/teamfortresstv/v/78990145
IF "%url%" EQU "" GOTO End
IF "%url: =%" NEQ "%url%" GOTO Input
SET start=0:52:25
SET dur=16
ECHO.
FOR /F "delims==" %%A IN ('youtube-dl.exe --no-warnings --get-filename "%url%"') DO SET filename=%%A
FOR /F %%B IN ('youtube-dl.exe -g "%url%"') DO (
ffmpeg.exe -hide_banner -ss "%start%" -i "%%B" -c copy -t "%dur%" -bsf aac_adtstoasc "%filename%"
)
:End

