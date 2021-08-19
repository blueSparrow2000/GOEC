'''
How to add world map to the game:

wWen you finish designing a map (in an Excel file called 'map builder'), you should ctrl + C/ctrl + V the map into txt file to finally save the map.
Then, add the map's to 'map_lists' in initial_setting.Setting() class's method 'get_map_name()'.
'''

import re

_world = {}  # {(x,y) : tile (Object)}
starting_position = (0, 0)


def code_finder(tile_name, pattern):
    # 이런 형식의 타일을 다룰 수 있음:
    # 타일이름 + 상태/코드 + 4자리 수(string)
    # 예시) JumpRoomCode0000
    p = re.compile(pattern)
    m = p.search(tile_name)
    if not m:
        return False
    code = tile_name[m.end():]
    return code


def build_locked_tile(tile_name, _world, x, y, refined_tile_name):
    code = code_finder(tile_name, 'Locked')
    if not code:
        return False
    address_code = code
    _world[(x, y)] = getattr(__import__('tiles'), refined_tile_name)(x, y, refined_tile_name)
    _world.get((x, y)).locked_state = address_code
    return True


def build_jump_tile(tile_name, _world, x, y, refined_tile_name):
    code = code_finder(tile_name, 'Code')
    if not code or refined_tile_name != 'JumpRoom':
        return False
    jump_code = code
    # print(_world)
    _world[(x, y)] = getattr(__import__('tiles'), refined_tile_name)(x, y, refined_tile_name, _world)
    _world.get((x, y)).jump_code = jump_code
    return True


def build_jumped_tile(tile_name, _world, x, y, refined_tile_name):
    code = code_finder(tile_name, 'Code')
    if not code or refined_tile_name != 'JumpedRoom':
        return False
    jump_code = code
    _world[(x, y)] = getattr(__import__('tiles'), refined_tile_name)(x, y,
                                                                     refined_tile_name)  # JumpRoom과 다르게 _world 인자를 주지 않는다.
    _world.get((x, y)).jump_code = jump_code
    return True


def build_key_tile(tile_name, _world, x, y, refined_tile_name):
    if tile_name.startswith('FindKeyRoom'):
        key_address_code = tile_name[-4:]
        _world[(x, y)] = getattr(__import__('tiles'), refined_tile_name)(x, y, refined_tile_name, key_address_code)
        return True
    return False


def tile_name_refiner(tile_name):
    p = re.compile('Locked')
    m = p.search(tile_name)
    if m:
        return tile_name[:m.start()]
    else:  # not locked
        p2 = re.compile('Code')
        m2 = p2.search(tile_name)
        if m2:
            return tile_name[:m2.start()]
        else:
            p3 = re.compile('[0-9]+')
            m3 = p3.search(tile_name)
            if m3:
                return tile_name[:m3.start()]
            else:  # not a 'findkey' room
                return tile_name


# Wow cool!!!
def load_tiles(mapName='cave', mode='Normal', reveal=None):  # using array
    glossary = {'': '     ', '\n': '\n', 'EmptyCavePath': '   ', 'GoldRoom': ' ○ ', 'MerchantRoom': ' $ ',
                'StartingRoom': ' ☼ ',
                'FindRabbitFootRoom': ' ♪ ', 'FindStaffRoom': ' ᛡ ', 'FindWandRoom': ' ∫ ', 'GandalphRoom': ' ☥ ',
                'HarryPotterRoom': ' ⚚ ',
                'ScorpionRoom': ' ⚘ ', 'BanditRoom': ' ⚳ ', 'RetiredMageRoom': ' ᛘ ', 'FindKeyRoom': ' ⚷ ',
                'LeaveCaveRoom': ' ⚐ ',
                'FindDaggerRoom': ' ҁ ', 'WandererRoom': ' 𐏑 ', 'GuardRoom': ' ♦ ', 'JumpRoom': ' ⚭ ',
                'JumpedRoom': '   ',
                'MemoryRoom': '   ',
                'SlateRoom': ' 𐏒 '}  # ♺ '':'⛊⛏' 🧭  # Mapping table of "whole tile information : tile abbreviation"
    # glossary = {'': '|||||', '\n': '\n','EmptyCavePath':'   '}
    minimap = []  # Complete minimap array (Minimap that computer has)
    playerminimap = []  # Incomplete minimap that is shown to the player (Minimap that player has - records visited tiles, refering to the complete minimap)

    """Parses a file that describes the world space into the _world object"""
    map = 'resources/{}.txt'.format(mapName)
    with open(map, 'r') as f:
        rows = f.readlines()

    x_max = len(rows[0].split('\t'))  # Assumes all rows contain the same number of tabs
    for y in range(len(rows)):
        current_row = []
        cols = rows[y].split('\t')
        for x in range(x_max):
            tile_name = cols[x].replace('\n', '')  # Windows users may need to replace '\r\n'('\n' set to default)
            if tile_name == 'StartingRoom':
                global starting_position
                starting_position = (x, y)

            refined_tile_name = tile_name_refiner(tile_name)
            if refined_tile_name not in glossary.keys():
                glossary[refined_tile_name] = tile_name[0:3]
            tile_abbr = glossary['']  # minimap array에 저장되는 기호
            if tile_name != '':
                # tile_abbr = '|{}|'.format(glossary[tile_name])
                # tile_abbr = ' {} '.format(glossary[tile_name])
                tile_abbr = '[{}]'.format(glossary[refined_tile_name])
            current_row.append(tile_abbr)

            if tile_name == '':
                _world[(x, y)] = None
            else:
                is_locked_tile = build_locked_tile(tile_name, _world, x, y, refined_tile_name)
                is_jump_tile = build_jump_tile(tile_name, _world, x, y, refined_tile_name)
                is_jumped_tile = build_jumped_tile(tile_name, _world, x, y, refined_tile_name)
                is_key_tile = build_key_tile(tile_name, _world, x, y, refined_tile_name)

                if is_locked_tile or is_jump_tile or is_jumped_tile or is_key_tile:
                    pass
                else:
                    _world[(x, y)] = getattr(__import__('tiles'), refined_tile_name)(x, y, refined_tile_name)

        minimap.append(current_row)
    playerminimap = Playerminimap(minimap, glossary, mode, reveal)
    return playerminimap


