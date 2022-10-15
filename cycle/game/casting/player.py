import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Player(Actor):
    """
    A player controlled by a user.
    
    The responsibility of Player is to move and grow.

    Attributes:
        _cycle_color (arguement): A value passed into the instance of the object, with a color specified from our constants list.
        _segments (list): A list to hold the number of segments.
        _prepare_body() (function): A function that prepares the body.
    """
    def __init__(self, a, b, color):
        super().__init__()
        self._segments = []
        self._prepare_body(a, b, color)

    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments[0]

    def grow_tail(self, number_of_segments, color):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(color)
            self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self, a, b, color2):

        for i in range(constants.PLAYER_LENGTH):
            position = Point(a, b - i * constants.CELL_SIZE)
            velocity = Point(0, 1 * constants.CELL_SIZE)
            text = "@" if i == 0 else "#"
            color = constants.BLUE if i == 0 else color2

            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)