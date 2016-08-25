# TwitchVODDL

Welcome to TwitchVODDL! This is [Backcap](https://www.youtube.com/c/backcap)'s downloader for Twitch highlights.
Made by nei ([@neistuff](https://twitter.com/neistuff)), with great help from shounic ([@shounic_](https://twitter.com/shounic_)).

## Notes:

For now, only Windows releases are available due to the unability to test on other platforms.

I plan on trying to do a bash version for Linux/Mac in the following weeks. Or months. I don't know, it will depend on the time I have.

## Usage:

* Download the latest [release](https://github.com/neistuff/TwitchVODDL/releases)
* Put the URL, the start time and the end time of the highlights in highlights.txt.
	* This must suit the following format: `url hh:mm:ss hh:mm:ss`. Example: `https://www.twitch.tv/teamfortresstv/v/78990145 0:49:52 0:50:11`.
	* You can put more than one highlight, just put them in seperate lines.
* Start `TwitchVODDL.py` in a Python interpreter
* The script does the rest, so "????"
* Profit!

## Credits:

* shounic for helping me figuring out how to use youtube-dl
* The amazing [ffmpeg](ffmpeg.org) and [youtube-dl](https://github.com/rg3/youtube-dl/) teams for these useful tools
* [reino17](https://github.com/reino17/) on GitHub for this very complete [batch file](https://github.com/rg3/youtube-dl/issues/4821#issuecomment-97564929)
* Myself (nei) for putting everything together

Also, this is under GPL v3.

Enjoy!