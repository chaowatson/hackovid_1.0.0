# Project name: Hackovid
# Course: Python game programming
# Group: 3-1
# Game type: role-playing game
# Engineer: Watson Chao
# Institute: department of Engineering Science - NCKU
# File: font.py

import pygame
from config import *
from sprites import *


class Font:
    def __init__(self):
        # 設定字型
        pygame.init()
        self.font = pygame.font.Font("texts/NotoSerifCJKtc-Regular.otf", 20)
        pygame.font.init()

    def get_text(self, text_file):
        # 讀取文字檔
        file = open(text_file, "r", encoding="utf-8")
        text = (file.read())
        return text

    def get_image(self, text):
        # 取得圖片
        image = self.font.render(text, True, (0, 0, 0), (255, 255, 255))
        return image




# 取得文字
HINT = Font().get_text('texts/plots/hint.txt')


PLOT_CONFIRMED_CASE_1 = Font().get_text('texts/plots/plot_confirmed_case_1.txt')
PLOT_CONFIRMED_CASE_2 = Font().get_text('texts/plots/plot_confirmed_case_2.txt')
PLOT_CONFIRMED_CASE_3 = Font().get_text('texts/plots/plot_confirmed_case_3.txt')
PLOT_CONFIRMED_CASE_4 = Font().get_text('texts/plots/plot_confirmed_case_4.txt')
PLOT_CONFIRMED_CASE_5 = Font().get_text('texts/plots/plot_confirmed_case_5.txt')
PLOT_CONFIRMED_CASE_6 = Font().get_text('texts/plots/plot_confirmed_case_6.txt')
# 設定情節-第一節
PLOT_ONE_1 = Font().get_text('texts/plots/plot_one_1.txt')
PLOT_ONE_2 = Font().get_text('texts/plots/plot_one_2.txt')
PLOT_ONE_3 = Font().get_text('texts/plots/plot_one_3.txt')
PLOT_ONE_4 = Font().get_text('texts/plots/plot_one_4.txt')
PLOT_ONE_5 = Font().get_text('texts/plots/plot_one_5.txt')
PLOT_ONE_6 = Font().get_text('texts/plots/plot_one_6.txt')
PLOT_ONE_7 = Font().get_text('texts/plots/plot_one_7.txt')
PLOT_ONE_8 = Font().get_text('texts/plots/plot_one_8.txt')
PLOT_ONE_9 = Font().get_text('texts/plots/plot_one_9.txt')
PLOT_ONE_10 = Font().get_text('texts/plots/plot_one_10.txt')
PLOT_ONE_11 = Font().get_text('texts/plots/plot_one_11.txt')

# 設定情節-第二節
PLOT_TWO_1 = Font().get_text('texts/plots/plot_two_1.txt')
PLOT_TWO_2 = Font().get_text('texts/plots/plot_two_2.txt')
PLOT_TWO_3 = Font().get_text('texts/plots/plot_two_3.txt')
PLOT_TWO_4 = Font().get_text('texts/plots/plot_two_4.txt')
PLOT_TWO_5 = Font().get_text('texts/plots/plot_two_5.txt')

# 設定情節-第三節
PLOT_THREE_1 = Font().get_text('texts/plots/plot_three_1.txt')
PLOT_THREE_2 = Font().get_text('texts/plots/plot_three_2.txt')
PLOT_THREE_3 = Font().get_text('texts/plots/plot_three_3.txt')
PLOT_THREE_4 = Font().get_text('texts/plots/plot_three_4.txt')
PLOT_THREE_5 = Font().get_text('texts/plots/plot_three_5.txt')
PLOT_THREE_6 = Font().get_text('texts/plots/plot_three_6.txt')

# 設定情節-第四節
PLOT_FOUR_1 = Font().get_text('texts/plots/plot_four_1.txt')
PLOT_FOUR_2 = Font().get_text('texts/plots/plot_four_2.txt')

