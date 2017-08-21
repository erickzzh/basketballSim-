from collections import OrderedDict
from pprint import pprint
import pandas as pandapandapanda
import matplotlib.pyplot as plt
from matplotlib import style

def ranking_points_per_game(NBA_teams,NBA_teams_checklist,Ranking):
    for y in NBA_teams_checklist:
        Ranking[NBA_teams[y].team_name]= NBA_teams[y].get_team_theoretical_points()
    #rank by value 
    ranking_descending=OrderedDict(sorted(Ranking.items(), key=lambda t: t[1],reverse=True))
    for key, value in ranking_descending.items() :
        print (key, value)

def trade_player(NBA_teams,NBA_teams_checklist):
    pprint(NBA_teams_checklist)
    team1=input("Which team? (enter abbre only) : ").upper()
    NBA_teams[team1].print_roster_and_points()
    player1=input("Which player? (enter Full name including upper case and space) : ")#will change later
    pprint(NBA_teams_checklist)
    team2=input("Which team? (enter abbre only) : ").upper()
    NBA_teams[team2].print_roster_and_points()
    player2=input("Which player? (enter Full name including upper case and space) : ")#will change later
    NBA_teams[team1].trade_players_roster(player1,player2)
    NBA_teams[team2].trade_players_roster(player2,player1)
    TEMP=NBA_teams[team1].roster_class[player1]
    NBA_teams[team1].roster_class[player1]=NBA_teams[team2].roster_class[player2]
    NBA_teams[team1].roster_class[player2]=NBA_teams[team1].roster_class.pop(player1)
    NBA_teams[team2].roster_class[player2]=TEMP
    NBA_teams[team2].roster_class[player1]=NBA_teams[team2].roster_class.pop(player2)

def off_and_deff_efficiency_rating(overall_team_standings,offensive_efficiency,defensive_efficiency,NBA_teams,NBA_teams_checklist):
    #offensive efficiency and defensive efficiency 
    for b in range(0,len(overall_team_standings["overallteamstandings"]["teamstandingsentry"])):
        team_name_abbr=overall_team_standings['overallteamstandings']['teamstandingsentry'][b]['team']['Abbreviation']
        field_goal_attempts=float(overall_team_standings['overallteamstandings']['teamstandingsentry'][b]['stats']['FgAttPerGame']['#text'])
        turnovers=float(overall_team_standings['overallteamstandings']['teamstandingsentry'][b]['stats']['TovPerGame']['#text'])
        freethrow_attempts=float(overall_team_standings['overallteamstandings']['teamstandingsentry'][b]['stats']['FtAttPerGame']['#text'])
        offensive_rebonds=float(overall_team_standings['overallteamstandings']['teamstandingsentry'][b]['stats']['OffRebPerGame']['#text'])
        points_scored=float(overall_team_standings['overallteamstandings']['teamstandingsentry'][b]['stats']['PtsPerGame']['#text'])
        points_allowed=float(overall_team_standings['overallteamstandings']['teamstandingsentry'][b]['stats']['PtsAgainstPerGame']['#text'])
        game_possession=0.96*(field_goal_attempts+turnovers+0.44*freethrow_attempts-offensive_rebonds)
        offensive_efficiency[team_name_abbr]=100*points_scored/game_possession
        defensive_efficiency[team_name_abbr]=100*points_allowed/game_possession
        print(team_name_abbr,offensive_efficiency[team_name_abbr],defensive_efficiency[team_name_abbr])


    fig, ax=plt.subplots()
    #create classes for each team
    for key,value in NBA_teams_checklist.items():
        NBA_teams[key].offensive_efficiency=offensive_efficiency[key]
        NBA_teams[key].defensive_efficiency=defensive_efficiency[key]

        ax.scatter(NBA_teams[key].offensive_efficiency,NBA_teams[key].defensive_efficiency)

    #invert the y-axis
    #top right savage teams
    #bottom left dumb fk teams
    #need to work on the annotate function
    plt.ylim(125,110)  
    plt.xlabel("offensive efficiency")
    plt.ylabel("defensive efficiency")
    plt.title("efficiency plot")
    plt.show()