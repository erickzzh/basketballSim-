from getData import *
from Team_class import *
from collections import OrderedDict
import os
import pandas as pandapandapanda
import matplotlib.pyplot as plt
from matplotlib import style




dir = os.path.dirname(__file__)+'/results/'
NBA_teams_checklist={}
NBA_teams={}
Ranking={}
offensive_efficiency={}
defensive_efficiency={}
active_players_json=open(dir+'active_players-nba-2016-2017-regular.json').read()
conference_team_standing_json=open(dir+"conference_team_standings-nba-2016-2017-regular.json").read()
cumulative_player_stats_json=open(dir+"cumulative_player_stats-nba-2016-2017-regular.json").read()
division_team_standings_json=open(dir+"division_team_standings-nba-2016-2017-regular.json").read()
full_game_schedule_json=open(dir+"full_game_schedule-nba-2016-2017-regular.json").read()
overall_team_standings_json=open(dir+"overall_team_standings-nba-2016-2017-regular.json").read()
player_injuries_json=open(dir+"player_injuries-nba-2016-2017-regular.json").read()
playoff_team_standings_json=open(dir+"playoff_team_standings-nba-2016-playoff.json").read()

active_players=json.loads(active_players_json)
conference_team_standing=json.loads(conference_team_standing_json)
cumulative_player_stats=json.loads(cumulative_player_stats_json)
division_team_standings=json.loads(division_team_standings_json)
full_game_schedule=json.loads(full_game_schedule_json)
overall_team_standings=json.loads(overall_team_standings_json)
player_injuries=json.loads(player_injuries_json)
playoff_team_standings=json.loads(playoff_team_standings_json)

#########################trade players###################
def trade_player():
    pprint(NBA_teams_checklist)
    team1=input("Which team? (enter abbre only) : ").upper()
    NBA_teams[team1].print_roster_and_points()
    player1=input("Which player? (enter Full name including upper case) : ")#will change later
    pprint(NBA_teams_checklist)
    team2=input("Which team? (enter abbre only) : ").upper()
    NBA_teams[team2].print_roster_and_points()
    player2=input("Which player? (enter Full name including upper case) : ")#will change later
    NBA_teams[team1].trade_players_roster(player1,player2)
    NBA_teams[team2].trade_players_roster(player2,player1)
    TEMP=NBA_teams[team1].roster_class[player1]
    NBA_teams[team1].roster_class[player1]=NBA_teams[team2].roster_class[player2]
    NBA_teams[team1].roster_class[player2]=NBA_teams[team1].roster_class.pop(player1)
    NBA_teams[team2].roster_class[player2]=TEMP
    NBA_teams[team2].roster_class[player1]=NBA_teams[team2].roster_class.pop(player2)
#########################################################

# #############################ranking###################
def ranking_points_per_game():
    for y in NBA_teams_checklist:
        Ranking[NBA_teams[y].team_name]= NBA_teams[y].get_team_theorical_points()
    #rank by value 
    ranking_descending=OrderedDict(sorted(Ranking.items(), key=lambda t: t[1],reverse=True))
    for key, value in ranking_descending.items() :
        print (key, value)
#########################################################


more_data=input("Enter data(Y/N): ")
if more_data.lower() == 'y':
    more_data=True
else:
    more_data=None

#check for more data
while more_data:
    print("Enter 'general' for data contain \ncumulative player stats\nfull game schedule\nactive player\noverall team standings\nconference team standings\ndivision team standings\nplayoff team standings\nplayer injuries\nlatest updates\n\n")
    print("Or enter 'daily'  for \ndaily_game_schedule\ndaily_player_stats three\nscoreboard\nroster_player\n\n")
    print("or enter 'gamelogs' for \nplayer game logs\nteam game logs\n\n")
    print("or enter 'game' for \ngame_playbyplay\ngame_boxscore\ngame_startinglineup\n\n")

    request_type=input("Enter the data type: ")
    if request_type=="general":
        request_general()
    elif request_type=="daily":
        request_daily()
    elif request_type=="gamelogs":
        request_gamelogs()
    elif request_type=="game":
        request_game()
    else:
        print("Wrong input try again")
    
    more=input("More data?: (Y/N)")
    if more.lower() =="y":
        more_data=True
        clear_input()
    else:
        more_data=None
        
        clear_input()

##################################populates the roster list as well as creating the team class(including all attributes within the team class)######################
#populate the team check list to get a complete team abbre
for a in range(0,len(cumulative_player_stats['cumulativeplayerstats']['playerstatsentry'])):
    team_name_abbr=str(cumulative_player_stats['cumulativeplayerstats']['playerstatsentry'][a]['team']['Abbreviation'])
    team_name_and_city=str(cumulative_player_stats['cumulativeplayerstats']['playerstatsentry'][a]['team']['City']+" "+cumulative_player_stats['cumulativeplayerstats']['playerstatsentry'][a]['team']['Name'])
    if team_name_abbr not in NBA_teams_checklist.keys():
        NBA_teams_checklist[team_name_abbr]=team_name_and_city
    else:
        pass

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
    NBA_teams[key]=Team(key,value)
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

#populate each team with a complete roster
for x in range(0,len(cumulative_player_stats['cumulativeplayerstats']['playerstatsentry'])):
    team_name_abbr=str(cumulative_player_stats['cumulativeplayerstats']['playerstatsentry'][x]['team']['Abbreviation'])
    FirstName=str(cumulative_player_stats['cumulativeplayerstats']['playerstatsentry'][x]['player']['FirstName'] + " ")
    LastName=str(cumulative_player_stats['cumulativeplayerstats']['playerstatsentry'][x]['player']['LastName'])
    FullName=FirstName+LastName
    player_position=str(cumulative_player_stats['cumulativeplayerstats']['playerstatsentry'][x]['player']['Position'])
    player_points_per_game=float(cumulative_player_stats['cumulativeplayerstats']['playerstatsentry'][x]['stats']['PtsPerGame']['#text'])
    #populate the roster
    NBA_teams[team_name_abbr].add_players_roster(FullName)
    #populate the player class
    NBA_teams[team_name_abbr].add_players_class(FirstName,LastName,player_points_per_game,player_position)
#NBA_teams['BOS'].print_roster()   //print roster
#NBA_teams['CLE'].print_player_points_helper("Kevin Love")      //print points by passing a name
#NBA_teams['GSW'].team_theorical_points() 
#####################################################################################################################


#NBA_teams['BOS'].change_effeiciency()