# 設定情節-第五節
PLOT_FIVE_1 = Font().get_text('texts/plots/plot_five_1.txt')
PLOT_FIVE_2 = Font().get_text('texts/plots/plot_five_2.txt')
PLOT_FIVE_3 = Font().get_text('texts/plots/plot_five_3.txt')
PLOT_FIVE_4 = Font().get_text('texts/plots/plot_five_4.txt')
PLOT_FIVE_5 = Font().get_text('texts/plots/plot_five_5.txt')

PLOT_SIX_1 = Font().get_text('texts/plots/plot_six_1.txt')
PLOT_SIX_2 = Font().get_text('texts/plots/plot_six_2.txt')
PLOT_SIX_3 = Font().get_text('texts/plots/plot_six_3.txt')
PLOT_SIX_4 = Font().get_text('texts/plots/plot_six_4.txt')
PLOT_SIX_5 = Font().get_text('texts/plots/plot_six_5.txt')
PLOT_SIX_6 = Font().get_text('texts/plots/plot_six_6.txt')
PLOT_SIX_7 = Font().get_text('texts/plots/plot_six_7.txt')
PLOT_SIX_8 = Font().get_text('texts/plots/plot_six_8.txt')
PLOT_SIX_9 = Font().get_text('texts/plots/plot_six_9.txt')
PLOT_SIX_10 = Font().get_text('texts/plots/plot_six_10.txt')
PLOT_SIX_11 = Font().get_text('texts/plots/plot_six_11.txt')
PLOT_SIX_12 = Font().get_text('texts/plots/plot_six_12.txt')
PLOT_SIX_13 = Font().get_text('texts/plots/plot_six_13.txt')
PLOT_SIX_14 = Font().get_text('texts/plots/plot_six_14.txt')
PLOT_SIX_15 = Font().get_text('texts/plots/plot_six_15.txt')
PLOT_SIX_16 = Font().get_text('texts/plots/plot_six_16.txt')
PLOT_SIX_17 = Font().get_text('texts/plots/plot_six_17.txt')
PLOT_SIX_18 = Font().get_text('texts/plots/plot_six_18.txt')

PLOT_SEVEN_1 = Font().get_text('texts/plots/plot_seven_1.txt')
PLOT_SEVEN_2 = Font().get_text('texts/plots/plot_seven_2.txt')
PLOT_SEVEN_3 = Font().get_text('texts/plots/plot_seven_3.txt')
PLOT_SEVEN_4 = Font().get_text('texts/plots/plot_seven_4.txt')
PLOT_SEVEN_5 = Font().get_text('texts/plots/plot_seven_5.txt')
PLOT_SEVEN_6 = Font().get_text('texts/plots/plot_seven_6.txt')
PLOT_SEVEN_7 = Font().get_text('texts/plots/plot_seven_7.txt')

PLOT_EIGHT_GAMEOVER_1 = Font().get_text('texts/plots/plot_eight_gameover_1.txt')
PLOT_EIGHT_GAMEOVER_2 = Font().get_text('texts/plots/plot_eight_gameover_2.txt')
PLOT_EIGHT_GAMEOVER_3 = Font().get_text('texts/plots/plot_eight_gameover_3.txt')

PLOT_EIGHT_1 = Font().get_text('texts/plots/plot_eight_1.txt')
PLOT_EIGHT_2 = Font().get_text('texts/plots/plot_eight_2.txt')
PLOT_EIGHT_3 = Font().get_text('texts/plots/plot_eight_3.txt')
PLOT_EIGHT_4 = Font().get_text('texts/plots/plot_eight_4.txt')
PLOT_EIGHT_5 = Font().get_text('texts/plots/plot_eight_5.txt')
PLOT_EIGHT_6 = Font().get_text('texts/plots/plot_eight_6.txt')
PLOT_EIGHT_7 = Font().get_text('texts/plots/plot_eight_7.txt')
PLOT_EIGHT_8 = Font().get_text('texts/plots/plot_eight_8.txt')
PLOT_EIGHT_9 = Font().get_text('texts/plots/plot_eight_9.txt')

