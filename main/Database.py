import sqlite3
import os
import json
from Player_class import Player

dir = os.path.dirname(__file__)+'/results/'
active_players_json=open(dir+'active_players-nba-2016-2017-regular.json').read()
conference_team_standing_json=open(dir+"conference_team_standings-nba-2016-2017-regular.json").read()
cumulative_player_stats_json=open(dir+"cumulative_player_stats-nba-2016-2017-regular.json").read()
division_team_standings_json=open(dir+"division_team_standings-nba-2016-2017-regular.json").read()
full_game_schedule_json=open(dir+"full_game_schedule-nba-2016-2017-regular.json").read()
overall_team_standings_json=open(dir+"overall_team_standings-nba-2016-2017-regular.json").read()
player_injuries_json=open(dir+"player_injuries-nba-2016-2017-regular.json").read()
playoff_team_standings_json=open(dir+"playoff_team_standings-nba-2016-playoff.json").read()
team_gamelogs_base=dir+"team_gamelogs-nba-2016-2017-regular-"

active_players=json.loads(active_players_json)
conference_team_standing=json.loads(conference_team_standing_json)
cumulative_player_stats=json.loads(cumulative_player_stats_json)
division_team_standings=json.loads(division_team_standings_json)
full_game_schedule=json.loads(full_game_schedule_json)
overall_team_standings=json.loads(overall_team_standings_json)
player_injuries=json.loads(player_injuries_json)
playoff_team_standings=json.loads(playoff_team_standings_json)






year_team_player =sqlite3.connect("NBA_Database.db")
#cursor
c=year_team_player.cursor()

def create_table_year():
	c.execute('CREATE TABLE IF NOT EXISTS season_year(startyear REAL PRIMARY KEY,endyear REAL)')

#i have no idea how to split all those params into different lines
def create_table_teams():
	c.execute('''CREATE TABLE IF NOT EXISTS team(teamID REAL PRIMARY KEY,
                                                    team_name_abbre TEXT,
                                                    full_name TEXT,
                                                    field_goal_attempts REAL,
                                                    turnovers REAL,
                                                    freethrow_attempts REAL,
                                                    offensive_rebonds REAL,
                                                    points_scored REAL,
                                                    points_allowed REAL,
                                                    game_possession REAL,
                                                    offensive_efficiency REAL,
                                                    defensive_efficiency REAL,
                                                    treys_made REAL,
                                                    free_throws_made REAL, 
                                                    startyear REAL,
                                                    FOREIGN KEY (startyear) REFERENCES season_year(startyear)ON DELETE SET NULL)''')



def create_table_player():
	c.execute('''CREATE TABLE IF NOT EXISTS player(playerID REAL PRIMARY KEY,
                                                    Firstname TEXT,
                                                    Lastname TEXT,
                                                    Fullname TEXT,
                                                    position TEXT,
                                                    points_per_game REAL,
                                                    assists_per_game REAL,
                                                    effective_field_goal_percentage REAL,
                                                    true_shooting_percentage REAL,
                                                    field_goal_attempts REAL,
                                                    field_goals_made REAL,
                                                    free_throw_attempts REAL,
                                                    free_throws_made REAL,
                                                    treys_made REAL,
                                                    off_reb_per_game REAL,
                                                    points_produced REAL,
                                                    teamID REAL, 
                                                    startyear REAL,
                                                    FOREIGN KEY (teamID) REFERENCES team(teamID) ON DELETE SET NULL,
                                                    FOREIGN KEY (startyear) REFERENCES season_year(startyear) ON DELETE SET NULL)''')




def data_entry_test():
	c.execute('INSERT INTO season_year VALUES(2016,2017)')
	c.execute('INSERT INTO team VALUES(01,"bos","boston",2016)')
	c.execute('INSERT INTO team VALUES(02,"cle","cavs",2016)')
	c.execute('INSERT INTO player VALUES(001,"erick","zhang",01)')
	c.execute('INSERT INTO player VALUES(002,"erick","zhang jr",01)')
	c.execute('INSERT INTO player VALUES(010,"ALEX","LEE",02)')
	c.execute('INSERT INTO player VALUES(011,"ALEX","LEE JR",02)')
	#run everytime after modifying the  database
	year_team_player.commit()
	c.close()
	year_team_player.close()

