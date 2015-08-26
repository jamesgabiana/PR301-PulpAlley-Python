import doctest
import Character
import cmd
import os
import pickle
from League import League
from League import InvalidInput
import unittest
from League import InvalidAction
import Ability
import sys
__author__ = 'JamesG'


class Controller(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "Command: "
        self.league = League()

    def do_create(self, line):
        """
        -- Create --
        Creates a new League
        To create new league, type "create league_name" then enter

        The roster for a starting league has 10 slots. In
        addition to adding characters to your roster, you
        may also select special perks to further
        customize your league. Most of the characters
        and perks will fill 1 to 3 slots. You are not
        required to fill all your slots, but players are
        encouraged to include 4 to 6 characters in their
        first leagues. Sample characters and leagues are
        included for those wanting to jump straight into
        the action.

        """
        self.league.start_create(line)

    def do_leader(self, line):
        """
        -- Leader (Level 4) --
        Each league must include one
        (and only one) Leader. Leaders are the central
        characters around which the rest of the league
        forms. These are extraordinary and legendary
        individuals, or at least legends-in-the-making.
        Leaders possess truly amazing skills and may
        select from the greatest range of abilities. Unlike
        all other characters, Leaders do not subtract
        from your roster slots - they're free!

        type "leader <attributes>" to create leader followed \
by the attributes and skills
        e.g leader Kim Jong-un, d10, 3d8, 3d10, 3d10, 2d8, 3d10, \
2d10, Sharp, Deadeye, Agile
        """

        self.league.add_leader(line)

    def do_sidekick(self, line):
        """
        -- SideKick (Level 3) --
        A sidekick is the stalwart
        companion and closest colleague of the league's
        leader. Sidekicks are exceptional characters,
        experts in their fields, and possess superior skills.
        Not every leader will have a sidekick, but if you
        choose to include one in your league, they fill 3
        roster slots. A league may not normally have
        more than one sidekick, unless they have the
        Company of Heroes perk.

        type "sidekick <attributes>" to create sidekick followed \
by the attributes and skills
        eg sidekick Mr. Wang, d8, 3d8, 3d8, 3d8, 2d6, 2d6, 2d6, Sharp, Deadeye
        """
        self.league.add_sidekick(line)

    def do_ally(self, line):
        """
        -- Ally (Level 2) --
        Allies have the training and
        experience to make them a valuable part of any
        league. Leagues may include many allies, and it is
        common for them to be the most numerous type
        of character in a league. Unlike followers, allies
        have the opportunity to roll Health and Recovery
        checks. An ally takes 2 roster slots.

        type "ally <attributes>" to create ally followed \
by the attributes and skills
        eg ally Rob, d6, 2d6, 2d6, 1d6, 1d6, 1d6, 1d6, animal
        """
        self.league.add_ally(line)

    def do_follower(self, line):
        """
        -- Follower (Level 1) --
        Although Followers are the
        least skilled characters, with leadership and luck
        they may prove to be quite useful. A follower fills
        only 1 slot on the league roster.

        type "follower <attributes>" to create follower followed \
by the attributes and skills
        eg follower Wolfeschlegelsteinhausenbergerdorff, d6*, 1d6, 1d6, 1d6, 1d6, 1d6, 1d6, animal
        """
        self.league.add_follower(line)

    def do_exit(self, line):
        """
        -- Exit --
        Exits the game
        """
        return True

    def do_save(self, name):
        """
        -- Save --
        Saves the game.

        type "save <file_name>"
        """
        try:
            if name == "":
                raise InvalidInput("Please enter a name of the "
                                   "file. eg. save <file_name>")
            data = [self.league]
            with open(name + ".pickle", "wb") as file:
                pickle.dump(data, file)
            print("File has been saved as " + name + ".pickle")
        except InvalidInput as err:
            print(err)

    def do_load(self, f_name):
        """
        -- Load --
        Load a League

        type "load <filename>"
        """
        try:
            if f_name == "":
                raise InvalidInput("Please enter the name of the "
                                    "file. eg. load <file_name>")
            if os.path.exists(f_name + ".pickle") is False:
                raise InvalidInput("The file \"" + f_name +
                                        "\" does not exist")
            with open(f_name + ".pickle", "rb") as file:
                data = pickle.load(file)
            self.league = data[0]
            print("File loaded from " + f_name +
                  ".pickle...")
        except InvalidInput as err:
            print(err)

    def do_display(self, line):
        """
        -- Display --
        displays the League

        type "display" to display the league
        """
        print(str(self.league.leader))
        print("")
        if len(self.league.sidekick_members) > 0:
            for key, value in self.league.sidekick_members.items():
                print(value)
        if len(self.league.ally_members) > 0:
            for key, value in self.league.ally_members.items():
                print(value)
        if len(self.league.follower_members) > 0:
            for key, value in self.league.follower_members.items():
                print(value)

    def do_restart(self, line):
        """
        -- Restart --
        Reinitialize the League

        type "restart" to start over again
        """
        self.league.leader = Character.Leader
        self.league.name = ""
        self.league.limit = 10
        self.league.league_slot = 0
        self.league.sidekick_count = 1
        self.league.ally_count = 1
        self.league.follower_count = 1
        self.league.sidekick_members = {}
        self.league.ally_members = {}
        self.league.follower_members = {}
        self.league.has_leader = False
        self.league.league_status = ""
        self.league.is_creating_league = False
        self.league.league_information()

    def preloop(self):
        """
        >>> league.add_leader("James, d10, 3d8, 3d10, 3d10, 2d8, "\
"3d10, 2d10, Sharp, Deadeye, Agile")
        'Invalid Action: You must enter the name of the League first \
before you can start creating characters!!!(type create <league_name>)'
        >>> league.add_sidekick("James, d10, 3d8, 3d10, 3d10, 2d8, "\
"3d10, 2d10, Sharp, Deadeye, Agile")
        'Invalid Action: You must enter the name of the League first \
before you can start creating characters!!!(type create <league_name>)'
        >>> league.add_ally("James, d10, 3d8, 3d10, 3d10, 2d8, 3d10, "\
"2d10, Sharp, Deadeye, Agile")
        'Invalid Action: You must enter the name of the League first \
before you can start creating characters!!!(type create <league_name>)'
        >>> league.add_follower("James, d10, 3d8, 3d10, 3d10, 2d8, 3d10, "\
"2d10, Sharp, Deadeye, Agile")
        'Invalid Action: You must enter the name of the League first \
before you can start creating characters!!!(type create <league_name>)'
        >>> league.start_create("Alpha")
        ------------------------------ Create League -----------------\
-------------
        Type <character_role> followed by the attributes and skills \
using the format and order below:
        name, health, brawl, shoot, dodge, might, finesse, cunning, \
1st_Skill, 2nd_Skill, 3rd_Skill
        (eg leader Kim Jong-un, d10, 3d8, 3d10, 3d10, 2d8, 3d10, \
2d10, Sharp, Deadeye, Agile)
        Your League's name, is Alpha
        <BLANKLINE>
        >>> league.add_sidekick("James, d8, 3d8, 3d8, 3d8, 2d6, "\
"2d6, 2d6, Sharp, Deadeye")
        'Invalid Action: Please create a leader first, you have \
not created a leader yet!!!'
        >>> league.add_ally("James, d6, 2d6, 2d6, 1d6, 1d6, 1d6, "\
"1d6, animal")
        'Invalid Action: Please create a leader first, you have not \
created a leader yet!!!'
        >>> league.add_follower("James, d6*, 1d6, 1d6, 1d6, 1d6, "\
"1d6, 1d6, animal")
        'Invalid Action: Please create a leader first, you have not \
created a leader yet!!!'
        >>> league.add_leader("James, d10, 3d8, 3d10, 3d10, 2d8, 3d10, "\
"2d10, Sharp, Agile")
        Please enter 3 abilities, you entered 2
        'Invalid Input: leader abilities'
        <BLANKLINE>
        >>> league.add_leader("James, d10, 3d8, 3d10, 3d10, 2d8, "\
"3d10, 2d10, Sharp, Agile, Animal, Clever")
        Please enter 3 abilities, you entered 4
        'Invalid Input: leader abilities'
        <BLANKLINE>
        >>> league.add_leader("James, d10, 3d8, 3d10, 3d10, 2d8, 3d10, "\
"2d10, Sharp, Agile, Agile")
        'Invalid Action: Please no duplicates "Agile"'
        <BLANKLINE>
        >>> league.add_leader("James, d8, 3d8, 3d10, 3d10, 2d8, 3d10, "\
"2d10, Sharp, Deadeye, Agile")
        'Invalid Input: Leader health must be d10 not d8'
        Failed to create leader, Please try again
        <BLANKLINE>
        >>> league.add_leader("James, d10, 3d8, 3d10, 3d10, 2d8, 3d10, "\
"2d10, Sharp, Deadeye, Agile")
        You have 10 slots left to use, You have a leader
        <BLANKLINE>
        You have successfully added a leader
        >>> league.add_leader("James, d10, 3d8, 3d10, 3d10, 2d8, 3d10, "\
"2d10, Sharp, Deadeye, Agile")
        'Invalid Action: You already created a leader named "James", \
please create other character'
        >>> league.add_sidekick("James, d8, 3d8, 3d8, 3d8, 2d6, 2d6, "\
"2d6, Sharp")
        Please enter 2 abilities, you entered 1
        'Invalid Input: sidekick abilities'
        <BLANKLINE>
        >>> league.add_sidekick("James, d8, 3d8, 3d8, 3d8, 2d6, 2d6, "\
"2d6, Sharp, Agile, Animal")
        Please enter 2 abilities, you entered 3
        'Invalid Input: sidekick abilities'
        <BLANKLINE>
        >>> league.add_sidekick("James, d8, 3d8, 3d8, 3d8, 2d6, "\
"2d6, 2d6")
        You entered nothing!!!
        'Invalid Input: sidekick abilities'
        <BLANKLINE>
        >>> league.add_follower("James, d6*, 1d6, 1d6, 1d6, 1d6, "\
"1d6, 1d6")
        You entered nothing!!!
        'Invalid Input: follower abilities'
        <BLANKLINE>
        """
        self.league.league_information()

    def postloop(self):
        print("Thank you for for playing Pulp Alley")


def initialized():
    league.leader = Character.Leader
    league.name = ""
    league.limit = 10
    league.league_slot = 0
    league.sidekick_count = 1
    league.ally_count = 1
    league.follower_count = 1
    league.sidekick_members = {}
    league.ally_members = {}
    league.follower_members = {}
    league.has_leader = False
    league.league_status = ""
    league.is_creating_league = False


class MainTest(unittest.TestCase):
    global league
    league = League()

    def setUp(self):
        initialized()

    def create_leader(self):
        league.add_leader("James, d10, 3d8, 3d10, 3d10, 2d8, 3d10, " +
                          "2d10, Sharp, Deadeye, Agile")

    def tearDown(self):
        pass

    def test_01_create_league_no_name(self):
        """
        Try to create league with no name
        error raised "Please enter the name, you entered nothing!!"
        """
        self.assertRaises(InvalidInput, league.start_create(""))

    def test_02_create_character_before_league(self):
        """
        Try to create character before league
        error raised "You must enter the name of the League first \
        before you can start creating characters!!!(type create <league_name>)"
        """
        self.assertRaises(InvalidAction,
                          league.add_leader("James, d10, 3d8, 3d10, 3d10, " +
                                            "2d8, 3d10, 2d10"))
        self.assertRaises(InvalidAction,
                          league.add_sidekick("James, d10, 3d8, 3d10, 3d10, " +
                                              "2d8, 3d10, 2d10"))
        self.assertRaises(InvalidAction,
                          league.add_ally("James, d10, 3d8, 3d10, 3d10, " +
                                          "2d8, 3d10, 2d10"))
        self.assertRaises(InvalidAction,
                          league.add_follower("James, d10, 3d8, 3d10, 3d10, " +
                                              "2d8, 3d10, 2d10"))

    def test_03_create_other_character_before_leader(self):
        """
        Try to create other character before league
        error raised "Please create a leader first, you have \
        not created a leader yet!!!"
        """
        league.start_create("Alpha")
        self.assertRaises(InvalidAction,
                          league.add_sidekick("James, d10, 3d8, " +
                                              "3d10, 3d10, 2d8, 3d10, 2d10"))
        self.assertRaises(InvalidAction,
                          league.add_ally("James, d10, 3d8, 3d10, " +
                                          "3d10, 2d8, 3d10, 2d10"))
        self.assertRaises(InvalidAction,
                          league.add_follower("James, d10, 3d8, 3d10, " +
                                              "3d10, 2d8, 3d10, 2d10"))

    def test_07_create_character_with_missing_skills(self):
        """
        try to create character with missing skills
        error raised Please enter 3 abilities, you entered 1
            'Invalid Input: Please Enter a valid input for abilities'

            Please enter 3 abilities, you entered 2
            'Invalid Input: Please Enter a valid input for abilities'
        """
        league.start_create("Alpha")
        self.assertRaises(InvalidInput,
                          league.add_leader("James, d10, 3d8, 3d10, 3d10, " +
                                            "2d8, 3d10, 2d10, Sharp"))
        self.assertRaises(InvalidInput,
                          league.add_leader("James, d10, 3d8, 3d10, 3d10, " +
                                            "2d8, 3d10, 2d10, Sharp, Deadeye"))

    def test_08_invalid_dice_input(self):
        """
        invalid dice
        """
        word = "Sharp, Deadeye, Agile"
        league.start_create("Alpha")
        self.assertRaises(InvalidInput,
                          league.add_leader("leader James, ddd12, 3d8, " +
                                            "3d10, " +
                                            "3d10, 2d8, 3d10, 2d10, " +
                                            word))
        self.assertRaises(InvalidInput,
                          league.add_leader("leader James, d10, sdf12, " +
                                            "3d10, " +
                                            "3d10, 2d8, 3d10, 2d10, " +
                                            word))
        self.assertRaises(InvalidInput,
                          league.add_leader("leader James, d10, 3d8, 3d10, " +
                                            "3d10, " +
                                            "fdfkdsk34, 3d10, 2d10, " +
                                            word))

    def test_09_invalid_skill_input(self):
        """
        invalid skills
        """
        league.start_create("Alpha")
        word = "James, d10, 3d8, 3d10, 3d10, 2d8, 3d10, 2d10, "
        self.assertRaises(InvalidInput,
                          league.add_leader(word + "sadf, Deadeye, Agile"))
        self.assertRaises(InvalidInput,
                          league.add_leader(word + "Sharp, fd4g4, Agile"))
        self.assertRaises(InvalidInput,
                          league.add_leader(word + "Sharp, Deadeye, sdf"))

    def test_10_skill_duplicates(self):
        league.start_create("Alpha")
        self.assertRaises(InvalidInput,
                          league.add_leader("James, d10, 3d8, 3d10, 3d10, " +
                                            "2d8, 3d10, 2d10, Sharp, " +
                                            "Agile, Agile"))

    def test_11_skill_excess_skills(self):
        league.start_create("Alpha")
        self.assertRaises(InvalidInput,
                          league.add_leader("James, d10, 3d8, 3d10, 3d10, " +
                                            "2d8, 3d10, 2d10, Sharp, "
                                            "Deadeye, Agile, Animal"))

    def test_12_set_level_3_2_skills_to_follower(self):
        league.start_create("Alpha")
        league.add_leader("James, d10, 3d8, 3d10, 3d10, 2d8, " +
                          "3d10, 2d10, Sharp, Deadeye, Agile")
        self.assertRaises(InvalidInput,
                          league.add_follower("James, d6*, 1d6, " +
                                              "1d6, 1d6, 1d6, 1d6, 1d6, " +
                                              "Hardened Veteran"))

    def test_13_set_dice_rule(self):
        """
        try and create a leader without following the dice rules
        """
        self.assertRaises(InvalidInput,
                          league.add_leader("James, d10, 2d10, 3d10, " +
                                            "3d10, 2d8, 3d10, 2d10, " +
                                            "Sharp, Deadeye, Agile"))

    def test_14_try_create_two_leaders(self):

        # 'Invalid Action: You already created a leader named \
        # "James", please create other character'

        league.start_create("Alpha")
        league.add_leader("James, d10, 3d8, 3d10, 3d10, 2d8, 3d10, " +
                          "2d10, Sharp, Deadeye, Agile")
        self.assertRaises(InvalidAction,
                          league.add_leader("James, d10, 3d8, 3d10, " +
                                            "3d10, 2d8, 3d10, 2d10, Sharp, " +
                                            "Deadeye, Agile"))

    def create_character_with_missing_attributes(self, role, add_char, *args):
        league.start_create("Alpha")
        if role != "leader":
            self.create_leader()
        word = ""
        count = 0
        for x in args:
            if count == 0:
                self.assertRaises(InvalidInput, add_char(word))
            else:
                word += ", " + x
                self.assertRaises(InvalidInput, add_char(word))
            count += 1

    def test_15_create_leader_with_missing_attributes(self):
        self.create_character_with_missing_attributes("leader",
                                                      league.add_leader,
                                                      "James", "d8", "3d8",
                                                      "3d8",
                                                      "3d8", "2d8", "2d8")

    def test_16_create_sidekick_with_missing_attributes(self):
        self.create_character_with_missing_attributes("sidekick",
                                                      league.add_sidekick,
                                                      "James",
                                                      "d8", "3d8", "3d8",
                                                      "3d8",
                                                      "2d8", "2d8")

    def test_17_create_ally_with_missing_attributes(self):
        self.create_character_with_missing_attributes("ally",
                                                      league.add_ally,
                                                      "James",
                                                      "d8", "3d8", "3d8",
                                                      "3d8",
                                                      "2d8", "2d8")

    def test_18_create_follower_with_missing_attributes(self):
        self.create_character_with_missing_attributes("ally",
                                                      league.add_follower,
                                                      "James",
                                                      "d8", "3d8", "3d8",
                                                      "3d8",
                                                      "2d8", "2d8")

    def bonus_die(self, role, add_char, attr):
        league.start_create("Alpha")
        if role != "leader":
            self.create_leader()
        add_char(attr)

    def test_19_bonus_die_leader(self):
        word = "James, d10, 3d8, 3d10, 3d10, 2d8, 3d10, 2d10, "
        self.bonus_die("leader", league.add_leader, word + "Agile, Fierce,"
                                                           "Clever")
        self.assertTrue(league.leader.dodge == "4d10")
        self.assertTrue(league.leader.brawl == "4d8")
        self.assertTrue(league.leader.cunning == "3d10")
        initialized()
        self.bonus_die("leader", league.add_leader, word + "Animal, Mighty,"
                                                           "Savvy")
        self.assertTrue(league.leader.shoot == "--")
        self.assertTrue(league.leader.might == "3d8")
        self.assertTrue(league.leader.finesse == "5d10")
        initialized()
        self.bonus_die("leader", league.add_leader, word + "marksman,"
                                                           "Fierce, Clever")
        self.assertTrue(league.leader.shoot == "4d10")

    def test_20_bonus_die_sidekick(self):
        word = "James, d8, 3d8, 3d8, 3d8, 2d6, 2d6, 2d6, "
        self.bonus_die("sidekick", league.add_sidekick, word + "Agile,"
                                                               "Animal")
        self.assertTrue(league.sidekick_members["sidekick1"].shoot == "--")
        self.assertTrue(league.sidekick_members["sidekick1"].dodge == "5d8")
        self.assertTrue(league.sidekick_members["sidekick1"].finesse == "3d6")
        initialized()
        self.bonus_die("sidekick", league.add_sidekick, word + "Clever,"
                                                               "Fierce")
        self.assertTrue(league.sidekick_members["sidekick1"].cunning == "3d6")
        self.assertTrue(league.sidekick_members["sidekick1"].brawl == "4d8")
        initialized()
        self.bonus_die("sidekick", league.add_sidekick, word + "marksman,"
                                                               "mighty")
        self.assertTrue(league.sidekick_members["sidekick1"].shoot == "4d8")
        self.assertTrue(league.sidekick_members["sidekick1"].might == "3d6")
        initialized()
        self.bonus_die("sidekick", league.add_sidekick, word + "savvy, mighty")
        self.assertTrue(league.sidekick_members["sidekick1"].finesse == "3d6")

    def test_21_bonus_die_ally(self):
        word = "James, d6, 2d6, 2d6, 1d6, 1d6, 1d6, 1d6, "
        for x in Ability.Ability.level1:
            self.bonus_die("sidekick", league.add_ally, word + str(x))
            if x == "Animal":
                self.assertTrue(league.ally_members["ally1"].shoot == "--")
            elif x == "Agile":
                self.assertTrue(league.ally_members["ally1"].dodge == "2d6")
            elif x == "Clever":
                self.assertTrue(league.ally_members["ally1"].cunning == "2d6")
            elif x == "Fierce":
                self.assertTrue(league.ally_members["ally1"].brawl == "3d6")
            elif x == "Marksman":
                self.assertTrue(league.ally_members["ally1"].shoot == "3d6")
            elif x == "Mighty":
                self.assertTrue(league.ally_members["ally1"].might == "2d6")
            elif x == "Savvy":
                self.assertTrue(league.ally_members["ally1"].finesse == "2d6")
            initialized()

    def test_22_bonus_die_follower(self):
        word = "James, d6*, 1d6, 1d6, 1d6, 1d6, 1d6, 1d6, "
        for x in Ability.Ability.level1:
            self.bonus_die("follower", league.add_follower, word + str(x))
            if x == "Animal":
                self.assertTrue(league.follower_members["follower1"].shoot ==
                                "--")
            elif x == "Agile":
                self.assertTrue(league.follower_members["follower1"].dodge ==
                                "2d6")
            elif x == "Clever":
                self.assertTrue(league.follower_members["follower1"].cunning ==
                                "2d6")
            elif x == "Fierce":
                self.assertTrue(league.follower_members["follower1"].brawl ==
                                "2d6")
            elif x == "Marksman":
                self.assertTrue(league.follower_members["follower1"].shoot ==
                                "2d6")
            elif x == "Mighty":
                self.assertTrue(league.follower_members["follower1"].might ==
                                "2d6")
            elif x == "Savvy":
                self.assertTrue(league.follower_members["follower1"].finesse ==
                                "2d6")
            initialized()


def cmd_switch():
    con = Controller()
    try:
        if len(sys.argv) == 3 and sys.argv[1] == "load":
            print("load league")
            con.do_load(sys.argv[2])
            return
        else:
            return
        raise InvalidInput("argument not supported")
    except InvalidInput as err:
        print(err)


def main():

    initialized()
    # doctest.testmod(verbose=True)
    cmd_switch()
    control = Controller()
    control.cmdloop()

if __name__ == '__main__':
    # unittest.main()
    main()