PLOT_NINE_1 = Font().get_text('texts/plots/plot_nine_1.txt')
PLOT_NINE_2 = Font().get_text('texts/plots/plot_nine_2.txt')
PLOT_NINE_3 = Font().get_text('texts/plots/plot_nine_3.txt')
PLOT_NINE_4 = Font().get_text('texts/plots/plot_nine_4.txt')
PLOT_NINE_5 = Font().get_text('texts/plots/plot_nine_5.txt')
PLOT_NINE_6 = Font().get_text('texts/plots/plot_nine_6.txt')
PLOT_NINE_7 = Font().get_text('texts/plots/plot_nine_7.txt')
PLOT_NINE_8 = Font().get_text('texts/plots/plot_nine_8.txt')
PLOT_NINE_9 = Font().get_text('texts/plots/plot_nine_9.txt')

PLOT_TEN_1 = Font().get_text('texts/plots/plot_ten_1.txt')
PLOT_TEN_2 = Font().get_text('texts/plots/plot_ten_2.txt')
PLOT_TEN_3 = Font().get_text('texts/plots/plot_ten_3.txt')
PLOT_TEN_4 = Font().get_text('texts/plots/plot_ten_4.txt')
PLOT_TEN_5 = Font().get_text('texts/plots/plot_ten_5.txt')
PLOT_TEN_6 = Font().get_text('texts/plots/plot_ten_6.txt')
PLOT_TEN_7 = Font().get_text('texts/plots/plot_ten_7.txt')
PLOT_TEN_8 = Font().get_text('texts/plots/plot_ten_8.txt')
PLOT_TEN_9 = Font().get_text('texts/plots/plot_ten_9.txt')
PLOT_TEN_10 = Font().get_text('texts/plots/plot_ten_10.txt')
PLOT_TEN_11 = Font().get_text('texts/plots/plot_ten_11.txt')

PLOT_ELEVEN_1 = Font().get_text('texts/plots/plot_eleven_1.txt')
PLOT_ELEVEN_2 = Font().get_text('texts/plots/plot_eleven_2.txt')
PLOT_ELEVEN_3 = Font().get_text('texts/plots/plot_eleven_3.txt')
PLOT_ELEVEN_4 = Font().get_text('texts/plots/plot_eleven_4.txt')
PLOT_ELEVEN_5 = Font().get_text('texts/plots/plot_eleven_5.txt')
PLOT_ELEVEN_6 = Font().get_text('texts/plots/plot_eleven_6.txt')
PLOT_ELEVEN_7 = Font().get_text('texts/plots/plot_eleven_7.txt')
PLOT_ELEVEN_8 = Font().get_text('texts/plots/plot_eleven_8.txt')
PLOT_ELEVEN_9 = Font().get_text('texts/plots/plot_eleven_9.txt')
PLOT_ELEVEN_10 = Font().get_text('texts/plots/plot_eleven_10.txt')
PLOT_ELEVEN_11 = Font().get_text('texts/plots/plot_eleven_11.txt')
PLOT_ELEVEN_12 = Font().get_text('texts/plots/plot_eleven_12.txt')
PLOT_ELEVEN_13 = Font().get_text('texts/plots/plot_eleven_13.txt')
PLOT_ELEVEN_14 = Font().get_text('texts/plots/plot_eleven_14.txt')
PLOT_ELEVEN_15 = Font().get_text('texts/plots/plot_eleven_15.txt')
PLOT_ELEVEN_16 = Font().get_text('texts/plots/plot_eleven_16.txt')

PLOT_TWELVE_1 = Font().get_text('texts/plots/plot_twelve_1.txt')
PLOT_TWELVE_2 = Font().get_text('texts/plots/plot_twelve_2.txt')
PLOT_TWELVE_3 = Font().get_text('texts/plots/plot_twelve_3.txt')
PLOT_TWELVE_4 = Font().get_text('texts/plots/plot_twelve_4.txt')
PLOT_TWELVE_5 = Font().get_text('texts/plots/plot_twelve_5.txt')
PLOT_TWELVE_6 = Font().get_text('texts/plots/plot_twelve_6.txt')
PLOT_TWELVE_7 = Font().get_text('texts/plots/plot_twelve_7.txt')
PLOT_TWELVE_8 = Font().get_text('texts/plots/plot_twelve_8.txt')
PLOT_TWELVE_9 = Font().get_text('texts/plots/plot_twelve_9.txt')
PLOT_TWELVE_10 = Font().get_text('texts/plots/plot_twelve_10.txt')
PLOT_TWELVE_11 = Font().get_text('texts/plots/plot_twelve_11.txt')
PLOT_TWELVE_12 = Font().get_text('texts/plots/plot_twelve_12.txt')

