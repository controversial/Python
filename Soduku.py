#Soduku Solver


def alt(one, two):
    return [a + b for a in one for b in two]

def split(string, num):
    return [string[i:i+num] for i in range(0, len(string), num)]

#-----------------------------------
<<<<<<< HEAD
#basic units of soduku
=======
#Basic units of soduku
>>>>>>> origin/master

rows = 'abcdefghi'

cols = '123456789'

tiles = [a + b for a in rows for b in cols]

<<<<<<< HEAD
boxes = [alt(r, c) for r in split(rows, 3) for c in split(cols, 3)]
#-----------------------------------
#Dictionaries for getting the row, column, or unit that a tile belongs to
#Will return
=======
units = [alt(r, c) for r in split(rows, 3) for c in split(cols, 3)]
#-----------------------------------
#Dictionaries for getting the row, column, or unit that a tile belongs to
#Will return 
>>>>>>> origin/master
row = dict((x, []) for x in tiles)
for item in tiles:
    for choice in tiles:
        if choice[0] ==  item[0]:
            row[item].append(choice)

col = dict((x, []) for x in tiles)
for item in tiles:
    for choice in tiles:
        if choice[1] ==  item[1]:
            col[item].append(choice)

<<<<<<< HEAD
box = {item: category for category in units for item in category}
=======
unit = {item: category for category in units for item in category}
>>>>>>> origin/master

peers = {}
for item in tiles:
    peers[item] = row[item]+col[item]+unit[item]
    s = []
    for i in peers[item]:
        if i not in s:
            s.append(i)
    peers[item] = s
<<<<<<< HEAD
    peers[item].remove(item)

=======
    
print peers['a1']
>>>>>>> origin/master
#-----------------------------------
#Dictionies for storing logical information about each tile

#Stores all values a tile can't be
<<<<<<< HEAD
possibilities = dict((x, []) for x in tiles)
=======
impossibilities = dict((x, []) for x in tiles)

#Dictionary that will store the final value of each tile
values = dict((x, 0) for x in tiles)

>>>>>>> origin/master
