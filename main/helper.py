from collections import OrderedDict
from pprint import pprint
import pandas as pandapandapanda
import matplotlib.pyplot as plt
from matplotlib import style
import math
import numpy as np
import copy
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

def ranking_win_share(NBA_teams, NBA_teams_checklist, Ranking_wins):
    for x in NBA_teams_checklist:
        Ranking_wins[NBA_teams[x].team_name] = NBA_teams[x].total_win_share
    #rank by value
    ranking_desc = OrderedDict(sorted(Ranking_wins.items(), key = lambda t: t[1], reverse= True))
    print('\n')
    for key, value in ranking_desc.items():
        print("%s total win share: %.2f" % (key, value))
    print('\n')

def get_each_team_schedule(NBA_teams, full_game_schedule):
    for b in range(0, len(full_game_schedule["fullgameschedule"]["gameentry"])):
        base = full_game_schedule["fullgameschedule"]["gameentry"][b]
        homeTeam = base['homeTeam']['Abbreviation']
        awayTeam = base['awayTeam']['Abbreviation']
        NBA_teams[homeTeam].game_schedule.append(awayTeam)
        NBA_teams[awayTeam].game_schedule.append(homeTeam)


def sim(NBA_teams, NBA_teams_checklist,Ranking,overall_team_standings):
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

def ranking_by_sim(Ranking):
    #rank by value
    ranking_descending=OrderedDict(sorted(Ranking.items(), key=lambda t: t[1],reverse=True))
    for key, value in ranking_descending.items():
        print (key, value, "-", round(82-value,1))

def trade_player(NBA_teams, NBA_teams_checklist,Ranking):
    pprint(NBA_teams_checklist)
    team1 = input("Which team? (enter abbre only) : ").upper()
    team_one = NBA_teams[team1]
    team_one.print_roster_and_points()
    team_one_players_to_trade = []
    roster_copy = []
    roster_copy.extend(team_one.roster)
    # print(len(team_one.roster))
    # print(*roster_copy, sep='\n')
    player1 = input("Which player? (enter Full name including upper case and space) : ")#will change later
    team_one_players_to_trade.append(player1)
    team_one_id = team_one.teamid
    roster_copy.remove(player1)
    # print("After one player was added:")
    # print(*roster_copy, sep='\n')
    # print("Original list:")
    # team_one.print_roster_and_points()
    keep_trading = True if input("Add another player to the trade? (type Y/N): ").upper() == "Y" else False

    while(keep_trading):
        print("Players remaining:")
        print(*roster_copy, sep='\n')
        another_player = input("Which player? (enter Full name including upper case and space) : ")#will change later
        team_one_players_to_trade.append(another_player)
        roster_copy.remove(another_player)
        keep_trading = True if input("Add another player from this team to the trade? (type Y/N): ").upper() == "Y" else False

    pprint(NBA_teams_checklist)

    team2 = input("Which team to trade with? (enter abbre only) : ").upper()
    team_two = NBA_teams[team2]
    team_two.print_roster_and_points()
    team_two_players_to_trade = []
    roster_copy = []
    roster_copy.extend(team_two.roster)

    player2=input("Which player? (enter Full name including upper case and space) : ")#will change later
    team_two_id = team_two.teamid
    team_two_players_to_trade.append(player2)
    roster_copy.remove(player2)

    keep_trading = True if input("Add another player to the trade? (type Y/N): ").upper() == "Y" else False

    while(keep_trading):
        print("Players remaining:")
        print(*roster_copy, sep='\n')
        another_player = input("Which player? (enter Full name including upper case and space) : ")#will change later
        team_two_players_to_trade.append(another_player)
        roster_copy.remove(another_player)
        keep_trading = True if input("Add another player from this team to the trade? (type Y/N): ").upper() == "Y" else False

    # new new trade stuff
    team_one_player_win_shares = 0
    team_two_player_win_shares = 0
    team_one_player_objects = {}
    team_two_player_objects = {}
    for a_player in team_one_players_to_trade:
        win_share = team_one.roster_class[a_player].get_win_share_normalized()
        team_one_player_win_shares += win_share
        #get all of the player objects from the teams to trade
        team_one_player_objects[a_player] = team_one.roster_class[a_player]
        team_one.roster_class.pop(a_player)
        #remove player names from the roster list
        team_one.roster.remove(a_player)
    team_one.roster.extend(team_two_players_to_trade)

    # do the same for the other team
    for a_player in team_two_players_to_trade:
        win_share = team_two.roster_class[a_player].get_win_share_normalized()
        team_two_player_win_shares += win_share
        team_two_player_objects[a_player] = team_two.roster_class[a_player]
        team_two.roster_class.pop(a_player)
        team_two.roster.remove(a_player)
    team_two.roster.extend(team_one_players_to_trade)

    # now, trade the player objects between roster classes
    team_two.roster_class.update(team_one_player_objects)
    team_one.roster_class.update(team_two_player_objects)
    

    #trade with win share
    temp_sim_win = team_one.get_sim_win()/100 - team_one.get_sim_win()/100 * team_one_player_win_shares + team_two.get_sim_win()/100 * team_two_player_win_shares
    print(temp_sim_win)
    team_one.set_sim_win(temp_sim_win*100)
    team_one.set_sim_FAT_L(82 - temp_sim_win/100)
    temp_sim_win = team_two.get_sim_win()/100 - team_two.get_sim_win()/100 * team_two_player_win_shares + team_one.get_sim_win()/100 * team_one_player_win_shares
    print(temp_sim_win)
   
    team_two.set_sim_win(temp_sim_win*100)
    team_two.set_sim_FAT_L(82 - temp_sim_win/100)

    Ranking[team_one.team_name] = team_one.get_sim_win()/100
    Ranking[team_two.team_name] = team_two.get_sim_win()/100


    print('after the trade:\n')
    print(team1 + '\n')
    team_one.print_roster_and_points()
    print('\n' + team2 + '\n')
    team_two.print_roster_and_points()
    print ('\n')
    #update the actual database

    trade_multi_players_db(team1, team2, team_one_id, team_two_id, team_one_player_objects, team_two_player_objects)
    #trade_player_db(player_one_object, player_two_object)

