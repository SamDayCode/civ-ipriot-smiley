import time
from blinkable import Blinkable
from smiley import Smiley


class Angry(Smiley):
    """
    Angry is a subclass of Smiley and of Blinkable.

    Note that Blinkable is an interface (an abstract base
    class that only contains an abstract method). By subclassing
    Blinkable, this class promises to implement the abstract
    method.See {meth:blink} below.
    """
    def __init__(self):
        super().__init__(complexion=self.RED)

        self.draw_mouth()
        self.draw_eyes()
        self.draw_emote()

    def draw_mouth(self):
        """
        Method that draws the mouth on the standard faceless smiley.
        """
        mouth = [43, 44, 45, 53]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
        Method that draws the eyes (open or closed) on the standard smiley.
        :param wide_open: True if eyes opened, False otherwise
        """
        eyes = [25, 26, 29, 30]
        for pixel in eyes:
            self.pixels[pixel] = self.BLANK if wide_open else self.complexion()

    def draw_emote(self, on=True):
        """
        Method that draws the mouth on the standard faceless angry.
        """
        emote = [5, 12, 14, 21]
        for pixel in emote:
            self.pixels[pixel] = self.BLANK if on else self.complexion()

    def blink(self, delay=0.05):
        """
        Make the angry smiley emote once with a certain delay (in s).
        This is the implementation of the abstract method from the
        Blinkable abstract class.

        :param delay: Delay in seconds
        """
        self.counter1 = 4
        while self.counter1 > 0:
            self.draw_emote(on=False)
            self.show()
            time.sleep(delay)
            self.draw_emote(on=True)
            self.show()
            time.sleep(delay)
            self.counter1 = self.counter1 - 1


