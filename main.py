# Project name: Hackovid
# Course: Python game programming
# Group: 3-1
# Game type: role-playing game
# Engineer: Watson Chao
# Institute: department of Engineering Science - NCKU
# File: main.py

import pygame
import sys, os
from config import *
from sprites import *
from font import *
from plot import *


class Game:  # 遊戲初始設置
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # 設定視窗大小
        pygame.display.set_caption("Hackovid")
        self.clock = pygame.time.Clock()    # 設定時間
        self.running = True
        self.restart = True
        self.game_over_by_get_caught = False
        self.game_over_by_confirmed_case = False
        self.game_over_by_get_shot = False
        self.good_end = False
        self.fade_in_counter = 255
        self.fade_out_counter = 0
        self.fade_in_from_black = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
        self.fade_out_to_black = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
        self.fade_in_from_black.fill((0, 0, 0))
        self.fade_out_to_black.fill((0, 0, 0))
        # 載入圖片及音樂
        self.intro = pygame.transform.scale(pygame.image.load("./images/hackovid_intro.png"), (WIN_WIDTH, WIN_HEIGHT))
        self.get_caught = pygame.transform.scale(pygame.image.load("./images/gameover_caught.png"), (WIN_WIDTH, WIN_HEIGHT))
        self.get_shot = pygame.transform.scale(pygame.image.load("./images/gameover_shot.png"), (WIN_WIDTH, WIN_HEIGHT))
        self.confirmed_case = pygame.transform.scale(pygame.image.load("./images/gameover_confirmed.png"), (WIN_WIDTH, WIN_HEIGHT))
        self.character_spritesheet = SpritesSheet('images/character.png')
        self.terrain_spritesheet = SpritesSheet('images/terrain.png')
        self.furniture_spritesheet = SpritesSheet('images/furniture.png')
        self.street_spritesheet = SpritesSheet('images/street.png')
        self.dialogue_frame = SpritesSheet('images/dialogue_frame.png')
        self.item_spritesheet = SpritesSheet('images/object.png')
        self.bag_spritesheet = SpritesSheet('images/bag.png')
        self.news_1 = SpritesSheet('./images/news1.png')
        self.news_2 = SpritesSheet('./images/news2.png')
        self.password_hint = SpritesSheet('./images/password_hint.png')
        self.password_paper = SpritesSheet('./images/password_paper.png')
        self.mail = SpritesSheet('./images/mail.png')
        self.clue_paper = SpritesSheet('./images/clue_paper.png')
        self.bullet = SpritesSheet('./images/bullet.png')
        self.intro_music = r'music/intro.mp3'
        self.bad_end_music = r'music/bad_end.mp3'
        self.home_music = r'music/home.mp3'
        self.street_music = r'music/street.mp3'
        self.school_music = r'music/school.mp3'
        self.police_music = r'music/police.mp3'
        self.chase_music = r'music/chase.mp3'
        self.scene_4_music = r'music/scene_4.mp3'
        self.get_effect = r'music/get.wav'
        self.killed_effect = r'music/killed.wav'
        self.enter_effect = r'music/enter.wav'
        self.door_effect = r'music/door.wav'
        self.walk_effect = r'music/walk.wav'
        self.choose_effect = r'music/choose.wav'
        self.shot_effect = r'music/deagle.wav'

    def do_fade_in(self):
        self.clock.tick(FPS)
        self.fade_in_from_black.set_alpha(self.fade_in_counter)
        self.screen.blit(self.fade_in_from_black, (0, 0))
        self.fade_in_counter -= 4

    def do_fade_out(self):
        self.clock.tick(FPS)
        self.fade_out_to_black.set_alpha(self.fade_out_counter)
        self.screen.blit(self.fade_out_to_black, (0, 0))
        self.fade_out_counter += 4

    def create_tilemap(self):   # 在畫面上畫出地圖
        # 依地圖判斷播放的音樂
        if self.map_in_use == tilemap or self.map_in_use == tilemap_4:
            pygame.mixer.music.load(self.home_music)
            pygame.mixer.music.set_volume(0.7)
            pygame.mixer.music.play(-1)
        elif self.map_in_use == tilemap_2 or self.map_in_use == tilemap_5 or self.map_in_use == tilemap_8:
            pygame.mixer.music.load(self.street_music)
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.play(-1)
        elif self.map_in_use == tilemap_3 or self.map_in_use == tilemap_6:
            pygame.mixer.music.load(self.school_music)
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.play(-1)
        elif self.map_in_use == tilemap_7 or self.map_in_use == tilemap_12:
            pygame.mixer.music.load(self.police_music)
            pygame.mixer.music.set_volume(0.3)
            pygame.mixer.music.play(-1)
        elif self.map_in_use == tilemap_9 or self.map_in_use == tilemap_10 or self.map_in_use == tilemap_11:
            pygame.mixer.music.load(self.chase_music)
            pygame.mixer.music.set_volume(0.3)
            pygame.mixer.music.play(-1)
        # 生成地圖
        for i, row in enumerate(self.map_in_use):
            for j, column in enumerate(row):

                if column == "P":
                    self.players.generate_player(j, i)
                if column == "!":
                    self.NPCs.generate_NPC('Mom', j, i)
                if column == "@":
                    self.NPCs.generate_NPC('Government official', j, i)
                if column == "#":
                    self.NPCs.generate_NPC('Boss', j, i)
                if column == "$":
                    self.NPCs.generate_NPC('Guard', j, i)
                if column == "%":
                    self.NPCs.generate_NPC('Police', j, i)
                if column == "^":
                    self.NPCs.generate_NPC('Police2', j, i)
                if column == "*":
                    self.NPCs.generate_NPC('Police3', j, i)

                if column == "/":
                    self.blocks.generate_block('block', j, i)
                if column == "A":
                    self.blocks.generate_block('low_cabinet', j, i)
                if column == "B":
                    if self.map_in_use == tilemap or self.map_in_use == tilemap_4:
                        self.blocks.generate_block('wall', j, i)
                    elif self.map_in_use == tilemap_3 or self.map_in_use == tilemap_6:
                        self.blocks.generate_block('grey wall', j, i)
                    elif self.map_in_use == tilemap_7 or self.map_in_use == tilemap_12:
                        self.blocks.generate_block('blue wall', j, i)
                if column == "b":
                    self.blocks.generate_block('buildings', j, i)
                if column == "C":
                    self.blocks.generate_block('computer', j, i)
                if column == "D":
                    self.blocks.generate_block('blackboard', j, i)
                if column == "E":
                    self.blocks.generate_block('bookcase', j, i)
                if column == "e":
                    self.blocks.generate_block('student_desk', j, i)
                if column == "F":
                    self.blocks.generate_block('rysofa', j, i)
                if column == "f":
                    self.blocks.generate_block('locker', j, i)
                if column == "G":
                    self.blocks.generate_block('lysofa', j, i)
                if column == "g":
                    self.blocks.generate_block('window', j, i)
                if column == "H":
                    self.blocks.generate_block('chair', j, i)
                if column == "I":
                    self.blocks.generate_block('bysofa', j, i)
                if column == "J":
                    self.blocks.generate_block('cactus', j, i)
                if column == "K":
                    self.blocks.generate_block('desk', j, i)
                if column == "L":
                    self.blocks.generate_block('clock', j, i)
                if column == "M":
                    self.blocks.generate_block('black', j, i)
                if column == "Q":
                    self.blocks.generate_block('police', j, i)
                if column == "R":
                    self.blocks.generate_block('room_sofa', j, i)
                if column == "S":
                    self.blocks.generate_block('bed', j, i)
                if column == "T":
                    self.blocks.generate_block('TV', j, i)
                if column == "U":
                    self.blocks.generate_block('school', j, i)
                if column == "V":
                    self.blocks.generate_block('home', j, i)
                if column == "W":
                    self.blocks.generate_block('tree', j, i)
                if column == "X":
                    self.blocks.generate_block('tree_1', j, i)
                if column == "x":
                    self.blocks.generate_block('fence', j, i)
                if column == "Y":
                    self.blocks.generate_block('tree_2', j, i)
                if column == "y":
                    self.blocks.generate_block('mailbox', j, i)
                if column == "Z":
                    self.blocks.generate_block('tree_3', j, i)
                if column == "z":
                    self.blocks.generate_block('roadblock', j, i)
                if column == "1":
                    self.doors.generate_door('home', j, i)
                if column == "2":
                    self.doors.generate_door('school', j, i)
                if column == "3":
                    self.doors.generate_door('police station', j, i)

                if column == "c":
                    self.dialogueSpots.generate_dialogueSpot('computer', j, i)
                if column == "m":
                    self.dialogueSpots.generate_dialogueSpot('Mom', j, i)
                if column == "d":
                    self.dialogueSpots.generate_dialogueSpot('Guard', j, i)
                if column == "v":
                    self.dialogueSpots.generate_dialogueSpot('police', j, i)
                if column == '-':
                    self.dialogueSpots.generate_dialogueSpot('stay back', j, i)


                if self.map_in_use == tilemap or self.map_in_use == tilemap_4:
                    self.grounds.generate_ground('wood', j, i)
                elif self.map_in_use == tilemap_2 or self.map_in_use == tilemap_5 or self.map_in_use == tilemap_8 or\
                        self.map_in_use == tilemap_9 or self.map_in_use == tilemap_9 or self.map_in_use == tilemap_10\
                        or self.map_in_use == tilemap_11:
                    self.grounds.generate_ground('grass', j, i)
                elif self.map_in_use == tilemap_3 or self.map_in_use == tilemap_6:
                    self.grounds.generate_ground('cement', j, i)
                elif self.map_in_use == tilemap_7 or self.map_in_use == tilemap_12:
                    self.grounds.generate_ground('grey', j, i)
                if self.map_in_use == tilemap_2 or self.map_in_use == tilemap_5 or self.map_in_use == tilemap_8 or\
                        self.map_in_use == tilemap_9 or self.map_in_use == tilemap_10 or self.map_in_use == tilemap_11:
                    if column == "O" or column == "p" or column == "$" or column == "d" or column == "#" or column == "@"\
                            or column == "神" or column == "強":
                        self.grounds.generate_ground('road', j, i)

                if column == "k":
                    self.items.generate_item('clue paper', j, i)
                if column == "a":
                    self.items.generate_item('mask', j, i)
                if column == "n":
                    self.items.generate_item('alcohol', j, i)
                if column == "w":
                    self.items.generate_item('cloak', j, i)
                if column == "r":
                    self.items.generate_item('health ID card', j, i)
                if column == "u":
                    self.items.generate_item('forehead thermometer', j, i)
                if column == "h":
                    self.items.generate_item('blinkers', j, i)
                if column == ",":
                    self.items.generate_item('switch', j, i)
                if column == ">":
                    self.items.generate_item('booklet', j, i)
                if column == "[":
                    self.items.generate_item('bauta', j, i)
                if column == "{":
                    self.items.generate_item('vaccine', j, i)
                if column == "『":
                    self.items.generate_item('gloves', j, i)
                if column == "「":
                    self.items.generate_item('face shield', j, i)
                if column == "強":
                    self.items.generate_item('handkerchief', j, i)
                if column == "i":
                    self.dialogueSpots.generate_dialogueSpot('clue paper', j, i)
                if column == "q":
                    self.dialogueSpots.generate_dialogueSpot('mask', j, i)
                if column == "l":
                    self.dialogueSpots.generate_dialogueSpot('alcohol', j, i)
                if column == "o":
                    self.dialogueSpots.generate_dialogueSpot('cloak', j, i)
                if column == "t":
                    self.dialogueSpots.generate_dialogueSpot('health ID card', j, i)
                if column == "s":
                    self.dialogueSpots.generate_dialogueSpot('forehead thermometer', j, i)
                if column == "j":
                    self.dialogueSpots.generate_dialogueSpot('blinkers', j, i)
                if column == "<":
                    self.dialogueSpots.generate_dialogueSpot('switch', j, i)
                if column == "?":
                    self.dialogueSpots.generate_dialogueSpot('booklet', j, i)
                if column == "]":
                    self.dialogueSpots.generate_dialogueSpot('bauta', j, i)
                if column == "}":
                    self.dialogueSpots.generate_dialogueSpot('vaccine', j, i)
                if column == "』":
                    self.dialogueSpots.generate_dialogueSpot('gloves', j, i)
                if column == "」":
                    self.dialogueSpots.generate_dialogueSpot('face shield', j, i)
                if column == "神":
                    self.dialogueSpots.generate_dialogueSpot('handkerchief', j, i)

    def check_threat(self):
        if self.map_in_use == tilemap_2 or self.map_in_use == tilemap_5 or self.map_in_use == tilemap_8:
            if self.players.protection < 100:
                self.plots.confirmed_case = True
        elif self.map_in_use == tilemap_3 or self.map_in_use == tilemap_6:
            if self.players.protection < 150:
                self.plots.confirmed_case = True
        elif self.map_in_use == tilemap_7 or self.map_in_use == tilemap_12:
            if self.players.protection < 250:
                self.plots.confirmed_case = True
        for spot in self.dialogueSpots.dialogueSpots_list:
            if spot.name == 'guard' or spot.name == 'guard2':
                if self.dialogueSpots.in_dialogue:
                    if self.players.protection < 300:
                        self.plots.confirmed_case = True

    def new(self):
        # new game start
        # 生成初始配置
        self.playing = True
        self.game_over = False
        self.plots = Plot(self)
        self.plotBoxes = PlotBoxGroups(self)
        self.players = PlayerGroup(self)
        self.NPCs = NPCGroup(self)
        self.grounds = GroundGroup(self)
        self.blocks = BlockGroup(self)
        self.dialogueSpots = DialogueSpotGroup(self)
        self.dialogueBoxes = DialogueBoxGroup(self)
        self.typeboxes = TypeBoxGroup(self)
        self.arrows = ArrowGroup(self)
        self.doors = DoorGroup(self)
        self.items = ItemGroup(self)
        self.bag = Bag(self)
        self.bullets = BulletGroup(self)

        self.map_in_use = tilemap

        self.scene_1_1_complete = False
        self.scene_1_2_complete = False
        self.scene_1_3_complete = False
        self.scene_1_complete = False
        self.scene_2_1_complete = False
        self.scene_2_2_complete = False
        self.scene_2_complete = False
        self.scene_3_1_complete = False
        self.scene_3_complete = False
        self.scene_4_1_complete = False
        self.scene_4_2_complete = False
        self.scene_4_complete = False
        self.scene_5_1_complete = False
        self.scene_5_2_complete = False
        self.scene_5_3_complete = False
        self.scene_5_complete = False
        self.scene_4_1_music_played = False

        self.create_tilemap()

        self.enter_sound = pygame.mixer.Sound(self.enter_effect)
        self.enter_sound.set_volume(0.3)

        self.door_sound = pygame.mixer.Sound(self.door_effect)
        self.door_sound.set_volume(0.3)

        self.walk_sound = pygame.mixer.Sound(self.walk_effect)
        self.walk_sound.set_volume(0.3)

        self.choose_sound = pygame.mixer.Sound(self.choose_effect)
        self.choose_sound.set_volume(0.1)

        self.killed_sound = pygame.mixer.Sound(self.killed_effect)
        self.killed_sound.set_volume(0.3)

        self.shot_sound = pygame.mixer.Sound(self.shot_effect)
        self.shot_sound.set_volume(0.7)

        self.get_sound = pygame.mixer.Sound(self.get_effect)
        self.get_sound.set_volume(0.5)

    def events(self):
        # game loop events
        if self.map_in_use == tilemap_4 and self.scene_2_2_complete:
            self.scene_2_complete = True
        if self.map_in_use == tilemap_3:
            self.scene_1_complete = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.playing = False
                    self.running = False
                if self.plots.playing_plot:
                    if event.key == pygame.K_SPACE:
                        self.enter_sound.play()
                        self.plots.plot_counter += 1
                if self.typeboxes.is_typing:
                    self.dialogueSpots.in_dialogue = False
                    if event.key == pygame.K_SPACE:
                        if self.typeboxes.submitted:
                            self.typeboxes.typeBoxes_list.clear()
                            self.typeboxes.submitted = False
                            self.typeboxes.is_typing = False
                            self.typeboxes.hack_mail = False
                            self.typeboxes.login_mail = False
                            self.typeboxes.login_password = False
                            if self.typeboxes.account_correct:
                                self.typeboxes.account_correct = False
                                self.scene_3_1_complete = True
                            if self.typeboxes.got_mail_password:
                                self.typeboxes.got_mail_password = False
                                self.scene_4_complete = True
                            if self.typeboxes.password_correct:
                                self.typeboxes.password_correct = False
                                self.scene_5_1_complete = True
                            if self.typeboxes.mail_correct:
                                self.typeboxes.mail_correct = False
                                self.typeboxes.is_typing = True
                                if not self.typeboxes.generated:
                                    self.typeboxes.generate = True
                                self.typeboxes.login_password = True
                        else:
                            self.typeboxes.check_user_input()
                    else:
                        self.typeboxes.user_input += event.unicode
            # 設定事件
                elif self.dialogueSpots.player_at_dialogueSpot:
                    # 按鍵事件
                    if event.type == pygame.KEYDOWN:

                        # 中斷對話
                        if event.key == pygame.K_q:
                            if self.dialogueBoxes.displaying:
                                self.dialogueSpots.in_dialogue = False
                                self.dialogueBoxes.displaying = False
                            else:
                                self.dialogueSpots.in_dialogue = False
                                self.dialogueBoxes.generated = False
                                self.dialogueBoxes.delete = True
                        # 選擇選項
                        if self.dialogueSpots.in_dialogue:
                            if event.key == pygame.K_s:
                                for arrow in self.arrows.arrows_list:
                                    if arrow.rect.y == ARROW_CHOOSE_ONE_Y:
                                        arrow.rect.y = ARROW_CHOOSE_TWO_Y
                                        break
                                    if arrow.rect.y == ARROW_CHOOSE_TWO_Y:
                                        arrow.rect.y = ARROW_CHOOSE_THREE_Y
                                        break
                                    if arrow.rect.y == ARROW_CHOOSE_THREE_Y:
                                        arrow.rect.y = ARROW_CHOOSE_FOUR_Y
                                        break
                                    if arrow.rect.y == ARROW_CHOOSE_FOUR_Y:
                                        arrow.rect.y = ARROW_CHOOSE_ONE_Y
                                        break
                            if event.key == pygame.K_w:
                                for arrow in self.arrows.arrows_list:
                                    if arrow.rect.y == ARROW_CHOOSE_ONE_Y:
                                        arrow.rect.y = ARROW_CHOOSE_FOUR_Y
                                        break
                                    if arrow.rect.y == ARROW_CHOOSE_TWO_Y:
                                        arrow.rect.y = ARROW_CHOOSE_ONE_Y
                                        break
                                    if arrow.rect.y == ARROW_CHOOSE_THREE_Y:
                                        arrow.rect.y = ARROW_CHOOSE_TWO_Y
                                        break
                                    if arrow.rect.y == ARROW_CHOOSE_FOUR_Y:
                                        arrow.rect.y = ARROW_CHOOSE_THREE_Y
                                        break
                        # 接續對話、確定選擇
                        if event.key == pygame.K_SPACE:
                            if self.dialogueSpots.player_at_dialogueSpot and not self.dialogueBoxes.displaying and \
                                    not self.plots.playing_plot and not self.dialogueSpots.in_dialogue and not self.typeboxes.is_typing:
                                self.choose_sound.play()
                                if not self.dialogueBoxes.generated:
                                    self.dialogueSpots.in_dialogue = True
                                    self.dialogueBoxes.generate = True
                            elif self.dialogueSpots.in_dialogue:
                                self.enter_sound.play()
                                self.items.detect_pick_up_item()
                                if self.dialogueBoxes.detect_scene_5(self.dialogueBoxes.detect_choice()):
                                    self.dialogueBoxes.dialogue_end()
                                elif self.dialogueBoxes.detect_scene_3(self.dialogueBoxes.detect_choice()):
                                    self.dialogueBoxes.end_by_get_money(self.dialogueBoxes.detect_choice())
                                elif self.dialogueBoxes.detect_scene_1_3():
                                    self.dialogueBoxes.end_by_mom_run()
                                elif self.dialogueBoxes.detect_login_mail(self.dialogueBoxes.detect_choice()):
                                    self.dialogueBoxes.dialogue_end()
                                    self.typeboxes.is_typing = True
                                    self.typeboxes.login_mail = True
                                    if not self.typeboxes.generated:
                                        self.typeboxes.generate = True
                                elif self.dialogueBoxes.detect_hacking_mail(self.dialogueBoxes.detect_choice()):
                                    self.dialogueBoxes.dialogue_end()
                                    self.typeboxes.is_typing = True
                                    self.typeboxes.hack_mail = True
                                    if not self.typeboxes.generated:
                                        self.typeboxes.generate = True
                                elif self.dialogueBoxes.displaying:
                                    if self.scene_4_1_complete and not self.scene_4_1_music_played:
                                        self.scene_4_1_music_played = True
                                        pygame.mixer.music.load(self.scene_4_music)
                                        pygame.mixer.music.set_volume(0.3)
                                        pygame.mixer.music.play(-1)
                                    self.dialogueSpots.in_dialogue = False
                                    self.dialogueBoxes.displaying = False
                                    self.dialogueBoxes.image_displaying.clear()
                                elif self.dialogueBoxes.detect_scene_3_1(self.dialogueBoxes.detect_choice()):
                                    self.dialogueBoxes.dialogue_end()
                                    self.typeboxes.is_typing = True
                                    if not self.typeboxes.generated:
                                        self.typeboxes.generate = True
                                elif self.dialogueBoxes.detect_scene_1_2(self.dialogueBoxes.detect_choice()):
                                    self.dialogueBoxes.end_by_news()
                                elif self.dialogueBoxes.detect_hack_tool(self.dialogueBoxes.detect_choice()):
                                    self.dialogueBoxes.end_by_password_hint()
                                elif self.dialogueBoxes.detect_scene_5_2(self.dialogueBoxes.detect_choice()):
                                    self.dialogueBoxes.end_by_check_mail()
                                elif self.dialogueBoxes.detect_end(self.dialogueBoxes.detect_choice()):
                                    self.dialogueBoxes.dialogue_end()
                                else:
                                    self.dialogueBoxes.detect_scene_4_2(self.dialogueBoxes.detect_choice())
                                    self.dialogueBoxes.next_dialogue(self.dialogueBoxes.detect_choice())

                                for arrow in self.arrows.arrows_list:
                                    arrow.rect.y = ARROW_CHOOSE_ONE_Y

    def update(self):
        # game loop update
        self.check_threat()
        if self.game_over:
            pass
        elif self.plots.playing_plot:
            self.plots.update()
        elif self.typeboxes.is_typing:
            self.typeboxes.update()
            self.dialogueSpots.update()
            self.dialogueBoxes.update()
            self.dialogueSpots.refresh_dialogueSpots()
        elif self.dialogueSpots.in_dialogue:
            self.dialogueSpots.update()
            self.dialogueBoxes.update()
            self.arrows.update()
        else:
            self.plots.update()
            self.dialogueSpots.refresh_dialogueSpots()
            self.typeboxes.update()
            self.doors.update()
            self.players.update()
            self.grounds.update()
            self.NPCs.update()
            self.blocks.update()
            self.dialogueSpots.update()
            self.dialogueBoxes.update()
            self.arrows.update()
            self.bullets.update()

    def draw(self):
        # game loop draw
        if not self.plots.plot_1_played:
            self.plotBoxes.draw(self.screen)
            self.do_fade_in()
        elif self.game_over:
            self.do_fade_out()
            if self.fade_out_counter > 255:
                self.playing = False

        else:
            self.dialogueSpots.draw(self.screen)
            self.doors.draw(self.screen)
            self.grounds.draw(self.screen)
            self.blocks.draw(self.screen)
            self.players.draw(self.screen)
            self.items.draw(self.screen)
            self.NPCs.draw(self.screen)
            self.dialogueBoxes.draw(self.screen)
            self.arrows.draw(self.screen)
            self.typeboxes.draw(self.screen)
            self.plotBoxes.draw(self.screen)
            self.bag.draw(self.screen)
            self.bullets.draw(self.screen)

        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        # game loop
        while self.playing:
            self.update()
            self.events()
            self.draw()
        self.running = False

    def intro_screen(self):
        self.restart = False
        in_intro = True
        intro_text = Font().get_text('texts/intro.txt')
        intro_text_image = pygame.font.Font("texts/NotoSerifCJKtc-Regular.otf", 24).render(intro_text, True, (255, 255, 255), (0, 0, 0))
        intro_text_image = intro_text_image.convert()
        counter = 0
        choose_sound = pygame.mixer.Sound(self.choose_effect)
        choose_sound.set_volume(0.1)
        pygame.mixer.music.load(self.intro_music)
        pygame.mixer.music.set_volume(0.7)
        pygame.mixer.music.play(-1)
        fade_in = True
        fade_out = False
        while in_intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.playing = False
                    self.running = False
                    in_intro = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.playing = False
                        self.running = False
                        in_intro = False
                    if event.key == pygame.K_SPACE:
                        choose_sound.play()
                        in_intro = False
            intro_text_image.set_alpha(counter)
            self.screen.blit(intro_text_image, (1000, 725))
            self.screen.blit(self.intro, (0, 0))
            self.screen.blit(intro_text_image, (1000, 725))
            self.clock.tick(FPS)
            pygame.display.update()

            if fade_in:
                counter += 4
            if fade_out:
                counter -= 4
            if counter >= 255:
                fade_out = True
                fade_in = False
            if counter == 0:
                fade_in = True
                fade_out = False

    def gameover(self):
        from pygamevideo import Video
        import time
        self.restart = True
        self.counter = 0
        in_gameover = True
        text = Font().get_text('texts/hint.txt')
        text_image = pygame.font.Font("texts/NotoSerifCJKtc-Regular.otf", 24).render(text, True, (255, 255, 255), (0, 0, 0))
        text_image = text_image.convert()
        choose_sound = pygame.mixer.Sound(self.choose_effect)
        choose_sound.set_volume(0.1)
        start = time.time()
        if self.good_end:
            video = Video("movie/end.mp4")
            pygame.mixer.quit()
            video.play(False)

        if self.game_over_by_get_caught or self.game_over_by_get_shot or self.game_over_by_confirmed_case:
            pygame.mixer.music.load(self.bad_end_music)
            pygame.mixer.music.set_volume(0.7)
            pygame.mixer.music.play(-1)
            self.fade_in_counter = 255

        while in_gameover:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.playing = False
                    self.running = False
                    self.restart = False
                    in_gameover = False
                if event.type == pygame.KEYDOWN:
                    if not self.good_end:
                        if event.key == pygame.K_ESCAPE:
                            self.playing = False
                            self.running = False
                            in_gameover = False
                        if event.key == pygame.K_SPACE:
                            choose_sound.play()
                            self.playing = False
                            self.running = False
                            in_gameover = False
            current_time = time.time()
            time_passed = current_time - start
            if self.game_over_by_get_caught:
                self.screen.blit(self.get_caught, (0, 0))
                self.screen.blit(text_image, (1000, 725))
                self.do_fade_in()
            if self.game_over_by_confirmed_case:
                self.screen.blit(self.confirmed_case, (0, 0))
                self.screen.blit(text_image, (1000, 725))
                self.do_fade_in()
            if self.game_over_by_get_shot:
                self.screen.blit(self.get_shot, (0, 0))
                self.screen.blit(text_image, (1000, 725))
                self.do_fade_in()
            if self.good_end:
                if time_passed <= 45:
                    video.draw_to(self.screen, (0, 0))

                else:
                    in_gameover = False




            self.clock.tick(FPS)
            pygame.display.update()



hackovid = Game()
while hackovid.restart:
    hackovid = Game()
    hackovid.intro_screen()
    hackovid.new()
    while hackovid.running:
        hackovid.main()
        hackovid.gameover()
pygame.quit()
sys.exit()
