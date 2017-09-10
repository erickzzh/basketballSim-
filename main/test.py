for x in range(0,len(cumulative_player_stats['cumulativeplayerstats']['playerstatsentry'])):
    base = cumulative_player_stats['cumulativeplayerstats']['playerstatsentry'][x]
    raw_player = base['player']
    playerID = raw_player['ID']

    if playerID in active_players_list:
        raw_stats = base['stats']

        team_name_abbr = str(base['team']['Abbreviation'])
        team_id = base['team']['ID']
        #generate the player object and relevant stats
        player = PlayerFactory.make_player(raw_player)
        PlayerFactory.stats_filler(raw_stats, player)
        PlayerFactory.stat_calculator(player)
        TeamFactory.team_basic_stats_filler(NBA_teams, overall_team_standings)
        PlayerFactory.usage(player,raw_stats,NBA_teams,team_name_abbr)
        player.set_team_id(team_id)
        player.set_team_abbr(team_name_abbr)
        #populate the roster
        NBA_teams[team_name_abbr].add_players_roster(player.FullName)
        #populate the player class
        NBA_teams[team_name_abbr].add_player(player)
    else:
        pass