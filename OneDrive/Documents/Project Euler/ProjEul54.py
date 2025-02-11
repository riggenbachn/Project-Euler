import sys

cardsinorder=["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
class player:
    def __init__(self, textofhand):
        striptext=textofhand.strip()
        handtemp =[]
        i=0
        while i<len(striptext)-1:
            handtemp.append(striptext[i:i+2])
            i+=3
        self.hand=handtemp
        self.rank=[]
    #find the rank of the hand and returns the rank as a number between 0 (high card) and 9(royal flush) and the highest card that makes up the rank
    def findrank(self):
        nosuits=[]
        suits=[]
        for card in self.hand:
            nosuits.append(card[0])
            suits.append(card[1])
        #check if the hand has all the same suit
        allsamesuit = (suits[0]==suits[1] and suits[1]==suits[2] and suits[2]==suits[3] and suits[3]==suits[4])    
        #checks for (royal) flush
        if set(nosuits)==set(["T","J","Q","K", "A"]):
            if allsamesuit:
                self.rank=[9,12]
                return [9,"A"]
            else:
                self.rank=[4,12]
                return [4,12]
        #check for straight
        #looks like A2345 doesnt count as a flush according to the rules, if code gives the wrong answer check if this was just left out.
        straight=False
        highcard=0
        i=12
        j=0
        count =0
        while i>=0:
            for card in nosuits:
                if card==cardsinorder[i]:
                    count+=1
                    if highcard==0:
                        highcard=i
                    break
            if count>4:
                break
            i=i-1
        if highcard==i+4 and count==5:
            if allsamesuit:
                return [8, highcard]
            else:
                return [4, highcard]
        #sort the hand into collections of cards with the same value
        cardsofakind=[]
        wasntadded=True
        for card in nosuits:
            wasntadded=True
            for subhand in cardsofakind:
                if card==subhand[0]:
                    subhand.append(card)
                    wasntadded=False
                    break
            if wasntadded:
                cardsofakind.append([card])
        #checks for four of a kind or full house
        if len(cardsofakind)==2:
            if len(cardsofakind[0])==4:
                return [7,cardsinorder.index(cardsofakind[0][0])]
            elif len(cardsofakind[0])==3:
                return [6,cardsinorder.index(cardsofakind[0][0])]
            elif len(cardsofakind[0])==2:
                return [6,cardsinorder.index(cardsofakind[1][0])]
            else:
                return [7,cardsinorder.index(cardsofakind[1][0])]
        #next highest possiblility is a flush
        if allsamesuit:
            return [5,highcard]
        #we already handled a straight in checking for royal and straight flushes, so we can skip that and go to pairs
        twopairs=[]
        for pair in cardsofakind:
            if len(pair)==3:
                return [3,pair[0]]
            elif len(pair)==2:
                twopairs.append(pair[:])
        #checks for two pair and finds the higher card value of the two pair
        if len(twopairs)==2:
            j=12
            while j>=0:
                if cardsinorder[j]==twopairs[0][0]:
                    return [2,cardsinorder.index(twopairs[0][0])]
                elif cardsinorder[j]==twopairs[1][0]:
                    return [2,cardsinorder.index(twopairs[1][0])]
                j=j-1
        #next smallest possiblility is a single pair
        elif len(twopairs)==1:
            return [1,cardsinorder.index(twopairs[0][0])]
        #if the program has not returned anything at this point, the hand msut be a high card hand.
        else:
            return [0,highcard]
    #for testing the code
    def printhand(self):
        print(self.hand)
    #in case the rank of the hands is the same, this returns all the cards in the hand in descending order
    def handvalues(self):
        output=[]
        i=12
        while i>=0:
            for card in self.hand:
                if card[0]==cardsinorder[i]:
                    output.append(i)
            i=i-1
        return output
        
        
    #returns the hand in case the rank is a tie and need to check highcard
    def returnhand(self):
        return slef.hand()

class pokergame:
    #take in a string and turn it into an array with entries the individual cards
    def __init__(self,game):
        self.player1=player(game[:15])
        self.player2=player(game[15:])
    #returns 1 if p1 wins, 0 if p2 wins (I know this is strange, it makes the loop in the main program easier to write.)
    def whowins(self):
        p1performance=self.player1.findrank()
        p2performance=self.player2.findrank()
        if p1performance[0]>p2performance[0]:
            return 1
        elif p1performance[0]<p2performance[0]:
            return 0
        elif p1performance[1]>p2performance[1]:
            return 1
        elif p1performance[1]<p2performance[1]:
            return 0
        else:
            p1hand=self.player1.handvalues()
            p2hand=self.player1.handvalues()
            i=0
            while i<5:
                if p1hand[i]>p2hand[i]:
                    return 1
                elif p1hand[i]<p2hand[i]:
                    return 0
                i+=1
            return 0
    #for testing purposes
    def p1(self):
        return self.player1
    def p2(self):
        return self.player2
    def testranking(self):
        self.player1.printhand()
        print(self.player1.findrank())
        print(self.player1.handvalues())
        self.player2.printhand()
        print(self.player2.findrank())
        

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
ans=0
listofgames=breakupgames(games)
count=0
for g in listofgames:
    newgame=pokergame(g)
    ans+=newgame.whowins()
print(ans)