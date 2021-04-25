from images.CrocodileAssets import CrocodileAssets
from constants.BackgroundConstants import BackgroundConstants
from constants.CrocodileConstants import CrocodileConstants
import random

class Crocodile:

    def __init__(self, axis_x):
        self.__index_height = 0
        self.__axis_x, self.__saved_axis_x = axis_x, axis_x
        self.__possible_height = [
            CrocodileConstants.CROCODILE_ONE,
            CrocodileConstants.CROCODILE_TWO,
            CrocodileConstants.CROCODILE_THREE
        ]
        self.__images = CrocodileAssets()
        self.__crocodile_options = [
            self.__images.crocodile_one,
            self.__images.crocodile_two,
            self.__images.crocodile_three
        ]


    def draw(self, window):
        self.__index_height %= CrocodileConstants.QUANTITY_OF_CROCODILE
        crocodile = self.__index_height
        window.blit(self.__crocodile_options[crocodile],
                    (self.__axis_x, self.__possible_height[crocodile], 70, 30))
        self.__index_height += CrocodileConstants.VELOCITY_TO_CHANGE_IMAGE

    def move(self):
        self.__axis_x -= BackgroundConstants.VELOCITY

        if  self.__axis_x < - CrocodileConstants.AXIS_X_TO_CHANGE_CROCODILE:
            self.__axis_x = self.__saved_axis_x + random.randint(623, 1926)

