from abc import ABCMeta, abstractmethod
from Ability import Ability
from TableMaker import TableMaker
from itertools import zip_longest
__author__ = 'JamesG'


class Character:

    __metaclass__ = ABCMeta
    space_count = ""
    cut_count = 0

    def __init__(self, name, health, brawl, shoot,
                 dodge, might, finesse, cunning):
        self.name = name
        self.health = health
        self.brawl = brawl
        self.shoot = shoot
        self.dodge = dodge
        self.might = might
        self.finesse = finesse
        self.cunning = cunning

    def get_skill(self, skill):
        # better way?
        level_dict = [Ability.level1,
                      Ability.level2, Ability.level3]
        for dic in level_dict:
            for x, value in dic.items():
                if x.lower() == skill.lower():
                    return value

        # bad way?
        # for (x, x_val), (y, y_val), (z, z_val) in \
        #         zip_longest(Ability.level1.items(),
        #                     Ability.level2.items(),
        #                     Ability.level3.items()):
        #     if x is not None and x.lower() == skill.lower():
        #         return x_val
        #     if y is not None and y.lower() == skill.lower():
        #         return y_val
        #     if z is not None and z.lower() == skill.lower():
        #         return z_val

    def more_skills(self):
        skills = ""
        if self.__class__.__name__ == "Leader" or \
           self.__class__.__name__ == "SideKick":
            skills += "\n" + self.second_skill + ": " +\
                      self.get_skill(self.second_skill)
        if self.__class__.__name__ == "Leader":
            skills += "\n" + self.third_skill + ": " + \
                      self.get_skill(self.third_skill)

        return skills

    def __str__(self):
        return TableMaker.table_maker(False, self.__class__.__name__,
                                      self.name,
                                      self.health, self.brawl,
                                      self.shoot, self.dodge, self.might,
                                      self.finesse, self.cunning) + "\n"\
            "{}: {}".format(self.first_skill,
                            self.get_skill(self.first_skill)) + \
            self.more_skills()


class Leader(Character):
    def __init__(self, name, health, brawl, shoot, dodge, might,
                 finesse, cunning):
        Character.__init__(self, name, health, brawl, shoot, dodge,
                           might, finesse, cunning)
        self.first_skill = None
        self.second_skill = None
        self.third_skill = None
        # The parent constructor can also be invoke by
        # using, super().__init__(name, brawl...) no need to include self


class SideKick(Character):
    def __init__(self, name, health, brawl, shoot, dodge, might,
                 finesse, cunning):
        Character.__init__(self, name, health, brawl, shoot, dodge,
                           might, finesse, cunning)
        self.first_skill = None
        self.second_skill = None


class Ally(Character):
    def __init__(self, name, health, brawl, shoot, dodge, might,
                 finesse, cunning):
        Character.__init__(self, name, health, brawl, shoot, dodge,
                           might, finesse, cunning)
        self.first_skill = None


class Follower(Character):
    def __init__(self, name, health, brawl, shoot, dodge, might,
                 finesse, cunning):
        Character.__init__(self, name, health, brawl, shoot, dodge,
                           might, finesse, cunning)
        self.first_skill = None
