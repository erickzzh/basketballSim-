import base64
import requests
import urllib
import json
import username_password as authorize
from pprint import pprint
from ohmysportsfeedspy import MySportsFeeds


#global variables
file_format=None
league_name=None
season_name_type=None
season_name_begin=None
season_name_end=None
more_data=True
#request prototype 
# def request():
#     #cumulative player stats, full game schedule, player game logs, team game logs, active players, overall team standings, conference team standings, division team standings,playeroff team standings, player injuries, lastest updates
#     #inputs
#     file_format = "json"
#     league_name=input("League name: ")
#     season_name_begin=input("Enter the beginning of the season ")+"-"
#     season_name_end=input("Enter the end of the season ")+"-"
#     data_category="player_gamelogs" #temp need to dynamically change the data type
#     ####data_category=input("Enter the data type that you want ")###
#     season_name_type=input("Enter either 'regular' or 'playoff '")
#     #optional_parameter=input("Enter optional parameters ")
    
#     #differentiate the two type of games 
#     if season_name_type=="playoff":
#         global Output
#         Data_query = MySportsFeeds('1.0',verbose=True)
#         Data_query.authenticate(authorize.username, authorize.password)
#         Output = Data_query.msf_get_data(league=league_name,season=season_name_begin+season_name_type,feed=data_category,format=file_format)#can add more optional params manually 
#     else:
#         Data_query = MySportsFeeds('1.0',verbose=True)
#         Data_query.authenticate(authorize.username, authorize.password)
#         Output = Data_query.msf_get_data(league=league_name,season=season_name_begin+season_name_end+season_name_type,feed=data_category,format=file_format,)#can add more optional params manually 
#     clear_input()


def clear_input():
    season_name_type=None
    season_name_begin=None
    season_name_end=None
    optional_parameter=None
    URL=None

def initial_inputs():
    global file_format
    global league_name
    global season_name_begin
    global season_name_end
    global season_name_type
    file_format = "json"
    league_name=input("League name: ")
    season_name_begin=input("Enter the beginning of the season ")+"-"
    season_name_end=input("Enter the end of the season ")+"-"
    season_name_type=input("Enter either 'regular' or 'playoff '")
    #optional_parameter=input("Enter optional parameters ")
    
    #differentiate the two type of games 

def request_general():
    file_format = "json"
    league_name=input("League name: ")
    season_name_begin=input("Enter the beginning of the season ")+"-"
    season_name_end=input("Enter the end of the season ")+"-"
    season_name_type=input("Enter either 'regular' or 'playoff '")
    data_type=["cumulative_player_stats","full_game_schedule","active_players","overall_team_standings","conference_team_standings","division_team_standings","playoff_team_standings","player_injuries","latest_updates"]
    #for loop to download all the data at a given season
    for x in range(0,9):
        if season_name_type=="playoff":
            
            Data_query = MySportsFeeds('1.0',verbose=True)
            Data_query.authenticate(authorize.username, authorize.password)
            Output = Data_query.msf_get_data(league=league_name,season=season_name_begin+season_name_type,feed=data_type[x],format=file_format)#can add more optional params manually 
        elif data_type[x]== "playoff_team_standings":

            Data_query = MySportsFeeds('1.0',verbose=True)
            Data_query.authenticate(authorize.username, authorize.password)
            Output = Data_query.msf_get_data(league=league_name,season=season_name_begin+"playoff",feed=data_type[x],format=file_format)#can add more optional params manually 
        else:
            Data_query = MySportsFeeds('1.0',verbose=True)
            Data_query.authenticate(authorize.username, authorize.password)
            Output = Data_query.msf_get_data(league=league_name,season=season_name_begin+season_name_end+season_name_type,feed=data_type[x],format=file_format)#can add more optional params manually 
