from beautifultable import BeautifulTable
# https://beautifultable.readthedocs.io/en/latest/quickstart.html#building-the-table

table = BeautifulTable()
table.rows.append(["A", "B", "C", "D", "E", "F", "J", "I", "J"])
table.rows.append(["A", "B", "C", "D", "E", "F", "J", "I", "J"])
table.rows.append(["A", "B", "C", "D", "E", "F", "J", "I", "J"])
table.rows.append(["A", "B", "C", "D", "E", "F", "J", "I", "J"])
table.rows.append(["A", "B", "C", "D", "E", "F", "J", "I", "J"])
table.rows.append(["A", "B", "C", "D", "E", "F", "J", "I", "J"])

table.set_style(BeautifulTable.STYLE_BOX)
print(table)
table.rows[5][1] = 'A'
print(table)






# from tabulate import tabulate
#
# print(tabulate([["A", "B", "C", "D", "E", "F", "J", "H"], ["V", "D"]],
#                ["s", "n"], "mediawiki"))