import math
import items


class Setting:
    def __init__(self):
        self.map_scores = {'tutorial': 0, 'room_tester': 0, 'cave': 10, 'deep_cave': 20, 'dungeon': 40, 'prison': 50}
        self.map_lists = ['tutorial', 'room_tester', 'cave', 'deep_cave', 'dungeon', 'prison']
        # Below maps: Coming Soon!
        # 'dungeon'
        self.mod_score_multiplier = {'Easy': 0.1,
                                     'Normal': 1,
                                     'Hard': 1.2,
                                     'Sudden Death': 1.3,
                                     'God': 0}
        self.mods_and_remarks = {'Easy': 'cave is lit, you can see all the tiles from the beggining',
                                 'Normal': '(Default) cave is dim, but you can preview your top, bottom, left, and right tiles',
                                 'Hard': 'preview exists, but you forget what was in the room you visited...',
                                 'Sudden Death': "cave is so dark that you can't even see ONE INCH ahead...",
                                 'God': 'items will make you INVINCIBLE'}  # 'Hardcore'
        self.max_handicap = 6

        self.map = None
        self.mode = None
        self.handicap = None

    def get_map_score(self):
        return self.map_scores[self.map]

    def get_mode_score_multiplier(self):
        return self.mod_score_multiplier[self.mode]

    def get_score_lowering_factor_handicap(self):
        return self.handicap

    def get_setting_score(self):
        handicap_degrading_factor = 0.9
        return round(self.get_map_score() * self.get_mode_score_multiplier() * math.pow(handicap_degrading_factor,
                                                                                        self.get_score_lowering_factor_handicap()),
                     1)

    def get_map_name(self):
        print('\033[91m{}\033[0m'.format('Now, choose the map!'))
        self.map = self.choice_selector(self.map_lists)
        if not self.map:
            self.map = 'cave'
        print('Choice: {}'.format(self.map))
        if self.map == 'prison':
            print("You chose prison: story map. It's best to play in normal mode or harder.")
        print('=' * 70)

        return self.map

    def get_player_name(self):
        name = input('\033[91m{}\033[0m'.format(
            "Enter player's name (if you don't know what to do, press 'Enter' or press 'q'): "))
        name = name.strip()
        if name and name != 'q':
            print("Great! Your name is \033[92m{}\033[0m.".format(name))
            print('=' * 70)
            return name
        else:
            name = 'Cave Runner'
            print("Your name is \033[92m{}\033[0m. Remember.".format(name))
            print('=' * 70)
            return name

    def get_game_mode(self):
        print('\033[91m{}\033[0m'.format('Please choose the gamemode.\n'))
        mod_lists = list(self.mods_and_remarks.keys())

        # show details of options
        for mod in mod_lists:
            print('{} - {}'.format(mod, self.mods_and_remarks[mod]))
        print('=' * 70)

        self.mode = self.choice_selector(mod_lists)
        if not self.mode:
            self.mode = 'Normal'
        print('Choice: {} - {}'.format(self.mode, self.mods_and_remarks[self.mode]))
        print('=' * 70)
        return self.mode

    def give_items_corresponding_to_mode(self, player, mode=None):
        if mode == 'Easy':
            player.inventory_reset()
            player.give(items.RabbitFoot(100), items.Dagger(), items.BeefJerky())
        elif mode == 'God':
            player.inventory_reset()
            player.give(items.Shield(1), items.Scepter())
        else:
            pass

    def get_minimap_visibility(self, map_name, selected_mode):
        if selected_mode == 'Easy':
            return 'all'
        elif selected_mode == 'Normal':
            return 'partial'
        elif selected_mode == 'Hard':
            return 'forgetting'
        elif selected_mode == 'Sudden Death':
            return None
        elif selected_mode == 'God':
            return 'all'
        else:
            return None

    def get_handicap(self):
        self.handicap = -1  # initialize
        while self.handicap != 0 and self.handicap != 'q' and (not 1 <= self.handicap <= self.max_handicap):
            self.handicap = input('\033[91m{}\033[0m'.format(
                "Enter player's level(integer) from 1 to {}. Maximum possible handicap is {} levels. (If you don't want handicap, press '0' or press 'q'): ".format(
                    self.max_handicap, self.max_handicap)))
            try:
                self.handicap = int(self.handicap)
            except:
                if self.handicap == 'q':
                    break
                else:
                    self.handicap = -1
        if self.handicap == 0 or self.handicap == 'q':
            print("No handicap!")
            self.handicap = 0
        print('=' * 70)
        return self.handicap

    def set_player_level(self, player, level_handicap):
        for x in range(level_handicap):
            player.gain_xp(player.xpmax)
        # print('='*70)

    # returns mapping table(dictionary) of "choice number : the choice(action)"
    def available_actions(self, choiceList):
        actions = {}
        for i in range(len(choiceList)):
            num = '{}'.format(i + 1)
            actions[num] = choiceList[i]
        return actions

    # shows the mapping table and returns available action and hotkey list
    def show_available_choices(self, choiceList):
        available_actions = self.available_actions(choiceList)

        # print('\n', '=' * 70, '\n')
        print("Select an item: \n")
        for selection in available_actions.items():
            print('{}: {}'.format(selection[0], selection[1]))
        print("(Type 'q' to use default setting)")
        print()

        available_hotkeys = ['%s' % (i + 1) for i in range(len(available_actions))] + ['q']
        return available_actions, available_hotkeys

    def choice_selector(self, choiceList):
        available_choices, available_hotkeys = self.show_available_choices(choiceList)
        set_input = input('Select: ')
        while set_input not in available_hotkeys:
            print(available_hotkeys)
            print(
                "Incorrect selection. Please choose from the list above. \nIf you want to quit (use default setting), type 'q'.")
            set_input = input('Select: ')

        if set_input != 'q':
            return available_choices[set_input]

        return None
