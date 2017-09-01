'''contains the TeamFactory class, for loading data from the DB into
    instances of the Team class'''
import sqlite3
from Team_class import Team
import pandas as pandapandapanda
import matplotlib.pyplot as plt
from matplotlib import style
import math
import numpy as np

class TeamFactory:
	"""Contains methods that create and modify player objects"""

	################################
	###                          ###
	### DATABASE READING METHODS ###
	###                          ###
	################################

	@classmethod
	def teams_from_db(cls):
		'''grab and return all team data from the database, as a collection of teams'''
		#connect to our sqlite database
		year_team_player = sqlite3.connect("NBA_Database.db")
		#setup cursor
		c = year_team_player.cursor()
		#ignored startyear
		db_teams = c.execute('''SELECT teamID,
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
	                                field_goal_attempts_pct,
	                                defensive_rebonds,
	                                opponent_fg_pct,
	                                opponent_dor_pct,
	                                opponent_possession from team''')
		return (cls.extract_data(db_teams))


	@classmethod
	def extract_data(cls,db_teams):
		teams=[]
		#waiting on TeamFactory
		for (teamID, team_name_abbre,team_name, full_name, field_goal_attempts,turnovers, 
	         freethrow_attempts, offensive_rebonds, points_scored, points_allowed, game_possession, offensive_efficiency, defensive_efficiency,
	         treys_made, free_throws_made, field_goal_attempts_pct, defensive_rebonds, opponent_fg_pct, opponent_dor_pct, opponent_possession) in db_teams:

			a_team = Team.alt_init(team_name_abbre,team_name)
	            
			a_team.set_teamID(teamID)
			a_team.set_team_name_abbr(team_name_abbre)
			a_team.set_team_name(full_name)
			a_team.set_field_goal_attempts(field_goal_attempts)
			a_team.set_turnover(turnovers)
			a_team.set_free_throw_attempts(freethrow_attempts)
			a_team.set_offensive_rebounds(offensive_rebonds)
			a_team.set_points_scored(points_scored)
			a_team.set_possessions(game_possession)
			a_team.set_offensive_efficiency(offensive_efficiency)
			a_team.set_defensive_efficiency(defensive_efficiency)
			a_team.set_treys_made(treys_made)
			a_team.set_free_throw_made(free_throws_made)
			a_team.set_field_goal_attempts_pct(field_goal_attempts_pct)
			a_team.set_defensive_rebonds(defensive_rebonds)
			a_team.set_opponent_fg_pct(opponent_fg_pct)
			a_team.set_opponent_dor_pct(opponent_dor_pct)
			a_team.set_opponent_possession(opponent_possession)

			teams.append(a_team)
		return teams



    ###########################
    ###                     ###
    ### API READING METHODS ###
    ###                     ###
    ###########################

	@classmethod
	def team_basic_stats_filler(cls, NBA_teams, overall_team_standings):

	    for b in range(0, len(overall_team_standings["overallteamstandings"]["teamstandingsentry"])):
	        base_team = overall_team_standings['overallteamstandings']['teamstandingsentry'][b]['team']
	        base_stats = overall_team_standings['overallteamstandings']['teamstandingsentry'][b]['stats']
	        team_name_abbr = base_team['Abbreviation']

	        #reading in data from JSON
	        field_goal_attempts = float(base_stats['FgAttPerGame']['#text'])
	        turnovers = float(base_stats['TovPerGame']['#text'])
	        free_throw_attempts = float(base_stats['FtAttPerGame']['#text'])


	        #set field_goal_attempts,free_throw_attempts,turnover into team stats
	        NBA_teams[team_name_abbr].set_field_goal_attempts(field_goal_attempts)
	        NBA_teams[team_name_abbr].set_free_throw_attempts(free_throw_attempts)
	        NBA_teams[team_name_abbr].set_turnover(turnovers)

	@classmethod
	def winning_percentage(cls, NBA_teams, NBA_teams_checklist, overall_team_standings):
	#'''this function is to support the player usage function'''
    #assign each team with a winning percentage
	    for b in range(0, len(overall_team_standings["overallteamstandings"]["teamstandingsentry"])):
	        team_name_abbr = overall_team_standings['overallteamstandings']['teamstandingsentry'][b]['team']['Abbreviation']
	        true_winning_percentage = float(overall_team_standings['overallteamstandings']['teamstandingsentry'][b]['stats']['WinPct']['#text'])

	        NBA_teams[team_name_abbr].winning_percentage = true_winning_percentage
	        #print(team_name_abbr,true_winning_percentage)

	    #assign each team with a expected winning percentage against each team in the league
	    for a in NBA_teams_checklist:
	        team_a_winning_pc = NBA_teams[a].winning_percentage
	        for c in NBA_teams_checklist:
	            team_b_winning_pc = NBA_teams[c].winning_percentage
	            if a == 0 and b == 0:
	                print("No games yet")
	            else:
	                a_against_b = (team_a_winning_pc-team_a_winning_pc*team_b_winning_pc)/(team_a_winning_pc+team_b_winning_pc-2*team_a_winning_pc*team_b_winning_pc)
	                NBA_teams[a].expected_winning_percentage[c] = abs(a_against_b)

	@classmethod
	def four_factors(cls, NBA_teams, NBA_teams_checklist, overall_team_standings):
	    '''finds the factors that typically correspond to wins/losses in the NBA'''
	    effective_field_goal_percentage = {}
	    turnover_rate = {}
	    offensive_rebounding_percentage = {}
	    free_throw_rate = {}

	    for b in range(0, len(overall_team_standings["overallteamstandings"]["teamstandingsentry"])):
	        base_team = overall_team_standings['overallteamstandings']['teamstandingsentry'][b]['team']
	        base_stats = overall_team_standings['overallteamstandings']['teamstandingsentry'][b]['stats']
	        team_name_abbr = base_team['Abbreviation']

	        #reading in data from JSON
	        field_goal_attempts = float(base_stats['FgAttPerGame']['#text'])
	        field_goals_made = float(base_stats['FgMadePerGame']['#text'])
	        treys_made = float(base_stats['Fg3PtMadePerGame']['#text'])
	        turnovers = float(base_stats['TovPerGame']['#text'])
	        free_throw_attempts = float(base_stats['FtAttPerGame']['#text'])
	        free_throws_made = float(base_stats['FtMadePerGame']['#text'])
	        offensive_rebounds = float(base_stats['OffRebPerGame']['#text'])
	        turnover = float(base_stats['TovPerGame']['#text'])

	        #set field_goal_attempts,free_throw_attempts,turnover into team stats
	        NBA_teams[team_name_abbr].set_field_goal_attempts(field_goal_attempts)
	        NBA_teams[team_name_abbr].set_free_throw_attempts(free_throw_attempts)
	        NBA_teams[team_name_abbr].set_turnover(turnover)

	        #Calculating Effective Field Goal Percentage = (Field Goals Made) + 0.5*3P Field Goals Made))/(Field Goal Attempts)
	        effective_field_goal_percentage[team_name_abbr] = ((field_goals_made + (0.5 * treys_made)) / field_goal_attempts) * 100

	        #Calculating Turnover Rate = Turnovers/(Field Goal Attempts + 0.44*Free Throw Attempts + Turnovers)
	        turnover_rate[team_name_abbr] = turnovers / (field_goal_attempts + 0.44 * free_throw_attempts + turnovers)

	        #Calculating Offensive Rebounding Percentage = (Offensive Rebounds)/[(Offensive Rebounds)+(Opponent's Defensive Rebounds)]
	        #offensive_rebounding_percentage[team_name_abbr] = offensive_rebounds / (offensive_rebounds + )
	        
	        #Calculating Free Throw Rate=(Free Throws Made)/(Field Goals Attempted) or Free Throws Attempted/Field Goals Attempted
	        free_throw_rate[team_name_abbr] = free_throws_made / field_goal_attempts

	        print("Team: %s, Effective FG %%: %.2f, Turnover Rate: %.2f, Free Throw Rate: %.2f" % (team_name_abbr,
	                                                                                               effective_field_goal_percentage[team_name_abbr],
	                                                                                               turnover_rate[team_name_abbr],
	                                                                                               free_throw_rate[team_name_abbr]))
	    # end of for loop

	    #update NBA_teams objects with the calculated values
	    for key, value in NBA_teams_checklist.items():
	        NBA_teams[key].effective_field_goal_percentage = effective_field_goal_percentage[key]
	        NBA_teams[key].turnover_rate = turnover_rate[key]
	        NBA_teams[key].free_throw_rate = free_throw_rate[key]
	@classmethod
	def off_and_deff_efficiency_rating(cls, overall_team_standings, offensive_efficiency, defensive_efficiency, NBA_teams, NBA_teams_checklist):
	    '''offensive efficiency and defensive efficiency of each team'''
	    game_possession = {}
	    points_allowed = {}
	    for b in range(0,len(overall_team_standings["overallteamstandings"]["teamstandingsentry"])):
	        base = overall_team_standings['overallteamstandings']['teamstandingsentry'][b]
	        base_team = base['team']
	        base_stats = base['stats']

	        team_name_abbr = base_team['Abbreviation']

	        field_goal_attempts = float(base_stats['FgAttPerGame']['#text'])
	        turnovers = float(base_stats['TovPerGame']['#text'])
	        freethrow_attempts = float(base_stats['FtAttPerGame']['#text'])
	        offensive_rebounds = float(base_stats['OffRebPerGame']['#text'])
	        points_scored = float(base_stats['PtsPerGame']['#text'])
	        points_allowed[team_name_abbr] = float(base_stats['PtsAgainstPerGame']['#text'])
	        
	        game_possession[team_name_abbr] = 0.96 * (field_goal_attempts + turnovers + 0.44 * freethrow_attempts - offensive_rebounds)
	        offensive_efficiency[team_name_abbr]=100 * points_scored / game_possession[team_name_abbr]
	        defensive_efficiency[team_name_abbr]=100 * points_allowed[team_name_abbr] / game_possession[team_name_abbr]
	        print(team_name_abbr, offensive_efficiency[team_name_abbr], defensive_efficiency[team_name_abbr])


	    fig, ax = plt.subplots()
	    #create classes for each team
	    for key, value in NBA_teams_checklist.items():
	        NBA_teams[key].offensive_efficiency = offensive_efficiency[key]
	        NBA_teams[key].defensive_efficiency = defensive_efficiency[key]
	        NBA_teams[key].set_possessions(game_possession[key])
	        NBA_teams[key].set_points_allowed(points_allowed[key])

	        ax.scatter(NBA_teams[key].offensive_efficiency, NBA_teams[key].defensive_efficiency)

	    #invert the y-axis
	    #top right savage teams
	    #bottom left dumb fk teams
	    #need to work on the annotate function
	    plt.ylim(125, 110)
	    plt.xlabel("offensive efficiency")
	    plt.ylabel("defensive efficiency")
	    plt.title("efficiency plot")
	    plt.show()