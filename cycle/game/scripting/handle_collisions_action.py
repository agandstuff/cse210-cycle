import constants
import itertools
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the players collide or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the players collides with one of the others segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        players = cast.get_actors("players")
        player1 = players[0]
        head1 = player1.get_segments()[0]
        segments1 = player1.get_segments()[1:]

        player2 = players[1]
        head2 = player2.get_segments()[0]
        segments2 = player2.get_segments()[1:]

        for seg1,seg2 in itertools.zip_longest(segments1, segments2):
            print(f'h1x:{head1.get_position().get_x()},h1y:{head1.get_position().get_y()}')
            print(f'h2x:{head2.get_position().get_x()},h2y:{head2.get_position().get_y()}')
            print(f's1x:{seg1.get_position().get_x()},s1y:{seg1.get_position().get_y()}')
            print(f's2x:{seg2.get_position().get_x()},s2y:{seg2.get_position().get_y()}')
            
            a = 6
            
            head1Seg2X = (abs(head1.get_position().get_x() - seg2.get_position().get_x()) < a)
            head1Seg2Y = (abs(head1.get_position().get_y() - seg2.get_position().get_y()) < a)
            
            print(head1Seg2X,head1Seg2Y)

            head2Seg1X = (abs(head2.get_position().get_x() - seg1.get_position().get_x()) < a)
            head2Seg1Y = (abs(head2.get_position().get_y() - seg1.get_position().get_y()) < a)

            print(head2Seg1X,head2Seg1Y)
            
            if (head1Seg2X and head1Seg2Y
                    or head2Seg1X and head2Seg1Y):
                
                print('#####################GAME OVER##################')
                self._is_game_over = True

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and shows players moving across the board not colliding if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            players = cast.get_actors("players")
            player1 = players[0]
            segments1 = player1.get_segments()

            player2 = players[1]
            segments2 = player2.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments1:
                segment.set_color(constants.WHITE)

            for segment in segments2:
                segment.set_color(constants.WHITE)