PLOT_THIRTEEN_1 = Font().get_text('texts/plots/plot_thirteen_1.txt')
PLOT_THIRTEEN_2 = Font().get_text('texts/plots/plot_thirteen_2.txt')
PLOT_THIRTEEN_3 = Font().get_text('texts/plots/plot_thirteen_3.txt')
PLOT_THIRTEEN_4 = Font().get_text('texts/plots/plot_thirteen_4.txt')
PLOT_THIRTEEN_5 = Font().get_text('texts/plots/plot_thirteen_5.txt')
PLOT_THIRTEEN_6 = Font().get_text('texts/plots/plot_thirteen_6.txt')
PLOT_THIRTEEN_7 = Font().get_text('texts/plots/plot_thirteen_7.txt')

PLOT_FOURTEEN_1 = Font().get_text('texts/plots/plot_fourteen_1.txt')
PLOT_FOURTEEN_2 = Font().get_text('texts/plots/plot_fourteen_2.txt')
PLOT_FOURTEEN_3 = Font().get_text('texts/plots/plot_fourteen_3.txt')
PLOT_FOURTEEN_4 = Font().get_text('texts/plots/plot_fourteen_4.txt')
PLOT_FOURTEEN_5 = Font().get_text('texts/plots/plot_fourteen_5.txt')
PLOT_FOURTEEN_6 = Font().get_text('texts/plots/plot_fourteen_6.txt')
PLOT_FOURTEEN_7 = Font().get_text('texts/plots/plot_fourteen_7.txt')
PLOT_FOURTEEN_8 = Font().get_text('texts/plots/plot_fourteen_8.txt')
PLOT_FOURTEEN_9 = Font().get_text('texts/plots/plot_fourteen_9.txt')
PLOT_FOURTEEN_10 = Font().get_text('texts/plots/plot_fourteen_10.txt')
PLOT_FOURTEEN_11 = Font().get_text('texts/plots/plot_fourteen_11.txt')
PLOT_FOURTEEN_12 = Font().get_text('texts/plots/plot_fourteen_12.txt')
PLOT_FOURTEEN_13 = Font().get_text('texts/plots/plot_fourteen_13.txt')
PLOT_FOURTEEN_14 = Font().get_text('texts/plots/plot_fourteen_14.txt')
PLOT_FOURTEEN_15 = Font().get_text('texts/plots/plot_fourteen_15.txt')
PLOT_FOURTEEN_16 = Font().get_text('texts/plots/plot_fourteen_16.txt')

PLOT_FIFTEEN_1 = Font().get_text('texts/plots/plot_fifteen_1.txt')
PLOT_FIFTEEN_2 = Font().get_text('texts/plots/plot_fifteen_2.txt')
PLOT_FIFTEEN_3 = Font().get_text('texts/plots/plot_fifteen_3.txt')
PLOT_FIFTEEN_4 = Font().get_text('texts/plots/plot_fifteen_4.txt')
PLOT_FIFTEEN_5 = Font().get_text('texts/plots/plot_fifteen_5.txt')
PLOT_FIFTEEN_6 = Font().get_text('texts/plots/plot_fifteen_6.txt')
PLOT_FIFTEEN_7 = Font().get_text('texts/plots/plot_fifteen_7.txt')
PLOT_FIFTEEN_8 = Font().get_text('texts/plots/plot_fifteen_8.txt')
PLOT_FIFTEEN_9 = Font().get_text('texts/plots/plot_fifteen_9.txt')
PLOT_FIFTEEN_10 = Font().get_text('texts/plots/plot_fifteen_10.txt')
PLOT_FIFTEEN_11 = Font().get_text('texts/plots/plot_fifteen_11.txt')
PLOT_FIFTEEN_12 = Font().get_text('texts/plots/plot_fifteen_12.txt')
PLOT_FIFTEEN_13 = Font().get_text('texts/plots/plot_fifteen_13.txt')
PLOT_FIFTEEN_14 = Font().get_text('texts/plots/plot_fifteen_14.txt')
PLOT_FIFTEEN_15 = Font().get_text('texts/plots/plot_fifteen_15.txt')
PLOT_FIFTEEN_16 = Font().get_text('texts/plots/plot_fifteen_16.txt')

