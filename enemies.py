import random, math
import items, util

'''
Enemy's possible actions should be written here.
That is, enemy must determine which attack and how much damage it will do in this module.

However, note that actions are executed on the tile.py.
=> Make a 'corresponding tile' in order to place the enemy mobs!
'''


class Enemy:
    def __init__(self, name, description, hp, damage, death_message='...', drop_prob_dict=None, xp=0):
        self.name = name
        self.description = description
        self.hp = hp
        self.hpmax = hp
        self.damage = damage
        self.death_message = death_message
        self.drop_prob_dict = drop_prob_dict
        self.xp = xp
        self.skill_list = []
        self.skills = len(self.skill_list)

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return "{}\n{}\nHP: \033[91m{}\033[0m\nDamage: {}".format(self.name, self.description, self.hpmax, self.damage)

    def death(self, player):  # death message + item drop + player xp + player.check_level_up()
        print('{}: {}'.format(self.name, self.death_message), '\n')
        if self.drop_prob_dict:
            for drop in self.drop_prob_dict.keys():
                drop_prob = self.drop_prob_dict[drop]
                if util.random_success(drop_prob):
                    player.give(drop)
                    print('Found {}!'.format(drop.name))
        player.gain_xp(self.xp)

    def bleed_player(self, player, probability):
        if util.random_success(probability):
            player.make_bleed()
            print("You are \033[91m{}\033[0m!".format("bleeding"))


class Scorpion(Enemy):
    def __init__(self):
        self.number = random.randint(1, 3)
        many_suffix = ''
        if self.number > 1:
            many_suffix = 's'
        super().__init__(name='{} Scorpion{}'.format(self.number, many_suffix), description="It's sting is very itchy!",
                         hp=5 * self.number,
                         damage=1 * self.number, death_message='KIAAAA...', drop_prob_dict={items.ScorpionSting(): 0.8},
                         xp=1 * self.number)


class Bandit(Enemy):
    def __init__(self):
        self.proficiency = 1 + random.uniform(0, 1)
        super().__init__(name='Bandit', description='Fierce human, eager to steal some gold. Uses dagger.', hp=20,
                         damage=math.floor(4 * self.proficiency), death_message='Huff! Huff...',
                         drop_prob_dict={items.Dagger(): 0.1, items.Gold(25): 0.5}, xp=7)
        self.skill_list = [self.deep_blade]
        self.skills = len(self.skill_list)

    def deep_blade(self, player):
        blade_damage = self.damage * 2
        script = 'Huff!'
        if player.take_enemy_damage(blade_damage):
            print("{}: {}".format(self.name, script))
            print("The blade cut deeply. Worth {} damage. \n{} HP: \033[91m{}\033[0m".format(blade_damage, player.name,
                                                                                             round(player.hp, 1)))
            bleeding_probability = 0.05
            self.bleed_player(player, bleeding_probability)


class RetiredMage(Enemy):
    def __init__(self):
        self.proficiency = 1 + random.uniform(0, 1)
        super().__init__(name='Retired mage', description='A very dangerous person.', hp=15,
                         damage=math.floor(10 * self.proficiency), death_message='Phew~...',
                         drop_prob_dict={items.Wand(): 0.05, items.Gold(50): 0.15}, xp=18)


class Slate(Enemy):
    def __init__(self):
        self.proficiency = 1 + random.uniform(0, 0.5)
        super().__init__(name='Slate the living blade',
                         description="The product of a magical explosion. Has 2 blade hands.", hp=50,
                         damage=math.floor(5 * self.proficiency), death_message='Sizzle... swizzle...',
                         drop_prob_dict={items.Gold(100): 0.1, items.Dagger(): 0.5}, xp=20)
        self.skill_list = [self.blade_storm]
        self.skills = len(self.skill_list)

    def blade_storm(self, player):  # | | 이런 이중 칼을 들고있는 몬스터..!
        blade_scratch_numbers = [2, 4, 6]
        scratch_number = random.choice(blade_scratch_numbers)
        blade_damage = scratch_number * self.damage
        script = 'Swizzle...! ' * scratch_number
        if player.take_enemy_damage(blade_damage):
            print("{}: {}".format(self.name, script))
            print("Blade storm was worth {} damage. \n{} HP: \033[91m{}\033[0m".format(blade_damage, player.name,
                                                                                       round(player.hp, 1)))
            bleeding_probability = 0.05 * scratch_number
            self.bleed_player(player, bleeding_probability)


