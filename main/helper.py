from collections import OrderedDict
from pprint import pprint
import pandas as pandapandapanda
import matplotlib.pyplot as plt
from matplotlib import style
import math
import numpy as np
from Database import *

def assign_teamid(NBA_teams, overall_team_standings):
    for b in range(0, len(overall_team_standings["overallteamstandings"]["teamstandingsentry"])):
        base_team = overall_team_standings['overallteamstandings']['teamstandingsentry'][b]['team']
        teamid = base_team['ID']
        team_name_abbr = base_team['Abbreviation']
        NBA_teams[team_name_abbr].teamid = teamid

def ranking_points_per_game(NBA_teams, NBA_teams_checklist, Ranking):
    for y in NBA_teams_checklist:
        Ranking[NBA_teams[y].team_name] = NBA_teams[y].get_team_theoretical_points()
    #rank by value
    ranking_descending = OrderedDict(sorted(Ranking.items(), key=lambda t: t[1], reverse=True))
    for key, value in ranking_descending.items():
        print (key, value)

def get_each_team_schedule(NBA_teams, full_game_schedule):
    for b in range(0, len(full_game_schedule["fullgameschedule"]["gameentry"])):
        base = full_game_schedule["fullgameschedule"]["gameentry"][b]
        homeTeam = base['homeTeam']['Abbreviation']
        awayTeam = base['awayTeam']['Abbreviation']
        NBA_teams[homeTeam].game_schedule.append(awayTeam)
        NBA_teams[awayTeam].game_schedule.append(homeTeam)


def ranking(NBA_teams, NBA_teams_checklist,Ranking):
    for b in range(0, len(overall_team_standings["overallteamstandings"]["teamstandingsentry"])):
        team_name_abbr = overall_team_standings['overallteamstandings']['teamstandingsentry'][b]['team']['Abbreviation']
        team = NBA_teams[team_name_abbr]
        for x in range(0,50):
            for a in range(0, len(team.game_schedule)):
                opponent = team.game_schedule[a]
                # #remove team from the opponent's game schedule
                # while team_name_abbr in NBA_teams[opponent].game_schedule: NBA_teams[opponent].game_schedule.remove(team_name_abbr)
                expected_winning_percentage = team.expected_winning_percentage[opponent]
                temp_array = [team_name_abbr, opponent]
                winning_team = np.random.choice(temp_array, 1, p=[expected_winning_percentage, 1-expected_winning_percentage])

                if winning_team[0] == team_name_abbr:
                    team.sim_win += 1
                    NBA_teams[opponent].sim_FAT_L += 1
                else:
                    NBA_teams[opponent].sim_win += 1
                    team.sim_FAT_L += 1

    for y in NBA_teams_checklist:
        Ranking[NBA_teams[y].team_name] = round(NBA_teams[y].get_sim_win()/100,1)

    #rank by value
    ranking_descending=OrderedDict(sorted(Ranking.items(), key=lambda t: t[1],reverse=True))
    for key, value in ranking_descending.items():
        print (key, value, "-", round(82-value,1))

def trade_player(NBA_teams, NBA_teams_checklist):
    pprint(NBA_teams_checklist)
    team1 = input("Which team? (enter abbre only) : ").upper()
    team_one = NBA_teams[team1]
    team_one.print_roster_and_points()

    player1 = input("Which player? (enter Full name including upper case and space) : ")#will change later
    pprint(NBA_teams_checklist)

    team2 = input("Which team? (enter abbre only) : ").upper()
    team_two = NBA_teams[team2]
    team_two.print_roster_and_points()

    player2=input("Which player? (enter Full name including upper case and space) : ")#will change later

    team_one.trade_players_roster(player1, player2)
    team_two.trade_players_roster(player2, player1)

    player_one_object = team_one.roster_class[player1]
    player_two_object = team_two.roster_class[player2]

    #new trade stuff
    team_one.roster_class[player1] = player_two_object
    team_one.roster_class[player2] = team_one.roster_class.pop(player1)
    team_two.roster_class[player2] = player_one_object
    team_two.roster_class[player1] = team_two.roster_class.pop(player2)

    print('after the trade:\n')
    print(team1 + '\n')
    team_one.print_roster_and_points()
    print('\n' + team2 + '\n')
    team_two.print_roster_and_points()
    print ('\n')
    #update the actual database
    trade_player_db(player_one_object, player_two_object)

def off_and_deff_efficiency_rating(overall_team_standings, offensive_efficiency, defensive_efficiency, NBA_teams, NBA_teams_checklist):
    '''offensive efficiency and defensive efficiency of each team'''
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
        points_allowed = float(base_stats['PtsAgainstPerGame']['#text'])

        game_possession = 0.96 * (field_goal_attempts + turnovers + 0.44 * freethrow_attempts - offensive_rebounds)
        offensive_efficiency[team_name_abbr]=100 * points_scored / game_possession
        defensive_efficiency[team_name_abbr]=100 * points_allowed / game_possession
        print(team_name_abbr, offensive_efficiency[team_name_abbr], defensive_efficiency[team_name_abbr])


    fig, ax = plt.subplots()
    #create classes for each team
    for key, value in NBA_teams_checklist.items():
        NBA_teams[key].offensive_efficiency = offensive_efficiency[key]
        NBA_teams[key].defensive_efficiency = defensive_efficiency[key]

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

def four_factors(NBA_teams, NBA_teams_checklist, overall_team_standings):
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

def winning_percentage(NBA_teams, NBA_teams_checklist, overall_team_standings):
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

