# MISSION: The complete set of examples for ''Python 5000 - Turtle Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-08-09 05:18:34
# FILE: ex_nagy_ord_char.py
# AUTHOR: Randall Nagy
#

for ss in range(100):
    print() #  clear the screen

data = "Randall Nagy"

for dat in data:
    print(dat, ord(dat),
          chr(ord(dat)), sep='\t')