def request_daily():
    initial_inputs()
    data_type=["daily_game_schedule","daily_player_stats","scoreboard"]
    data_category=input("Enter 'all' for daily_game_schedule, daily_player_stats three, and scoreboard or any given data ")
    date= input("Enter the date of the data that you want in the format of YYYYMMDD")
    if data_category=="all":
        for x in range(0,3):
            if season_name_type=="playoff":
                global Output
                Data_query = MySportsFeeds('1.0',verbose=True)
                Data_query.authenticate(authorize.username, authorize.password)
                Output = Data_query.msf_get_data(league=league_name,season=season_name_begin+season_name_type,feed=data_type[x],format=file_format,fordate=date)#can add more optional params manually 
            else: 
                Data_query = MySportsFeeds('1.0',verbose=True)
                Data_query.authenticate(authorize.username, authorize.password)
                Output = Data_query.msf_get_data(league=league_name,season=season_name_begin+season_name_end+season_name_type,feed=data_type[x],format=file_format,fordate=date)#can add more optional params manually 
    else:
        if season_name_type=="playoff":
            global Output
            Data_query = MySportsFeeds('1.0',verbose=True)
            Data_query.authenticate(authorize.username, authorize.password)
            Output = Data_query.msf_get_data(league=league_name,season=season_name_begin+season_name_type,feed=data_category,format=file_format,fordate=date)#can add more optional params manually 
        else: 
            Data_query = MySportsFeeds('1.0',verbose=True)
            Data_query.authenticate(authorize.username, authorize.password)
            Output = Data_query.msf_get_data(league=league_name,season=season_name_begin+season_name_end+season_name_type,feed=data_category,format=file_format,fordate=date)#can add more optional params manually 
def request_gamelogs():
    initial_inputs()
    data_category=input("enter either 'player' or 'team' to request for data ")

    if data_category=="player":
        player=input("Enter the player's name in the form of: last name, first-last,first-last-playerID")
        if season_name_type=="playoff":
            global Output
            Data_query = MySportsFeeds('1.0',verbose=True)
            Data_query.authenticate(authorize.username, authorize.password)
            Output = Data_query.msf_get_data(league=league_name,season=season_name_begin+season_name_type,feed="player_gamelogs",format=file_format,player=plyaer)#can add more optional params manually 
        else: 
            Data_query = MySportsFeeds('1.0',verbose=True)
            Data_query.authenticate(authorize.username, authorize.password)
            Output = Data_query.msf_get_data(league=league_name,season=season_name_begin+season_name_end+season_name_type,feed="player_gamelogs",format=file_format,player=plyaer)#can add more optional params manually 
    else:
        team=input("Enter the team's abbr in the form of: abbreviation or city-teamname")
        if season_name_type=="playoff":
            global Output
            Data_query = MySportsFeeds('1.0',verbose=True)
            Data_query.authenticate(authorize.username, authorize.password)
            Output = Data_query.msf_get_data(league=league_name,season=season_name_begin+season_name_type,feed="team_gamelogs",format=file_format,team=team)#can add more optional params manually 
        else: 
            Data_query = MySportsFeeds('1.0',verbose=True)
            Data_query.authenticate(authorize.username, authorize.password)
            Output = Data_query.msf_get_data(league=league_name,season=season_name_begin+season_name_end+season_name_type,feed="team_gamelogs",format=file_format,team=team)#can add more optional params manually 
def request_game():
    initial_inputs()
    data_type=["game_playbyplay","game_boxscore","game_startinglineup"]
    data_category=input("Enter 'all' for game_playbyplay,game_boxscore,and game_startinglineup or any given data ")
    gameid=input("Enter game id in the form of:game date YYYYMMDD + '-'+ away team abbr +'-'+ home team abbr. Example 20161212-BOS-CLE")
    if data_category=="all":
        for x in range(0,3):
            if season_name_type=="playoff":
                global Output
                Data_query = MySportsFeeds('1.0',verbose=True)
                Data_query.authenticate(authorize.username, authorize.password)
                Output = Data_query.msf_get_data(league=league_name,season=season_name_begin+season_name_type,feed=data_type[x],format=file_format,gameid=gameid)#can add more optional params manually 
            else: 
                Data_query = MySportsFeeds('1.0',verbose=True)
                Data_query.authenticate(authorize.username, authorize.password)
                Output = Data_query.msf_get_data(league=league_name,season=season_name_begin+season_name_end+season_name_type,feed=data_type[x],format=file_format,gameid=gameid)#can add more optional params manually 
    else:
        if season_name_type=="playoff":
            Data_query = MySportsFeeds('1.0',verbose=True)
            Data_query.authenticate(authorize.username, authorize.password)
            Output = Data_query.msf_get_data(league=league_name,season=season_name_begin+season_name_type,feed=data_category,format=file_format,gameid=gameid)#can add more optional params manually 
        else: 
            Data_query = MySportsFeeds('1.0',verbose=True)
            Data_query.authenticate(authorize.username, authorize.password)
            Output = Data_query.msf_get_data(league=league_name,season=season_name_begin+season_name_end+season_name_type,feed=data_category,format=file_format,gameid=gameid)#can add more optional params manually 

#if delete every 5 mins redownload 
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





























