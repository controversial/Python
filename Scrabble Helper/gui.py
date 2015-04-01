from Tkinter import *
tk = Tk()


#Open the file, read it, and put each word separately into a list
f = open('ospd.txt')
words = f.read()
wordlist = words.split()

def main():
        lb.delete(0, END)
        for display in match(inputbox.get()):
                lb.insert(END, display + ": " + str(score(display)))

#Set up tkinter widgets
global inputbox
topframe = Frame(tk)

inputbox = Entry(topframe, width=16)
inputbox.pack(side=LEFT, padx=(1, 5))

button = Button(topframe, text='Find', command=main)
button.pack(side=RIGHT)

topframe.pack(side=TOP)

lb = Listbox(tk, height=5)
lb.pack(side=LEFT)

sb = Scrollbar(tk, orient=VERTICAL)
sb.pack(side=LEFT, fill='y')

sb.configure(command=lb.yview)
lb.configure(yscrollcommand=sb.set)

#Return the number of times every present letter occurs in a given string as a dictionary
def occurrence(s):
	dict = {}
	s = s.lower()
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	for x in alphabet:
		if s.count(x) > 0:
			dict[x] = s.count(x)
	return dict

scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
	         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
	         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
	         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
	         "x": 8, "z": 10}

#Give a score to a string
def score(string):
	#Value of all scrabble tiles
	scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
	         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
	         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
	         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
	         "x": 8, "z": 10}
	
	thescore = 0
	for l in string:
		thescore += scores[l]
	return thescore


#Find words that match
def match(tiles):
        rack = tiles
        possibilities = []
        for word in wordlist:
                freq = occurrence(rack)
                match = ''
                word = word.lower()
                for letter in word:
                        if letter in freq.keys():
                                if freq[letter] > 0:
                                        freq[letter] -= 1
                                        match += letter
                        if match == word:
                                possibilities.append(word)


        #Create a list, sorted by score
        d = {}
        for poss in possibilities:
                d[poss] = score(poss)
        final = sorted(d, key=d.get, reverse=True)

        return final


 
while 1:
        tk.update()