def team_entry():
    for b in range(0,len(overall_team_standings["overallteamstandings"]["teamstandingsentry"])):
        teamid=overall_team_standings['overallteamstandings']['teamstandingsentry'][b]['team']['ID']
        team_name_abbre=overall_team_standings['overallteamstandings']['teamstandingsentry'][b]['team']['Abbreviation']
        team_name=overall_team_standings['overallteamstandings']['teamstandingsentry'][b]['team']['Name']
        city = overall_team_standings['overallteamstandings']['teamstandingsentry'][b]['team']['City']
        full_name=city+" "+team_name
        field_goal_attempts=float(overall_team_standings['overallteamstandings']['teamstandingsentry'][b]['stats']['FgAttPerGame']['#text'])
        turnovers=float(overall_team_standings['overallteamstandings']['teamstandingsentry'][b]['stats']['TovPerGame']['#text'])
        freethrow_attempts=float(overall_team_standings['overallteamstandings']['teamstandingsentry'][b]['stats']['FtAttPerGame']['#text'])
        offensive_rebonds=float(overall_team_standings['overallteamstandings']['teamstandingsentry'][b]['stats']['OffRebPerGame']['#text'])
        points_scored=float(overall_team_standings['overallteamstandings']['teamstandingsentry'][b]['stats']['PtsPerGame']['#text'])
        points_allowed=float(overall_team_standings['overallteamstandings']['teamstandingsentry'][b]['stats']['PtsAgainstPerGame']['#text'])
        game_possession=0.96*(field_goal_attempts+turnovers+0.44*freethrow_attempts-offensive_rebonds)
        offensive_efficiency=100*points_scored/game_possession
        defensive_efficiency=100*points_allowed/game_possession
        treys_made = float(overall_team_standings['overallteamstandings']['teamstandingsentry'][b]['stats']['Fg3PtMadePerGame']['#text'])
        free_throws_made = float(overall_team_standings['overallteamstandings']['teamstandingsentry'][b]['stats']['FtMadePerGame']['#text'])



        #need to change this to set it dynamically but dk which file to use
        startyear=2016
        c.execute('INSERT INTO team(teamID,team_name_abbre,full_name,field_goal_attempts,turnovers,freethrow_attempts,offensive_rebonds,points_scored,points_allowed,game_possession,offensive_efficiency,defensive_efficiency,treys_made,free_throws_made,startyear) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
        						  ,(teamid,team_name_abbre,full_name,field_goal_attempts,turnovers,freethrow_attempts,offensive_rebonds,points_scored,points_allowed,game_possession,offensive_efficiency,defensive_efficiency,treys_made,free_throws_made,startyear))
        year_team_player.commit()




def player_entry(active_players):
    for x in range(0,len(cumulative_player_stats['cumulativeplayerstats']['playerstatsentry'])):
        base = cumulative_player_stats['cumulativeplayerstats']['playerstatsentry'][x]
        raw_stats = base['stats']
        raw_player = base['player']
        fitsname = raw_player['FirstName']
        lastname = raw_player['LastName']
        full_name = fitsname+" "+lastname
        position = raw_player['Position']
        playerid = raw_player['ID']
        teamID = base['team']['ID']
        team_name_abbr = str(base['team']['Abbreviation'])
        points_per_game = float(raw_stats['PtsPerGame']['#text'])
        assists_per_game = float(raw_stats['AstPerGame']['#text'])
        field_goal_attempts = float(raw_stats['FgAttPerGame']['#text'])
        field_goals_made = float(raw_stats['FgMadePerGame']['#text'])
        free_throw_attempts = float(raw_stats['FtAttPerGame']['#text'])
        free_throws_made = float(raw_stats['FtMadePerGame']['#text'])
        treys_made = float(raw_stats['Fg3PtMadePerGame']['#text'])
        off_reb_per_game = float(raw_stats['OffRebPerGame']['#text'])
        if free_throw_attempts > 0:
            effective_field_goal_percentage = ((field_goals_made + (0.5 * treys_made)) / field_goal_attempts) * 100.0
            true_shooting_percentage = points_per_game / (2.0 * (field_goal_attempts + 0.44 * free_throw_attempts)) * 100.0
        points_produced = ((1.45 * field_goals_made) +
                           (2.2 * treys_made) + free_throws_made +
                           (0.6 * off_reb_per_game) +
                           (0.6 * assists_per_game))
        startyear=2016
        c.execute('''INSERT INTO player(playerID,
                                        Firstname,
                                        Lastname,
                                        Fullname,
                                        position,
                                        points_per_game,
                                        assists_per_game,
                                        effective_field_goal_percentage,
                                        true_shooting_percentage,
                                        field_goal_attempts,
                                        field_goals_made,
                                        free_throw_attempts,
                                        free_throws_made,
                                        treys_made,
                                        off_reb_per_game,
                                        points_produced,
                                        teamID, 
                                        startyear
                                                ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                                        (playerid,
                                        fitsname,
                                        lastname,
                                        full_name,
                                        position,
                                        points_per_game,
                                        assists_per_game,
                                        effective_field_goal_percentage,
                                        true_shooting_percentage,
                                        field_goal_attempts,
                                        field_goals_made,
                                        free_throw_attempts,
                                        free_throws_made,
                                        treys_made,
                                        off_reb_per_game,
                                        points_produced,
                                        teamID,
                                        startyear))
                
        year_team_player.commit()
def grab_data():
	c.execute('SELECT Firstname FROM player WHERE teamID=01 AND startyear=2016')
	data=c.fetchall()
	print(data)

def trade_player_db(firstPlayer,secondPlayer):
    original_first_team = str(firstPlayer.get_team_id())
    original_second_team = str(secondPlayer.get_team_id())
    #trade first player to second's team
    c.execute('UPDATE player SET teamID = ' + original_second_team + ' WHERE playerID = ' + str(firstPlayer.get_player_id()))

    #trade second player to first's team
    c.execute('UPDATE player SET teamID = ' + original_first_team + ' WHERE playerID = ' + str(secondPlayer.get_player_id()))
    year_team_player.commit()
#data_entry()