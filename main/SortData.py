from getData import *
from Team_class import *
import os
from helper import *


NBA_teams_checklist={}
NBA_teams={}
Ranking={}
offensive_efficiency={}
defensive_efficiency={}


dir = os.path.dirname(__file__)+'/results/'
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
#create classes for each team
for key,value in NBA_teams_checklist.items():
    NBA_teams[key]=Team(key,value)

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
#NBA_teams['GSW'].team_theoretical_points() 
#####################################################################################################################
###########################test###############################################

ranking_points_per_game(NBA_teams,NBA_teams_checklist,Ranking)
#trade_player(NBA_teams,NBA_teams_checklist)
ranking_points_per_game(NBA_teams,NBA_teams_checklist,Ranking)
off_and_deff_efficiency_rating(overall_team_standings,offensive_efficiency,defensive_efficiency,NBA_teams,NBA_teams_checklist)
#NBA_teams['BOS'].change_effeiciency()
four_factors(NBA_teams,NBA_teams_checklist, overall_team_standings)

