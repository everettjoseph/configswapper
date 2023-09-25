# configswapper

This is a graphics configuration swapper tool. The primary use is to quickly swap graphical configuration files in preparation for playing on a different monitor.
For example if you have a 1080p monitor that you use for some games due to GPU performance, but maybe on other games you want to use your 4k TV so you can sit back with a controller.
Or maybe sometimes you like to have the 4k TV playing a show while playing a game, then another time you'd like to play the game on the 4k TV again.
This was the issue for me.
Normally, this causes annoying issues of having to reconfigure graphical settings within the game each time.

This simple python script eliminates that.

INSTRUCTIONS -
(Using Left 4 Dead 2 as an example)
Place the python script and .json file in your home user directory or wherever else your python directory is. 
1. Start by launching all of your games and configuring their graphics for your first monitor/TV. So if you want to configure for 1080p first, launch every game and configure it on that monitor/TV.
2. create a folder called "GameConfig" with respectively titled resolution folders inside it. 
3. create game folders inside of the resolution folders.
  ex. for 1080p you'll have /GameConfigs/1080p/Left4Dead2/
      for 4k you'll have /GameConfigs/4k/Left4Dead2/
4. Copy/Paste the graphical configuration file from your game into it's respective resolution folder that you created in /GameConfigs/
   ex. If I wanted to use Left 4 Dead 2 I would be copying steamapps/common/Left 4 Dead 2/left4dead2/cfg/video.txt, i would copy that into /GameConfigs/1080p/Left4Dead2
5. Now, repeat and do the same thing but with your other resolution/monitor.
   ex. I would launch L4D2 on my 4k monitor, configure the graphics and exit. Copy /lef4dead2/cfg/video.txt to /GameConfigs/4k/Left4Dead2


When running the script you're greeted with a window displays a few buttons. Start by clicking "New Game"

1. First, you'll type the name of the game for "Game Name". This is just what displays in your game list and doesn't have to be exact.

2. In the "Game Directory" option, point to where the config file is stored for the game. It will default to the steamapps/common folder.
  For instance, if i wanted to use Left 4 Dead 2 i would point to steamapps/common/Left 4 Dead 2/left4dead2/cfg/ and it OK, as the config file for L4D2, video.txt, is stored here. 

3. For "Config 1 Name" just make it whatever your first resolution is. Here i'll name mine "1080p"
4. use "Select files" under config 1, then select the config file for your first resolution.
   ex. Here i would be selecting /GameConfigs/1080p/Left4Dead2/video.txt
   tip - you can select mulitple files.
5. Repeat for config 2.
   ex. I would make config 2 "4k", then point it to /GameConfigs/4k/Left4Dead2/video.txt
6. Select save. You'll be brought back to the home menu

In the home menu it displays your current list of configs for games, as well as the last configuration selected.
Select a game and click "swap config" to be displayed your options and you can choose.
Selecting "swap all configs" will swap every game to the config that you type in. It must match the options exactly, if a game doesn't have that option it will simply be skipped.