# def off_and_deff_efficiency_rating(overall_team_standings, offensive_efficiency, defensive_efficiency, NBA_teams, NBA_teams_checklist):
#     '''offensive efficiency and defensive efficiency of each team'''
#     game_possession = {}
#     points_allowed = {}
#     for b in range(0,len(overall_team_standings["overallteamstandings"]["teamstandingsentry"])):
#         base = overall_team_standings['overallteamstandings']['teamstandingsentry'][b]
#         base_team = base['team']
#         base_stats = base['stats']

#         team_name_abbr = base_team['Abbreviation']

#         field_goal_attempts = float(base_stats['FgAttPerGame']['#text'])
#         turnovers = float(base_stats['TovPerGame']['#text'])
#         freethrow_attempts = float(base_stats['FtAttPerGame']['#text'])
#         offensive_rebounds = float(base_stats['OffRebPerGame']['#text'])
#         points_scored = float(base_stats['PtsPerGame']['#text'])
#         points_allowed[team_name_abbr] = float(base_stats['PtsAgainstPerGame']['#text'])
        
#         game_possession[team_name_abbr] = 0.96 * (field_goal_attempts + turnovers + 0.44 * freethrow_attempts - offensive_rebounds)
#         offensive_efficiency[team_name_abbr]=100 * points_scored / game_possession[team_name_abbr]
#         defensive_efficiency[team_name_abbr]=100 * points_allowed[team_name_abbr] / game_possession[team_name_abbr]
#         print(team_name_abbr, offensive_efficiency[team_name_abbr], defensive_efficiency[team_name_abbr])


#     fig, ax = plt.subplots()
#     #create classes for each team
#     for key, value in NBA_teams_checklist.items():
#         NBA_teams[key].offensive_efficiency = offensive_efficiency[key]
#         NBA_teams[key].defensive_efficiency = defensive_efficiency[key]
#         NBA_teams[key].set_possessions(game_possession[key])
#         NBA_teams[key].set_points_allowed(points_allowed[key])

#         ax.scatter(NBA_teams[key].offensive_efficiency, NBA_teams[key].defensive_efficiency)

#     #invert the y-axis
#     #top right savage teams
#     #bottom left dumb fk teams
#     #need to work on the annotate function
#     plt.ylim(125, 110)
#     plt.xlabel("offensive efficiency")
#     plt.ylabel("defensive efficiency")
#     plt.title("efficiency plot")
#     plt.show()

# def four_factors(NBA_teams, NBA_teams_checklist, overall_team_standings):
#     '''finds the factors that typically correspond to wins/losses in the NBA'''
#     effective_field_goal_percentage = {}
#     turnover_rate = {}
#     offensive_rebounding_percentage = {}
#     free_throw_rate = {}

#     for b in range(0, len(overall_team_standings["overallteamstandings"]["teamstandingsentry"])):
#         base_team = overall_team_standings['overallteamstandings']['teamstandingsentry'][b]['team']
#         base_stats = overall_team_standings['overallteamstandings']['teamstandingsentry'][b]['stats']
#         team_name_abbr = base_team['Abbreviation']

#         #reading in data from JSON
#         field_goal_attempts = float(base_stats['FgAttPerGame']['#text'])
#         field_goals_made = float(base_stats['FgMadePerGame']['#text'])
#         treys_made = float(base_stats['Fg3PtMadePerGame']['#text'])
#         turnovers = float(base_stats['TovPerGame']['#text'])
#         free_throw_attempts = float(base_stats['FtAttPerGame']['#text'])
#         free_throws_made = float(base_stats['FtMadePerGame']['#text'])
#         offensive_rebounds = float(base_stats['OffRebPerGame']['#text'])
#         turnover = float(base_stats['TovPerGame']['#text'])