PLOT_SIXTEEN_1 = Font().get_text('texts/plots/plot_sixteen_1.txt')
PLOT_SIXTEEN_2 = Font().get_text('texts/plots/plot_sixteen_2.txt')
PLOT_SIXTEEN_3 = Font().get_text('texts/plots/plot_sixteen_3.txt')
PLOT_SIXTEEN_4 = Font().get_text('texts/plots/plot_sixteen_4.txt')
PLOT_SIXTEEN_5 = Font().get_text('texts/plots/plot_sixteen_5.txt')
PLOT_SIXTEEN_6 = Font().get_text('texts/plots/plot_sixteen_6.txt')
PLOT_SIXTEEN_7 = Font().get_text('texts/plots/plot_sixteen_7.txt')
PLOT_SIXTEEN_8 = Font().get_text('texts/plots/plot_sixteen_8.txt')
PLOT_SIXTEEN_9 = Font().get_text('texts/plots/plot_sixteen_9.txt')
PLOT_SIXTEEN_10 = Font().get_text('texts/plots/plot_sixteen_10.txt')
PLOT_SIXTEEN_11 = Font().get_text('texts/plots/plot_sixteen_11.txt')
PLOT_SIXTEEN_12 = Font().get_text('texts/plots/plot_sixteen_12.txt')
PLOT_SIXTEEN_13 = Font().get_text('texts/plots/plot_sixteen_13.txt')
PLOT_SIXTEEN_14 = Font().get_text('texts/plots/plot_sixteen_14.txt')
PLOT_SIXTEEN_15 = Font().get_text('texts/plots/plot_sixteen_15.txt')
PLOT_SIXTEEN_16 = Font().get_text('texts/plots/plot_sixteen_16.txt')

PLOT_GET_SHOT_1 = Font().get_text('texts/plots/plot_get_shot_1.txt')
PLOT_GET_SHOT_2 = Font().get_text('texts/plots/plot_get_shot_2.txt')
PLOT_GET_SHOT_3 = Font().get_text('texts/plots/plot_get_shot_3.txt')
PLOT_GET_SHOT_4 = Font().get_text('texts/plots/plot_get_shot_4.txt')
PLOT_GET_SHOT_5 = Font().get_text('texts/plots/plot_get_shot_5.txt')
PLOT_GET_SHOT_6 = Font().get_text('texts/plots/plot_get_shot_6.txt')

PLOT_NOT_GET_MONEY = Font().get_text('texts/plots/plot_not_get_money.txt')

ACCOUNT_TITLE = Font().get_text('texts/type/account_title.txt')
ACCOUNT_SUBTITLE = Font().get_text('texts/type/account_subtitle.txt')

ACCOUNT_HINT = Font().get_text('texts/type/account_hint.txt')
ACCOUNT_CORRECT_TITLE = Font().get_text('texts/type/account_correct_title.txt')
ACCOUNT_INCORRECT_TITLE = Font().get_text('texts/type/account_incorrect_title.txt')
ACCOUNT_CORRECT_SUBTITLE = Font().get_text('texts/type/account_correct_subtitle.txt')
ACCOUNT_INCORRECT_SUBTITLE = Font().get_text('texts/type/account_incorrect_subtitle.txt')

