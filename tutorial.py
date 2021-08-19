'''
튜토리얼 객체

처음 유저에게 몇 가지 action을 시킨다.
0 동굴에서 탈출하는게 목적임. 동굴 탈출하기!
1 미니맵 - 타일을 이동하는 action을 선택하면, 이동 후의 미니맵을 보여준다.
*: 나의 g현재 위치
?: 내가 방문하지 않은 타일
S,F...: 방 이름의 앞 글자를 딴 이니셜. 서로 같은 이니셜이지만, 실제로는 다른 방일 수도 있다.
미니맵은 어디까지나 탐험을 도와주는 보조 기능일 뿐, 당신의 실력으로 탈출해야 한다!

2 인벤토리 확인 - 내가 가진 물건들과 간략한 설명을 보여주는 칸이다. 물건의 데미지를 보고 싶다거나, 금화가 얼마나 있는지 알고 싶을 때 열어보자.
3 스테이터스 확인 - 스테이터스는 나의 각종 능력치를 올려줘 동굴탈출을 더 원활하게 만들어 준다.
레벨업시 스킬포인트를 하나 준다. 한번 찍으면 바꿀 수 없으니 신중하게 선택하도록 하자.
4 몬스터 도감 열기 - 지금까지 만났던 몬스터들을 적어둔 도감이다. 몬스터의 체력과 공격력을 대강 알 수 있다.
5 음식 먹기 - 치유를 할 수도 있고, 경험치를 얻을 수도 있다.
6 다른 타일로 이동하기 - 다른 타일로 이동하면 해당 타일의 이벤트가 발생한다.

타일을 이동할 때 마다 (이전에 방문한 적이 없는 타일이면) 타일을 간략히 소개한다. - 이때, 원래 타일에 있던 intro_text대신 튜토리얼 대사가 나오도록 한다. 그럼 끝!
금 타일 - 금을 자동으로 제공한다
단검 발견 방 - 무기를 발견한다: 이 무기를 사용해서 동굴의 몬스터를 잡을 수 있음
전갈의 방 - 첫 전투. z를 눌러 공격을 선택하고, 무기를 정하면 공격됨/ f를 누르면 도망을 갈 수 있지만, 아직 flee 확률이 {} % 밖에 되지 않으니 성공하기 힘든다.
일단 끝까지 공격하자/ 죽으면 몹의 드롭들이 나온다.
'''
import items


