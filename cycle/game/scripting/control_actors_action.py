import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the player.
    
    The responsibility of ControlActorsAction is to get the direction and move the player's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
        _direction1 (Point): An instance of point to control the direction.
        _direction2 (Point):An instance of point to control the direction.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction1 = Point(0, constants.CELL_SIZE)
        self._direction2 = Point(0, -1 * constants.CELL_SIZE)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        players = cast.get_actors("players")
        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction1 = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction1 = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('w'):
            self._direction1 = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('s'):
            self._direction1 = Point(0, constants.CELL_SIZE)
        
        player1 = cast.get_first_actor("players")
        player1.turn_head(self._direction1)

        if self._keyboard_service.is_key_down('j'):
            self._direction2 = Point(-constants.CELL_SIZE, 0)

        if self._keyboard_service.is_key_down('l'):
            self.direction2 = Point(constants.CELL_SIZE, 0)
        
        if self._keyboard_service.is_key_down('i'):
            self._direction2 = Point(0, -constants.CELL_SIZE)

        if self._keyboard_service.is_key_down('k'):
            self._direction2 = Point(0, constants.CELL_SIZE)

        player2 = players[1]
        player2.turn_head(self._direction2)