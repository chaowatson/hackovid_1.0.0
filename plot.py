# Project name: Hackovid
# Course: Python game programming
# Group: 3-1
# Game type: role-playing game
# Engineer: Watson Chao
# Institute: department of Engineering Science - NCKU
# File: plot.py

import pygame
from config import *
from sprites import *
from font import *


class Plot:
    def __init__(self, game):
        self.game = game

        self.plot_1_played = False
        self.plot_2_played = False
        self.plot_3_played = False
        self.plot_4_played = False
        self.plot_5_played = False
        self.plot_6_played = False
        self.plot_7_played = False
        self.plot_8_1_played = False
        self.plot_8_2_played = False
        self.plot_9_played = False
        self.plot_10_played = False
        self.to_play_not_get_money = False
        self.plot_11_played = False
        self.plot_12_played = False
        self.plot_13_played = False
        self.plot_14_played = False
        self.plot_15_played = False
        self.plot_16_played = False
        self.plot_confirmed_case_played = False
        self.plot_get_shot_played = False
        self.confirmed_case = False
        self.get_shot = False

        self.playing_plot = False
        self.plot_counter = 0


        self.scene_2_2_gameover = False

    def play_confirmed_case(self):
        self.playing_plot = True
        self.game.plotBoxes.generate_plots(PLOT_CONFIRMED_CASE_1)
        if self.plot_counter == 1:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_CONFIRMED_CASE_2)
        if self.plot_counter == 2:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_CONFIRMED_CASE_3)
        if self.plot_counter == 3:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_CONFIRMED_CASE_4)
        if self.plot_counter == 4:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_CONFIRMED_CASE_5)
        if self.plot_counter == 5:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_CONFIRMED_CASE_6)
        if self.plot_counter == 6:
            self.plot_counter = 0
            self.game.plotBoxes.plotBoxes_list.clear()
            self.plot_confirmed_case_played = True
            self.playing_plot = False
            pygame.mixer.music.fadeout(750)
            self.game.game_over_by_confirmed_case = True
            self.game.game_over = True

    def play_plot_1(self):
        self.playing_plot = True
        self.game.plotBoxes.generate_plots(PLOT_ONE_1)
        if self.plot_counter == 1:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_ONE_2)
        if self.plot_counter == 2:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_ONE_3)
        if self.plot_counter == 3:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_ONE_4)
        if self.plot_counter == 4:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_ONE_5)
        if self.plot_counter == 5:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_ONE_6)
        if self.plot_counter == 6:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_ONE_7)
        if self.plot_counter == 7:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_ONE_8)
        if self.plot_counter == 8:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_ONE_9)
        if self.plot_counter == 9:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_ONE_10)
        if self.plot_counter == 10:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_ONE_11)
        if self.plot_counter == 11:
            self.plot_counter = 0
            self.game.plotBoxes.plotBoxes_list.clear()
            self.plot_1_played = True
            self.playing_plot = False

    def play_plot_2(self):
        self.playing_plot = True
        self.game.plotBoxes.generate_plots(PLOT_TWO_1)
        if self.plot_counter == 1:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_TWO_2)
        if self.plot_counter == 2:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_TWO_3)
        if self.plot_counter == 3:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_TWO_4)
        if self.plot_counter == 4:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_TWO_5)
        if self.plot_counter == 5:
            self.plot_counter = 0
            self.game.plotBoxes.plotBoxes_list.clear()
            self.plot_2_played = True
            self.playing_plot = False

    def play_plot_3(self):
        self.playing_plot = True
        self.game.plotBoxes.generate_plots(PLOT_THREE_1)
        if self.plot_counter == 1:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_THREE_2)
        if self.plot_counter == 2:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_THREE_3)
        if self.plot_counter == 3:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_THREE_4)
        if self.plot_counter == 4:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_THREE_5)
        if self.plot_counter == 5:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_THREE_6)
        if self.plot_counter == 6:
            self.plot_counter = 0
            self.game.plotBoxes.plotBoxes_list.clear()
            self.plot_3_played = True
            self.playing_plot = False

    def play_plot_4(self):
        self.playing_plot = True
        self.game.plotBoxes.generate_plots(PLOT_FOUR_1)
        if self.plot_counter == 1:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_FOUR_2)
        if self.plot_counter == 2:
            self.plot_counter = 0
            self.game.plotBoxes.plotBoxes_list.clear()
            self.plot_4_played = True
            self.playing_plot = False

    def play_plot_5(self):
        self.playing_plot = True
        self.game.plotBoxes.generate_plots(PLOT_FIVE_1)
        if self.plot_counter == 1:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_FIVE_2)
        if self.plot_counter == 2:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_FIVE_3)
        if self.plot_counter == 3:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_FIVE_4)
        if self.plot_counter == 4:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_FIVE_5)
        if self.plot_counter == 5:
            self.plot_counter = 0
            self.game.plotBoxes.plotBoxes_list.clear()
            self.plot_5_played = True
            self.playing_plot = False

    def play_plot_6(self):
        self.playing_plot = True
        self.game.plotBoxes.generate_plots(PLOT_SIX_1)
        if self.plot_counter == 1:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_SIX_2)
        if self.plot_counter == 2:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_SIX_3)
        if self.plot_counter == 3:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_SIX_4)
        if self.plot_counter == 4:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_SIX_5)
        if self.plot_counter == 5:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_SIX_6)
        if self.plot_counter == 6:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_SIX_7)
        if self.plot_counter == 7:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_SIX_8)
        if self.plot_counter == 8:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_SIX_9)
        if self.plot_counter == 9:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_SIX_10)
        if self.plot_counter == 10:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_SIX_11)
        if self.plot_counter == 11:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_SIX_12)
        if self.plot_counter == 12:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_SIX_13)
        if self.plot_counter == 13:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_SIX_14)
        if self.plot_counter == 14:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_SIX_15)
        if self.plot_counter == 15:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_SIX_16)
        if self.plot_counter == 16:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_SIX_17)
        if self.plot_counter == 17:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_SIX_18)
        if self.plot_counter == 18:
            self.plot_counter = 0
            self.game.plotBoxes.plotBoxes_list.clear()
            self.plot_6_played = True
            self.playing_plot = False

    def play_plot_7(self):
        self.playing_plot = True
        self.game.plotBoxes.generate_plots(PLOT_SEVEN_1)
        if self.plot_counter == 1:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_SEVEN_2)
        if self.plot_counter == 2:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_SEVEN_3)
        if self.plot_counter == 3:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_SEVEN_4)
        if self.plot_counter == 4:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_SEVEN_5)
        if self.plot_counter == 5:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_SEVEN_6)
        if self.plot_counter == 6:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_SEVEN_7)
        if self.plot_counter == 7:
            self.plot_counter = 0
            self.game.plotBoxes.plotBoxes_list.clear()
            self.plot_7_played = True
            self.game.NPCs.move_detection()
            self.playing_plot = False

    def play_plot_8_1(self):
        self.playing_plot = True
        self.game.plotBoxes.generate_plots(PLOT_EIGHT_GAMEOVER_1)
        if self.plot_counter == 1:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_EIGHT_GAMEOVER_2)
        if self.plot_counter == 2:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_EIGHT_GAMEOVER_3)
        if self.plot_counter == 3:
            self.plot_counter = 0
            self.game.plotBoxes.plotBoxes_list.clear()
            self.plot_8_1_played = True
            self.playing_plot = False
            pygame.mixer.music.fadeout(750)
            self.game.game_over_by_get_caught = True
            self.game.game_over = True

    def play_plot_8_2(self):
        self.playing_plot = True
        self.game.plotBoxes.generate_plots(PLOT_EIGHT_1)
        if self.plot_counter == 1:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_EIGHT_2)
        if self.plot_counter == 2:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_EIGHT_3)
        if self.plot_counter == 3:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_EIGHT_4)
        if self.plot_counter == 4:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_EIGHT_5)
        if self.plot_counter == 5:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_EIGHT_6)
        if self.plot_counter == 6:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_EIGHT_7)
        if self.plot_counter == 7:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_EIGHT_8)
        if self.plot_counter == 8:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_EIGHT_9)
        if self.plot_counter == 9:
            self.plot_counter = 0
            self.game.plotBoxes.plotBoxes_list.clear()
            self.plot_8_2_played = True
            self.playing_plot = False

    def play_plot_9(self):
        self.playing_plot = True
        self.game.plotBoxes.generate_plots(PLOT_NINE_1)
        if self.plot_counter == 1:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_NINE_2)
        if self.plot_counter == 2:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_NINE_3)
        if self.plot_counter == 3:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_NINE_4)
        if self.plot_counter == 4:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_NINE_5)
        if self.plot_counter == 5:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_NINE_6)
        if self.plot_counter == 6:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_NINE_7)
        if self.plot_counter == 7:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_NINE_8)
        if self.plot_counter == 8:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_NINE_9)
        if self.plot_counter == 9:
            self.plot_counter = 0
            self.game.plotBoxes.plotBoxes_list.clear()
            self.plot_9_played = True
            self.playing_plot = False

    def play_plot_10(self):
        self.playing_plot = True
        self.game.plotBoxes.generate_plots(PLOT_TEN_1)
        if self.plot_counter == 1:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_TEN_2)
        if self.plot_counter == 2:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_TEN_3)
        if self.plot_counter == 3:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_TEN_4)
        if self.plot_counter == 4:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_TEN_5)
        if self.plot_counter == 5:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_TEN_6)
        if self.plot_counter == 6:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_TEN_7)
        if self.plot_counter == 7:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_TEN_8)
        if self.plot_counter == 8:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_TEN_9)
        if self.plot_counter == 9:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_TEN_10)
        if self.plot_counter == 10:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_TEN_11)
        if self.plot_counter == 11:
            self.plot_counter = 0
            self.game.plotBoxes.plotBoxes_list.clear()
            self.plot_10_played = True
            self.playing_plot = False

    def play_plot_11(self):
        self.playing_plot = True
        self.game.plotBoxes.generate_plots(PLOT_ELEVEN_1)
        if self.plot_counter == 1:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_ELEVEN_2)
        if self.plot_counter == 2:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_ELEVEN_3)
        if self.plot_counter == 3:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_ELEVEN_4)
        if self.plot_counter == 4:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_ELEVEN_5)
        if self.plot_counter == 5:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_ELEVEN_6)
        if self.plot_counter == 6:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_ELEVEN_7)
        if self.plot_counter == 7:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_ELEVEN_8)
        if self.plot_counter == 8:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_ELEVEN_9)
        if self.plot_counter == 9:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_ELEVEN_10)
        if self.plot_counter == 10:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_ELEVEN_11)
        if self.plot_counter == 11:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_ELEVEN_12)
        if self.plot_counter == 12:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_ELEVEN_13)
        if self.plot_counter == 13:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_ELEVEN_14)
        if self.plot_counter == 14:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_ELEVEN_15)
        if self.plot_counter == 15:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_ELEVEN_16)
        if self.plot_counter == 16:
            self.plot_counter = 0
            self.game.plotBoxes.plotBoxes_list.clear()
            self.plot_11_played = True
            self.playing_plot = False

    def play_plot_12(self):
        self.playing_plot = True
        self.game.plotBoxes.generate_plots(PLOT_TWELVE_1)
        if self.plot_counter == 1:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_TWELVE_2)
        if self.plot_counter == 2:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_TWELVE_3)
        if self.plot_counter == 3:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_TWELVE_4)
        if self.plot_counter == 4:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_TWELVE_5)
        if self.plot_counter == 5:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_TWELVE_6)
        if self.plot_counter == 6:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_TWELVE_7)
        if self.plot_counter == 7:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_TWELVE_8)
        if self.plot_counter == 8:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_TWELVE_9)
        if self.plot_counter == 9:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_TWELVE_10)
        if self.plot_counter == 10:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_TWELVE_11)
        if self.plot_counter == 11:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_TWELVE_12)
        if self.plot_counter == 12:
            self.plot_counter = 0
            self.game.plotBoxes.plotBoxes_list.clear()
            self.plot_12_played = True
            self.playing_plot = False

    def play_plot_13(self):
        self.playing_plot = True
        self.game.plotBoxes.generate_plots(PLOT_THIRTEEN_1)
        if self.plot_counter == 1:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_THIRTEEN_2)
        if self.plot_counter == 2:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_THIRTEEN_3)
        if self.plot_counter == 3:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_THIRTEEN_4)
        if self.plot_counter == 4:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_THIRTEEN_5)
        if self.plot_counter == 5:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_THIRTEEN_6)
        if self.plot_counter == 6:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_THIRTEEN_7)
        if self.plot_counter == 7:
            self.plot_counter = 0
            self.game.plotBoxes.plotBoxes_list.clear()
            self.plot_13_played = True
            self.playing_plot = False

    def play_plot_14(self):
        self.playing_plot = True
        self.game.plotBoxes.generate_plots(PLOT_FOURTEEN_1)
        if self.plot_counter == 1:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_FOURTEEN_2)
        if self.plot_counter == 2:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_FOURTEEN_3)
        if self.plot_counter == 3:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_FOURTEEN_4)
        if self.plot_counter == 4:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_FOURTEEN_5)
        if self.plot_counter == 5:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_FOURTEEN_6)
        if self.plot_counter == 6:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_FOURTEEN_7)
        if self.plot_counter == 7:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_FOURTEEN_8)
        if self.plot_counter == 8:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_FOURTEEN_9)
        if self.plot_counter == 9:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_FOURTEEN_10)
        if self.plot_counter == 10:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_FOURTEEN_11)
        if self.plot_counter == 11:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_FOURTEEN_12)
        if self.plot_counter == 12:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_FOURTEEN_13)
        if self.plot_counter == 13:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_FOURTEEN_14)
        if self.plot_counter == 14:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_FOURTEEN_15)
        if self.plot_counter == 15:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_FOURTEEN_16)
        if self.plot_counter == 16:
            mail_rect = self.game.bag.bag_item_list[0]
            mail_rect_x = mail_rect[0]
            mail_rect_y = mail_rect[1]
            self.game.players.items_list.append(Item.Mail(self.game, mail_rect_x/TILE_SIZE, mail_rect_y/TILE_SIZE))
            self.game.get_sound.play()
            self.game.bag.bag_item_list.pop(0)
            self.game.scene_5_3_complete = True
            self.plot_counter = 0
            self.game.plotBoxes.plotBoxes_list.clear()
            self.plot_14_played = True
            self.playing_plot = False

    def play_plot_15(self):
        self.playing_plot = True
        self.game.plotBoxes.generate_plots(PLOT_FIFTEEN_1)
        if self.plot_counter == 1:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_FIFTEEN_2)
        if self.plot_counter == 2:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_FIFTEEN_3)
        if self.plot_counter == 3:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_FIFTEEN_4)
        if self.plot_counter == 4:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_FIFTEEN_5)
        if self.plot_counter == 5:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_FIFTEEN_6)
        if self.plot_counter == 6:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_FIFTEEN_7)
        if self.plot_counter == 7:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_FIFTEEN_8)
        if self.plot_counter == 8:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_FIFTEEN_9)
        if self.plot_counter == 9:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_FIFTEEN_10)
        if self.plot_counter == 10:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_FIFTEEN_11)
        if self.plot_counter == 11:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_FIFTEEN_12)
        if self.plot_counter == 12:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_FIFTEEN_13)
        if self.plot_counter == 13:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_FIFTEEN_14)
        if self.plot_counter == 14:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_FIFTEEN_15)
        if self.plot_counter == 15:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_FIFTEEN_16)
        if self.plot_counter == 16:
            self.plot_counter = 0
            self.game.plotBoxes.plotBoxes_list.clear()
            self.plot_15_played = True
            self.playing_plot = False

    def play_plot_16(self):
        self.playing_plot = True
        self.game.plotBoxes.generate_plots(PLOT_SIXTEEN_1)
        if self.plot_counter == 1:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_SIXTEEN_2)
        if self.plot_counter == 2:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_SIXTEEN_3)
        if self.plot_counter == 3:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_SIXTEEN_4)
        if self.plot_counter == 4:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_SIXTEEN_5)
        if self.plot_counter == 5:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_SIXTEEN_6)
        if self.plot_counter == 6:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_SIXTEEN_7)
        if self.plot_counter == 7:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_SIXTEEN_8)
        if self.plot_counter == 8:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_SIXTEEN_9)
        if self.plot_counter == 9:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_SIXTEEN_10)
        if self.plot_counter == 10:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_SIXTEEN_11)
        if self.plot_counter == 11:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_SIXTEEN_12)
        if self.plot_counter == 12:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_SIXTEEN_13)
        if self.plot_counter == 13:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_SIXTEEN_14)
        if self.plot_counter == 14:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_SIXTEEN_15)
        if self.plot_counter == 15:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_SIXTEEN_16)
        if self.plot_counter == 16:
            self.plot_counter = 0
            self.game.plotBoxes.plotBoxes_list.clear()
            self.plot_16_played = True
            self.playing_plot = False
            pygame.mixer.music.fadeout(750)
            self.game.good_end = True
            self.game.game_over = True

    def play_get_shot(self):
        self.playing_plot = True
        self.game.plotBoxes.generate_plots(PLOT_GET_SHOT_1)
        if self.plot_counter == 1:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_GET_SHOT_2)
        if self.plot_counter == 2:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_GET_SHOT_3)
        if self.plot_counter == 3:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_GET_SHOT_4)
        if self.plot_counter == 4:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_GET_SHOT_5)
        if self.plot_counter == 5:
            self.game.plotBoxes.plotBoxes_list.clear()
            self.game.plotBoxes.generate_plots(PLOT_GET_SHOT_6)
        if self.plot_counter == 6:
            self.plot_counter = 0
            self.game.plotBoxes.plotBoxes_list.clear()
            self.plot_get_shot_played = True
            self.playing_plot = False
            pygame.mixer.music.fadeout(750)
            self.game.game_over_by_get_shot = True
            self.game.game_over = True

    def play_not_get_money(self):
        self.playing_plot = True
        self.game.plotBoxes.generate_plots(PLOT_NOT_GET_MONEY)
        if self.plot_counter == 1:
            self.plot_counter = 0
            self.game.plotBoxes.plotBoxes_list.clear()
            self.to_play_not_get_money = False
            self.playing_plot = False

    def update(self):
        if self.confirmed_case:
            self.play_confirmed_case()
        elif not self.plot_1_played:
            self.play_plot_1()
        elif not self.plot_2_played:
            self.play_plot_2()
        elif not self.plot_3_played and self.game.dialogueSpots.player_at_dialogueSpot:
            self.play_plot_3()
        elif not self.plot_4_played and self.game.dialogueSpots.player_at_dialogueSpot:
            self.play_plot_4()
            self.game.scene_1_1_complete = True
        elif not self.plot_5_played and self.game.scene_1_2_complete:
            self.play_plot_5()
        elif not self.plot_6_played and self.game.scene_1_complete:
            self.play_plot_6()
        elif not self.plot_7_played and self.game.scene_2_1_complete:
            self.play_plot_7()
        elif not self.plot_8_1_played and self.scene_2_2_gameover:
            self.play_plot_8_1()
        elif not self.plot_8_2_played and self.game.scene_2_2_complete:
            self.play_plot_8_2()
        elif not self.plot_9_played and self.game.scene_2_complete:
            self.play_plot_9()
        elif not self.plot_10_played and self.game.scene_3_1_complete:
            self.play_plot_10()
        elif self.to_play_not_get_money:
            self.play_not_get_money()
        elif not self.plot_11_played and self.game.scene_3_complete:
            self.play_plot_11()
        elif not self.plot_12_played and self.game.scene_4_1_complete:
            self.play_plot_12()
        elif not self.plot_13_played and self.game.scene_4_complete:
            self.play_plot_13()
        elif not self.plot_14_played and self.game.scene_5_2_complete:
            self.play_plot_14()
        elif not self.plot_15_played and self.game.map_in_use == tilemap_9:
            self.play_plot_15()
        elif not self.plot_16_played and self.game.scene_5_complete:
            self.play_plot_16()
        elif self.get_shot:
            self.play_get_shot()

