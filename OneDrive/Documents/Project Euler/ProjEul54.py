import sys

class pokergame:
    #take in a string and turn it into an array with entries the individual cards
    def __init__(self,game):
        h1=[]
        h2=[]
        textofh1=game[:15]
        textofh2=game[15:]
        textofh1=textofh1.strip()
        textofh2=textofh2.strip()
        i=0
        while i<len(textofh1)-1:
            h1.append(textofh1[i:i+2])
            i+=3
        self.player1=h1
        i=0
        while i<len(textofh2)-1:
            h2.append(textofh2[i:i+2])
            i+=3
        self.player2=h2
    def whowins(self):
        return 1
    #for testing purposes
    def p1(self):
        return self.player1
    def p2(self):
        return self.player2

#takes in a long string an splits it up into individual hands
def breakupgames(games):
    out=[]
    i=0
    while i<len(games):
        out.append(games[i:i+30].strip())
        i+=30
    return out

#Opens the text file with the name passed as an argument
with open(sys.argv[1], 'r') as file:
    games = file.read()
#removes the new line characters
games=games.replace("\n"," ")
#testing
listofgames=breakupgames(games)
print(listofgames[0])
firstg=pokergame(listofgames[0])
print(firstg.p1(), firstg.p2(), firstg.whowins())