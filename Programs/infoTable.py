# pip install prettytable
from prettytable import PrettyTable

# create a table with headers
table = PrettyTable(["Student Name", "Subject", "Grade"])

# add rows for different students
table.add_row(["Alice", "Math", "A"])
table.add_row(["Bob", "Math", "B"])
table.add_row(["Alice", "English", "B"])
table.add_row(["Bob", "English", "A"])

print(table)