class Gandalph(Enemy):
    def __init__(self):
        super().__init__(name='\033[95m{}\033[0m'.format('Gandalph the grey'),
                         description="What? Gandalph..? Why the 'cave' is he here?", hp=200,
                         damage=15, death_message='For even the very wise cannot see all ends...',
                         drop_prob_dict={items.Staff('\033[95m{}\033[0m'.format('『charming』')): 1, items.Gold(200): 1},
                         xp=100)
        self.skill_list = [self.heal, self.fireBall]
        self.skills = len(self.skill_list)

    # helper method for heal
    def heal_calc(self, amt):
        self.hp = min(self.hpmax, self.hp + amt)

    def heal(self, player):
        self.heal_calc(20)
        print("{} healed himself!\n{} HP: \033[91m{}\033[0m".format(self.name, self.name, round(self.hp, 1)))

    def fireBall(self, player):
        fireBall_damage = random.randint(10, 40)
        if player.take_enemy_damage(fireBall_damage):
            print("{} fired a fireball worth {} damage. \n{} HP: \033[91m{}\033[0m".format(self.name, fireBall_damage,
                                                                                           player.name,
                                                                                           round(player.hp, 1)))


class HarryPotter(Enemy):
    def __init__(self):
        super().__init__(name='\033[95m{}\033[0m'.format('Harry Potter'),
                         description="A graduate of the Hogwart... as far as I know.", hp=100,
                         damage=20,
                         death_message='Numbing the pain for a while will make it worse when you finally feel it...',
                         drop_prob_dict={items.Wand(): 1, items.Gold(100): 1, items.Key('9999'): 1}, xp=100)
        self.skill_list = [self.heal, self.crusio, self.AvadaKedavra]
        self.skills = len(self.skill_list)

    # helper method for heal
    def heal_calc(self, amt):
        self.hp = min(self.hpmax, self.hp + amt)

    def heal(self, player):
        self.heal_calc(20)
        print("{} healed himself!\n{} HP: \033[91m{}\033[0m".format(self.name, self.name, round(self.hp, 1)))

    def crusio(self, player):
        crusio_damage = random.randint(25, 35)
        if player.take_enemy_damage(crusio_damage):
            print("{}: Crusio!".format(self.name))
            print("Spell was worth {} damage. \n{} HP: \033[91m{}\033[0m".format(crusio_damage, player.name,
                                                                                 round(player.hp, 1)))

    def AvadaKedavra(self, player):  # can cast only once!
        AvadaKedavra_damage = random.randint(99,
                                             99)  # Sudden death spell. Player needs to have high defence status to not instant-die.
        if player.take_enemy_damage(AvadaKedavra_damage):
            print("{}: Avada-Kedavra!".format(self.name))
            print("Spell was worth {} damage. \n{} HP: \033[91m{}\033[0m".format(AvadaKedavra_damage, player.name,
                                                                                 round(player.hp, 1)))
            self.skill_list.remove(self.AvadaKedavra)
            self.skills = len(self.skill_list)


###################################################################################################################### In progress...
class DrStrange(Enemy):
    def __init__(self):
        super().__init__(name='Dr.Strange', description="", hp=100,
                         damage=20, death_message='', drop_prob_dict={}, xp=100)
        self.skill_list = []
        self.skills = len(self.skill_list)
