# player.do_action 에서 쓰임!
from player import Player


class Action():
    def __init__(self, method, name, hotkey, **kwargs):
        self.method = method
        self.hotkey = hotkey
        self.name = name
        self.kwargs = kwargs

    def __str__(self):
        return "{}: {}".format(self.hotkey, self.name)


# class EnterCave(Action):
#     def __init__(self):
#         super().__init__(method=None, name='entered cave', hotkey='')


class MoveUp(Action):
    def __init__(self):
        super().__init__(method=Player.move_up, name='Move up', hotkey='w')


class MoveDown(Action):
    def __init__(self):
        super().__init__(method=Player.move_down, name='Move down', hotkey='s')


class MoveRight(Action):
    def __init__(self):
        super().__init__(method=Player.move_right, name='Move right', hotkey='d')


class MoveLeft(Action):
    def __init__(self):
        super().__init__(method=Player.move_left, name='Move left', hotkey='a')


class ViewInventory(Action):
    """Prints the player's inventory"""

    def __init__(self):
        super().__init__(method=Player.print_inventory, name='View my pocket(inventory)', hotkey='i')

class ViewMobpedia(Action):
    def __init__(self):
        super().__init__(method=Player.print_viewed_mobs, name='View mobs seen by me', hotkey='vm')

class ViewStatus(Action):
    """Prints the player's status"""

    def __init__(self):
        super().__init__(method=Player.print_status, name='View my current status', hotkey='vs')

class ViewMinimap(Action):
    """Prints minimap"""

    def __init__(self):
        super().__init__(method=Player.show_minimap, name='View minimap', hotkey='m')

class Attack(Action):
    def __init__(self, enemy):
        super().__init__(method=Player.attack, name="Attack", hotkey='z', enemy=enemy)

class Flee(Action):
    def __init__(self, tile):
        super().__init__(method=Player.flee, name="Flee", hotkey='f', tile=tile)

class Eat(Action):
    def __init__(self):
        super().__init__(method=Player.eat, name="Eat items in my pocket(inventory)", hotkey='e')

class Talk(Action):
    def __init__(self, npc):
        super().__init__(method=Player.talk, name="Talk to NPC", hotkey='t', npc = npc)

class Trade(Action):
    def __init__(self, npc):
        super().__init__(method=Player.trade, name="Trade", hotkey='v', npc = npc)

class Sell(Action):
    def __init__(self, npc):
        super().__init__(method=Player.sell, name="Sell", hotkey='sl', npc = npc)

class AttackPreviousOption(Action):
    def __init__(self, enemy):
        super().__init__(method=Player.attack_with_previous_option, name="Attack with previous option", hotkey='x', enemy=enemy)
