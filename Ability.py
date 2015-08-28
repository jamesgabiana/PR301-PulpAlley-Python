__author__ = 'JamesG'


class Ability(object):

    level1 = {"Agile": "This character\'s Dodge is increased by +1 die.",
              "Animal": "This character may not shoot, but adds +1d to two "
                        "other skills.",
              "Clever": "This character\'s Cunning is increased by +1 die.",
              "Fierce": "This character\'s Brawl is increased by +1 die.",
              "Marksman": "This character\'s Shoot is increased by +1 die.",
              "Mighty": "This character\'s Might is increased by +1 die.",
              "Savvy": "This character\'s Finesse is increased by +1 die.",
              "Speedy": "This character may run up to 15\" -- instead "
                        "of 12\"."}

    level2 = {"Athletic": "Once per turn, shift this character\'s dice-type "
                          "up when rolling for Might or Finesse.",
              "Brute": "Once per turn, this character may re-roll one Brawl "
                       "or Might die.",
              "Crafty": "Once per turn, this character may re-roll one Dodge "
                        "or Cunning die.",
              "Daredevil": "Once per turn, this character receives a +1d bonus"
                           " when rolling for a Peril.",
              "Eagle-Eyed": "This character\'s close range is 12\", and their "
                            "long range is 48\" - instead of 6\" and 24\".",
              "Finagler": "Once per turn, shift this character\'s "
                          "dice-type up "
                          "when rolling for Finesse or Cunning.",
              "Intrepid": "This character may move in any direction when they "
                          "successfully dodge an attack or peril.",
              "Sharp": "Once per turn, this character may re-roll one Shoot "
                       "or Finesse die.",
              "Specialist": "Once per turn, shift this character\'s dice-type "
                            "up when rolling for Cunning or Might.",
              "Stealthy": "This character may hide as an action - instead of "
                          "a full action."}

    level3 = {"Astute": "This character\'s Shoot and Finesse dice-type "
                        "are not "
                        "lowered due to injuries.",
              "Brash": "This character is not limited to rushing the "
                       "closest enemy.",
              "Deadeye": "This character is not limited to shooting the "
                         "closest enemy",
              "Deductive": "As an action for this character, you may draw one "
                           "Fortune card.",
              "Hardened Veteran": "This character ignores the multiple "
                                  "combats penalty.",
              "Indomitable": "This character may re-roll one Recovery check "
                             "per turn.",
              "Muscles of Steel": "This character\'s Brawl and Might "
                                  "dice-type "
                                  "are not lowered due to injuries.",
              "Shrewd": "This character\'s Dodge and Cunning dice-type "
                        "are not "
                        "lowered due to injuries.",
              "Quick-Shot": "Once per turn, this character may shift their "
                            "shooting dice-type down to "
                            "gain a +2d bonus -- only against targets in "
                            "close range.",
              "Quick-Strike": "Once per turn, this character may shift their "
                              "brawling dice-type down to gain a +2d bonus."}


class Dice(object):

    dice_array = ["d6", '1d6', '2d6', '3d6', '4d6', '5d6', '6d6',
                  'd8', '1d8', '2d8', '3d8', '4d8', '5d8', '6d8', '7d8', '8d8',
                  'd10', '1d10', '2d10', '3d10', '4d10', '5d10', '6d10',
                  '7d10', '8d10', '9d10', '10d10',
                  'd12', '1d12', '2d12', '3d12', '4d12', '5d12', '6d12',
                  '7d12', '8d12', '9d12', '10d12', '11d12', '12d12']
# 'd6*'