__author__ = 'JamesG'


class TableMaker(object):

    def table_maker(is_skill, *args):
        table = [["", "name", "health", "brawl", "shoot", "dodge",
                  "might", "finesse", "cunning"]]
        table.append(list(args))
        col_pos = []
        final_table = ""
        line = ""
        i = 0
        total = 0

        if is_skill is False:
            for x in table[1]:
                if x == table[1][0]:
                    table[1][0] = "|" + table[1][0]
                    table[0][0] = "|" + table[0][0]
                if len(table[0][i]) < len(table[1][i]):
                    count_space = (len(table[1][i]) - len(table[0][i]))
                    extra_space = " " * count_space
                    table[1][i] += " |"
                    table[0][i] += extra_space + " |"
                    total += len(table[0][i])
                    col_pos.append(total)
                elif len(table[0][i]) > len(table[1][i]):
                    count_space = (len(table[0][i]) - len(table[1][i]))
                    extra_space = " " * count_space
                    table[0][i] += " |"
                    table[1][i] += extra_space + " |"
                    total += len(table[1][i])
                    col_pos.append(total)
                else:
                    table[0][i] += " |"
                    table[1][i] += " |"
                    total += len(table[1][i])
                    col_pos.append(total)
                i += 1

            for x in table[0]:
                for y in str(x):
                    if x.endswith(y) is True:
                        line += "+"
                    else:
                        line += "-"
            table.insert(0, line[:-1] + "+")
            table.insert(2, line[:-1] + "+")
            table.append(line[:-1] + "+")

            for row in table:
                if row is table[-1]:
                    final_table += "".join(row)
                else:
                    final_table += "".join(row) + "\n"

        return final_table