class Tutorial():
    def __init__(self):
        self.language = None
        self.tutorial_tiles_intro_dic = {}
        self.comment = {'Korean': '좋아요!', 'English': 'Good!'}
        self.starting_message = {'Korean': '게임을 시작합니다!\n', 'English': "Let's start the game!\n"}
        self.intro_texts = {'Korean': '''
        동굴에 제 발로 들어오신 것을 환영합니다!
        여긴 튜토리얼 동굴입니다. 

        ======= 목표 [ ⚐ ] ========
        동굴에서 탈출하는 것입니다.

        ===== 행동 방법 [ ☨ ] =====
        플레이어가 할 수 있는 행동은 선택지로 제공됩니다.
        선택지 왼쪽에 있는 단축키를 타이핑하면 행동을 할 수 있습니다.
        기본적인 움직임(앞, 뒤, 오른쪽, 왼쪽) 및 인벤토리 확인, 스테이터스 확인, 동굴 몬스터 도감 보기, 음식먹기 등이 가능합니다.
        인벤토리 사이즈는 현재 무제한이니 아이템이 넘친다는 걱정은 하지 않아도 됩니다.

        ======= 미니맵 [ ■ ] =======
        이동할 때마다 미니맵이 갱신됩니다. 
        아래의 범례를 참고하십시오.

        [ \033[95m☨\033[0m ] : 나의 현재 위치
        [ ■ ] : 내가 방문하지 않은 타일
        [ ☼ ] :동굴 입구
        [ ⚐ ] : 동굴 출구!

        미니맵은 어디까지나 탐험을 도와주는 보조 기능일 뿐, 당신의 실력(기억력과 결단력)으로 탈출해야 합니다!

        === 스테이터스(스텟) [ 'vs' ]===
        이 게임에는 플레이어의 능력치를 증가시켜주는 스테이터스가 있습니다.
        플레이어가 레벨업 하면 스테이터스를 1씩 올릴 수 있습니다. 
        다만 한번 올리면 번복이 불가하니 신중하게 선택하십시오. 
        레벨이 높을수록 레벨업에 필요한 경험치량이 (∝log) 증가합니다.
        현재 민첩, 방어, 학습, 물리 공격, 마법 공격, 공격 안정성의 6가지가 존재합니다.
        튜토리얼을 하기 전에 플레이어의 기본 레벨을 결정할때 미리 레벨업 해둘 수 있습니다.
        각종 스텟에 대한 더 자세한 설명을 알고 싶다면 선택지의 ['vs': View status] 에 해당하는 'vs'를 입력하십시오.

        ======= 도감 [ 'vm' ] ========   
        지금까지 만났던 몬스터들을 적어둔 도감입니다. 
        해당 몬스터의 체력과 공격력을 대강 알 수 있습니다. 
        다만, 같은 이름의 몬스터라도 정보가 조금씩 다를 수 있으니 주의하십시오.

        ======= 먹기(힐) [ 'e' ] ======== 
        치료하는 방법은 음식을 먹는 것입니다. 
        당신의 인벤토리에는 사과가 있으니, 나중에 그걸 드셔보십시오.
        전투 중이 아니라면 언제든 먹어도 상관 없습니다. 
        전투 중에 드신다면, 해당 턴에는 몬스터를 공격할 수 없습니다.

        ======= 공격 [ 'z'/'x' ] ========
        몬스터가 있는 타일로 이동하면 몬스터가 나타납니다.
        선택지에 ['z': attack] 가 생기며, 'z'를 입력한 후 사용자가 원하는 무기를 선택지에서 선택하면 됩니다.
        또는, 직전에 사용했던 무기를 그대로 사용하여 공격하고 싶은 경우 ['x': Attack with previous option] 을 고르면 됩니다.
        무기의 종류와 정보는 전투 중일때를 제외하면, 인벤토리 'i'를 통해 언제든지 볼 수 있습니다.

        ======= 타일(방) [   ] ========
        마지막으로 타일입니다. 
        이 게임은 플레이어가 타일을 이동하며 사건이 발생합니다.
        미니맵에 나와있는 칸의 단위가 타일(방)입니다.
        플레이어가 가보지 않은 타일은 뭐가 있는지 알 수 없지만 (미니맵에서 가려집니다), Easy나 Normal,Hard 모드는 예외입니다.
        Easy 모드에서는 모든 타일이 시작부터 미니맵에 공개됩니다.
        Normal, Hard 모드에서는 가보지 않아도 플레이어의 상,하,좌,우의 타일은 미니맵에서 미리볼수 있습니다. 마치 탐험가가 호롱불을 들고 있어 주변을 빛추어 알 수 있는 것 처럼요.

        흔한 타일로는 '빈(비어있는) 동굴길', '금화의 방', '몬스터의 방',  '아이템의 방', '잠긴 방' 등이 있습니다.
        동굴길은 자신의 독백을 들으실 수 있습니다.
        금화의 방엔 소량의 금화가 있습니다.
        몬스터의 방엔 몬스터가 숨어 있어서, 당신을 공격할 것입니다. 현명하게 대처하십시오.
        아이템의 방은 플레이어에게 공짜 아이템을 제공합니다.
        잠긴 방은 잠겨있습니다. 열쇠의 방(아이템의 방의 일종)을 찾아서 열쇠를 얻던지, 열쇠를 가지고 있는 몬스터를 죽여서 빼앗던지 하십시오.
        주의할 점은, 해당 방에 맞는 열쇠가 있어야 그 방을 열 수 있다는 것입니다.

        ===== 점수 계산 [ - ] =====
        게임이 끝나면 점수를 받게 되며, 이는 leader board (간단한 txt 파일) 에 기록됩니다.
        현재 버전의 점수 계산은 다음과 같이 수행됩니다. (첫 번째 숫자로 반올림 함)
        
        점수 = (세팅 점수) + (칭호 점수)
        
        세팅 점수 = (map에 대한 점수) * (gamemode에 대한 점수) * (0.9)^(핸디캡 개수)
        
        칭호 점수 = (획득한 칭호의 수) - 2 * (획득한 '킬러' 칭호의 수)
        
        참고: 인벤토리에 일정량의 특정한 '몹 드롭'이 있을 때 해당 몹에 대한 '킬러' 칭호를 얻습니다.
        불필요한 킬을 줄이는 것도 프로의 자질입니다!
        원하는 경우 게임 한판이 끝났을 때 leader board 를 볼 수 있습니다.

        ==== 마무리 멘트 [ ♪ ] =====
        작은 선물을 당신의 주머니에 넣어두었습니다. 
        'i'를 입력하여 인벤토리에서 확인하십시오. 
        행운을 빕니다!

        아래는 미니맵입니다.
        ''',

                            'English': '''
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
        The tiles you haven't been to is considered unknown and is not shown to player, except three gamemodes; Easy, Normal, Hard.
        In Easy mode, all tiles are visible from the beggining.
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
        This is my little present. 
        Check it in your inventory by typing 'i'. 
        Good luck!

        Below is a minimap.
        '''}

    # def ask_language(self):
    #     lang_selection = {'1': 'Korean', '2': 'English'}
    #     languages = list(lang_selection.values())
    #     print("Select tutorial language: ")
    #     hotkeys = list(lang_selection.keys())
    #     print("{}: {}\n{}: {}".format(hotkeys[0],lang_selection[hotkeys[0]],hotkeys[1],lang_selection[hotkeys[1]]))
    #     user_input = ''
    #     while user_input not in ['1','2']:
    #         user_input = input("Select (1 or 2): ")
    #     self.language = lang_selection[user_input]
    #     print('='*70)

    def set_language(self, lang):
        self.language = lang

    def intro(self, player):
        print(self.intro_texts[self.language])
        player.give(items.Bow(), items.Arrow(), items.Wand(), items.RabbitFoot(100))
        print()
        player.show_minimap()
        self.key_input()

    def key_input(self):
        question = {'Korean': "아무거나 눌러 튜토리얼을 종료하십시오: ", 'English': "Type anything to continue: "}
        user_input = input(question[self.language])
        print(self.comment[self.language])
        print(self.starting_message[self.language])
        print('='*70)