HACKING_MAIL_TITLE = Font().get_text('texts/type/hacking_mail_title.txt')
HACKING_MAIL_SUBTITLE = Font().get_text('texts/type/hacking_mail_subtitle.txt')

MAIL_PASSWORD_TITLE = Font().get_text('texts/type/mail_password_title.txt')
MAIL_PASSWORD_SUBTITLE = Font().get_text('texts/type/mail_password_subtitle.txt')
MAIL_NOT_FOUND_TITLE = Font().get_text('texts/type/mail_not_found_title.txt')
MAIL_NOT_FOUND_SUBTITLE = Font().get_text('texts/type/mail_not_found_subtitle.txt')

LOGIN_MAIL_TITLE = Font().get_text('texts/type/login_mail_title.txt')
LOGIN_MAIL_SUBTITLE = Font().get_text('texts/type/login_mail_subtitle.txt')

LOGIN_PASSWORD_TITLE = Font().get_text('texts/type/login_password_title.txt')
LOGIN_PASSWORD_SUBTITLE = Font().get_text('texts/type/login_password_subtitle.txt')

MAIL_CORRECT_TITLE = Font().get_text('texts/type/mail_correct_title.txt')
MAIL_CORRECT_SUBTITLE = Font().get_text('texts/type/mail_correct_subtitle.txt')

PASSWORD_CORRECT_TITLE = Font().get_text('texts/type/password_correct_title.txt')
PASSWORD_CORRECT_SUBTITLE = Font().get_text('texts/type/password_correct_subtitle.txt')

PASSWORD_INCORRECT_TITLE = Font().get_text('texts/type/password_incorrect_title.txt')
PASSWORD_INCORRECT_SUBTITLE = Font().get_text('texts/type/password_incorrect_subtitle.txt')

# 設定電腦的對話和選項
COMPUTER_title = Font().get_text('texts/computer/computer_title')
COMPUTER_first_choice = Font().get_text('texts/computer/computer_first_choice')
COMPUTER_second_choice = Font().get_text('texts/computer/computer_second_choice')
COMPUTER_third_choice = Font().get_text('texts/computer/computer_third_choice')
COMPUTER_fourth_choice = Font().get_text('texts/computer/computer_fourth_choice')

COMPUTER_title_1 = Font().get_text('texts/computer/computer_title_1')
COMPUTER_first_choice_1 = Font().get_text('texts/computer/computer_first_choice_1')
COMPUTER_second_choice_1 = Font().get_text('texts/computer/computer_second_choice_1')
COMPUTER_third_choice_1 = Font().get_text('texts/computer/computer_third_choice_1')
COMPUTER_fourth_choice_1 = Font().get_text('texts/computer/computer_fourth_choice_1')

COMPUTER_title_2 = Font().get_text('texts/computer/computer_title_2')
COMPUTER_first_choice_2 = Font().get_text('texts/computer/computer_first_choice_2')
COMPUTER_second_choice_2 = Font().get_text('texts/computer/computer_second_choice_2')
COMPUTER_third_choice_2 = Font().get_text('texts/computer/computer_third_choice_2')
COMPUTER_fourth_choice_2 = Font().get_text('texts/computer/computer_fourth_choice_2')

COMPUTER_title_3 = Font().get_text('texts/computer/computer_title_3')
COMPUTER_first_choice_3 = Font().get_text('texts/computer/computer_first_choice_3')
COMPUTER_second_choice_3 = Font().get_text('texts/computer/computer_second_choice_3')
COMPUTER_third_choice_3 = Font().get_text('texts/computer/computer_third_choice_3')
COMPUTER_fourth_choice_3 = Font().get_text('texts/computer/computer_fourth_choice_3')

COMPUTER_title_3_1 = Font().get_text('texts/computer/computer_title_3_1')
COMPUTER_first_choice_3_1 = Font().get_text('texts/computer/computer_first_choice_3_1')
COMPUTER_second_choice_3_1 = Font().get_text('texts/computer/computer_second_choice_3_1')
COMPUTER_third_choice_3_1 = Font().get_text('texts/computer/computer_third_choice_3_1')
COMPUTER_fourth_choice_3_1 = Font().get_text('texts/computer/computer_fourth_choice_3_1')

