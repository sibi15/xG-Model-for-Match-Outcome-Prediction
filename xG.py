import random

# 1 goal
def calculateGoals(shots):
        Goals = 0
        for shot in shots:
            if shot >= random.random():
                Goals += 1      
        return Goals

# 1 match
def calculateWinner(home, away):
    HomeGoals = 0
    AwayGoals = 0
    
    HomeGoals = calculateGoals(home)
    AwayGoals = calculateGoals(away)
    
    if HomeGoals > AwayGoals:
        #print("Home Wins! {} - {}".format(HomeGoals, AwayGoals))
        return ("home")
    elif AwayGoals > HomeGoals:
        return ("away")
        #print("Away Wins! {} - {}".format(HomeGoals, AwayGoals))
    else:
        return ("draw")
        #print("Draw! {} - {}".format(HomeGoals, AwayGoals))

# lot of matches
def calculateChance(home, away):
    home_win = 0;
    away_win = 0;
    draw = 0;
    
    for i in range(0,10000):
        matchWinner = calculateWinner(home,away)
        if matchWinner == "home":
            home_win += 1
        elif matchWinner == "away":
            away_win += 1
        else:
            draw += 1

    home_win = home_win/100
    away_win = away_win/100
    draw = draw/100
    
    print("Over 10000 games, home wins {}%, away wins {}% and there is a draw in {}% of games.".format(home_win,away_win,draw))


HomexG = []
AwayxG = []

n_home = int(input("Enter number of shots taken by home team: ")
for i in range(n_home):
    HomexG[i] = int(input("Enter home team shot xG: ")
                    
n_away = int(input("Enter number of shots taken by away team: ")
for i in range(n_away):
    AwayxG[i] = int(input("Enter away team shot xG: ")
calculateChance(HomexG,AwayxG)
