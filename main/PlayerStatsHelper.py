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
        return Player.alt_init(first_name, last_name, position)

    @classmethod
    def stats_filler(cls, raw_stats, player):
        """grab statistics and generate remaining ones for the given player"""
        points_per_game = float(raw_stats['PtsPerGame']['#text'])
        field_goal_attempts = float(raw_stats['FgAttPerGame']['#text'])
        field_goals_made = float(raw_stats['FgMadePerGame']['#text'])
        free_throw_attempts = float(raw_stats['FtAttPerGame']['#text'])
        treys_made = float(raw_stats['Fg3PtMadePerGame']['#text'])

        player.points_per_game = points_per_game

        #Calculating:
        # Effective Field Goal Percentage = (Field Goals Made) + 0.5*3P Field Goals Made))/(Field Goal Attempts)
        # True Shooting Percentage = (Player's Total Points)/[(2*(Player's Field Goal Attempts+ 0.44*Player's Free Throw Attempts)]
        if field_goal_attempts > 0:

            effective_field_goal_percentage = ((field_goals_made + (0.5 * treys_made)) / field_goal_attempts) * 100
            true_shooting_percentage = points_per_game / (2 * (field_goal_attempts + 0.44 * free_throw_attempts)) * 100
            player.set_effective_field_goal_percentage(effective_field_goal_percentage)
            player.set_true_shooting_percentage(true_shooting_percentage)

        else:
            #avoid division errors, simply set the values to 0
            player.set_effective_field_goal_percentage(0)
            player.set_true_shooting_percentage(0)
        