COMPUTER_title_3_2 = Font().get_text('texts/computer/computer_title_3_2')
COMPUTER_first_choice_3_2 = Font().get_text('texts/computer/computer_first_choice_3_2')
COMPUTER_second_choice_3_2 = Font().get_text('texts/computer/computer_second_choice_3_2')
COMPUTER_third_choice_3_2 = Font().get_text('texts/computer/computer_third_choice_3_2')
COMPUTER_fourth_choice_3_2 = Font().get_text('texts/computer/computer_fourth_choice_3_2')

COMPUTER_title_4 = Font().get_text('texts/computer/computer_title_4')
COMPUTER_first_choice_4 = Font().get_text('texts/computer/computer_first_choice_4')
COMPUTER_second_choice_4 = Font().get_text('texts/computer/computer_second_choice_4')
COMPUTER_third_choice_4 = Font().get_text('texts/computer/computer_third_choice_4')
COMPUTER_fourth_choice_4 = Font().get_text('texts/computer/computer_fourth_choice_4')

COMPUTER2_first_choice_3_2 = Font().get_text('texts/computer/computer2_first_choice_3_2')
COMPUTER2_first_choice_4 = Font().get_text('texts/computer/computer2_first_choice_4')
COMPUTER2_second_choice_4 = Font().get_text('texts/computer/computer2_second_choice_4')
COMPUTER2_third_choice_4 = Font().get_text('texts/computer/computer2_third_choice_4')
COMPUTER2_title_4_3 = Font().get_text('texts/computer/computer2_title_4_3')
COMPUTER2_first_choice_4_3 = Font().get_text('texts/computer/computer2_first_choice_4_3')
COMPUTER2_second_choice_4_3 = Font().get_text('texts/computer/computer2_second_choice_4_3')
COMPUTER2_third_choice_4_3 = Font().get_text('texts/computer/computer2_third_choice_4_3')
COMPUTER2_fourth_choice_4_3 = Font().get_text('texts/computer/computer2_fourth_choice_4_3')

COMPUTER3_title_3_2 = Font().get_text('texts/computer/computer3_title_3_2')
COMPUTER3_first_choice_3_2 = Font().get_text('texts/computer/computer3_first_choice_3_2')
COMPUTER3_second_choice_3_2 = Font().get_text('texts/computer/computer3_second_choice_3_2')

COMPUTER4_first_choice_3_2 = Font().get_text('texts/computer/computer4_first_choice_3_2')

COMPUTER5_title_4_3 = Font().get_text('texts/computer/computer5_title_4_3')
COMPUTER5_first_choice_4_3 = Font().get_text('texts/computer/computer5_first_choice_4_3')
COMPUTER5_second_choice_4_3 = Font().get_text('texts/computer/computer5_second_choice_4_3')
COMPUTER5_third_choice_4_3 = Font().get_text('texts/computer/computer5_third_choice_4_3')
COMPUTER5_fourth_choice_4_3 = Font().get_text('texts/computer/computer5_fourth_choice_4_3')

COMPUTER6_first_choice_2 = Font().get_text('texts/computer/computer6_first_choice_2')
COMPUTER6_second_choice_2 = Font().get_text('texts/computer/computer6_second_choice_2')

COMPUTER7_title_2 = Font().get_text('texts/computer/computer7_title_2')
COMPUTER7_first_choice_2 = Font().get_text('texts/computer/computer7_first_choice_2')

# 設定媽媽的對話和選項
MOM_title = Font().get_text('texts/mom/mom_title')
MOM_first_choice = Font().get_text('texts/mom/mom_first_choice')
MOM_second_choice = Font().get_text('texts/mom/mom_second_choice')
MOM_third_choice = Font().get_text('texts/mom/mom_third_choice')
MOM_fourth_choice = Font().get_text('texts/mom/mom_fourth_choice')

