import Character
import re
import sys
from Ability import Ability, Dice
from View import View

__author__ = 'JamesG'


class League(object):
    view = View()

    def __init__(self):
        self.leader = Character.Leader
        self.name = ""
        self.limit = 10
        self.league_slot = 0
        self.sidekick_count = 1
        self.ally_count = 1
        self.follower_count = 1
        self.sidekick_members = {}
        self.ally_members = {}
        self.follower_members = {}
        self.has_leader = False
        self.league_status = ""
        self.is_creating_league = False

    def league_information(self):

        if self.is_creating_league and not self.has_leader:
            print("------------------------------ Create League -----------"
                  "-------------------\n" +
                  "Type <character_role> followed by the attributes and "
                  "skills using the format and order below:\n" +
                  "name, health, brawl, shoot, dodge, might, finesse, "
                  "cunning, 1st_Skill, 2nd_Skill, 3rd_Skill\n" +
                  "(eg leader Kim Jong-un, d10, 3d8, 3d10, 3d10, 2d8, 3d10, "
                  "2d10, Sharp, Deadeye, Agile)")
        elif self.has_leader is True:
            if not self.has_leader:
                leader_status = "You have not created a leader yet"
            else:
                leader_status = "You have a leader"
            display = "You have " + str(10 - self.league_slot) + \
                      " slots left to use, " + leader_status + "\n"
            print(display)
        elif self.is_creating_league is False \
                and self.has_leader is False and self.league_slot == 0:
            self.view.start()

    def start_create(self, name):

        try:
            if name != "":
                self.name = name
                self.is_creating_league = True
                self.league_information()
                print("Your League\'s name, is " + str(self.name) + "\n")
            else:
                raise InvalidInput("Please enter the name, you "
                                        "entered nothing!!")
        except InvalidInput as err:
            print(err)

    def add_leader(self, attributes_skills):
        try:
            if self.is_creating_league is True \
                    and self.has_leader is False:
                temp_list = self.split_user_input(attributes_skills)
                self.create_new_league("leader", temp_list)
            elif self.has_leader is True:
                raise InvalidAction("You already created a leader "
                                         "named \"" +
                                         str(self.leader.name) +
                                         "\", please create other "
                                         "character")
            else:
                raise InvalidAction("You must enter the name "
                                         "of the League "
                                         "first before you can start "
                                         "creating "
                                         "characters!!!(type create"
                                         " <league_name>)")
        except InvalidAction as err:
            print(err)

    def add_sidekick(self, attributes_skills):
        try:
            if self.has_leader is True:
                temp_list = self.split_user_input(attributes_skills)
                self.create_new_league("sidekick", temp_list)
            elif self.is_creating_league is False:
                raise InvalidAction("You must enter the name "
                                         "of the League "
                                         "first before you can start "
                                         "creating characters!!!"
                                         "(type create <league_name>)")
            else:
                raise InvalidAction("Please create a leader first,"
                                         " you have not created a "
                                         "leader yet!!!")
        except InvalidAction as err:
            print(err)

    def add_ally(self, attributes_skills):
        try:
            if self.has_leader is True:
                temp_list = self.split_user_input(attributes_skills)
                self.create_new_league("ally", temp_list)
            elif self.is_creating_league is False:
                raise InvalidAction("You must enter the name "
                                         "of the League "
                                         "first before you can start "
                                         "creating characters!!!(type "
                                         "create <league_name>)")
            else:
                raise InvalidAction("Please create a leader first, "
                                         "you have not created a "
                                         "leader yet!!!")
        except InvalidAction as err:
            print(err)

    def add_follower(self, attributes_skills):
        try:
            if self.has_leader is True:
                temp_list = self.split_user_input(attributes_skills)
                self.create_new_league("follower", temp_list)
            elif self.is_creating_league is False:
                raise InvalidAction("You must enter the name "
                                         "of the League "
                                         "first before you can start "
                                         "creating characters!!!"
                                         "(type create <league_name>)")
            else:
                raise InvalidAction("Please create a leader first, "
                                         "you have not created a "
                                         "leader yet!!!")
        except InvalidAction as err:
            print(err)

    def create_new_league(self, new_char, attributes_skills):

        if new_char == "leader":
            if self.has_leader is False:
                self.create_new_character("leader",
                                          attributes_skills)
            else:
                print("You already created a leader<name>, "
                      "please create other character")

        elif new_char == "sidekick":
            try:
                if self.league_slot <= 7:
                    self.create_new_character("sidekick",
                                              attributes_skills)
                    if self.league_slot == 10:
                        print("***You have successfully created "
                              "a new league***")
                elif self.league_slot > 7:
                    raise InvalidAction("Cannot create anymore "
                                             "sidekicks you only have  " +
                                             str(10 - self.league_slot) +
                                             " slots left(requires 3 more)" +
                                             "Please create an ally or "
                                             "follower")
            except InvalidAction as err:
                print(err)

        elif new_char == "ally":
            try:
                if self.league_slot <= 8:
                    self.create_new_character("ally",
                                              attributes_skills)
                    if self.league_slot == 10:
                        print("***You have successfully created a "
                              "new league***")
                elif self.league_slot > 8:
                    raise InvalidAction("Cannot create anymore "
                                             "allies you only have  " +
                                             str(10 - self.league_slot) +
                                             " slots left"
                                             "(requires 2 more)" +
                                             "Please create a follower")
            except InvalidAction as err:
                print(err)

        elif new_char == "follower":

            try:
                if self.league_slot < 10:
                    self.create_new_character("follower",
                                              attributes_skills)
                    if self.league_slot == 10:
                        print("***You have successfully created "
                              "a new league***")
                elif self.league_slot >= 10:
                    raise InvalidAction("Cannot create anymore "
                                             "follower you only have  " +
                                             str(10 - self.league_slot) +
                                             " slots left"
                                             "(requires 1 more)")
            except InvalidAction as err:
                print(err)

    def split_user_input(self, user_input):
        temp_list = []
        word = ""
        count = 0
        for item in user_input:
            count += 1
            if item != ",":
                word += str(item)
                if count == len(user_input):
                    temp_list.append(word.lstrip())
            elif item == ",":
                temp_list.append(word.lstrip())
                word = ""
        return temp_list

    def check_level1_ability(self, item):
        count = 0
        for key, value in Ability.level1.items():
            if item.lower() == key.lower():
                count += 1
                break
        return count

    def check_level2_ability(self, item):
        count = 0
        for key, value in Ability.level2.items():
            if item.lower() == key.lower():
                count += 1
                break
        return count

    def check_level3_ability(self, item):
        count = 0
        for key, value in Ability.level3.items():
            if item.lower() == key.lower():
                count += 1
                break
        return count

    def wrong_skill_input(self, role, invalid_input,
                          ability_count, count, user_input_count):

        if invalid_input:
            print("Please enter the abilities and skills for the " +
                  role + " again, (type help " + role + ")")
        elif count == 0:
            print("You entered nothing!!!")
        else:
            print("Please enter " + str(ability_count) +
                  " abilities, you entered " + str(user_input_count))

    def check_ability_input(self, role, temp_list):

        invalid_input = False
        count = 0

        for item in temp_list:
            ini_count = count
            count += self.check_level1_ability(item)
            if role != "follower":
                if count == ini_count:
                    count += self.check_level2_ability(item)
                    if role == "leader" or role == "sidekick":
                        if count == ini_count:
                            count += self.check_level3_ability(item)
            if count == ini_count:
                invalid_input = True
                if role == "leader" or role == "sidekick":
                    print("\"" + item + "\"" + " is not an "
                                               "ability")
                elif role == "ally":
                    print("\"" + item + "\"" + " is not a "
                                               "level 1 or "
                                               "level 2 ability")
                elif role == "follower":
                    print("\"" + item + "\"" + " is not a "
                                               "level 1 ability")
        else:
            if role == "leader":
                if count != 3 or invalid_input is True:
                    self.wrong_skill_input(role, invalid_input, 3,
                                           count, len(temp_list))
                    return 0
                else:
                    return temp_list
            elif role == "sidekick":
                if count != 2 or invalid_input is True:
                    self.wrong_skill_input(role, invalid_input, 2,
                                           count, len(temp_list))
                    return 0
                else:
                    return temp_list
            elif role == "ally":
                if count != 1 or invalid_input is True:
                    self.wrong_skill_input(role, invalid_input, 1,
                                           count, len(temp_list))
                    return 0
                else:
                    return temp_list
            elif role == "follower":
                if count != 1 or invalid_input is True:
                    self.wrong_skill_input(role, invalid_input, 1,
                                           count, len(temp_list))
                    return 0
                else:
                    return temp_list

    def check_duplicates(self, skills):
        i = 0
        if len(skills) == 3:
            for x in skills:
                if i == 2:
                    if skills[0].lower() == skills[2].lower():
                        return skills[2]
                if i < 2 and x.lower() == skills[i + 1].lower():
                    return x
                i += 1
            else:
                return 0

        elif len(skills) == 2:
            if skills[i].lower() == skills[i + 1].lower():
                return skills[i]
            else:
                return 0
        else:
            return 0

    def set_character_skills(self, role, skills):

        # implement boolean checkpoint if instance is created
        if role == "leader":
            try:
                temp_list = self.check_ability_input(role, skills)
                if temp_list == 0:
                    raise InvalidInput("leader abilities")
                else:
                    if self.check_duplicates(temp_list) != 0:
                        raise InvalidAction("Please no duplicates " +
                                                 "\"" +
                                                 str(
                                                     self.check_duplicates(
                                                         temp_list)) +
                                                 "\"")
                    else:
                        self.leader.first_skill = temp_list[0]
                        self.leader.second_skill = temp_list[1]
                        self.leader.third_skill = temp_list[2]
                        self.bonus_die(self.leader, temp_list)
                        self.has_leader = True
                        self.league_information()
                        print("You have successfully added a leader")
            except InvalidAction as err:
                print(err)
                print("")
            except InvalidInput as err:
                print(err)
                print("")

        elif role == "sidekick":
            try:
                temp_list = self.check_ability_input(role, skills)
                if temp_list == 0:
                    raise InvalidInput("sidekick abilities")
                else:
                    if self.check_duplicates(temp_list) != 0:
                        raise InvalidAction("Please no duplicates " +
                                                 "\"" +
                                                 str(
                                                     self.check_duplicates(
                                                         temp_list)
                                                 ) +
                                                 "\"")
                    else:
                        new_side_kick = \
                            self.sidekick_members["sidekick" +
                                                  str(self.sidekick_count)]
                        new_side_kick.first_skill = temp_list[0]
                        new_side_kick.second_skill = temp_list[1]
                        self.sidekick_count += 1
                        self.league_slot += 3
                        self.bonus_die(new_side_kick, temp_list)
                        self.league_information()
                        print("You have successfully added a sidekick")
            except InvalidInput as err:
                print(err)
                print("")
            except InvalidAction as err:
                print(err)
                print("")

        elif role == "ally":
            try:
                temp_list = self.check_ability_input(role, skills)
                if temp_list == 0:
                    raise InvalidInput("ally abilities")
                else:
                    new_ally = self.ally_members["ally" + str(self.ally_count)]
                    new_ally.first_skill = temp_list[0]
                    self.ally_count += 1
                    self.league_slot += 2
                    self.bonus_die(new_ally, temp_list)
                    self.league_information()
                    print("You have successfully added an ally")
            except InvalidInput as err:
                print(err)
                print("")

        elif role == "follower":
            try:
                temp_list = self.check_ability_input(role, skills)
                if temp_list == 0:
                    raise InvalidInput("follower abilities")
                else:
                    new_follower = \
                        self.follower_members["follower" +
                                              str(self.follower_count)]
                    new_follower.first_skill = temp_list[0]
                    self.follower_count += 1
                    self.league_slot += 1
                    self.bonus_die(new_follower, temp_list)
                    self.league_information()
                    print("You have successfully added a follower")
            except InvalidInput as err:
                print(err)
                print("")

    def get_attribute_name(self, elem):
        attr_array = ["name", "health", "brawl", "shoot", "dodge",
                      "might", "finesse", "cunning"]
        return attr_array[elem]

    def regular_exp(self, dice):

        dice_group = [1, 2]
        match = re.search(r'(\d{0,2})([d])(\d{1,2})', dice)

        if match.group(1) == "":
            dice_group[0] = 0
        else:
            dice_group[0] = int(match.group(1))

        dice_group[1] = int(match.group(3))
        return dice_group

    def check_attributes(self, role, attr):

        i, dice_count1, dice_count2, type_dice_count1, \
            type_dice_count2, role_dice_count1, \
            role_dice_count2, role_type_dice_count1, \
            role_type_dice_count2 = (0,) * 9
        dice_num1, dice_num2, dice_type1, \
            dice_type2 = ("",) * 4
        constraint1, constraint2 = (0,) * 2

        for item in attr[1:8]:
            count = 0
            i += 1
            for dice in Dice.dice_array:
                if item == dice:
                    count += 1
            else:
                if count == 0:
                    print(InvalidInput(item + " is not a valid "
                                                   "input for " +
                                            self.get_attribute_name(i)))
                    return 0

            if role == "leader":
                dice_count1, dice_count2, \
                    type_dice_count1, type_dice_count2 = 2, 3, 8, 10
                dice_num1, dice_num2, dice_type1,\
                    dice_type2 = "dice 2", "dice 3",\
                    "d8 type dice", "d10 type dice"
                constraint1, constraint2 = 2, 4

                if attr[1] != "d10":
                    print(InvalidInput("Leader health must "
                                            "be d10 not " + str(attr[1])))
                    return 0
                elif i > 1:
                    dice_elements = self.regular_exp(item)
                    if dice_elements[0] == dice_count1:
                        role_dice_count1 += 1
                    elif dice_elements[0] == dice_count2:
                        role_dice_count2 += 1
                    if dice_elements[1] == type_dice_count1:
                        role_type_dice_count1 += 1
                    elif dice_elements[1] == type_dice_count2:
                        role_type_dice_count2 += 1

            elif role == "sidekick":
                dice_count1, dice_count2, type_dice_count1, \
                    type_dice_count2 = 2, 3, 6, 8
                dice_num1, dice_num2, \
                    dice_type1, \
                    dice_type2 = "dice 2", \
                                 "dice 3", \
                                 "d6 type dice", "d8 type dice"
                constraint1, constraint2 = 3, 3

                if attr[1] != "d8":
                    print(InvalidInput("Sidekick health must be "
                                            "d8 not " + str(attr[1])))
                    return 0
                elif i > 1:
                    dice_elements = self.regular_exp(item)
                    if dice_elements[0] == dice_count1:
                        role_dice_count1 += 1
                    elif dice_elements[0] == dice_count2:
                        role_dice_count2 += 1
                    if dice_elements[1] == type_dice_count1:
                        role_type_dice_count1 += 1
                    elif dice_elements[1] == type_dice_count2:
                        role_type_dice_count2 += 1

            elif role == "ally":
                dice_count1, dice_count2, type_dice_count1 = 2, 1, 6
                dice_num1, dice_num2, dice_type1 = "dice 2", "dice 1", \
                                                   "d6 type dice"
                constraint1, constraint2 = 2, 4

                if attr[1] != "d6":
                    print(InvalidInput("Ally health must be "
                                            "d6 not " + str(attr[1])))
                    return 0
                elif i > 1:
                    dice_elements = self.regular_exp(item)
                    if dice_elements[0] == dice_count1:
                        role_dice_count1 += 1
                    elif dice_elements[0] == dice_count2:
                        role_dice_count2 += 1
                    if dice_elements[1] == type_dice_count1:
                        role_type_dice_count1 += 1

            elif role == "follower":

                if attr[1] != "d6*":
                    print(InvalidInput("Follower health "
                                            "must be d6* not " +
                                            str(attr[1])))
                    return 0
                elif i > 1:
                    for x in attr[1:8]:
                        if x == "1d6":
                            role_dice_count1 += 1

                    if role_dice_count1 != 6:
                        self.view.invalid_dice_input("Follower",
                                                     "1d6", "ALL",
                                                     role_dice_count1)
                        return 0
                    else:
                        return 1

        else:
            return self.check_dice(role, dice_num1, dice_num2,
                                   dice_type1, dice_type2,
                                   role_dice_count1,
                                   role_dice_count2,
                                   role_type_dice_count1,
                                   role_type_dice_count2,
                                   constraint1, constraint2)

    def check_dice(self, role, dice_num1, dice_num2,
                   dice_type1, dice_type2,
                   role_dice_count1, role_dice_count2,
                   role_type_dice_count1,
                   role_type_dice_count2,
                   constraint1, constraint2):
        word_num_dict = {0: "ZERO", 1: "ONE", 2: "TWO",
                         3: "THREE", 4: "FOUR",
                         5: "FIVE", 6: "SIX"}

        invalid_dice = False
        if role_dice_count1 != constraint1:
            self.view.invalid_dice_input(role, dice_num1,
                                         word_num_dict
                                         [constraint1],
                                         word_num_dict
                                         [role_dice_count1])
            invalid_dice = True
        if role != "follower":
            if role_dice_count2 != constraint2:
                self.view.invalid_dice_input(role, dice_num2,
                                             word_num_dict
                                             [constraint2],
                                             word_num_dict
                                             [role_dice_count2])
                invalid_dice = True
        if role == "ally" or role == "follower":
            constraint1 = 6
        if role_type_dice_count1 != constraint1:
            self.view.invalid_dice_input(role, dice_type1,
                                         word_num_dict
                                         [constraint1],
                                         word_num_dict
                                         [role_type_dice_count1])
            invalid_dice = True
        if role is not "ally" and "follower":
            if role_type_dice_count2 != constraint2:
                self.view.invalid_dice_input(role, dice_type2,
                                             word_num_dict
                                             [constraint2],
                                             word_num_dict
                                             [role_type_dice_count2])
                invalid_dice = True
        if invalid_dice is True:
            return 0
        else:
            return 1

    def get_member_attributes(self, role, new_object, temp_list):
        # attr = self.view.set_league_attributes(role)
        new_member = new_object(temp_list[0],
                                temp_list[1],
                                temp_list[2],
                                temp_list[3],
                                temp_list[4],
                                temp_list[5],
                                temp_list[6],
                                temp_list[7])
        return new_member

    def missing_inputs(self, ini):
        word = ""
        for x in range(ini, 8):
            word += str(self.get_attribute_name(x)) + ", "
        return word.rstrip(", ")

    def create_new_character(self, role, attributes_skills):

        try:
            j = 0
            for item in range(0, 8):
                err = attributes_skills[j]
                j += 1
        except UnboundLocalError:
            print(InvalidInput("Please enter a value for " +
                               self.missing_inputs(0)))
            print("Failed to create " + role + ", Please try "
                                               "again")
            print("")
            return err
        except IndexError:
            print(InvalidInput("Please enter a value "
                               "for " +
                               self.missing_inputs(j)))
            print("Failed to create " + role + ", "
                                               "Please "
                                               "try again")
            print("")
            return ""

        # attributes = [attr for attr in vars(Character) if not
        # callable(attr) and not attr.startswith("__")]
        if self.check_attributes(role, attributes_skills) == 1:
            if role == "leader":
                new_object = Character.Leader
                self.leader = \
                    self.get_member_attributes(role, new_object,
                                               attributes_skills)
            elif role == "sidekick":
                new_member = "sidekick" + str(self.sidekick_count)
                new_object = Character.SideKick
                self.sidekick_members[new_member] = \
                    self.get_member_attributes(role,
                                               new_object,
                                               attributes_skills)
            elif role == "ally":
                new_member = "ally" + str(self.ally_count)
                new_object = Character.Ally
                self.ally_members[new_member] = \
                    self.get_member_attributes(role,
                                               new_object,
                                               attributes_skills)
            elif role == "follower":
                new_member = "follower" + str(self.follower_count)
                new_object = Character.Follower
                self.follower_members[new_member] = \
                    self.get_member_attributes(role, new_object,
                                               attributes_skills)

            temp_list = attributes_skills[8:]
            self.set_character_skills(role, temp_list)
        else:
            print("Failed to create " + role + ", Please try again")
            print("")

    def get_dice(self, num):
        pass

    def bonus_die(self, member, skills):
        i = 0
        for x in skills:
            if x.lower() == "agile":
                dice_type = self.regular_exp(member.dodge)
                new_attr = str(dice_type[0] + 1) + "d" + str(dice_type[1])
                member.dodge = new_attr
            elif x.lower() == "animal":
                dice_type = self.regular_exp(member.dodge)
                new_attr = str(dice_type[0] + 1) + "d" + str(dice_type[1])
                member.dodge = new_attr

                dice_type = self.regular_exp(member.finesse)
                new_attr = str(dice_type[0] + 1) + "d" + str(dice_type[1])
                member.shoot = "--"
                member.finesse = new_attr
            elif x.lower() == "clever":
                dice_type = self.regular_exp(member.cunning)
                new_attr = str(dice_type[0] + 1) + "d" + str(dice_type[1])
                member.cunning = new_attr
            elif x.lower() == "fierce":
                dice_type = self.regular_exp(member.brawl)
                new_attr = str(dice_type[0] + 1) + "d" + str(dice_type[1])
                member.brawl = new_attr
            elif x.lower() == "marksman":
                if member.shoot != "--":
                    dice_type = self.regular_exp(member.shoot)
                    new_attr = str(dice_type[0] + 1) + "d" + str(dice_type[1])
                    member.shoot = new_attr
            elif x.lower() == "mighty":
                dice_type = self.regular_exp(member.might)
                new_attr = str(dice_type[0] + 1) + "d" + str(dice_type[1])
                member.might = new_attr
            elif x.lower() == "savvy":
                dice_type = self.regular_exp(member.finesse)
                new_attr = str(dice_type[0] + 1) + "d" + str(dice_type[1])
                member.finesse = new_attr


class InvalidAction(Exception):
    def __init__(self, info):
        self.info = info

    def __str__(self):
        return "Invalid Action: " + self.info


class InvalidInput(Exception):
    def __init__(self, info):
        self.info = info

    def __str__(self):
        return "Invalid Input: " + self.info