#         #set field_goal_attempts,free_throw_attempts,turnover into team stats
#         NBA_teams[team_name_abbr].set_field_goal_attempts(field_goal_attempts)
#         NBA_teams[team_name_abbr].set_free_throw_attempts(free_throw_attempts)
#         NBA_teams[team_name_abbr].set_turnover(turnover)

#         #Calculating Effective Field Goal Percentage = (Field Goals Made) + 0.5*3P Field Goals Made))/(Field Goal Attempts)
#         effective_field_goal_percentage[team_name_abbr] = ((field_goals_made + (0.5 * treys_made)) / field_goal_attempts) * 100

#         #Calculating Turnover Rate = Turnovers/(Field Goal Attempts + 0.44*Free Throw Attempts + Turnovers)
#         turnover_rate[team_name_abbr] = turnovers / (field_goal_attempts + 0.44 * free_throw_attempts + turnovers)

#         #Calculating Offensive Rebounding Percentage = (Offensive Rebounds)/[(Offensive Rebounds)+(Opponent's Defensive Rebounds)]
#         #offensive_rebounding_percentage[team_name_abbr] = offensive_rebounds / (offensive_rebounds + )
        
#         #Calculating Free Throw Rate=(Free Throws Made)/(Field Goals Attempted) or Free Throws Attempted/Field Goals Attempted
#         free_throw_rate[team_name_abbr] = free_throws_made / field_goal_attempts

#         print("Team: %s, Effective FG %%: %.2f, Turnover Rate: %.2f, Free Throw Rate: %.2f" % (team_name_abbr,
#                                                                                                effective_field_goal_percentage[team_name_abbr],
#                                                                                                turnover_rate[team_name_abbr],
#                                                                                                free_throw_rate[team_name_abbr]))
#     # end of for loop

#     #update NBA_teams objects with the calculated values
#     for key, value in NBA_teams_checklist.items():
#         NBA_teams[key].effective_field_goal_percentage = effective_field_goal_percentage[key]
#         NBA_teams[key].turnover_rate = turnover_rate[key]
#         NBA_teams[key].free_throw_rate = free_throw_rate[key]


# def winning_percentage(NBA_teams, NBA_teams_checklist, overall_team_standings):
#     '''this function is to support the player usage function'''
#     #assign each team with a winning percentage
#     for b in range(0, len(overall_team_standings["overallteamstandings"]["teamstandingsentry"])):
#         team_name_abbr = overall_team_standings['overallteamstandings']['teamstandingsentry'][b]['team']['Abbreviation']
#         true_winning_percentage = float(overall_team_standings['overallteamstandings']['teamstandingsentry'][b]['stats']['WinPct']['#text'])

#         NBA_teams[team_name_abbr].winning_percentage = true_winning_percentage
#         #print(team_name_abbr,true_winning_percentage)

#     #assign each team with a expected winning percentage against each team in the league
#     for a in NBA_teams_checklist:
#         team_a_winning_pc = NBA_teams[a].winning_percentage
#         for c in NBA_teams_checklist:
#             team_b_winning_pc = NBA_teams[c].winning_percentage
#             if a == 0 and b == 0:
#                 print("No games yet")
#             else:
#                 a_against_b = (team_a_winning_pc-team_a_winning_pc*team_b_winning_pc)/(team_a_winning_pc+team_b_winning_pc-2*team_a_winning_pc*team_b_winning_pc)
#                 NBA_teams[a].expected_winning_percentage[c] = abs(a_against_b)

# def team_basic_stats_filler(NBA_teams, overall_team_standings):

#     for b in range(0, len(overall_team_standings["overallteamstandings"]["teamstandingsentry"])):
#         base_team = overall_team_standings['overallteamstandings']['teamstandingsentry'][b]['team']
#         base_stats = overall_team_standings['overallteamstandings']['teamstandingsentry'][b]['stats']
#         team_name_abbr = base_team['Abbreviation']

#         #reading in data from JSON
#         field_goal_attempts = float(base_stats['FgAttPerGame']['#text'])
#         turnovers = float(base_stats['TovPerGame']['#text'])
#         free_throw_attempts = float(base_stats['FtAttPerGame']['#text'])


#         #set field_goal_attempts,free_throw_attempts,turnover into team stats
#         NBA_teams[team_name_abbr].set_field_goal_attempts(field_goal_attempts)
#         NBA_teams[team_name_abbr].set_free_throw_attempts(free_throw_attempts)
#         NBA_teams[team_name_abbr].set_turnover(turnovers)


