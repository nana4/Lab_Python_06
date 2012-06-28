"""
Lab_Python_06
Part 1
"""

"""
Whatever the datastructure you choose,
it should represent the following data:

player		| date		| score
_______________________________________
rooney		| 6/23/2012	| 2
rooney		| 6/25/2012	| 2
ronaldo		| 6/19/2012	| 0
ronaldo		| 6/20/2012	| 3
torres		| 6/21/2012	| 0
torres		| 6/21/2012	| 1
"""
'''
## create the player_stats data structure
import datetime
from datetime import date
a=str(date(2012,6,23))
b=str(date(2012,6,25))
c=str(date(2012,6,19))
d=str(date(2012,6,20))
e=str(date(2012,6,21))
f=str(date(2012,6,22))
player_stats={'rooney' : [(a,1),(b,2)],                       
              'ronaldo': [(c,0),(d,3)],                       
              'torres' : [(e,0),(f,1)]
              } 
## implement highest_score
print "HIGHEST SCORE IN SYSTEM"
def highest_score(player_stats):
    high = 0
    Hname=""
    for name in player_stats:
        for i in player_stats[name]:
            if i[1]>high:
                
                high=i[1]
                Hname=name
            else:
                pass

    print "Player with highest score is ",Hname,"\n Number of goals = ",high,"\ndate scored = ",i[0]     

highest_score(player_stats)
## implement highest_score_for_player
print "HIGHEST SCORE FOR EACH PLAYER"
def highest_score_for_player(player_stats):
    Hname = ""
    for name in player_stats:
        for i in player_stats[name]:
            high=0
            if i[1]>high:
                if high == i[1]:
                    print
                else:
                    high = i[1]
                Hname = name 
                print Hname,high  
    return
highest_score_for_player(player_stats)


## implement highest_scorer
print "HIGHEST SCORER"
def highest_scorer(player_stats):
    Hname = ""
    for name in player_stats:
        sum1=0
        sum2=0
        for i in player_stats[name]:
            
           sum1 = i[1]+ sum1
           if sum1 == sum2:
               Hname=name
               
           if sum1>sum2:
               sum2=sum1
               Hname +="and"+ name
               
    print Hname, " has the highest score of ", sum2,
    

    return
highest_scorer(player_stats)
'''
##PART II
import datetime
from datetime import date
class player:
    def __init__(self,firstname,lastname,team):
        
        
        self.first_name = firstname
        self.last_name = lastname
        self.scores = []
        self.team = team
        
    def add_score(self,date,score):
        scores = self.scores
        scores.append(score)
        return scores

    def total_score(self):
        t_score=sum(self.scores)
        return t_score
    
    def average_score(self):
        avg_score=sum(self.scores)/float(len(self.scores))
        return avg_score
    


class team :
        def __init__(self,t_name,t_league,t_mgr_name,t_pts,):
            self.team_name = t_name
            self.league =t_league
            self.players = []
            self.points = t_pts
            self.manager = t_mgr_name
            
        def __str__(self):
            desc = "Team name : "+ self.team_name + "\nNumber of players :" + str(len(self.players)) + "\nManager name : "+self.manager+\
                   "\npoints :"+str(self.points)
            return desc

            
        def add_player(self,player):
            self.players.append(player)
            return


portugal = team('Portugal','Euro','Del Rossi',9,)
spain    = team('Espanyol','Euro','Del Rossi',10,)##created team instances

Torres = player("Fernando","Torres",spain)
Ronaldo = player("Christiano","Ronaldo",portugal) ##created player instances






#torres_score = [0,0,1,0,1]
#for i in torres_score:
 #    Torres.add_score(date.today(),i)
#print Torres.total_score()##total goals for torres_score


#print Torres.average_score()

spain.add_player(Torres)
portugal.add_player(Ronaldo)
#print portugal
#print spain
class Match:
    def __init__(self,home,away,date):
        self.home_team = home
        self.away_team = away
        datetime.date = date
        self.home_scores = {}
        self.away_scores = {}
        self.Away_P_score=[]
        self.Home_P_score=[]
    def home_score(self):
        if len(self.Home_P_score) == 0:
            return 0
        else:
            return sum(self.Home_P_score)


    def away_score(self):
        if len(self.Away_P_score) == 0:
            return 0
        else:
            return sum(self.Away_P_score)
    def winner(self):
        H=self.home_score()
        A=self.away_score()
        if H>A:
            print "Winner of the game played on "+str(datetime.date)+"was\n"+self.home_team+ " with " +str(H)+"goals"
            return 
        elif H<A:
            print "Winner of the game played on "+str(datetime.date)+" was\n" + self.away_team + " with "  + str(A)+" goal(s)"
            return 
        else:
            print "the game ended in a draw"
            return 
        print A,H
    def add_score(self,player,score):
        
        team = player.team.team_name  ####come back here soon
        if team == self.home_team:
            #print "true",player.team.team_name
            
            self.home_scores[player.last_name] = score
            print self.home_scores
            for player in self.home_scores:
                self.Home_P_score.append(score)#self.home_scores[player]) 
            print sum(self.Home_P_score)##prints total goals scored in home team
            
            #print self.home_scores[self.player.last_name]
            #print self.player.last_name
            #print self.home_scores[player]###prints the player's current score
            return sum(self.Home_P_score)
        elif team == self.away_team:
            #print self.away_team
            self.away_scores[player.last_name] = score
            for away_player in self.away_scores:
                self.Away_P_score.append(score)#self.away_scores[player.last_name])
            return #sum(self.Away_P_score)

        else:
            self.away_scores[player.last_name] = score
            for away_player in self.away_scores:
                self.Home_P_score.append(self.home_scores[player.last_name])#add goal to dictionary
            print "false",player.team.team_name
            
            return #sum(self.Home_P_score)
       
       
euro_semi_final = Match('Espanyol','Portugal',str(datetime.date(2012,6,27)))
euro_semi_final.add_score(Torres,1)
euro_semi_final.add_score(Ronaldo,1)
euro_semi_final.add_score(Ronaldo,1)
euro_semi_final.add_score(Ronaldo,1)
euro_semi_final.add_score(Ronaldo,1)
euro_semi_final.add_score(Torres,1)
euro_semi_final.add_score(Torres,1)
print euro_semi_final.winner()




#print spain.team_name







'''team = "Espanyol"
if team == spain.team_name:
    print "true"
    print
    print Torres.team.team_name
    
else:
    print "false"
    print spain.team_name
    print
    print Torres.team.team_name
       '''
        

