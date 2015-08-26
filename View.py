from Tools.Scripts.treesync import raw_input
__author__ = 'JamesG'


class View(object):

    def start(self):
        print("-------------------------- Welcome to Pulp Alley -------"
              "-------------------\n" +
              "To create a new League, type \"create <league_name>\" and"
              " then enter\n" +
              "To load or edit from file, type \"load\" and then enter\n" +
              "To view commands, type \"help\" and then enter\n" +
              "To view information about a command, type"
              " \"help <command_name>\""
              " and then enter\n")

    def create_league(self):
        result = "To create a Leader, please type \"leader\"\n" + \
                 "To create a Sidekick, please type \"sidekick\"\n" +\
                 "To create an Ally, please type \"ally\"\n" + \
                 "To create a follower, please type \"follower\"\n"
        print(result)

    def invalid_dice_input(self, role, dice, count, num):
        print(role + " skills: " + count + " SKILLS!!! must"
                                           " start at " + dice +
              ".... you set " + str(num) + " SKILLS")

    def set_league_attributes(self, user_input):
        result = "Please Enter the attributes of the " + user_input +\
                 " using the format and order below: \n" + \
                 "name health brawl shoot dodge might finesse cunning \n"
        print(result)

    def set_league_skills(self, user_input):
        header = "Please Enter the skills of the " + user_input + \
                 " using the format and order below: (eg Agile Animal Clever)"
        if user_input == "leader":
            print(header)
            result = raw_input("1st_Skill 2nd_Skill 3rd_Skill \n")
        elif user_input == "sidekick":
            print(header)
            result = raw_input("1st_Skill 2nd_Skill \n")
        elif user_input == "ally":
            result = raw_input("Please Enter the level 1 or level 2 "
                               "skill for Ally: \n")
        elif user_input == "follower":
            result = raw_input("Please Enter the level 1 skill "
                               "for Follower: \n")
        print(result)
        return result.rstrip('\n')
