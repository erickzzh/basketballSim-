# Install the Python Requests library:
# `pip install requests`

import base64
import requests


def send_request():
    # Request

    try:
        response = requests.get(
            url={pull-url},
            params={
                "fordate": "20161121"
            },
            headers={
                "Authorization": "Basic " + base64.b64encode('{}:{}'.format({username},{password}).encode('utf-8')).decode('ascii')
            }
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')






hey():
	pass        
	json_data=open(roster_2016_2017_directory).read()
	data=json.loads(json_data)
	#pprint(data)
	pprint(data['rosterplayers']['playerentry





#DUBM
        for x in range(0,len(cumulative_player_stats['cumulativeplayerstats']['playerstatsentry'])):
    team_name_shortcut=str(cumulative_player_stats['cumulativeplayerstats']['playerstatsentry'][x]['team']['Abbreviation'])
    FirstName=str(cumulative_player_stats['cumulativeplayerstats']['playerstatsentry'][x]['player']['FirstName'] + " ")
    LastName=str(cumulative_player_stats['cumulativeplayerstats']['playerstatsentry'][x]['player']['LastName'])
    FullName=FirstName+LastName
    if team_name_shortcut=='OKL':
        OKL.add_players(FullName)
    elif team_name_shortcut=='BRO':
        BRO.add_players(FullName)
    elif team_name_shortcut=='SAC':
        SAC.add_players(FullName)
    elif team_name_shortcut=='NOP':
        NOP.add_players(FullName)
    elif team_name_shortcut=='MIN':
        MIN.add_players(FullName)
    elif team_name_shortcut=='SAS':
        SAS.add_players(FullName)
    elif team_name_shortcut=='ORL':
        ORL.add_players(FullName)
    elif team_name_shortcut=='IND':
        IND.add_players(FullName)
    elif team_name_shortcut=='MEM':
        MEM.add_players(FullName)
    elif team_name_shortcut=='POR':
        POR.add_players(FullName)
    elif team_name_shortcut=='CLE':
        CLE.add_players(FullName)
    elif team_name_shortcut=='LAC':
        LAC.add_players(FullName)
    elif team_name_shortcut=='PHI':
        PHI.add_players(FullName)
    elif team_name_shortcut=='HOU':
        HOU.add_players(FullName)
    elif team_name_shortcut=='MIL':
        MIL.add_players(FullName)
    elif team_name_shortcut=='NYK':
        NYK.add_players(FullName)
    elif team_name_shortcut=='DEN':
        DEN.add_players(FullName)
    elif team_name_shortcut=='MIA':
        MIA.add_players(FullName)
    elif team_name_shortcut=='PHX':
        PHX.add_players(FullName)
    elif team_name_shortcut=='DAL':
        DAL.add_players(FullName)
    elif team_name_shortcut=='GSW':
        GSW.add_players(FullName)
    elif team_name_shortcut=='CHA':
        CHA.add_players(FullName)
    elif team_name_shortcut=='DET':
        DET.add_players(FullName)
    elif team_name_shortcut=='ATL':
        ATL.add_players(FullName)
    elif team_name_shortcut=='WAS':
        WAS.add_players(FullName)
    elif team_name_shortcut=='LAL':
        LAL.add_players(FullName)
    elif team_name_shortcut=='UTA':
        UTA.add_players(FullName)
    elif team_name_shortcut=='BOS':
        BOS.add_players(FullName)
    elif team_name_shortcut=='CHI':
        CHI.add_players(FullName)
    elif team_name_shortcut=='TOR':
        TOR.add_players(FullName)





#SMART


for a in range(0,len(cumulative_player_stats['cumulativeplayerstats']['playerstatsentry'])):
    team_name_shortcut=str(cumulative_player_stats['cumulativeplayerstats']['playerstatsentry'][a]['team']['Abbreviation'])
    player_name=cumulative_player_stats['cumulativeplayerstats']['playerstatsentry'][a]['player']['FirstName'] + " " +cumulative_player_stats['cumulativeplayerstats']['playerstatsentry'][a]['player']['LastName']
    

    if team_name_shortcut not in NBA_teams_checklist:
        NBA_teams_checklist.insert(len(NBA_teams_checklist),team_name_shortcut)
    else:
        pass


for b in NBA_teams_checklist:
    NBA_teams[b]=Team(b)


NBA_teams['BOS'].add_players("sabi")
NBA_teams['CLE'].print_roster()

for x in range(0,len(cumulative_player_stats['cumulativeplayerstats']['playerstatsentry'])):
    team_name_shortcut=str(cumulative_player_stats['cumulativeplayerstats']['playerstatsentry'][x]['team']['Abbreviation'])
    FirstName=str(cumulative_player_stats['cumulativeplayerstats']['playerstatsentry'][x]['player']['FirstName'] + " ")
    LastName=str(cumulative_player_stats['cumulativeplayerstats']['playerstatsentry'][x]['player']['LastName'])
    FullName=FirstName+LastName
    #print(team_name_shortcut)
#    NBA_teams[team_name_shortcut].add_players(FullName)
#    NBA_teams['BOS'].print_roster()

#NBA_teams['BOS'].print_team_name()
#NBA_teams['BOS'].print_roster()        
#    else:
#        team_name_shortcut = Team(team_name_shortcut)
#        team_name_shortcut.add_players(player_name)

