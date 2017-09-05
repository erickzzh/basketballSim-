'''This module handles all interactions with our SQLite database'''
import sqlite3
import os
import json
from Player_class import Player

#open json files and load them into data structures for easier access
dir = os.path.dirname(__file__)+'/results/'

active_players_json = open(dir+'active_players-nba-2016-2017-regular.json').read()
conference_team_standing_json = open(dir+"conference_team_standings-nba-2016-2017-regular.json").read()
cumulative_player_stats_json = open(dir+"cumulative_player_stats-nba-2016-2017-regular.json").read()
division_team_standings_json = open(dir+"division_team_standings-nba-2016-2017-regular.json").read()
full_game_schedule_json = open(dir+"full_game_schedule-nba-2016-2017-regular.json").read()
overall_team_standings_json = open(dir+"overall_team_standings-nba-2016-2017-regular.json").read()
player_injuries_json = open(dir+"player_injuries-nba-2016-2017-regular.json").read()
playoff_team_standings_json = open(dir+"playoff_team_standings-nba-2016-playoff.json").read()

team_gamelogs_base = dir+"team_gamelogs-nba-2016-2017-regular-"

active_players = json.loads(active_players_json)
conference_team_standing = json.loads(conference_team_standing_json)
cumulative_player_stats = json.loads(cumulative_player_stats_json)
division_team_standings = json.loads(division_team_standings_json)
full_game_schedule = json.loads(full_game_schedule_json)
overall_team_standings = json.loads(overall_team_standings_json)
player_injuries = json.loads(player_injuries_json)
playoff_team_standings = json.loads(playoff_team_standings_json)


#connect to our sqlite database
year_team_player = sqlite3.connect("NBA_Database.db")
#setup cursor
c = year_team_player.cursor()

def create_table_year():
    '''make the table for the season if it hasn't been made yet'''
    c.execute('CREATE TABLE IF NOT EXISTS season_year(startyear REAL PRIMARY KEY,endyear REAL)')

def create_table_teams():
    '''makes the table that contains all team entries'''
    c.execute('''CREATE TABLE IF NOT EXISTS team(teamID REAL PRIMARY KEY,
                                                    team_name_abbre TEXT,
                                                    team_name TEXT,
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

                                                    field_goal_attempts_pct REAL,
                                                    defensive_rebonds REAL,
                                                    opponent_fg_pct REAL,
                                                    opponent_dor_pct REAL,
                                                    opponent_possession REAL,

                                                    opponent_fga REAL,
                                                    opponent_fgm REAL,
                                                    opponent_turnover REAL,
                                                    opponent_fta REAL,
                                                    opponent_ftm REAL,
                                                    fouls REAL,
                                                    blocks REAL,
                                                    steals REAL,
                                                    field_goal_made REAL,
                                                    FOREIGN KEY (startyear) REFERENCES season_year(startyear)ON DELETE SET NULL)''')

