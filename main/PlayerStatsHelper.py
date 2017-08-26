"""Player Manager module"""
from Player_class import Player

class PlayerManager:
    """Contains methods that create and modify player objects"""

    @classmethod
    def make_player(cls, raw_player):
        """create and return a new player from the given info"""
        first_name = raw_player['FirstName']
        last_name = raw_player['LastName']
        position = raw_player['Position']
        player_id = raw_player['ID']

        player = Player.alt_init(first_name, last_name, position)
        player.set_player_id(player_id)

        return player

    @classmethod
    def stats_filler(cls, raw_stats, player):
        """grab statistics from 2016-2017 season for the given player"""
        points_per_game = float(raw_stats['PtsPerGame']['#text'])
        field_goal_attempts = float(raw_stats['FgAttPerGame']['#text'])
        field_goals_made = float(raw_stats['FgMadePerGame']['#text'])
        free_throw_attempts = float(raw_stats['FtAttPerGame']['#text'])
        treys_made = float(raw_stats['Fg3PtMadePerGame']['#text'])

        player.set_points_per_game(points_per_game)
        player.set_field_goal_attempts(field_goal_attempts)
        player.set_field_goals_made(field_goals_made)
        player.set_free_throw_attempts(free_throw_attempts)
        player.set_treys_made(treys_made)

    @classmethod
    def stat_calculator(cls, player):
        """calculate any dependent statistics for the player"""

        # Effective Field Goal Percentage = (Field Goals Made) + 0.5*3P Field Goals Made))/(Field Goal Attempts)
        # True Shooting Percentage = (Player's Total Points)/[(2*(Player's Field Goal Attempts+ 0.44*Player's Free Throw Attempts)]
        if player.get_field_goal_attempts() > 0:
            #obtain all required totals from the player
            field_goal_attempts = player.get_field_goal_attempts()
            field_goals_made = player.get_field_goals_made()
            treys_made = player.get_treys_made()
            free_throw_attempts = player.get_free_throw_attempts()
            points_per_game = player.get_points()

            #calculate the necessary statistic and update the player accordingly
            effective_field_goal_percentage = ((field_goals_made + (0.5 * treys_made)) / field_goal_attempts) * 100.0
            true_shooting_percentage = points_per_game / (2.0 * (field_goal_attempts + 0.44 * free_throw_attempts)) * 100.0
            player.set_effective_field_goal_percentage(effective_field_goal_percentage)
            player.set_true_shooting_percentage(true_shooting_percentage)

        else:
            #avoid division errors, simply set the values to 0
            player.set_effective_field_goal_percentage(0)
            player.set_true_shooting_percentage(0)
