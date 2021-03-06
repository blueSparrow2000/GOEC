# GOEC ☨
The Game of Escaping Cave (GOEC) STABLE-VERSION  is now released!


Solo cave escape adventure.


This game is created based on https://letstalkdata.com/2014/08/how-to-write-a-text-adventure-in-python-part-1-items-and-enemies/


Basic template is created with above link.


All other classes/functions/texts are developed by myself.


Development period: 2021.8.13 ~ 2021.8.19

## How to Run


This is a terminal-game.


1. Download \* & unzip file(if you used 'tag' for downloading) in your interpreter. (If you use pyCharm, then put the file in PycharmProjects folder)
2. Go to interpreter -> open the project (GOEC) -> run game.py **

\* Download the code by using 'git bash'! 


**Example of using git bash command (Using Pycharm IDE)**


![interface](../main/images/commands.png)


** If 'Invalid Python interpreter selected ...' message comes out, click on 'Configure Python interpreter' and add one! Any interpreter of Python version greater or equal to 3.7 is ok. 


## Interface
* __Minimap__


![interface](../main/images/interface.png)


* __Attack__ 


![interface](../main/images/attack_capture1.png)


* __View mobs__


![interface](../main/images/capture1.png)


## Features
* Trading - trade gold for items & Sell items
* Unique story - short, but exclusive story written by me :) Not completed yet!
* Minimap - minimap contains carefully selected icons! 


## Quick preview of tutorial (in game)
        Welcome to the cave!
        This is the tutorial cave.

        ======= Goal [ ⚐ ] =========
        It's about escaping the cave.

        ===== How to act [ ☨ ] =====
        The actions the player can take are provided as options.
        You can perform an action by typing the hot key to the left of the option.
        Common actions are; basic movements (front, back, right, left) and inventory check, status check, cave monster encyclopedia view, food, etc.
        Inventory size is currently unlimited, so you don't have to worry about overflowing items.

        ====== Minimap [ ■ ] =======
        The minimap is updated every time you move.
        See the legend below.

        [ \033[95m☨\033[0m ] : Current position
        [ ■ ] : Room that you haven't visited or that is not near you!
        [ ☼ ] : Your starting position
        [ ⚐ ] : Exit!

        The mini-map is only an auxiliary function to help you explore. 
        Reading text is more important since this is a text-based-game :) Like reading novels? 
        (Do not rely on a minimap!)

        ==== Status (Stat) [ 'vs' ] ====
        In this game, there are statuses that enhance the player's abilities.
        As player level up, (s)he chooses which one of the statuses will be increased by 1.
        Once chosen, it cannot be reversed so please choose carefully.
        The higher the level, the greater the amount of experience required to level up (∝log).
        Currently, there are 6 types of stats: Agility, Defense, Learning, Strength (Physical), Magic Affinity, and Stability.
        You can level up in advance on the beggining of the game (you probably have seen the "Enter player's level" option before this tutorial).
        For more detailed explanations of various stats, refer to ['vs': View status] in the option (type 'vs').

        ===== Encyclopedia [ 'vm' ] =====
        This is a list containing the monsters the player have encountered so far.
        You can roughly see the HP and basic damage of the monster.
        However, be aware that even monsters with the same name may have slightly different information (HP, damage).
        Also, thier skills are not shown here. This is to give the game more tension and uncertainty.

        ======== Eat(Heal) [ 'e' ] ==========
        The way to heal yourself is to eat food.
        You have an apple in your inventory, so try them later.
        You can eat on any tile, but if you choose to eat during a battle, you cannot attack monsters during that turn.

        ======= Attack [ 'z'/'x' ]=========
        If you move to a tile with a monster, the monster will appear.
        ['z': attack] is created in the selection option. 
        After entering 'z', the user can select the desired weapon from the following selection list, which will attack automatically with that weapon.
        Alternatively, if you want to attack using the weapon you used just before, select ['x': Attack with previous option].
        Weapon and it's information can be viewed at any time (except during combat) through inventory (type 'i').

        ======= Tile(Room) [   ] =========
        Finally, the tiles. 
        In this game, events occur as the player moves through tiles.
        The unit of a cell on the minimap is a tile(room).
        The tiles you haven't been to is considered unknown and is not shown to player, except in these three gamemodes; Easy, Normal, Hard.
        In Easy mode, all the tiles are visible from the beggining.
        In Normal or Hard mode, you can preview your top, bottom, left, and right tiles even if you haven't been there.

        Common tiles include 'EmptyCavePath', 'Room of Gold Coins', 'Room of Monsters', 'Room of Items', and 'Locked Room'.
        You can hear your monologue on the EmptyCavePath. :D
        There is a small amount of gold in the Room of Gold Coins.
        A monster is hiding in the Room of Monsters and will attack you. This is when you get into the attack mode.
        NOTE: Monsters do not respawn once killed. (In reality, the dead can't come back to life, right?)
        The Item Room gives players free items.
        Locked rooms are locked. Find the key in a Key Room (a type of Room of Items) and get the key, or kill the monster holding the key.
        NOTE: You must have the correct key for the locked room to open it.

        ==== Score calculation [ - ] ===
        At the end of the game, you will recieve your score, which will be recorded on the leader board (simple txt file).
        Current version's score calculation is done as follows: (all rounded up to first digit each step)

        score = initial_setting_score + title_score

        initial_setting_score = map_score * gamemode_score * (0.9)^(handicap)

        title_score = (# of earned titles) - 2 * (# of earned 'killer' titles) 

        NOTE: 'killer' title is earned when you have certain amount of certain mob drops in your inventory. 
        Remember, reducing unnecessary kills is also a pro's quality!
        You can see the leader board if you want when the game ends.

        ==== Closing remarks [ ♪ ] =====   
        It doesn't matter if you don't remember all of this. You know, you learn by playing :)

        There is a little present for you. 
        Please check it in your inventory by typing 'i'. 
        Good luck!

        Below is a minimap.


## A brief description of each files


- #### actions.py
  - Stores player's actions

- #### enemies.py
  - Enemy's infomation and skills are stored here.

- #### game.py
  - This is where the game starts and runs.

- #### initial_setting.py
  - 'Setting' class fetches initial settings like map, mode, handicap (initial level) from user input on the terminal.

- #### items.py
  - Item's informations and effects are stored here.

- #### login.py
  - Login module for handling user accounts and leader board.

- #### npcs.py
  - NPC's are stored here. NPC inherits Enemy, that means they can harm you!

- #### player.py
  - All the player's activities are stored as methods here.

- #### statuses.py
  - Status informations are stored here.

- #### story_info.py
  - Story script and story-telling Storybot is stored here.

- #### test.py
  - Just for testing simple codes.

- #### title.py
  - Stores titles that player can achieve during the game.

- #### tutorial.py
  - Tutorial script is stored here.

- #### util.py
  - Utility functions are stored here.

- #### world.py
  - World is generated here. World files can be modified in folder 'resources'.

## License
[![MIT](https://img.shields.io/cocoapods/l/AFNetworking.svg?style=style&label=License&maxAge=2592000)](../master/LICENSE)

Copyright (c) 2021-present, blueSparrow2000


## EDIT:
Sorry to those who cloned earlier version.
I messed up with my github and some codes were not updated.
The codes probably didn't run...
Now that I have resetted everything, It should be good to go!