class Playerminimap():
    def __init__(self, minimap, glossary, mode, reveal):
        self.minimap = minimap
        self.glossary = glossary
        self.map = [[self.glossary[''] for x in range(len(self.minimap[0]))] for y in range(len(self.minimap))]
        self.reveal_wanted = reveal
        self.total_reveal = False
        self.partial_reveal = False
        self.forgetting = False
        self.mode = mode
        self.build()

    def build(self):
        self.reveal()
        if self.total_reveal:  # 여기다가 true/false넣기
            return
        for y in range(len(self.minimap)):
            for x in range(len(self.minimap[0])):
                if self.minimap[y][x] != self.glossary['']:  # if tile exists (not empty string)
                    # self.map[y][x] = '| ? |'
                    # self.map[y][x] = '  ?  '
                    # self.map[y][x] = '[ ? ]'
                    self.map[y][x] = '[ ■ ]'
                    # self.map[y][x] = '[ \033[40m \033[0m ]'

    def reveal(self):
        if self.reveal_wanted == 'all':
            self.map = self.minimap
            self.total_reveal = True
        elif self.reveal_wanted == 'partial':
            self.partial_reveal = True
        elif self.reveal_wanted == 'forgetting':
            self.partial_reveal = True
            self.forgetting = True
        else:
            pass

    # warning: must use after load_tiles()
    def load(self, player_x, player_y):
        near_player = [(player_x, player_y + 1), (player_x + 1, player_y), (player_x - 1, player_y),
                       (player_x, player_y - 1)]
        print('=' * 30, 'Mini Map', '=' * 30)
        for y in range(len(self.minimap)):
            for x in range(len(self.minimap[0])):
                if y == player_y and x == player_x:
                    print('[ \033[95m{}\033[0m ]'.format('☨'), end='')

                elif (x, y) in near_player and self.partial_reveal:  # partial reveal조건이 켜져있는 경우에만
                    print(self.minimap[y][x], end='')

                else:  # 나머지 cell에 대해서 (플레이어의 위치나 플레이어 근처 위치가 아닌 타일의 경우)
                    if self.forgetting:
                        if self.map[y][x] != self.glossary['']:  # 동굴 벽이 아니라면 '가려진 방'을 display
                            print('[ ■ ]', end='')  # 가려서 보여줌
                        else:
                            print(self.glossary[''], end='')  # 방이 아닌 유일한 경우는 '', 즉, None tile.
                    else:  # self.forgetting이 아니거나, glossary에서 ''인 경우, 기존의 '     '를 프린트 해 주어야 함.
                        print(self.map[y][x], end='')

            print()
        print('=' * 80)

    def update(self, x, y):  # tells minimap where-(x,y)- a player visited
        tile = tile_exists(x, y)
        # print(tile.name=='GoldRoom')
        if tile.name.startswith('Find') or tile.name == 'GoldRoom':
            self.minimap[y][x] = '[{}]'.format(
                self.glossary['EmptyCavePath'])  # item collected! ==> it is now empty in the minimap
        self.map[y][x] = self.minimap[y][x]  # revealed!


def tile_exists(x, y):
    return _world.get((x, y))