class PlotBox:
    def __init__(self, game, text):

        self.game = game
        self.text = text

        self.x = PLOT_BOX_X
        self.y = PLOT_BOX_Y
        self.width = DIALOGUE_BOX_WIDTH
        self.height = DIALOGUE_BOX_HEIGHT

        self.image = self.game.dialogue_frame.get_sprite(800, 200, 800, 200)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    @classmethod
    def text_box(cls, game, text):
        text_box = cls(game, text)
        text_box.text = text

        text_box.x = TEXT_BOX_X
        text_box.y = TEXT_BOX_Y
        text_box.width = TEXT_BOX_WIDTH
        text_box.height = TEXT_BOX_HEIGHT

        text_box.image = Font().get_image(text_box.text)

        text_box.rect = text_box.image.get_rect()
        text_box.rect.x = text_box.x
        text_box.rect.y = text_box.y
        return text_box

    @classmethod
    def hint_box(cls, game, text):
        hint_box = cls(game, text)
        hint_box.text = text

        hint_box.x = HINT_BOX_X
        hint_box.y = HINT_BOX_Y
        hint_box.width = HINT_BOX_WIDTH
        hint_box.height = HINT_BOX_HEIGHT

        hint_box.image = Font().get_image(hint_box.text)

        hint_box.rect = hint_box.image.get_rect()
        hint_box.rect.x = hint_box.x
        hint_box.rect.y = hint_box.y
        return hint_box


class PlotBoxGroups:
    def __init__(self, game):
        self.game = game
        self.plotBoxes_list = []

    def generate_plotBox(self, name, text):
        new_box = None
        if name is None:
            return
        if name == 'box':
            new_box = PlotBox(self.game, text)
        if name == 'text box':
            new_box = PlotBox.text_box(self.game, text)
        if name == 'hint box':
            new_box = PlotBox.hint_box(self.game, text)
        self.plotBoxes_list.append(new_box)

    def generate_plots(self, text):
        self.generate_plotBox('box', text)
        self.generate_plotBox('text box', text)
        self.generate_plotBox('hint box', HINT)

    def draw(self, screen):
        for plotBox in self.plotBoxes_list:
            screen.blit(plotBox.image, plotBox.rect)


