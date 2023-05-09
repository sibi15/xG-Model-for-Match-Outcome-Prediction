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

HomexG = [0.15,0.22,0.33,0.18]
AwayxG = [0.25,0.45,0.33]
calculateChance(HomexG,AwayxG)
