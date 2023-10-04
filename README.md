# configswapper

This is a graphics configuration swapper tool. The primary use is to quickly swap graphical configuration files in preparation for playing on a different monitor, in this case swapping between configurations for the steamdeck in handheld mode and docked mode. With the Steam Deck you have to reconfigure the graphical settings for games if you dock it, and then reconfigure them back once you play the game undocked again. This solves the issue, you can simply run the program after docking or after undocking and return all configurations to the desired configurations
This app alleviates the burden.

INSTRUCTIONS -
(Using Left 4 Dead 2 as an example)
Place the python script and .json file in your home/deck directory. (in the file browser its just called "Home" under the "Places" sidebar)
1. Start by launching all of your games and configuring their graphics for one mode at a time, so either handheld or docked. So if you want to configure for handheld first, launch every game and configure it while undocked.
2. Switch to desktop mode
3. Open terminal and run, "chmod +x /home/deck/configswap.py" you only have to run this one time. 
4. Right click on configswap.py and click "run in konsole" once the program opens, just close it. We opened it the first time so that it generates folders for us.
5. You'll notice that in the same directory as configswap.py it generated the "gameconfigs" folder. Inside of this folder are the "deck" and "dock" subfolders, and inside of those are individual folders for every steam game you have installed - they're auto-generated.
6. Copy/Paste the graphical configuration file from your game into it's respective configuration folder that you created in /gameconfigs/
  ex. for deck configuration you'll have /gameconfigs/deck/Left 4 Dead 2/yourconfigfile.example
      for dock configuration you'll have /gameconfigs/dock/Left 4 Dead 2/yourconfigfile.example
   IMPORTANT: do NOT rename configuration files. Keep them the exact same name.
   NOTE: you can include multiple files.
   NOTE: many games you also need to copy the video default files, as this will "detect" a new monitor. L4D2 is an example of this, and both the videodefaults.txt and video.txt must be copied.
9. Now, repeat and do the same thing but the with the steamdeck docked. Launch each game and configure it, then return to desktop mode and copy each configuration file from each game into its respective /gameconfigs/dock/game folder.


When running the script you're greeted with a window displays a few buttons. Start by clicking "New Game"

1. First, you'll type the name of the game for "Game Name". This is just what displays in your game list and doesn't have to be exact.

2. In the "Game Directory" option, point to where the config file is stored for the game. It will default to the steamapps/common folder.
  For instance, if i wanted to use Left 4 Dead 2 i would point to steamapps/common/Left 4 Dead 2/left4dead2/cfg/ and hit OK, as the config file for L4D2, video.txt and videodefaults.txt, is stored here. 

3. Select the files for the Deck config, you should point to the files for that game that you placed in the /gameconfigs/deck/ subfolder. Do the same for the dock config files.

4. Select save. You'll be brought back to the home menu

In the home menu it displays your current list of configs for games, as well as the last configuration selected.
Select a game and click "swap config" to select between dock and deck configurations.
Selecting "swap all configs" will swap every game to the config that you select.

Once you're done setting everything up you can add the python script configswap.py to your steam library. Return to gamemode and launch it. Open up steampinput and choose the mouse control options!

:)



