import constants
from game.scripting.action import Action


class MoveActorsAction(Action):
    """
    Action that updates and "moves" all the actors.

    The responsibility of the MoveActorsAction class is to move all actors currently in motion.
    """
    def execute(self, cast, script):
        actors = cast.get_all_actors()
        for actor in actors:
            actor.move_next()

        player1 = cast.get_first_actor("players")
        player2 = cast.get_actors("players")[1]

        if script.get_actions("update")[1]._is_game_over:
            player1.grow_tail(1, constants.WHITE)
            player2.grow_tail(1, constants.WHITE)
        else:
            player1.grow_tail(1, constants.BLUE)
            player2.grow_tail(1, constants.RED)