def create_table_player():
    '''makes the table that contains an entry for every player in the league'''
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
                                                    def_reb_per_game REAL,
                                                    points_produced REAL,
                                                    turnover REAL,
                                                    usage REAL,
                                                    minutes REAL,
                                                    blocks REAL,
                                                    steals REAL,
                                                    teamID REAL, 
                                                    teamName TEXT,
                                                    startyear REAL,
                                                    fouls REAL,
                                                    FOREIGN KEY (teamID) REFERENCES team(teamID) ON DELETE SET NULL,
                                                    FOREIGN KEY (startyear) REFERENCES season_year(startyear) ON DELETE SET NULL)''')
# def temp_method():
#     c.execute('''DROP TABLE player''')
#     year_team_player.commit()

def data_entry_test():
    '''test method for database functionality'''
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

def team_entry(NBA_teams):
    '''fill in all columns of each team in the teams table'''
    for b in range(0, len(overall_team_standings["overallteamstandings"]["teamstandingsentry"])):
        base = overall_team_standings['overallteamstandings']['teamstandingsentry'][b]
        stats = base['stats']
        teamid = base['team']['ID']
        team_name_abbre = base['team']['Abbreviation']
        team_name = base['team']['Name']
        city = base['team']['City']

        full_name = city + " " + team_name
        field_goal_attempts = float(stats['FgAttPerGame']['#text'])
        turnovers = float(stats['TovPerGame']['#text'])
        freethrow_attempts = float(stats['FtAttPerGame']['#text'])
        offensive_rebonds = float(stats['OffRebPerGame']['#text'])
        points_scored = float(stats['PtsPerGame']['#text'])
        points_allowed = float(stats['PtsAgainstPerGame']['#text'])
        game_possession = 0.96 * (field_goal_attempts + turnovers + 0.44 * freethrow_attempts - offensive_rebonds)
        offensive_efficiency = 100 * points_scored/game_possession
        defensive_efficiency = 100 * points_allowed/game_possession
        treys_made = float(stats['Fg3PtMadePerGame']['#text'])
        free_throws_made = float(stats['FtMadePerGame']['#text'])
        field_goal_attempts_pct = float(stats['FgPct']['#text'])
        defensive_rebonds = float(stats['DefRebPerGame']['#text'])
        field_goal_made = float(stats['FgMadePerGame']['#text'])
        opponent_fg_pct = 0
        opponent_dor_pct = 0
        opponent_possession = 0
        opponent_fga = 0
        opponent_fgm = 0
        opponent_turnover = 0
        opponent_fta = 0
        opponent_ftm = 0
        fouls = float(stats['FoulsPerGame']['#text'])
        blocks  = float(stats['BlkPerGame']['#text'])
        steals  = float(stats['StlPerGame']['#text'])

        startyear = 2016
        c.execute('''INSERT INTO team(teamID,
                                        team_name_abbre,
                                        team_name,
                                        full_name,
                                        field_goal_attempts,
                                        turnovers,freethrow_attempts,
                                        offensive_rebonds,
                                        points_scored,points_allowed,
                                        game_possession,
                                        offensive_efficiency,
                                        defensive_efficiency,
                                        treys_made,
                                        free_throws_made,
                                        startyear,
                                        field_goal_attempts_pct ,
                                        defensive_rebonds ,
                                        opponent_fg_pct ,
                                        opponent_dor_pct,
                                        opponent_possession,
                                        opponent_fga,
                                        opponent_fgm,
                                        opponent_turnover,
                                        opponent_fta,
                                        opponent_ftm,
                                        fouls,
                                        blocks,
                                        steals,
                                        field_goal_made                                        ) 
                                        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
        						    , (teamid, 
                                        team_name_abbre,
                                        team_name,
                                        full_name, 
                                        field_goal_attempts, 
                                        turnovers, 
                                        freethrow_attempts, 
                                        offensive_rebonds, 
                                        points_scored, 
                                        points_allowed, 
                                        game_possession, 
                                        offensive_efficiency, 
                                        defensive_efficiency, 
                                        treys_made, 
                                        free_throws_made, 
                                        startyear,

                                        field_goal_attempts_pct ,
                                        defensive_rebonds ,
                                        opponent_fg_pct ,
                                        opponent_dor_pct,
                                        opponent_possession,
                                        opponent_fga,
                                        opponent_fgm,
                                        opponent_turnover,
                                        opponent_fta,
                                        opponent_ftm,
                                        fouls,
                                        blocks,
                                        steals,
                                        field_goal_made))
        year_team_player.commit()

    #for loop to populate the opponent_fg_pct,opponent_dor_pct,opponent_possession values 
    for a in range(0, len(overall_team_standings["overallteamstandings"]["teamstandingsentry"])):
        base = overall_team_standings['overallteamstandings']['teamstandingsentry'][a]
        stats = base['stats']
        teamid = base['team']['ID']
        team_name_abbre = base['team']['Abbreviation']
        team_name = base['team']['Name']
        city = base['team']['City']


        opponent_fg_pct = 0
        opponent_dor_pct = 0
        opponent_possession = 0
        opponent_fga = 0
        opponent_fgm = 0
        opponent_turnover = 0
        opponent_fta = 0
        opponent_ftm = 0

        for x in range (0,82):
            opponent = NBA_teams[team_name_abbre].game_schedule[x]
            c.execute('SELECT teamID FROM team WHERE team_name_abbre=? AND startyear=2016',(opponent,))
            opponent_id = c.fetchone()[0]

            #get opponent field goal %
            c.execute('SELECT field_goal_attempts_pct FROM team WHERE teamID=? AND startyear=2016',(opponent_id,))
            fg_pct = c.fetchone()[0]
            print(fg_pct)
            opponent_fg_pct += fg_pct
            year_team_player.commit()

            #get opponent DOR%
            c.execute('SELECT offensive_rebonds FROM team WHERE teamID=? AND startyear=2016',(opponent_id,))
            opponent_ofr = c.fetchone()[0]
            c.execute('SELECT defensive_rebonds FROM team WHERE teamID=? AND startyear=2016',(teamid,))
            base_team_dfr = c.fetchone()[0]
            opponent_dor_pct += (opponent_ofr / (opponent_ofr + base_team_dfr))

            #get opponent possession
            c.execute('SELECT game_possession FROM team WHERE teamID=? AND startyear=2016',(opponent_id,))
            opponent_poss = c.fetchone()[0]   
            opponent_possession += opponent_poss 

            #get opponent fga
            c.execute('SELECT field_goal_attempts FROM team WHERE teamID=? AND startyear=2016',(opponent_id,))
            fga = c.fetchone()[0]   
            opponent_fga += fga 

            #get opponent fgm
            c.execute('SELECT field_goal_made FROM team WHERE teamID=? AND startyear=2016',(opponent_id,))
            fgm = c.fetchone()[0]   
            opponent_fgm += fgm 

             #get opponent turnover
            c.execute('SELECT turnovers FROM team WHERE teamID=? AND startyear=2016',(opponent_id,))
            turnover = c.fetchone()[0]   
            opponent_turnover += turnover 

             #get opponent turnover
            c.execute('SELECT field_goal_attempts FROM team WHERE teamID=? AND startyear=2016',(opponent_id,))
            freethrow_attempts = c.fetchone()[0]   
            opponent_fta+= freethrow_attempts 

            #get opponent turnover
            c.execute('SELECT free_throws_made FROM team WHERE teamID=? AND startyear=2016',(opponent_id,))
            ftm = c.fetchone()[0]   
            opponent_ftm+= ftm 


        #update table    
        c.execute('''UPDATE team SET opponent_fg_pct = ?/82,
                                     opponent_dor_pct = ?/82,
                                     opponent_possession = ?/82, 
                                     opponent_fga = ?/82,
                                     opponent_fgm = ?/82,
                                     opponent_turnover = ?/82,
                                     opponent_fta = ?/82,
                                     opponent_ftm = ?/82




                                     WHERE teamID = ?''',(opponent_fg_pct,opponent_dor_pct,opponent_possession,opponent_fga,opponent_fgm,opponent_turnover,opponent_fta,opponent_ftm,teamid))
        year_team_player.commit()       




