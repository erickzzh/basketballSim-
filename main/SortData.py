from getData import *
from Team_class import *


NBA_teams_checklist=[]
NBA_teams={}
active_players_json=open('/Users/erickzhang/Desktop/basketballsimulator/python/results/active_players-nba-2016-2017-regular.json').read()
conference_team_standing_json=open("/Users/erickzhang/Desktop/basketballsimulator/python/results/conference_team_standings-nba-2016-2017-regular.json").read()
cumulative_player_stats_json=open("/Users/erickzhang/Desktop/basketballsimulator/python/results/cumulative_player_stats-nba-2016-2017-regular.json").read()
division_team_standings_json=open("/Users/erickzhang/Desktop/basketballsimulator/python/results/division_team_standings-nba-2016-2017-regular.json").read()
full_game_schedule_json=open("/Users/erickzhang/Desktop/basketballsimulator/python/results/full_game_schedule-nba-2016-2017-regular.json").read()
overall_team_standings_json=open("/Users/erickzhang/Desktop/basketballsimulator/python/results/overall_team_standings-nba-2016-2017-regular.json").read()
player_injuries_json=open("/Users/erickzhang/Desktop/basketballsimulator/python/results/player_injuries-nba-2016-2017-regular.json").read()
playoff_team_standings_json=open("/Users/erickzhang/Desktop/basketballsimulator/python/results/playoff_team_standings-nba-2016-playoff.json").read()

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

while more_data:
    print("Enter 'general' for data contain \ncumulative player stats\nfull game schedule\nactive player\noverall team standings\nconference team standings\ndivision team standings\nplayoff team standings\nplayer injuries\nlatest updates\n\n")
    print("Or enter 'daily'  for \ndaily_game_schedule\ndaily_player_stats three\nscoreboard\n\n")
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

#populate the team check list to get a complete team abbre
for a in range(0,len(cumulative_player_stats['cumulativeplayerstats']['playerstatsentry'])):
    team_name_shortcut=str(cumulative_player_stats['cumulativeplayerstats']['playerstatsentry'][a]['team']['Abbreviation'])
    if team_name_shortcut not in NBA_teams_checklist:
        NBA_teams_checklist.insert(len(NBA_teams_checklist),team_name_shortcut)
    else:
        pass

#create classes for each team
for b in NBA_teams_checklist:
    NBA_teams[b]=Team(b)

#populate each team with a complete roster
for x in range(0,len(cumulative_player_stats['cumulativeplayerstats']['playerstatsentry'])):
    team_name_shortcut=str(cumulative_player_stats['cumulativeplayerstats']['playerstatsentry'][x]['team']['Abbreviation'])
    FirstName=str(cumulative_player_stats['cumulativeplayerstats']['playerstatsentry'][x]['player']['FirstName'] + " ")
    LastName=str(cumulative_player_stats['cumulativeplayerstats']['playerstatsentry'][x]['player']['LastName'])
    FullName=FirstName+LastName
    NBA_teams[team_name_shortcut].add_players(FullName)


NBA_teams['BOS'].print_roster()   
NBA_teams['CLE'].print_roster()     


