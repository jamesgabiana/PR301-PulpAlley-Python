__author__ = 'JamesG'


class TableMaker(object):

    def table_maker(*args):
        table = [["", "name", "health", "brawl", "shoot", "dodge",
                  "might", "finesse", "cunning"]]
        table.append(list(args))
        final_table = ""
        line = ""
        i = 0

        for x in table[1]:
            if len(table[0][i]) < len(table[1][i]):
                count_space = (len(table[1][i]) - len(table[0][i]))
                extra_space = " " * count_space
                table[1][i] += " |"
                table[0][i] += extra_space + " |"
            elif len(table[0][i]) > len(table[1][i]):
                count_space = (len(table[0][i]) - len(table[1][i]))
                extra_space = " " * count_space
                table[0][i] += " |"
                table[1][i] += extra_space + " |"
            else:
                table[0][i] += " |"
                table[1][i] += " |"
            i += 1

        for x in table[0]:
            for y in str(x):
                line += "_"

        table.insert(0, line[:-1])
        table.append(line[:-1] + "|")

        for row in table:
            if row is table[-1]:
                final_table += "".join(row)
            else:
                final_table += "".join(row) + "\n"

        return final_table