MOM_title_1 = Font().get_text('texts/mom/mom_title_1')
MOM_first_choice_1 = Font().get_text('texts/mom/mom_first_choice_1')
MOM_second_choice_1 = Font().get_text('texts/mom/mom_second_choice_1')
MOM_third_choice_1 = Font().get_text('texts/mom/mom_third_choice_1')
MOM_fourth_choice_1 = Font().get_text('texts/mom/mom_fourth_choice_1')

MOM_title_2 = Font().get_text('texts/mom/mom_title_2')
MOM_first_choice_2 = Font().get_text('texts/mom/mom_first_choice_2')
MOM_second_choice_2 = Font().get_text('texts/mom/mom_second_choice_2')
MOM_third_choice_2 = Font().get_text('texts/mom/mom_third_choice_2')
MOM_fourth_choice_2 = Font().get_text('texts/mom/mom_fourth_choice_2')

MOM2_third_choice = Font().get_text('texts/mom/mom2_third_choice')
MOM2_title_3 = Font().get_text('texts/mom/mom_title_3')
MOM2_first_choice_3 = Font().get_text('texts/mom/mom_first_choice_3')
MOM2_second_choice_3 = Font().get_text('texts/mom/mom_second_choice_3')
MOM2_third_choice_3 = Font().get_text('texts/mom/mom_third_choice_3')
MOM2_fourth_choice_3 = Font().get_text('texts/mom/mom_fourth_choice_3')

GUARD_title = Font().get_text('texts/guard/guard_title')
GUARD_first_choice = Font().get_text('texts/guard/guard_first_choice')
GUARD_second_choice = Font().get_text('texts/guard/guard_second_choice')
GUARD_third_choice = Font().get_text('texts/guard/guard_third_choice')
GUARD_fourth_choice = Font().get_text('texts/guard/guard_fourth_choice')

GUARD2_second_choice = Font().get_text('texts/guard/guard2_second_choice')
GUARD2_title_2 = Font().get_text('texts/guard/guard2_title_2')
GUARD2_first_choice_2 = Font().get_text('texts/guard/guard2_first_choice_2')
GUARD2_second_choice_2 = Font().get_text('texts/guard/guard2_second_choice_2')
GUARD2_third_choice_2 = Font().get_text('texts/guard/guard2_third_choice_2')
GUARD2_fourth_choice_2 = Font().get_text('texts/guard/guard2_fourth_choice_2')

POLICE_title = Font().get_text('texts/police/police_title')
POLICE_first_choice = Font().get_text('texts/police/police_first_choice')
POLICE_second_choice = Font().get_text('texts/police/police_second_choice')
POLICE_third_choice = Font().get_text('texts/police/police_third_choice')
POLICE_fourth_choice = Font().get_text('texts/police/police_fourth_choice')

POLICE2_first_choice = Font().get_text('texts/police/police2_first_choice')

STAY_BACK_title = Font().get_text('texts/stay_back_title.txt')
STAY_BACK_first_choice = Font().get_text('texts/stay_back_first_choice.txt')

TAKE = Font().get_text('texts/item/take.txt')
LEAVE = Font().get_text('texts/item/leave.txt')

CLUE_PAPER = Font().get_text('texts/item/clue_paper.txt')
MASK = Font().get_text('texts/item/mask.txt')
ALCOHOL = Font().get_text('texts/item/alcohol.txt')
CLOAK = Font().get_text('texts/item/cloak.txt')
HEALTH_ID_CARD = Font().get_text('texts/item/health_ID_card.txt')
FOREHEAD_THERMOMETER = Font().get_text('texts/item/forehead_thermometer.txt')
BLINKERS = Font().get_text('texts/item/blinkers.txt')
SWITCH = Font().get_text('texts/item/switch.txt')
BOOKLET = Font().get_text('texts/item/booklet.txt')
BAUTA = Font().get_text('texts/item/bauta.txt')
VACCINE = Font().get_text('texts/item/vaccine.txt')
GLOVES = Font().get_text('texts/item/gloves.txt')
FACE_SHIELD = Font().get_text('texts/item/face_shield.txt')
HANDKERCHIEF = Font().get_text('texts/item/handkerchief.txt')
