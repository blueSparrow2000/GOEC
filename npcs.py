import random
from enemies import Enemy
import items
'''
NPC's possible actions should be written here.
That is, NPC must determine what they do here.
However, note that actions are executed on the tile.py.

'''

class NPC(Enemy):
    def __init__(self, name, description, hp, damage,death_message='...', drop_prob_dict=None, xp = 0):
        self.maxhp = hp
        self.talks = ['...']
        super().__init__(name, description,  hp, damage,death_message, drop_prob_dict, xp)

    def is_attacked(self):
        return self.maxhp > self.hp

    def talk(self):
        return "{}: ".format(self.name) + random.choice(self.talks)

    def sell_talk(self,sentence):
        print('''
        {}: {}
        '''.format(self.name, sentence))

    def get_sell_ratio(self):
        self.sell_talk("I don't buy stuff!")
        return None

class Merchant(NPC):
    def __init__(self):
        self.item_list = [items.Dagger(), items.Shield(0.2), items.Bow(), items.Arrow(), items.Apple(), items.BeefJerky() ,items.Pill(), items.Styptic(), items.XpOrb(10), items.XpOrb(20)]
        super().__init__(name='Merchant', description="Rich, but he is also stuck in the same cave...", hp=20,
                         damage=2,death_message='...', drop_prob_dict={items.Gold(100):0.9}, xp = 10)
        self.talks = ["Please go ahead and look at these fantastic tools!", "Need any food?", "Money talks!",
                               "The items I sell are the cheapest in the cave!"]

    def show_trades(self,show = True):
        if show:
            print('=' * 30,'Item list','=' * 30)
            for item in self.item_list:
                print(item, end='\n\n')
            print('=' * 70)
        return self.item_list

    def get_sell_ratio(self):
        self.sell_talk("I buy anything you sell with 90% of the value! Haha!")
        return 0.9

class Wanderer(NPC):
    def __init__(self):
        super().__init__(name='Wanderer', description="You have no idea how long (s)he has been in the cave, but you can feel the traces of the years on his(her) face...", hp=80,
                         damage=5, death_message="Ahh... this is my last...", drop_prob_dict={items.Gold(100): 0.5}, xp=100)
        self.talks = ["...","Get away from me!","What do you want!","Leave me alone!"]

    def get_sell_ratio(self):
        self.sell_talk("I say 80%...")
        return 0.8

class Guard(NPC):
    def __init__(self):
        super().__init__(name='???', description="I see a man wearing iron armor. Why is he in the cave?", hp=1000,
                         damage=6, death_message="I couldn't fulfill my duty until the end...", drop_prob_dict={items.Gold(50): 0.75,items.Shield(0.2):1}, xp=100)
        self.talks = ['...','Do you want to confess now?','Get off.']

    def revealed(self):
        self.name = '\033[96m{}\033[0m'.format('Prison Guard')