def player_entry(active_players):
    '''fill in all columns of each player in the players table'''
    for x in range(0, len(cumulative_player_stats['cumulativeplayerstats']['playerstatsentry'])):
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
        def_reb_per_game = float(raw_stats['DefRebPerGame']['#text'])
        turnover = float(raw_stats['TovPerGame']['#text'])
        minutes = float(raw_stats['MinSecondsPerGame']['#text'])/60.0
        minutes = round(minutes,1)
        steals = float(raw_stats['StlPerGame']['#text'])
        blocks = float(raw_stats['BlkPerGame']['#text'])
        teamName = str(base['team']['Abbreviation'])
        fouls = float(raw_stats['FoulPersPerGame']['#text'])
        usage = 0


        if free_throw_attempts > 0:
            effective_field_goal_percentage = ((field_goals_made + (0.5 * treys_made)) / field_goal_attempts) * 100.0
            true_shooting_percentage = points_per_game / (2.0 * (field_goal_attempts + 0.44 * free_throw_attempts)) * 100.0
        points_produced = ((1.45 * field_goals_made) +
                           (2.2 * treys_made) + free_throws_made +
                           (0.6 * off_reb_per_game) +
                           (0.6 * assists_per_game))

        startyear = 2016
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
                                        def_reb_per_game,
                                        points_produced,
                                        turnover,
                                        usage,
                                        minutes,
                                        blocks,
                                        steals,
                                        teamID, 
                                        teamName,
                                        startyear,
                                        fouls)
                                        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
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
                                        def_reb_per_game,
                                        points_produced,
                                        turnover,
                                        usage,
                                        minutes,
                                        blocks,
                                        steals,
                                        teamID,
                                        teamName,
                                        startyear,
                                        fouls))

        year_team_player.commit()

def grab_data():
    '''obtain data for testing purposes'''
    c.execute('SELECT turnovers FROM team WHERE teamID=109 AND startyear=2016')
    data = c.fetchone()[0]
    print (data)

def trade_player_db(firstPlayer, secondPlayer):
    '''performs the necessary updates to the players table to perform a trade'''
    original_first_team = str(firstPlayer.get_team_id())
    original_second_team = str(secondPlayer.get_team_id())

    #trade first player to second's team
    c.execute('UPDATE player SET teamID = ' + original_second_team +
              ' WHERE playerID = ' + str(firstPlayer.get_player_id()))

    #trade second player to first's team
    c.execute('UPDATE player SET teamID = ' + original_first_team +
              ' WHERE playerID = ' + str(secondPlayer.get_player_id()))
    year_team_player.commit()

#data_entry()
