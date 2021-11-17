# Project name: Hackovid
# Course: Python game programming
# Group: 3-1
# Game type: role-playing game
# Engineer: Watson Chao
# Institute: department of Engineering Science - NCKU
# File: sprites.py

import pygame
import math
from config import *
from font import *


class SpritesSheet:    # 定義 SpritesSheet 功能
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface((width, height))
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey((0, 0, 0))
        return sprite


class Player:   # 定義角色相關內容

    def __init__(self, game, x, y):
        # 遊戲開始後，定義角色所處的層
        self.game = game
        self._layer = PLAYER_LAYER
        # 定義角色大小及位置
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = 2*TILE_SIZE
        self.height = 2*TILE_SIZE
        # 定義角色初始面向
        self.facing = 'down'
        self.animation_loop = 1
        # 定義角色初始移動變量
        self.x_change = 0
        self.y_change = 0
        # 定義角色初始移動變量
        self.image = self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)
        # 獲取角色位置
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def movement(self):
        # 設定上下左右的移動操控
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
        if keys[pygame.K_a]:
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pygame.K_s]:
            self.y_change += PLAYER_SPEED
            self.facing = 'down'
        if keys[pygame.K_d]:
            self.x_change += PLAYER_SPEED
            self.facing = 'right'

    def collide_blocks(self, direction):    # 定義角色碰撞方式
        # 如果撞到被定義為 block 的物件
        for block in self.game.blocks.blocks_list:
            hit = self.rect.colliderect(block.rect)
            # 如果橫向移動時撞到物品，角色停下
            if direction == "x":
                if hit:
                    if self.x_change > 0:
                        self.rect.right = block.rect.left
                    if self.x_change < 0:
                        self.rect.left = block.rect.right
            # 如果綜向移動時撞到物品，角色停下
            if direction == "y":
                if hit:
                    if self.y_change > 0:
                        self.rect.bottom = block.rect.top
                    if self.y_change < 0:
                        self.rect.top = block.rect.bottom
        # 如果撞到被定義為 npc 的物件
        for npc in self.game.NPCs.NPCs_list:
            hit = self.rect.colliderect(npc.rect)
            self.detect_gameover_2_2(npc)
            # 如果橫向移動時撞到物品，角色停下
            if direction == "x":
                if hit:
                    if self.x_change > 0:
                        self.rect.right = npc.rect.left
                    if self.x_change < 0:
                        self.rect.left = npc.rect.right
            # 如果綜向移動時撞到物品，角色停下
            if direction == "y":
                if hit:
                    if self.y_change > 0:
                        self.rect.bottom = npc.rect.top
                    if self.y_change < 0:
                        self.rect.top = npc.rect.bottom

            for item in self.game.items.items_list:
                hit = self.rect.colliderect(item.rect)
                # 如果橫向移動時撞到物品，角色停下
                if direction == "x":
                    if hit:
                        if self.x_change > 0:
                            self.rect.right = item.rect.left
                        if self.x_change < 0:
                            self.rect.left = item.rect.right
                # 如果綜向移動時撞到物品，角色停下
                if direction == "y":
                    if hit:
                        if self.y_change > 0:
                            self.rect.bottom = item.rect.top
                        if self.y_change < 0:
                            self.rect.top = item.rect.bottom

    def animate(self):  # 定義角色移動時動畫
        # 定義角色 向下 移動時圖片動畫
        down_animation = [self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height),
                          self.game.character_spritesheet.get_sprite(2*TILE_SIZE, 0, self.width, self.height),
                          self.game.character_spritesheet.get_sprite(4*TILE_SIZE, 0, self.width, self.height),
                          self.game.character_spritesheet.get_sprite(6*TILE_SIZE, 0, self.width, self.height)]
        # 定義角色 向上 移動時圖片動畫
        up_animation = [self.game.character_spritesheet.get_sprite(0, 2*TILE_SIZE, self.width, self.height),
                        self.game.character_spritesheet.get_sprite(2*TILE_SIZE, 2*TILE_SIZE, self.width, self.height),
                        self.game.character_spritesheet.get_sprite(4*TILE_SIZE, 2*TILE_SIZE, self.width, self.height),
                        self.game.character_spritesheet.get_sprite(6*TILE_SIZE, 2*TILE_SIZE, self.width, self.height)]
        # 定義角色 向左 移動時圖片動畫
        left_animation = [self.game.character_spritesheet.get_sprite(0, 4*TILE_SIZE, self.width, self.height),
                          self.game.character_spritesheet.get_sprite(2*TILE_SIZE, 4*TILE_SIZE, self.width, self.height),
                          self.game.character_spritesheet.get_sprite(4*TILE_SIZE, 4*TILE_SIZE, self.width, self.height),
                          self.game.character_spritesheet.get_sprite(6*TILE_SIZE, 4*TILE_SIZE, self.width, self.height)]
        # 定義角色 向右 移動時圖片動畫
        right_animation = [self.game.character_spritesheet.get_sprite(0, 6*TILE_SIZE, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(2*TILE_SIZE, 6*TILE_SIZE, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(4*TILE_SIZE, 6*TILE_SIZE, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(6*TILE_SIZE, 6*TILE_SIZE, self.width, self.height)]
        # 如果角色 向下 移動，讓角色圖片變為 面朝下 的圖片組
        if self.facing == 'down':
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)
            else:
                self.image = down_animation[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 4:
                    self.game.walk_sound.play()
                    self.animation_loop = 1
        # 如果角色 向上 移動，讓角色圖片變為 面朝上 的圖片組
        if self.facing == 'up':
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(0, 2*TILE_SIZE, self.width, self.height)
            else:
                self.image = up_animation[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 4:
                    self.game.walk_sound.play()
                    self.animation_loop = 1
        # 如果角色 向左 移動，讓角色圖片變為 面朝左 的圖片組
        if self.facing == 'left':
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(0, 4*TILE_SIZE, self.width, self.height)
            else:
                self.image = left_animation[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 4:
                    self.game.walk_sound.play()
                    self.animation_loop = 1
        # 如果角色 向右 移動，讓角色圖片變為 面朝右 的圖片組
        if self.facing == 'right':
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(0, 6*TILE_SIZE, self.width, self.height)
            else:
                self.image = right_animation[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 4:
                    self.game.walk_sound.play()
                    self.animation_loop = 1

    def detect_gameover_2_2(self, npc):
        if self.game.scene_2_1_complete:
            if npc.name == 'Boss' or npc.name == 'Government official':
                hit = self.rect.colliderect(npc.rect)
                if hit:
                    self.game.killed_sound.play()
                    self.game.game_over_by_get_caught =True
                    self.game.plots.scene_2_2_gameover = True


class PlayerGroup:  # 設角色 List 儲存角色圖片
    def __init__(self, game):
        self.players_list = []
        self.items_list =[]
        self.game = game
        self.protection = 0
        self.in_street = False

    def generate_player(self, x, y):    # 將角色加入角色 List
        self.players_list.append(Player(self.game, x, y))

    def detect_scene_2_1(self):
        for item in self.items_list:
            if item.name == 'clue paper':
                self.game.scene_2_1_complete = True


    def update(self):   # 更新角色資訊
        self.detect_scene_2_1()
        for player in self.players_list:
            player.movement()   # 角色的移動
            player.animate()    # 角色的動畫
            # 角色的碰撞
            player.rect.x += player.x_change
            player.collide_blocks("x")
            player.rect.y += player.y_change
            player.collide_blocks("y")
            # 角色移動變量歸零
            player.x_change = 0
            player.y_change = 0

    def draw(self, screen):  # 畫出角色
        for player in self.players_list:
            screen.blit(player.image, player.rect)


class NPC:  # 設置 NPC 相關內容
    def __init__(self, game, x, y):
        # 設置 NPC 所處的層
        self.game = game
        # 設置 NPC 大小
        self.name = None
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = 2*TILE_SIZE
        self.height = 2*TILE_SIZE
        # 設置 NPC 路徑
        self.path = None
        self.path_pos = 0
        # 設置 NPC 面向
        self.facing = 'down'
        self.animation_loop = 1
        # 設置 NPC 移動
        self.moving = False
        self.x_change = 0
        self.y_change = 0
        self.speed = 8

        self.max_count = TILE_SIZE/self.speed
        self.move_count = 0
        self.move_goal_x = None
        self.move_goal_y = None

        self.image = self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)
        # 獲取 NPC 位置
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.down_animation = []
        self.up_animation = []
        self.left_animation = []
        self.right_animation = []

        self.image_facing_up = None
        self.image_facing_down = None
        self.image_facing_left = None
        self.image_facing_right = None

    def move(self):  # 定義NPC移動
        if self.moving:
            if self.rect.x == self.move_goal_x and self.rect.y == self.move_goal_y:
                self.moving = False
                self.x_change = 0
                self.y_change = 0
            else:
                if self.path[self.path_pos] == 'x+':
                    self.x_change += self.speed
                elif self.path[self.path_pos] == 'x-':
                    self.x_change -= self.speed
                if self.path[self.path_pos] == 'y+':
                    self.y_change += self.speed
                elif self.path[self.path_pos] == 'y-':
                    self.y_change -= self.speed

            self.path_pos += 1

            if self.y_change == 0:
                if self.x_change > 0:
                    self.facing = 'right'
                if self.x_change < 0:
                    self.facing = 'left'
            if self.x_change == 0:
                if self.y_change > 0:
                    self.facing = 'down'
                if self.y_change < 0:
                    self.facing = 'up'


    def animate(self):
        down_animation = self.down_animation

        up_animation = self.up_animation

        left_animation = self.left_animation

        right_animation = self.right_animation

        if self.facing == 'down':
            if self.y_change == 0:
                self.image = self.image_facing_down
            else:
                self.image = down_animation[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 4:
                    self.game.walk_sound.play()
                    self.animation_loop = 1

        if self.facing == 'up':
            if self.y_change == 0:
                self.image = self.image_facing_up
            else:
                self.image = up_animation[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 4:
                    self.game.walk_sound.play()
                    self.animation_loop = 1

        if self.facing == 'left':
            if self.x_change == 0:
                self.image = self.image_facing_left
            else:
                self.image = left_animation[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 4:
                    self.game.walk_sound.play()
                    self.animation_loop = 1

        if self.facing == 'right':
            if self.x_change == 0:
                self.image = self.image_facing_right
            else:
                self.image = right_animation[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 4:
                    self.game.walk_sound.play()
                    self.animation_loop = 1


    @classmethod
    def Mom(cls, game, x, y):
        mom = cls(game, x, y)
        mom.name = 'Mom'
        mom.path = MOM_PATH
        mom.speed = 4
        mom.move_goal_x = 37*TILE_SIZE
        mom.move_goal_y = 26*TILE_SIZE
        mom.facing = 'down'
        mom.width = 2*TILE_SIZE
        mom.height = 2*TILE_SIZE
        mom.image = mom.game.character_spritesheet.get_sprite(8*TILE_SIZE, 8*TILE_SIZE, mom.width, mom.height)
        mom.image_facing_down = mom.game.character_spritesheet.get_sprite(8*TILE_SIZE, 8*TILE_SIZE, mom.width, mom.height)
        mom.image_facing_up = mom.game.character_spritesheet.get_sprite(8*TILE_SIZE, 10*TILE_SIZE, mom.width, mom.height)
        mom.image_facing_left = mom.game.character_spritesheet.get_sprite(8*TILE_SIZE, 12*TILE_SIZE, mom.width, mom.height)
        mom.image_facing_right = mom.game.character_spritesheet.get_sprite(8*TILE_SIZE, 14*TILE_SIZE, mom.width, mom.height)
        mom.down_animation = [mom.game.character_spritesheet.get_sprite(8*TILE_SIZE, 8*TILE_SIZE, mom.width, mom.height),
                          mom.game.character_spritesheet.get_sprite(10*TILE_SIZE, 8*TILE_SIZE, mom.width, mom.height),
                          mom.game.character_spritesheet.get_sprite(12*TILE_SIZE, 8*TILE_SIZE, mom.width, mom.height),
                          mom.game.character_spritesheet.get_sprite(14* TILE_SIZE, 8*TILE_SIZE, mom.width, mom.height)]

        mom.up_animation = [mom.game.character_spritesheet.get_sprite(8*TILE_SIZE, 10*TILE_SIZE, mom.width, mom.height),
                        mom.game.character_spritesheet.get_sprite(10*TILE_SIZE, 10*TILE_SIZE, mom.width, mom.height),
                        mom.game.character_spritesheet.get_sprite(12*TILE_SIZE, 10*TILE_SIZE, mom.width, mom.height),
                        mom.game.character_spritesheet.get_sprite(14*TILE_SIZE, 10*TILE_SIZE, mom.width, mom.height)]

        mom.left_animation = [mom.game.character_spritesheet.get_sprite(8*TILE_SIZE, 12*TILE_SIZE, mom.width, mom.height),
                          mom.game.character_spritesheet.get_sprite(10*TILE_SIZE, 12*TILE_SIZE, mom.width, mom.height),
                          mom.game.character_spritesheet.get_sprite(12*TILE_SIZE, 12*TILE_SIZE, mom.width, mom.height),
                          mom.game.character_spritesheet.get_sprite(14*TILE_SIZE, 12*TILE_SIZE, mom.width, mom.height)]

        mom.right_animation = [mom.game.character_spritesheet.get_sprite(8*TILE_SIZE, 14*TILE_SIZE, mom.width, mom.height),
                           mom.game.character_spritesheet.get_sprite(10*TILE_SIZE, 14*TILE_SIZE, mom.width, mom.height),
                           mom.game.character_spritesheet.get_sprite(12*TILE_SIZE, 14*TILE_SIZE, mom.width, mom.height),
                           mom.game.character_spritesheet.get_sprite(14*TILE_SIZE, 14*TILE_SIZE, mom.width, mom.height)]
        return mom

    @classmethod
    def Government_official(cls, game, x, y):
        government_official = cls(game, x, y)
        government_official.name = 'Government official'
        government_official.path = GOVERNMENT_OFFICIAL_PATH
        government_official.speed = 8
        government_official.move_goal_x = 11 * TILE_SIZE
        government_official.move_goal_y = 17 * TILE_SIZE
        government_official.facing = 'up'
        government_official.width = 2*TILE_SIZE
        government_official.height = 2*TILE_SIZE
        government_official.image = government_official.game.character_spritesheet.get_sprite(8*TILE_SIZE, 0*TILE_SIZE, government_official.width, government_official.height)
        government_official.image_facing_down = government_official.game.character_spritesheet.get_sprite(8*TILE_SIZE, 0*TILE_SIZE, government_official.width, government_official.height)
        government_official.image_facing_up = government_official.game.character_spritesheet.get_sprite(8*TILE_SIZE, 2*TILE_SIZE, government_official.width, government_official.height)
        government_official.image_facing_left = government_official.game.character_spritesheet.get_sprite(8*TILE_SIZE, 4*TILE_SIZE, government_official.width, government_official.height)
        government_official.image_facing_right = government_official.game.character_spritesheet.get_sprite(8*TILE_SIZE, 6*TILE_SIZE, government_official.width, government_official.height)
        government_official.down_animation = [government_official.game.character_spritesheet.get_sprite(8*TILE_SIZE, 0*TILE_SIZE, government_official.width, government_official.height),
                          government_official.game.character_spritesheet.get_sprite(10*TILE_SIZE, 0*TILE_SIZE, government_official.width, government_official.height),
                          government_official.game.character_spritesheet.get_sprite(12*TILE_SIZE, 0*TILE_SIZE, government_official.width, government_official.height),
                          government_official.game.character_spritesheet.get_sprite(14* TILE_SIZE, 0*TILE_SIZE, government_official.width, government_official.height)]

        government_official.up_animation = [government_official.game.character_spritesheet.get_sprite(8*TILE_SIZE, 2*TILE_SIZE, government_official.width, government_official.height),
                        government_official.game.character_spritesheet.get_sprite(10*TILE_SIZE, 2*TILE_SIZE, government_official.width, government_official.height),
                        government_official.game.character_spritesheet.get_sprite(12*TILE_SIZE, 2*TILE_SIZE, government_official.width, government_official.height),
                        government_official.game.character_spritesheet.get_sprite(14*TILE_SIZE, 2*TILE_SIZE, government_official.width, government_official.height)]

        government_official.left_animation = [government_official.game.character_spritesheet.get_sprite(8*TILE_SIZE, 4*TILE_SIZE, government_official.width, government_official.height),
                          government_official.game.character_spritesheet.get_sprite(10*TILE_SIZE, 4*TILE_SIZE, government_official.width, government_official.height),
                          government_official.game.character_spritesheet.get_sprite(12*TILE_SIZE, 4*TILE_SIZE, government_official.width, government_official.height),
                          government_official.game.character_spritesheet.get_sprite(14*TILE_SIZE, 4*TILE_SIZE, government_official.width, government_official.height)]

        government_official.right_animation = [government_official.game.character_spritesheet.get_sprite(8*TILE_SIZE, 6*TILE_SIZE, government_official.width, government_official.height),
                           government_official.game.character_spritesheet.get_sprite(10*TILE_SIZE, 6*TILE_SIZE, government_official.width, government_official.height),
                           government_official.game.character_spritesheet.get_sprite(12*TILE_SIZE, 6*TILE_SIZE, government_official.width, government_official.height),
                           government_official.game.character_spritesheet.get_sprite(14*TILE_SIZE, 6*TILE_SIZE, government_official.width, government_official.height)]
        return government_official

    @classmethod
    def Boss(cls, game, x, y):
        boss = cls(game, x, y)
        boss.name = 'Boss'
        boss.path = BOSS_PATH
        boss.speed = 8
        boss.move_goal_x = 11*TILE_SIZE
        boss.move_goal_y = 17*TILE_SIZE
        boss.facing = 'down'
        boss.width = 2 * TILE_SIZE
        boss.height = 2 * TILE_SIZE
        boss.image = boss.game.character_spritesheet.get_sprite(0 * TILE_SIZE, 8 * TILE_SIZE, boss.width, boss.height)
        boss.image_facing_down = boss.game.character_spritesheet.get_sprite(0 * TILE_SIZE, 8 * TILE_SIZE, boss.width,
                                                                          boss.height)
        boss.image_facing_up = boss.game.character_spritesheet.get_sprite(0 * TILE_SIZE, 10 * TILE_SIZE, boss.width,
                                                                        boss.height)
        boss.image_facing_left = boss.game.character_spritesheet.get_sprite(0 * TILE_SIZE, 12 * TILE_SIZE, boss.width,
                                                                          boss.height)
        boss.image_facing_right = boss.game.character_spritesheet.get_sprite(0 * TILE_SIZE, 14 * TILE_SIZE, boss.width,
                                                                           boss.height)
        boss.down_animation = [
            boss.game.character_spritesheet.get_sprite(0 * TILE_SIZE, 8 * TILE_SIZE, boss.width, boss.height),
            boss.game.character_spritesheet.get_sprite(2 * TILE_SIZE, 8 * TILE_SIZE, boss.width, boss.height),
            boss.game.character_spritesheet.get_sprite(4 * TILE_SIZE, 8 * TILE_SIZE, boss.width, boss.height),
            boss.game.character_spritesheet.get_sprite(6 * TILE_SIZE, 8 * TILE_SIZE, boss.width, boss.height)]

        boss.up_animation = [
            boss.game.character_spritesheet.get_sprite(0 * TILE_SIZE, 10 * TILE_SIZE, boss.width, boss.height),
            boss.game.character_spritesheet.get_sprite(2 * TILE_SIZE, 10 * TILE_SIZE, boss.width, boss.height),
            boss.game.character_spritesheet.get_sprite(4 * TILE_SIZE, 10 * TILE_SIZE, boss.width, boss.height),
            boss.game.character_spritesheet.get_sprite(6 * TILE_SIZE, 10 * TILE_SIZE, boss.width, boss.height)]

        boss.left_animation = [
            boss.game.character_spritesheet.get_sprite(0 * TILE_SIZE, 12 * TILE_SIZE, boss.width, boss.height),
            boss.game.character_spritesheet.get_sprite(2 * TILE_SIZE, 12 * TILE_SIZE, boss.width, boss.height),
            boss.game.character_spritesheet.get_sprite(4 * TILE_SIZE, 12 * TILE_SIZE, boss.width, boss.height),
            boss.game.character_spritesheet.get_sprite(6 * TILE_SIZE, 12 * TILE_SIZE, boss.width, boss.height)]

        boss.right_animation = [
            boss.game.character_spritesheet.get_sprite(0 * TILE_SIZE, 14 * TILE_SIZE, boss.width, boss.height),
            boss.game.character_spritesheet.get_sprite(2 * TILE_SIZE, 14 * TILE_SIZE, boss.width, boss.height),
            boss.game.character_spritesheet.get_sprite(4 * TILE_SIZE, 14 * TILE_SIZE, boss.width, boss.height),
            boss.game.character_spritesheet.get_sprite(6 * TILE_SIZE, 14 * TILE_SIZE, boss.width, boss.height)]
        return boss

    @classmethod
    def Guard(cls, game, x, y):
        guard = cls(game, x, y)
        guard.name = 'Guard'
        guard.path = GUARD_PATH
        guard.speed = 8
        guard.move_goal_x = 31 * TILE_SIZE
        guard.move_goal_y = 13 * TILE_SIZE
        guard.facing = 'up'
        guard.width = 2 * TILE_SIZE
        guard.height = 2 * TILE_SIZE
        guard.image = guard.game.character_spritesheet.get_sprite(8 * TILE_SIZE, 16 * TILE_SIZE, guard.width, guard.height)
        guard.image_facing_down = guard.game.character_spritesheet.get_sprite(8 * TILE_SIZE, 16 * TILE_SIZE, guard.width,
                                                                            guard.height)
        guard.image_facing_up = guard.game.character_spritesheet.get_sprite(8 * TILE_SIZE, 18 * TILE_SIZE, guard.width,
                                                                          guard.height)
        guard.image_facing_left = guard.game.character_spritesheet.get_sprite(8 * TILE_SIZE, 20 * TILE_SIZE, guard.width,
                                                                            guard.height)
        guard.image_facing_right = guard.game.character_spritesheet.get_sprite(8 * TILE_SIZE, 22 * TILE_SIZE, guard.width,
                                                                             guard.height)
        guard.down_animation = [
            guard.game.character_spritesheet.get_sprite(8 * TILE_SIZE, 16 * TILE_SIZE, guard.width, guard.height),
            guard.game.character_spritesheet.get_sprite(10 * TILE_SIZE, 16 * TILE_SIZE, guard.width, guard.height),
            guard.game.character_spritesheet.get_sprite(12 * TILE_SIZE, 16 * TILE_SIZE, guard.width, guard.height),
            guard.game.character_spritesheet.get_sprite(14 * TILE_SIZE, 16 * TILE_SIZE, guard.width, guard.height)]

        guard.up_animation = [
            guard.game.character_spritesheet.get_sprite(8 * TILE_SIZE, 18 * TILE_SIZE, guard.width, guard.height),
            guard.game.character_spritesheet.get_sprite(10 * TILE_SIZE, 18 * TILE_SIZE, guard.width, guard.height),
            guard.game.character_spritesheet.get_sprite(12 * TILE_SIZE, 18 * TILE_SIZE, guard.width, guard.height),
            guard.game.character_spritesheet.get_sprite(14 * TILE_SIZE, 18 * TILE_SIZE, guard.width, guard.height)]

        guard.left_animation = [
            guard.game.character_spritesheet.get_sprite(8 * TILE_SIZE, 20 * TILE_SIZE, guard.width, guard.height),
            guard.game.character_spritesheet.get_sprite(10 * TILE_SIZE, 20 * TILE_SIZE, guard.width, guard.height),
            guard.game.character_spritesheet.get_sprite(12 * TILE_SIZE, 20 * TILE_SIZE, guard.width, guard.height),
            guard.game.character_spritesheet.get_sprite(14 * TILE_SIZE, 20 * TILE_SIZE, guard.width, guard.height)]

        guard.right_animation = [
            guard.game.character_spritesheet.get_sprite(8 * TILE_SIZE, 22 * TILE_SIZE, guard.width, guard.height),
            guard.game.character_spritesheet.get_sprite(10 * TILE_SIZE, 22 * TILE_SIZE, guard.width, guard.height),
            guard.game.character_spritesheet.get_sprite(12 * TILE_SIZE, 22 * TILE_SIZE, guard.width, guard.height),
            guard.game.character_spritesheet.get_sprite(14 * TILE_SIZE, 22 * TILE_SIZE, guard.width, guard.height)]
        return guard

    @classmethod
    def Police(cls, game, x, y):
        police = cls(game, x, y)
        police.name = 'Poilce'
        police.path = None
        police.speed = 0
        police.move_goal_x = None
        police.move_goal_y = None
        police.facing = 'down'
        police.width = 2 * TILE_SIZE
        police.height = 2 * TILE_SIZE
        police.image = police.game.character_spritesheet.get_sprite(0 * TILE_SIZE, 16 * TILE_SIZE, police.width,
                                                                  police.height)
        police.image_facing_down = police.game.character_spritesheet.get_sprite(0 * TILE_SIZE, 16 * TILE_SIZE,
                                                                              police.width,
                                                                              police.height)
        police.image_facing_up = police.game.character_spritesheet.get_sprite(0 * TILE_SIZE, 18 * TILE_SIZE, police.width,
                                                                            police.height)
        police.image_facing_left = police.game.character_spritesheet.get_sprite(0 * TILE_SIZE, 20 * TILE_SIZE,
                                                                              police.width,
                                                                              police.height)
        police.image_facing_right = police.game.character_spritesheet.get_sprite(0 * TILE_SIZE, 22 * TILE_SIZE,
                                                                               police.width,
                                                                               police.height)
        police.down_animation = [
            police.game.character_spritesheet.get_sprite(0 * TILE_SIZE, 16 * TILE_SIZE, police.width, police.height),
            police.game.character_spritesheet.get_sprite(2 * TILE_SIZE, 16 * TILE_SIZE, police.width, police.height),
            police.game.character_spritesheet.get_sprite(4 * TILE_SIZE, 16 * TILE_SIZE, police.width, police.height),
            police.game.character_spritesheet.get_sprite(6 * TILE_SIZE, 16 * TILE_SIZE, police.width, police.height)]

        police.up_animation = [
            police.game.character_spritesheet.get_sprite(0 * TILE_SIZE, 18 * TILE_SIZE, police.width, police.height),
            police.game.character_spritesheet.get_sprite(2 * TILE_SIZE, 18 * TILE_SIZE, police.width, police.height),
            police.game.character_spritesheet.get_sprite(4 * TILE_SIZE, 18 * TILE_SIZE, police.width, police.height),
            police.game.character_spritesheet.get_sprite(6 * TILE_SIZE, 18 * TILE_SIZE, police.width, police.height)]

        police.left_animation = [
            police.game.character_spritesheet.get_sprite(0 * TILE_SIZE, 20 * TILE_SIZE, police.width, police.height),
            police.game.character_spritesheet.get_sprite(2 * TILE_SIZE, 20 * TILE_SIZE, police.width, police.height),
            police.game.character_spritesheet.get_sprite(4 * TILE_SIZE, 20 * TILE_SIZE, police.width, police.height),
            police.game.character_spritesheet.get_sprite(6 * TILE_SIZE, 20 * TILE_SIZE, police.width, police.height)]

        police.right_animation = [
            police.game.character_spritesheet.get_sprite(0 * TILE_SIZE, 22 * TILE_SIZE, police.width, police.height),
            police.game.character_spritesheet.get_sprite(2 * TILE_SIZE, 22 * TILE_SIZE, police.width, police.height),
            police.game.character_spritesheet.get_sprite(4 * TILE_SIZE, 22 * TILE_SIZE, police.width, police.height),
            police.game.character_spritesheet.get_sprite(6 * TILE_SIZE, 22 * TILE_SIZE, police.width, police.height)]
        return police

    @classmethod
    def Police2(cls, game, x, y):
        police = cls(game, x, y)
        police.name = 'Poilce2'
        police.path = None
        police.speed = 0
        police.move_goal_x = None
        police.move_goal_y = None
        police.facing = 'left'
        police.width = 2 * TILE_SIZE
        police.height = 2 * TILE_SIZE
        police.image = police.game.character_spritesheet.get_sprite(0 * TILE_SIZE, 16 * TILE_SIZE, police.width,
                                                                    police.height)
        police.image_facing_down = police.game.character_spritesheet.get_sprite(0 * TILE_SIZE, 16 * TILE_SIZE,
                                                                                police.width,
                                                                                police.height)
        police.image_facing_up = police.game.character_spritesheet.get_sprite(0 * TILE_SIZE, 18 * TILE_SIZE,
                                                                              police.width,
                                                                              police.height)
        police.image_facing_left = police.game.character_spritesheet.get_sprite(0 * TILE_SIZE, 20 * TILE_SIZE,
                                                                                police.width,
                                                                                police.height)
        police.image_facing_right = police.game.character_spritesheet.get_sprite(0 * TILE_SIZE, 22 * TILE_SIZE,
                                                                                 police.width,
                                                                                 police.height)
        police.down_animation = [
            police.game.character_spritesheet.get_sprite(0 * TILE_SIZE, 16 * TILE_SIZE, police.width, police.height),
            police.game.character_spritesheet.get_sprite(2 * TILE_SIZE, 16 * TILE_SIZE, police.width, police.height),
            police.game.character_spritesheet.get_sprite(4 * TILE_SIZE, 16 * TILE_SIZE, police.width, police.height),
            police.game.character_spritesheet.get_sprite(6 * TILE_SIZE, 16 * TILE_SIZE, police.width, police.height)]

        police.up_animation = [
            police.game.character_spritesheet.get_sprite(0 * TILE_SIZE, 18 * TILE_SIZE, police.width, police.height),
            police.game.character_spritesheet.get_sprite(2 * TILE_SIZE, 18 * TILE_SIZE, police.width, police.height),
            police.game.character_spritesheet.get_sprite(4 * TILE_SIZE, 18 * TILE_SIZE, police.width, police.height),
            police.game.character_spritesheet.get_sprite(6 * TILE_SIZE, 18 * TILE_SIZE, police.width, police.height)]

        police.left_animation = [
            police.game.character_spritesheet.get_sprite(0 * TILE_SIZE, 20 * TILE_SIZE, police.width, police.height),
            police.game.character_spritesheet.get_sprite(2 * TILE_SIZE, 20 * TILE_SIZE, police.width, police.height),
            police.game.character_spritesheet.get_sprite(4 * TILE_SIZE, 20 * TILE_SIZE, police.width, police.height),
            police.game.character_spritesheet.get_sprite(6 * TILE_SIZE, 20 * TILE_SIZE, police.width, police.height)]

        police.right_animation = [
            police.game.character_spritesheet.get_sprite(0 * TILE_SIZE, 22 * TILE_SIZE, police.width, police.height),
            police.game.character_spritesheet.get_sprite(2 * TILE_SIZE, 22 * TILE_SIZE, police.width, police.height),
            police.game.character_spritesheet.get_sprite(4 * TILE_SIZE, 22 * TILE_SIZE, police.width, police.height),
            police.game.character_spritesheet.get_sprite(6 * TILE_SIZE, 22 * TILE_SIZE, police.width, police.height)]
        return police

    @classmethod
    def Police3(cls, game, x, y):
        police = cls(game, x, y)
        police.name = 'Poilce3'
        police.path = None
        police.speed = 0
        police.move_goal_x = None
        police.move_goal_y = None
        police.facing = 'right'
        police.width = 2 * TILE_SIZE
        police.height = 2 * TILE_SIZE
        police.image = police.game.character_spritesheet.get_sprite(0 * TILE_SIZE, 16 * TILE_SIZE, police.width,
                                                                    police.height)
        police.image_facing_down = police.game.character_spritesheet.get_sprite(0 * TILE_SIZE, 16 * TILE_SIZE,
                                                                                police.width,
                                                                                police.height)
        police.image_facing_up = police.game.character_spritesheet.get_sprite(0 * TILE_SIZE, 18 * TILE_SIZE,
                                                                              police.width,
                                                                              police.height)
        police.image_facing_left = police.game.character_spritesheet.get_sprite(0 * TILE_SIZE, 20 * TILE_SIZE,
                                                                                police.width,
                                                                                police.height)
        police.image_facing_right = police.game.character_spritesheet.get_sprite(0 * TILE_SIZE, 22 * TILE_SIZE,
                                                                                 police.width,
                                                                                 police.height)
        police.down_animation = [
            police.game.character_spritesheet.get_sprite(0 * TILE_SIZE, 16 * TILE_SIZE, police.width, police.height),
            police.game.character_spritesheet.get_sprite(2 * TILE_SIZE, 16 * TILE_SIZE, police.width, police.height),
            police.game.character_spritesheet.get_sprite(4 * TILE_SIZE, 16 * TILE_SIZE, police.width, police.height),
            police.game.character_spritesheet.get_sprite(6 * TILE_SIZE, 16 * TILE_SIZE, police.width, police.height)]

        police.up_animation = [
            police.game.character_spritesheet.get_sprite(0 * TILE_SIZE, 18 * TILE_SIZE, police.width, police.height),
            police.game.character_spritesheet.get_sprite(2 * TILE_SIZE, 18 * TILE_SIZE, police.width, police.height),
            police.game.character_spritesheet.get_sprite(4 * TILE_SIZE, 18 * TILE_SIZE, police.width, police.height),
            police.game.character_spritesheet.get_sprite(6 * TILE_SIZE, 18 * TILE_SIZE, police.width, police.height)]

        police.left_animation = [
            police.game.character_spritesheet.get_sprite(0 * TILE_SIZE, 20 * TILE_SIZE, police.width, police.height),
            police.game.character_spritesheet.get_sprite(2 * TILE_SIZE, 20 * TILE_SIZE, police.width, police.height),
            police.game.character_spritesheet.get_sprite(4 * TILE_SIZE, 20 * TILE_SIZE, police.width, police.height),
            police.game.character_spritesheet.get_sprite(6 * TILE_SIZE, 20 * TILE_SIZE, police.width, police.height)]

        police.right_animation = [
            police.game.character_spritesheet.get_sprite(0 * TILE_SIZE, 22 * TILE_SIZE, police.width, police.height),
            police.game.character_spritesheet.get_sprite(2 * TILE_SIZE, 22 * TILE_SIZE, police.width, police.height),
            police.game.character_spritesheet.get_sprite(4 * TILE_SIZE, 22 * TILE_SIZE, police.width, police.height),
            police.game.character_spritesheet.get_sprite(6 * TILE_SIZE, 22 * TILE_SIZE, police.width, police.height)]
        return police


class NPCGroup:
    def __init__(self, game):
        self.NPCs_list = []
        self.game = game

    def generate_NPC(self, name, x, y):
        new_npc = None
        if name is None:
            return
        if name == 'Mom':
            new_npc = NPC.Mom(self.game, x, y)
        if name == 'Government official':
            new_npc = NPC.Government_official(self.game, x, y)
        if name == 'Boss':
            new_npc = NPC.Boss(self.game, x, y)
        if name == 'Guard':
            new_npc = NPC.Guard(self.game, x, y)
        if name == 'Police':
            new_npc = NPC.Police(self.game, x, y)
        if name == 'Police2':
            new_npc = NPC.Police2(self.game, x, y)
        if name == 'Police3':
            new_npc = NPC.Police3(self.game, x, y)

        self.NPCs_list.append(new_npc)

    def move_detection(self):
        for npc in self.NPCs_list:
            if self.game.scene_1_3_complete:
                if npc.name == 'Mom':
                    npc.moving = True
            if self.game.plots.plot_7_played and not self.game.plots.plot_8_1_played:
                if npc.name == 'Boss' or npc.name == 'Government official':
                    npc.moving = True
            for spot in self.game.dialogueSpots.in_used:
                if spot.name == 'guard' or spot.name == 'guard2':
                    if npc.name == 'Guard':
                        npc.moving = True

    def detect_scene_2_2(self):
        if not self.game.scene_2_2_complete:
            for npc1 in self.NPCs_list:
                if npc1.name == 'Boss':
                    for npc2 in self.NPCs_list:
                        if npc2.name == 'Government official':
                            hit = npc1.rect.colliderect(npc2.rect)
                            if hit:
                                for npc in self.NPCs_list:
                                    npc.moving = False
                                self.game.scene_2_2_complete = True
                                npc2.facing = 'up'

    def update(self):
        if self.game.scene_2_1_complete and not self.game.scene_2_2_complete:
            for npc in self.NPCs_list:
                if npc.name == 'Government official':
                    npc.facing = 'left'
            self.detect_scene_2_2()
        if self.game.scene_5_3_complete:
            for npc in self.NPCs_list:
                if npc.name == 'Government official':
                    npc.facing = 'right'
                if npc.name == 'Boss':
                    npc.facing = 'right'
        for npc in self.NPCs_list:
            npc.move()
            npc.animate()
            npc.rect.x += npc.x_change
            npc.rect.y += npc.y_change
            npc.x_change = 0
            npc.y_change = 0

    def draw(self, screen):
        for npc in self.NPCs_list:
            screen.blit(npc.image, npc.rect)


class Ground:   # 定義可路過的地板
    def __init__(self, game, x, y):
        # 遊戲開始設置地板的大小尺寸
        self.game = game
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        # 讀取地板素材
        self.image = self.game.terrain_spritesheet.get_sprite(0, 3*TILE_SIZE, self.width, self.height)
        # 讀取地板位置
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    @classmethod
    def grass(cls, game, x, y):
        grass = cls(game, x, y)
        grass.width = TILE_SIZE
        grass.height = TILE_SIZE
        grass.image = grass.game.terrain_spritesheet.get_sprite(3*TILE_SIZE, 6*TILE_SIZE, grass.width, grass.height)
        return grass

    @classmethod
    def road(cls, game, x, y):
        road = cls(game, x, y)
        road.width = TILE_SIZE
        road.height = TILE_SIZE
        road.image = road.game.terrain_spritesheet.get_sprite(0, 5*TILE_SIZE, road.width, road.height)
        return road

    @classmethod
    def cement(cls, game, x, y):
        cement = cls(game, x, y)
        cement.width = TILE_SIZE
        cement.height = TILE_SIZE
        cement.image = cement.game.terrain_spritesheet.get_sprite(TILE_SIZE, 3*TILE_SIZE, cement.width, cement.height)
        return cement

    @classmethod
    def grey(cls, game, x, y):
        grey = cls(game, x, y)
        grey.width = TILE_SIZE
        grey.height = TILE_SIZE
        grey.image = grey.game.terrain_spritesheet.get_sprite(5*TILE_SIZE, 0, grey.width, grey.height)
        return grey


class GroundGroup:
    def __init__(self, game):
        self.grounds_list = []  # 取得地板 List
        self.game = game

    def generate_ground(self, name, x, y):
        new_ground = None
        if name is None:
            return
        # 木頭地板
        if name == 'wood':
            new_ground = Ground(self.game, x, y)
        # 草地地板
        if name == 'grass':
            new_ground = Ground.grass(self.game, x, y)
        # 馬路地板
        if name == 'road':
            new_ground = Ground.road(self.game, x, y)
        if name == 'cement':
            new_ground = Ground.cement(self.game, x, y)
        if name == 'grey':
            new_ground = Ground.grey(self.game, x, y)
        # 將地板加入 List
        self.grounds_list.append(new_ground)

    def update(self):
        pass

    def draw(self, screen):
        for ground in self.grounds_list:
            screen.blit(ground.image, ground.rect)


class Block:
    def __init__(self, game, x, y):
        self.game = game
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.image = pygame.Surface((self.width, self.height))
        self.image.set_colorkey((0, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    @classmethod
    def wall(cls, game, x, y):
        wall = cls(game, x, y)
        wall.width = TILE_SIZE
        wall.height = TILE_SIZE
        wall.image = wall.game.terrain_spritesheet.get_sprite(0, 4*TILE_SIZE, wall.width, wall.height)
        return wall

    @classmethod
    def grey_wall(cls, game, x, y):
        grey_wall = cls(game, x, y)
        grey_wall.width = TILE_SIZE
        grey_wall.height = TILE_SIZE
        grey_wall.image = grey_wall.game.terrain_spritesheet.get_sprite(5 * TILE_SIZE, 0, grey_wall.width, grey_wall.height)
        return grey_wall

    @classmethod
    def blue_wall(cls, game, x, y):
        blue_wall = cls(game, x, y)
        blue_wall.width = TILE_SIZE
        blue_wall.height = TILE_SIZE
        blue_wall.image = blue_wall.game.terrain_spritesheet.get_sprite(128, 131, blue_wall.width,
                                                                        blue_wall.height)
        return blue_wall

    @classmethod
    def computer(cls, game, x, y):
        computer = cls(game, x, y)
        computer.width = 2 * TILE_SIZE
        computer.height = 2 * TILE_SIZE
        computer.image = computer.game.furniture_spritesheet.get_sprite(0, 0, 64, 64)
        return computer

    @classmethod
    def bed(cls, game, x, y):
        bed = cls(game, x, y)
        bed.width = 3 * TILE_SIZE
        bed.height = 5 * TILE_SIZE
        bed.image = pygame.transform.scale(bed.game.furniture_spritesheet.get_sprite(64, 0, 96, 160), (115, 192))
        return bed

    @classmethod
    def desk(cls, game, x, y):
        desk = cls(game, x, y)
        desk.width = 3 * TILE_SIZE
        desk.height = 2 * TILE_SIZE
        desk.image = desk.game.furniture_spritesheet.get_sprite(350, 0, 96, 64)
        return desk

    @classmethod
    def chair(cls, game, x, y):
        chair = cls(game, x, y)
        chair.width = 2 * TILE_SIZE
        chair.height = 2 * TILE_SIZE
        chair.image = chair.game.furniture_spritesheet.get_sprite(254, 160, 64, 64)
        return chair

    @classmethod
    def low_cabinet(cls, game, x, y):
        low_cabinet = cls(game, x, y)
        low_cabinet.width = 2 * TILE_SIZE
        low_cabinet.height = 2 * TILE_SIZE
        low_cabinet.image = low_cabinet.game.furniture_spritesheet.get_sprite(160, 96, 64, 64)
        return low_cabinet

    @classmethod
    def bookcase(cls, game, x, y):
        bookcase = cls(game, x, y)
        bookcase.width = 3 * TILE_SIZE
        bookcase.height = 4 * TILE_SIZE
        bookcase.image = bookcase.game.furniture_spritesheet.get_sprite(416, 64, 96, 128)
        return bookcase

    @classmethod
    def TV(cls, game, x, y):
        TV = cls(game, x, y)
        TV.width = 2 * TILE_SIZE
        TV.height = 2 * TILE_SIZE
        TV.image = TV.game.furniture_spritesheet.get_sprite(0, 130, 64, 64)
        return TV

    @classmethod
    def room_sofa(cls, game, x, y):
        room_sofa = cls(game, x, y)
        room_sofa.width = 6 * TILE_SIZE
        room_sofa.height = 6 * TILE_SIZE
        room_sofa.image = room_sofa.game.furniture_spritesheet.get_sprite(256, 368, 96, 64)
        return room_sofa

    @classmethod
    def tree(cls, game, x, y):
        tree = cls(game, x, y)
        tree.width = 1 * TILE_SIZE
        tree.height = 2 * TILE_SIZE
        tree.image = tree.game.furniture_spritesheet.get_sprite(160, 160, 32, 64)
        return tree

    @classmethod
    def rysofa(cls, game, x, y):
        rysofa = cls(game, x, y)
        rysofa.width = TILE_SIZE
        rysofa.height = TILE_SIZE
        rysofa.image = rysofa.game.furniture_spritesheet.get_sprite(0, 360, 64, 96)
        return rysofa

    @classmethod
    def lysofa(cls, game, x, y):
        lysofa = cls(game, x, y)
        lysofa.width = TILE_SIZE
        lysofa.height = TILE_SIZE
        lysofa.image = lysofa.game.furniture_spritesheet.get_sprite(189, 360, 64, 96)
        return lysofa

    @classmethod
    def bysofa(cls, game, x, y):
        bysofa = cls(game, x, y)
        bysofa.width = TILE_SIZE
        bysofa.height = TILE_SIZE
        bysofa.image = bysofa.game.furniture_spritesheet.get_sprite(256, 293, 96, 64)
        return bysofa

    @classmethod
    def cactus(cls, game, x, y):
        cactus = cls(game, x, y)
        cactus.width = TILE_SIZE
        cactus.height = TILE_SIZE
        cactus.image = cactus.game.furniture_spritesheet.get_sprite(128, 160, 32, 64)
        return cactus

    @classmethod
    def clock(cls, game, x, y):
        clock = cls(game, x, y)
        clock.width = TILE_SIZE
        clock.height = TILE_SIZE
        clock.image = clock.game.furniture_spritesheet.get_sprite(0, 64, 32, 32)
        return clock

    @classmethod
    def blackboard(cls, game, x, y):
        blackboard = cls(game, x, y)
        blackboard.width = 6 * TILE_SIZE
        blackboard.height = 3 * TILE_SIZE
        blackboard.image = blackboard.game.furniture_spritesheet.get_sprite(224, 64, blackboard.width, blackboard.height)
        return blackboard

    @classmethod
    def student_desk(cls, game, x, y):
        student_desk = cls(game, x, y)
        student_desk.width = 2 * TILE_SIZE
        student_desk.height = 2 *TILE_SIZE
        student_desk.image = student_desk.game.furniture_spritesheet.get_sprite(192, 160, student_desk.width, student_desk.height)
        return student_desk

    @classmethod
    def locker(cls, game, x, y):
        locker = cls(game, x, y)
        locker.width = TILE_SIZE
        locker.height = TILE_SIZE
        locker.image = pygame.transform.scale(locker.game.furniture_spritesheet.get_sprite(128, 192, locker.width, locker.height), (64, 64))
        return locker

    @classmethod
    def window(cls, game, x, y):
        window = cls(game, x, y)
        window.width = 4 * TILE_SIZE
        window.height = 2 * TILE_SIZE
        window.image = window.game.furniture_spritesheet.get_sprite(224, 0, window.width, window.height)
        return window

    @classmethod
    def police(cls, game, x, y):
        police = cls(game, x, y)
        police.width = 10 * TILE_SIZE
        police.height = 10 * TILE_SIZE
        police.image = police.game.street_spritesheet.get_sprite(320, 0, police.width, police.height)
        return police

    @classmethod
    def school(cls, game, x, y):
        school = cls(game, x, y)
        school.width = 10 * TILE_SIZE
        school.height = 10 * TILE_SIZE
        school.image = school.game.street_spritesheet.get_sprite(0, 0, school.width, school.height)
        return school

    @classmethod
    def tree_1(cls, game, x, y):
        tree_1 = cls(game, x, y)
        tree_1.width = 3 * TILE_SIZE
        tree_1.height = 3 * TILE_SIZE
        tree_1.image = tree_1.game.street_spritesheet.get_sprite(0, 17*TILE_SIZE, tree_1.width, tree_1.height)
        return tree_1

    @classmethod
    def tree_2(cls, game, x, y):
        tree_2 = cls(game, x, y)
        tree_2.width = 3 * TILE_SIZE
        tree_2.height = 3 * TILE_SIZE
        tree_2.image = tree_2.game.street_spritesheet.get_sprite(3*TILE_SIZE, 17*TILE_SIZE, tree_2.width, tree_2.height)
        return tree_2

    @classmethod
    def tree_3(cls, game, x, y):
        tree_3 = cls(game, x, y)
        tree_3.width = 3 * TILE_SIZE
        tree_3.height = 3 * TILE_SIZE
        tree_3.image = tree_3.game.street_spritesheet.get_sprite(6*TILE_SIZE, 17*TILE_SIZE, tree_3.width, tree_3.height)
        return tree_3

    @classmethod
    def home(cls, game, x, y):
        home = cls(game, x, y)
        home.width = 7 * TILE_SIZE
        home.height = 7 * TILE_SIZE
        home.image = home.game.street_spritesheet.get_sprite(640, 0, home.width, home.height)
        return home

    @classmethod
    def buildings(cls, game, x, y):
        buildings = cls(game, x, y)
        buildings.width = 14 * TILE_SIZE
        buildings.height = 7 * TILE_SIZE
        buildings.image = buildings.game.street_spritesheet.get_sprite(0, 320, buildings.width,  buildings.height)
        return buildings

    @classmethod
    def black(cls, game, x, y):
        black = cls(game, x, y)
        black.width = TILE_SIZE
        black.height = TILE_SIZE
        black.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        black.image.fill((0, 0, 0))
        return black

    @classmethod
    def roadblock(cls, game, x, y):
        roadblock = cls(game, x, y)
        roadblock.width = TILE_SIZE
        roadblock.height = TILE_SIZE
        roadblock.image = roadblock.game.street_spritesheet.get_sprite(0, 23*TILE_SIZE, roadblock.width,  roadblock.height)
        return roadblock

    @classmethod
    def mailbox(cls, game, x, y):
        mailbox = cls(game, x, y)
        mailbox.width = 3*TILE_SIZE
        mailbox.height = 3*TILE_SIZE
        mailbox.image = mailbox.game.street_spritesheet.get_sprite( 3*TILE_SIZE, 21*TILE_SIZE, mailbox.width,mailbox.height)
        return mailbox

    @classmethod
    def fence(cls, game, x, y):
        fence = cls(game, x, y)
        fence.width = 2 * TILE_SIZE
        fence.height = 2 * TILE_SIZE
        fence.image = fence.game.street_spritesheet.get_sprite(0, 21*TILE_SIZE, fence.width, fence.height)
        return fence


class BlockGroup:
    def __init__(self, game):
        self.blocks_list = []
        self.game = game

    def generate_block(self, name, x, y):
        new_block = None
        if name is None:
            return
        if name == 'block':
            new_block = Block(self.game, x, y)
        if name == 'wall':
            new_block = Block.wall(self.game, x, y)
        if name == 'grey wall':
            new_block = Block.grey_wall(self.game, x, y)
        if name == 'blue wall':
            new_block = Block.blue_wall(self.game, x, y)
        if name == 'computer':
            new_block = Block.computer(self.game, x, y)
        if name == 'bed':
            new_block = Block.bed(self.game, x, y)
        if name == 'desk':
            new_block = Block.desk(self.game, x, y)
        if name == 'chair':
            new_block = Block.chair(self.game, x, y)
        if name == 'low_cabinet':
            new_block = Block.low_cabinet(self.game, x, y)
        if name == 'bookcase':
            new_block = Block.bookcase(self.game, x, y)
        if name == 'TV':
            new_block = Block.TV(self.game, x, y)
        if name == 'room_sofa':
            new_block = Block.room_sofa(self.game, x, y)
        if name == 'tree':
            new_block = Block.tree(self.game, x, y)
        if name == 'rysofa':
            new_block = Block.rysofa(self.game, x, y)
        if name == 'lysofa':
            new_block = Block.lysofa(self.game, x, y)
        if name == 'bysofa':
            new_block = Block.bysofa(self.game, x, y)
        if name == 'cactus':
            new_block = Block.cactus(self.game, x, y)
        if name == 'clock':
            new_block = Block.clock(self.game, x, y)
        if name == 'blackboard':
            new_block = Block.blackboard(self.game, x, y)
        if name == 'student_desk':
            new_block = Block.student_desk(self.game, x, y)
        if name == 'locker':
            new_block = Block.locker(self.game, x, y)
        if name == 'window':
            new_block = Block.window(self.game, x, y)
        if name == 'black':
            new_block = Block.black(self.game, x, y)
        if name == 'police':
            new_block = Block.police(self.game, x, y)
        if name == 'school':
            new_block = Block.school(self.game, x, y)
        if name == 'tree_1':
            new_block = Block.tree_1(self.game, x, y)
        if name == 'tree_2':
            new_block = Block.tree_2(self.game, x, y)
        if name == 'tree_3':
            new_block = Block.tree_3(self.game, x, y)
        if name == 'home':
            new_block = Block.home(self.game, x, y)
        if name == 'buildings':
            new_block = Block.buildings(self.game, x, y)
        if name == 'roadblock':
            new_block = Block.roadblock(self.game, x, y)
        if name == 'mailbox':
            new_block = Block.mailbox(self.game, x, y)
        if name == 'fence':
            new_block = Block.fence(self.game, x, y)
        self.blocks_list.append(new_block)

    def update(self):
        pass

    def draw(self, screen):
        for block in self.blocks_list:
            screen.blit(block.image, block.rect)


class Arrow:
    def __init__(self):
        self.x = ARROW_X
        self.y = ARROW_Y
        self.width = ARROW_WIDTH
        self.height = ARROW_HEIGHT

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((0, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class ArrowGroup:
    def __init__(self, game):
        self.game = game
        self.arrows_list = []

    def generate_arrows(self):
        self.arrows_list.append(Arrow())

    def update(self):
        pass

    def draw(self, screen):
        for arrow in self.arrows_list:
            screen.blit(arrow.image, arrow.rect)


class TypeBox:
    def __init__(self, game, text):
        self.text = None

        self.is_typing_area = False

        self.game = game

        self.x = TYPE_BOX_X
        self.y = TYPE_BOX_Y

        self.width = TYPE_BOX_WIDTH
        self.height = TYPE_BOX_HEIGHT

        self.image = self.game.dialogue_frame.get_sprite(0, 200, 800, 200)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    @classmethod
    def title_box(cls, game, text):

        title_box = cls(game, text)

        title_box.text = text

        title_box.x = TITLE_TYPE_BOX_X
        title_box.y = TITLE_TYPE_BOX_Y
        title_box.width = TITLE_TYPE_BOX_WIDTH
        title_box.height = TITLE_TYPE_BOX_HEIGHT

        title_box.image = Font().get_image(title_box.text)

        title_box.rect = title_box.image.get_rect()
        title_box.rect.x = title_box.x
        title_box.rect.y = title_box.y
        return title_box

    @classmethod
    def subtitle_box(cls, game, text):
        subtitle_box = cls(game, text)

        subtitle_box.text = text

        subtitle_box.x = SUBTITLE_TYPE_BOX_X
        subtitle_box.y = SUBTITLE_TYPE_BOX_Y
        subtitle_box.width = SUBTITLE_TYPE_BOX_WIDTH
        subtitle_box.height = SUBTITLE_TYPE_BOX_HEIGHT

        subtitle_box.image = Font().get_image(subtitle_box.text)

        subtitle_box.rect = subtitle_box.image.get_rect()
        subtitle_box.rect.x = subtitle_box.x
        subtitle_box.rect.y = subtitle_box.y
        return subtitle_box

    @classmethod
    def typing_area(cls, game, text):
        typing_area = cls(game, text)
        typing_area.text = text
        typing_area.is_typing_area = True
        typing_area.x = TYPING_AREA_X
        typing_area.y = TYPING_AREA_Y
        typing_area.width = TYPING_AREA_WIDTH
        typing_area.height = TYPING_AREA_HEIGHT

        typing_area.image = Font().get_image(typing_area.text)

        typing_area.rect = typing_area.image.get_rect()
        typing_area.rect.x = typing_area.x
        typing_area.rect.y = typing_area.y
        return typing_area

    @classmethod
    def hint_box(cls, game, text):
        hint_box = cls(game, text)
        hint_box.text = text

        hint_box.x = HINT_BOX_X
        hint_box.y = HINT_BOX_TYPE_Y
        hint_box.width = HINT_BOX_WIDTH
        hint_box.height = HINT_BOX_HEIGHT

        hint_box.image = Font().get_image(hint_box.text)

        hint_box.rect = hint_box.image.get_rect()
        hint_box.rect.x = hint_box.x
        hint_box.rect.y = hint_box.y
        return hint_box


class TypeBoxGroup:
    def __init__(self, game):
        self.game = game
        self.typeBoxes_list = []
        self.generate = False
        self.generated = False
        self.delete = False

        self.is_typing = False
        self.hack_mail = False
        self.login_mail = False
        self.login_password = False
        self.user_input = ''
        self.account_correct = False
        self.got_mail_password = False
        self.mail_correct = False
        self.password_correct = False
        self.submitted = False

    def generate_box(self, name, text):
        new_box = None
        if name is None:
            return
        if name == 'box':
            new_box = TypeBox(self.game, text)
        if name == 'title box':
            new_box = TypeBox.title_box(self.game, text)
        if name == 'subtitle box':
            new_box = TypeBox.subtitle_box(self.game, text)
        if name == 'hint box':
            new_box = TypeBox.hint_box(self.game, text)
        if name == 'typing area':
            new_box = TypeBox.typing_area(self.game, text)
        self.typeBoxes_list.append(new_box)

    def generate_background(self):
        self.generate_box('box', None)
        self.generate_box('title box', ACCOUNT_TITLE)
        self.generate_box('subtitle box', ACCOUNT_SUBTITLE)
        self.generate_box('hint box', ACCOUNT_HINT)
        self.generate_box('typing area', None)

    def generate_login_mail(self):
        self.generate_box('box', None)
        self.generate_box('title box', LOGIN_MAIL_TITLE)
        self.generate_box('subtitle box', LOGIN_MAIL_SUBTITLE)
        self.generate_box('hint box', ACCOUNT_HINT)
        self.generate_box('typing area', None)

    def generate_login_password(self):
        self.generate_box('box', None)
        self.generate_box('title box', LOGIN_PASSWORD_TITLE)
        self.generate_box('subtitle box', LOGIN_PASSWORD_SUBTITLE)
        self.generate_box('hint box', ACCOUNT_HINT)
        self.generate_box('typing area', None)

    def generate_mail_correct(self):
        self.generate_box('box', None)
        self.generate_box('title box', MAIL_CORRECT_TITLE)
        self.generate_box('subtitle box', MAIL_CORRECT_SUBTITLE)
        self.generate_box('hint box', HINT)

    def generate_password_correct(self):
        self.generate_box('box', None)
        self.generate_box('title box', PASSWORD_CORRECT_TITLE)
        self.generate_box('subtitle box', PASSWORD_CORRECT_SUBTITLE)
        self.generate_box('hint box', HINT)

    def generate_password_incorrect(self):
        self.generate_box('box', None)
        self.generate_box('title box', PASSWORD_INCORRECT_TITLE)
        self.generate_box('subtitle box', PASSWORD_INCORRECT_SUBTITLE)
        self.generate_box('hint box', HINT)

    def generate_hacking_mail(self):
        self.generate_box('box', None)
        self.generate_box('title box', HACKING_MAIL_TITLE)
        self.generate_box('subtitle box', HACKING_MAIL_SUBTITLE)
        self.generate_box('hint box', ACCOUNT_HINT)
        self.generate_box('typing area', None)

    def generate_account_correct(self):
        self.generate_box('box', None)
        self.generate_box('title box', ACCOUNT_CORRECT_TITLE)
        self.generate_box('subtitle box', ACCOUNT_CORRECT_SUBTITLE)
        self.generate_box('hint box', HINT)

    def generate_account_incorrect(self):
        self.generate_box('box', None)
        self.generate_box('title box', ACCOUNT_INCORRECT_TITLE)
        self.generate_box('subtitle box', ACCOUNT_INCORRECT_SUBTITLE)
        self.generate_box('hint box', HINT)

    def generate_mail_password(self):
        self.generate_box('box', None)
        self.generate_box('title box', MAIL_PASSWORD_TITLE)
        self.generate_box('subtitle box', MAIL_PASSWORD_SUBTITLE)
        self.generate_box('hint box', HINT)

    def generate_mail_not_found(self):
        self.generate_box('box', None)
        self.generate_box('title box', MAIL_NOT_FOUND_TITLE)
        self.generate_box('subtitle box', MAIL_NOT_FOUND_SUBTITLE)
        self.generate_box('hint box', HINT)

    def refresh_typing_area(self):
        for typeBox in self.typeBoxes_list:
            if typeBox.is_typing_area:
                self.typeBoxes_list.pop(self.typeBoxes_list.index(typeBox))
                self.generate_box('typing area', self.user_input)

    def check_user_input(self):
        self.generate = False
        self.generated = False
        self.submitted = True
        if not self.game.scene_4_2_complete:
            if self.user_input == '9487666':
                self.user_input = ''
                self.account_correct = True
                self.generate_account_correct()
            else:
                self.user_input = ''
                self.generate_account_incorrect()
        elif self.hack_mail:
            if self.user_input == 'e94081018@gs.ncku.edu.tw':
                self.user_input = ''
                self.got_mail_password = True
                self.generate_mail_password()
            else:
                self.user_input = ''
                self.generate_mail_not_found()
        elif self.login_mail:
            if self.user_input == 'e94081018@gs.ncku.edu.tw':
                self.user_input = ''
                self.mail_correct = True
                self.generate_mail_correct()
            else:
                self.user_input = ''
                self.generate_mail_not_found()
        elif self.login_password:
            if self.user_input == '089487':
                self.user_input = ''
                self.password_correct = True
                self.generate_password_correct()
            else:
                self.user_input = ''
                self.generate_password_incorrect()


    def update(self):
        self.refresh_typing_area()
        if self.is_typing:
            if self.hack_mail:
                if self.generate and not self.generated:
                    self.generate_hacking_mail()
                    self.generate = False
                    self.generated = True
            elif self.login_mail:
                if self.generate and not self.generated:
                    self.generate_login_mail()
                    self.generate = False
                    self.generated = True
            elif self.login_password:
                if self.generate and not self.generated:
                    self.generate_login_password()
                    self.generate = False
                    self.generated = True
            else:
                if self.generate and not self.generated:
                    self.generate_background()
                    self.generate = False
                    self.generated = True

    def draw(self, screen):
        for typeBox in self.typeBoxes_list:
            screen.blit(typeBox.image, typeBox.rect)


class DialogueBox:
    def __init__(self, game, dialogueSpot):
        self.dialogueSpot = dialogueSpot
        self.text = None

        self.game = game

        self.x = DIALOGUE_BOX_X
        self.y = DIALOGUE_BOX_Y

        self.width = DIALOGUE_BOX_WIDTH
        self.height = DIALOGUE_BOX_HEIGHT

        self.image = self.game.dialogue_frame.get_sprite(800, 200, 800, 200)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    @classmethod
    def title_box(cls, game, dialogueSpot):

        title_box = cls(game, dialogueSpot)

        title_box.text = dialogueSpot[0].title

        title_box.x = TITLE_BOX_X
        title_box.y = TITLE_BOX_Y
        title_box.width = TITLE_BOX_WIDTH
        title_box.height = TITLE_BOX_HEIGHT

        title_box.image = Font().get_image(title_box.text)

        title_box.rect = title_box.image.get_rect()
        title_box.rect.x = title_box.x
        title_box.rect.y = title_box.y
        return title_box

    @classmethod
    def choice_one_box(cls, game, dialogueSpot):

        choice_one_box = cls(game, dialogueSpot)
        choice_one_box.text = dialogueSpot[0].first_choice

        choice_one_box.x = CHOICE_ONE_BOX_X
        choice_one_box.y = CHOICE_ONE_BOX_Y
        choice_one_box.width = CHOICE_ONE_BOX_WIDTH
        choice_one_box.height = CHOICE_ONE_BOX_HEIGHT

        choice_one_box.image = Font().get_image(choice_one_box.text)


        choice_one_box.rect = choice_one_box.image.get_rect()
        choice_one_box.rect.x = choice_one_box.x
        choice_one_box.rect.y = choice_one_box.y

        return choice_one_box

    @classmethod
    def choice_two_box(cls, game, dialogueSpot):

        choice_two_box = cls(game, dialogueSpot)
        choice_two_box.text = dialogueSpot[0].second_choice


        choice_two_box.x = CHOICE_TWO_BOX_X
        choice_two_box.y = CHOICE_TWO_BOX_Y
        choice_two_box.width = CHOICE_TWO_BOX_WIDTH
        choice_two_box.height = CHOICE_TWO_BOX_HEIGHT

        choice_two_box.image = choice_two_box.image = Font().get_image(choice_two_box.text)

        choice_two_box.rect = choice_two_box.image.get_rect()
        choice_two_box.rect.x = choice_two_box.x
        choice_two_box.rect.y = choice_two_box.y
        return choice_two_box

    @classmethod
    def choice_three_box(cls, game, dialogueSpot):

        choice_three_box = cls(game, dialogueSpot)
        choice_three_box.text = dialogueSpot[0].third_choice

        choice_three_box.x = CHOICE_THREE_BOX_X
        choice_three_box.y = CHOICE_THREE_BOX_Y
        choice_three_box.width = CHOICE_THREE_BOX_WIDTH
        choice_three_box.height = CHOICE_THREE_BOX_HEIGHT

        choice_three_box.image = choice_three_box.image = Font().get_image(choice_three_box.text)

        choice_three_box.rect = choice_three_box.image.get_rect()
        choice_three_box.rect.x = choice_three_box.x
        choice_three_box.rect.y = choice_three_box.y
        return choice_three_box

    @classmethod
    def choice_four_box(cls, game, dialogueSpot):

        choice_four_box = cls(game, dialogueSpot)
        choice_four_box.text = dialogueSpot[0].fourth_choice

        choice_four_box.x = CHOICE_FOUR_BOX_X
        choice_four_box.y = CHOICE_FOUR_BOX_Y
        choice_four_box.width = CHOICE_FOUR_BOX_WIDTH
        choice_four_box.height = CHOICE_FOUR_BOX_HEIGHT

        choice_four_box.image = choice_four_box.image = Font().get_image(choice_four_box.text)

        choice_four_box.rect = choice_four_box.image.get_rect()
        choice_four_box.rect.x = choice_four_box.x
        choice_four_box.rect.y = choice_four_box.y
        return choice_four_box

    @classmethod
    def text_box(cls, game, dialogueSpot):
        text_box = cls(game, dialogueSpot)
        text_box.text = dialogueSpot[0].text

        text_box.x = TEXT_BOX_X
        text_box.y = TEXT_BOX_Y
        text_box.width = TEXT_BOX_WIDTH
        text_box.height = TEXT_BOX_HEIGHT

        text_box.image = Font().get_image(text_box.text)

        text_box.rect = text_box.image.get_rect()
        text_box.rect.x = text_box.x
        text_box.rect.y = text_box.y
        return text_box


class DialogueBoxGroup:
    def __init__(self, game):
        self.game = game
        self.dialogueBoxes_list = []
        self.dialogueSpot = game.dialogueSpots.in_used
        self.generate = False
        self.generated = False
        self.delete = False
        self.counter = 0
        self.first_choice = 0
        self.second_choice = 0
        self.third_choice = 0

        self.news_1 = self.game.news_1.get_sprite(0, 0, 600, 480)
        self.news_2 = self.game.news_2.get_sprite(0, 0, 600, 480)
        self.password_hint = self.game.password_hint.get_sprite(0, 0, 600, 480)
        self.password_paper = self.game.password_paper.get_sprite(0, 0, 600, 480)
        self.mail = self.game.mail.get_sprite(0, 0, 600, 480)
        self.displaying = False
        self.image_displaying = []

    def generate_box(self, name):
        new_box = None
        if name is None:
            return
        if name == 'box':
            new_box = DialogueBox(self.game, self.dialogueSpot)
        if name == 'title box':
            new_box = DialogueBox.title_box(self.game, self.dialogueSpot)
        if name == 'choice one box':
            new_box = DialogueBox.choice_one_box(self.game, self.dialogueSpot)
        if name == 'choice two box':
            new_box = DialogueBox.choice_two_box(self.game, self.dialogueSpot)
        if name == 'choice three box':
            new_box = DialogueBox.choice_three_box(self.game, self.dialogueSpot)
        if name == 'choice four box':
            new_box = DialogueBox.choice_four_box(self.game, self.dialogueSpot)
        self.dialogueBoxes_list.append(new_box)

    def generate_four_choice(self):
        self.generate_box('box')
        self.generate_box('title box')
        self.generate_box('choice one box')
        self.generate_box('choice two box')
        self.generate_box('choice three box')
        self.generate_box('choice four box')

    def detect_choice(self):
        for arrow in self.game.arrows.arrows_list:
            if arrow.rect.y == ARROW_CHOOSE_ONE_Y:
                return "1"
            if arrow.rect.y == ARROW_CHOOSE_TWO_Y:
                return "2"
            if arrow.rect.y == ARROW_CHOOSE_THREE_Y:
                return "3"
            if arrow.rect.y == ARROW_CHOOSE_FOUR_Y:
                return "4"

    def detect_end(self, choice):
        if choice == "1":
            if self.counter == 0:
                self.first_choice = 1
                return self.dialogueSpot[0].first_choice_end
            if self.counter == 1:
                self.second_choice = 1
                if self.first_choice == 1:
                    return self.dialogueSpot[0].first_choice_1_end
                if self.first_choice == 2:
                    return self.dialogueSpot[0].first_choice_2_end
                if self.first_choice == 3:
                    return self.dialogueSpot[0].first_choice_3_end
                if self.first_choice == 4:
                    return self.dialogueSpot[0].first_choice_4_end
            if self.counter == 2:
                if self.first_choice == 1:
                    if self.second_choice == 1:
                        return self.dialogueSpot[0].first_choice_1_1_end
                    if self.second_choice == 2:
                        return self.dialogueSpot[0].first_choice_1_2_end
                    if self.second_choice == 3:
                        return self.dialogueSpot[0].first_choice_1_3_end
                    if self.second_choice == 4:
                        return self.dialogueSpot[0].first_choice_1_4_end
                if self.first_choice == 2:
                    if self.second_choice == 1:
                        return self.dialogueSpot[0].first_choice_2_1_end
                    if self.second_choice == 2:
                        return self.dialogueSpot[0].first_choice_2_2_end
                    if self.second_choice == 3:
                        return self.dialogueSpot[0].first_choice_2_3_end
                    if self.second_choice == 4:
                        return self.dialogueSpot[0].first_choice_2_4_end
                if self.first_choice == 3:
                    if self.second_choice == 1:
                        return self.dialogueSpot[0].first_choice_3_1_end
                    if self.second_choice == 2:
                        return self.dialogueSpot[0].first_choice_3_2_end
                    if self.second_choice == 3:
                        return self.dialogueSpot[0].first_choice_3_3_end
                    if self.second_choice == 4:
                        return self.dialogueSpot[0].first_choice_3_4_end
                if self.first_choice == 4:
                    if self.second_choice == 1:
                        return self.dialogueSpot[0].first_choice_4_1_end
                    if self.second_choice == 2:
                        return self.dialogueSpot[0].first_choice_4_2_end
                    if self.second_choice == 3:
                        return self.dialogueSpot[0].first_choice_4_3_end
                    if self.second_choice == 4:
                        return self.dialogueSpot[0].first_choice_4_4_end
        if choice == "2":
            if self.counter == 0:
                self.first_choice = 2
                return self.dialogueSpot[0].second_choice_end
            if self.counter == 1:
                self.second_choice = 2
                if self.first_choice == 1:
                    return self.dialogueSpot[0].second_choice_1_end
                if self.first_choice == 2:
                    return self.dialogueSpot[0].second_choice_2_end
                if self.first_choice == 3:
                    return self.dialogueSpot[0].second_choice_3_end
                if self.first_choice == 4:
                    return self.dialogueSpot[0].second_choice_4_end
            if self.counter == 2:
                if self.first_choice == 1:
                    if self.second_choice == 1:
                        return self.dialogueSpot[0].second_choice_1_1_end
                    if self.second_choice == 2:
                        return self.dialogueSpot[0].second_choice_1_2_end
                    if self.second_choice == 3:
                        return self.dialogueSpot[0].second_choice_1_3_end
                    if self.second_choice == 4:
                        return self.dialogueSpot[0].second_choice_1_4_end
                if self.first_choice == 2:
                    if self.second_choice == 1:
                        return self.dialogueSpot[0].second_choice_2_1_end
                    if self.second_choice == 2:
                        return self.dialogueSpot[0].second_choice_2_2_end
                    if self.second_choice == 3:
                        return self.dialogueSpot[0].second_choice_2_3_end
                    if self.second_choice == 4:
                        return self.dialogueSpot[0].second_choice_2_4_end
                if self.first_choice == 3:
                    if self.second_choice == 1:
                        return self.dialogueSpot[0].second_choice_3_1_end
                    if self.second_choice == 2:
                        return self.dialogueSpot[0].second_choice_3_2_end
                    if self.second_choice == 3:
                        return self.dialogueSpot[0].second_choice_3_3_end
                    if self.second_choice == 4:
                        return self.dialogueSpot[0].second_choice_3_4_end
                if self.first_choice == 4:
                    if self.second_choice == 1:
                        return self.dialogueSpot[0].second_choice_4_1_end
                    if self.second_choice == 2:
                        return self.dialogueSpot[0].second_choice_4_2_end
                    if self.second_choice == 3:
                        return self.dialogueSpot[0].second_choice_4_3_end
                    if self.second_choice == 4:
                        return self.dialogueSpot[0].second_choice_4_4_end
        if choice == "3":
            if self.counter == 0:
                self.first_choice = 3
                return self.dialogueSpot[0].third_choice_end
            if self.counter == 1:
                self.second_choice = 3
                if self.first_choice == 1:
                    return self.dialogueSpot[0].third_choice_1_end
                if self.first_choice == 2:
                    return self.dialogueSpot[0].third_choice_2_end
                if self.first_choice == 3:
                    return self.dialogueSpot[0].third_choice_3_end
                if self.first_choice == 4:
                    return self.dialogueSpot[0].third_choice_4_end
            if self.counter == 2:
                if self.first_choice == 1:
                    if self.second_choice == 1:
                        return self.dialogueSpot[0].third_choice_1_1_end
                    if self.second_choice == 2:
                        return self.dialogueSpot[0].third_choice_1_2_end
                    if self.second_choice == 3:
                        return self.dialogueSpot[0].third_choice_1_3_end
                    if self.second_choice == 4:
                        return self.dialogueSpot[0].third_choice_1_4_end
                if self.first_choice == 2:
                    if self.second_choice == 1:
                        return self.dialogueSpot[0].third_choice_2_1_end
                    if self.second_choice == 2:
                        return self.dialogueSpot[0].third_choice_2_2_end
                    if self.second_choice == 3:
                        return self.dialogueSpot[0].third_choice_2_3_end
                    if self.second_choice == 4:
                        return self.dialogueSpot[0].third_choice_2_4_end
                if self.first_choice == 3:
                    if self.second_choice == 1:
                        return self.dialogueSpot[0].third_choice_3_1_end
                    if self.second_choice == 2:
                        return self.dialogueSpot[0].third_choice_3_2_end
                    if self.second_choice == 3:
                        return self.dialogueSpot[0].third_choice_3_3_end
                    if self.second_choice == 4:
                        return self.dialogueSpot[0].third_choice_3_4_end
                if self.first_choice == 4:
                    if self.second_choice == 1:
                        return self.dialogueSpot[0].third_choice_4_1_end
                    if self.second_choice == 2:
                        return self.dialogueSpot[0].third_choice_4_2_end
                    if self.second_choice == 3:
                        return self.dialogueSpot[0].third_choice_4_3_end
                    if self.second_choice == 4:
                        return self.dialogueSpot[0].third_choice_4_4_end
        if choice == "4":

            if self.counter == 0:
                self.first_choice = 4
                return self.dialogueSpot[0].fourth_choice_end
            if self.counter == 1:
                self.second_choice = 4
                if self.first_choice == 1:
                    return self.dialogueSpot[0].fourth_choice_1_end
                if self.first_choice == 2:
                    return self.dialogueSpot[0].fourth_choice_2_end
                if self.first_choice == 3:
                    return self.dialogueSpot[0].fourth_choice_3_end
                if self.first_choice == 4:
                    return self.dialogueSpot[0].fourth_choice_4_end
            if self.counter == 2:
                if self.first_choice == 1:
                    if self.second_choice == 1:
                        return self.dialogueSpot[0].fourth_choice_1_1_end
                    if self.second_choice == 2:
                        return self.dialogueSpot[0].fourth_choice_1_2_end
                    if self.second_choice == 3:
                        return self.dialogueSpot[0].fourth_choice_1_3_end
                    if self.second_choice == 4:
                        return self.dialogueSpot[0].fourth_choice_1_4_end
                if self.first_choice == 2:
                    if self.second_choice == 1:
                        return self.dialogueSpot[0].fourth_choice_2_1_end
                    if self.second_choice == 2:
                        return self.dialogueSpot[0].fourth_choice_2_2_end
                    if self.second_choice == 3:
                        return self.dialogueSpot[0].fourth_choice_2_3_end
                    if self.second_choice == 4:
                        return self.dialogueSpot[0].fourth_choice_2_4_end
                if self.first_choice == 3:
                    if self.second_choice == 1:
                        return self.dialogueSpot[0].fourth_choice_3_1_end
                    if self.second_choice == 2:
                        return self.dialogueSpot[0].fourth_choice_3_2_end
                    if self.second_choice == 3:
                        return self.dialogueSpot[0].fourth_choice_3_3_end
                    if self.second_choice == 4:
                        return self.dialogueSpot[0].fourth_choice_3_4_end
                if self.first_choice == 4:
                    if self.second_choice == 1:
                        return self.dialogueSpot[0].fourth_choice_4_1_end
                    if self.second_choice == 2:
                        return self.dialogueSpot[0].fourth_choice_4_2_end
                    if self.second_choice == 3:
                        return self.dialogueSpot[0].fourth_choice_4_3_end
                    if self.second_choice == 4:
                        return self.dialogueSpot[0].fourth_choice_4_4_end

    def detect_scene_5(self, choice):
        if self.dialogueSpot[0].first_choice == POLICE2_first_choice:
            if choice == "1" :
                self.game.scene_5_complete = True
                return True
            else:
                return False
    def detect_scene_1_2(self, choice):
        if self.dialogueSpot[0].title == COMPUTER_title_3_1:
            if choice == "1" or choice == "2":
                return True
            else:
                return False
        else:
            return False

    def detect_scene_5_2(self, choice):
        if self.dialogueSpot[0].first_choice == COMPUTER7_first_choice_2:
            if choice == "1":
                return True

    def detect_scene_4_2(self, choice):
        if self.dialogueSpot[0].second_choice == GUARD2_second_choice:
            if choice == "2":
                self.game.scene_4_2_complete = True

    def detect_scene_1_3(self):
        if self.dialogueSpot[0].title == MOM2_title_3:
            return True
        else:
            return False

    def detect_scene_3_1(self, choice):
        if self.dialogueSpot[0].first_choice == COMPUTER2_first_choice_3_2 and choice == "1":
            return True
        else:
            return False

    def detect_hacking_mail(self, choice):
        if self.dialogueSpot[0].first_choice == COMPUTER5_first_choice_4_3 and choice == "1":
            return True
        else:
            return False

    def detect_login_mail(self, choice):
        if self.dialogueSpot[0].first_choice == COMPUTER6_first_choice_2 and choice == "1":
            return True
        else:
            return False

    def detect_scene_3(self, choice):
        if self.dialogueSpot[0].first_choice == COMPUTER3_first_choice_3_2 and choice == "1":
            return True
        if self.dialogueSpot[0].first_choice == COMPUTER3_first_choice_3_2 and choice == "2":
            return True
        else:
            return False

    def detect_hack_tool(self, choice):
        if self.dialogueSpot[0].first_choice == COMPUTER2_first_choice_4 and choice == "1":
            return True
        if self.dialogueSpot[0].first_choice == COMPUTER2_first_choice_4 and choice == "2":
            return True
        else:
            return False

    def end_by_get_money(self, choice):
        self.counter = 0
        self.first_choice = 0
        self.second_choice = 0
        self.third_choice = 0
        self.game.dialogueSpots.in_dialogue = False
        self.generated = False
        self.delete = True
        if choice == "1":
            self.game.scene_3_complete = True
        if choice == "2":
            self.game.plots.to_play_not_get_money = True

    def end_by_mom_run(self):
        self.counter = 0
        self.first_choice = 0
        self.second_choice = 0
        self.third_choice = 0
        self.game.dialogueSpots.in_dialogue = False
        self.generated = False
        self.delete = True
        self.game.scene_1_3_complete = True
        self.game.NPCs.move_detection()

    def get_news(self, choice):
        if choice == "1":
            news = self.news_1
            self.game.scene_1_2_complete = True
            return news
        if choice == "2":
            news = self.news_2
            if self.game.scene_3_complete:
                self.game.scene_4_1_complete = True
            return news

    def get_password_hint_or_password_paper(self, choice):
        if choice == "2":
            image = self.password_hint
            return image
        if choice == "1":
            image = self.password_paper
            return image

    def end_by_news(self):
        self.image_displaying.append(self.get_news(self.detect_choice()))
        self.displaying = True
        self.counter = 0
        self.first_choice = 0
        self.second_choice = 0
        self.third_choice = 0
        self.generated = False
        self.delete = True

    def end_by_password_hint(self):
        self.image_displaying.append(self.get_password_hint_or_password_paper(self.detect_choice()))
        self.displaying = True
        self.counter = 0
        self.first_choice = 0
        self.second_choice = 0
        self.third_choice = 0
        self.generated = False
        self.delete = True

    def end_by_check_mail(self):
        self.image_displaying.append(self.mail)
        self.displaying = True
        self.counter = 0
        self.first_choice = 0
        self.second_choice = 0
        self.third_choice = 0
        self.generated = False
        self.delete = True
        pygame.mixer.music.load(self.game.scene_4_music)
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
        self.game.scene_5_2_complete = True
    def dialogue_end(self):
        self.game.dialogueSpots.in_dialogue = False
        self.first_choice = 0
        self.second_choice = 0
        self.third_choice = 0
        self.generated = False
        self.delete = True

    def next_dialogue(self, choice):
        self.counter += 1
        self.dialogueSpot[0].next_dialogue(choice)
        self.dialogueBoxes_list.clear()
        self.generate_four_choice()

    def draw(self, screen):
        for dialogueBox in self.dialogueBoxes_list:
            screen.blit(dialogueBox.image, dialogueBox.rect)
        for image in self.image_displaying:
            screen.blit(image, (340, 160))

    def update(self):

        if not self.game.dialogueSpots.in_dialogue:
            self.counter = 0

        if self.generate and not self.generated:
            self.generate_four_choice()
            self.game.arrows.generate_arrows()
            self.generate = False
            self.generated = True

        if self.delete:
            self.dialogueBoxes_list.clear()
            self.game.arrows.arrows_list.clear()
            self.delete = False


class DialogueSpot:
    def __init__(self, game, x, y):

        self.game = game

        self.name = None

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.image = pygame.Surface((self.width, self.height))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.counter = 0

        self.title = None
        self.first_choice = None
        self.second_choice = None
        self.third_choice = None
        self.fourth_choice = None

        self.first_choice_end = None
        self.second_choice_end = None
        self.third_choice_end = None
        self.fourth_choice_end = None

        self.first_choice_1_end = None
        self.second_choice_1_end = None
        self.third_choice_1_end = None
        self.fourth_choice_1_end = None

        self.first_choice_1_1_end = None
        self.first_choice_1_2_end = None
        self.first_choice_1_3_end = None
        self.first_choice_1_4_end = None

        self.second_choice_1_1_end = None
        self.second_choice_1_2_end = None
        self.second_choice_1_3_end = None
        self.second_choice_1_4_end = None

        self.third_choice_1_1_end = None
        self.third_choice_1_2_end = None
        self.third_choice_1_3_end = None
        self.third_choice_1_4_end = None

        self.fourth_choice_1_1_end = None
        self.fourth_choice_1_2_end = None
        self.fourth_choice_1_3_end = None
        self.fourth_choice_1_4_end = None

        self.first_choice_2_end = None
        self.second_choice_2_end = None
        self.third_choice_2_end = None
        self.fourth_choice_2_end = None

        self.first_choice_2_1_end = None
        self.first_choice_2_2_end = None
        self.first_choice_2_3_end = None
        self.first_choice_2_4_end = None

        self.second_choice_2_1_end = None
        self.second_choice_2_2_end = None
        self.second_choice_2_3_end = None
        self.second_choice_2_4_end = None

        self.third_choice_2_1_end = None
        self.third_choice_2_2_end = None
        self.third_choice_2_3_end = None
        self.third_choice_2_4_end = None

        self.fourth_choice_2_1_end = None
        self.fourth_choice_2_2_end = None
        self.fourth_choice_2_3_end = None
        self.fourth_choice_2_4_end = None


        self.first_choice_3_end = None
        self.second_choice_3_end = None
        self.third_choice_3_end = None
        self.fourth_choice_3_end = None

        self.first_choice_3_1_end = None
        self.first_choice_3_2_end = None
        self.first_choice_3_3_end = None
        self.first_choice_3_4_end = None

        self.second_choice_3_1_end = None
        self.second_choice_3_2_end = None
        self.second_choice_3_3_end = None
        self.second_choice_3_4_end = None

        self.third_choice_3_1_end = None
        self.third_choice_3_2_end = None
        self.third_choice_3_3_end = None
        self.third_choice_3_4_end = None

        self.fourth_choice_3_1_end = None
        self.fourth_choice_3_2_end = None
        self.fourth_choice_3_3_end = None
        self.fourth_choice_3_4_end = None

        self.first_choice_4_end = None
        self.second_choice_4_end = None
        self.third_choice_4_end = None
        self.fourth_choice_4_end = None

        self.first_choice_4_1_end = None
        self.first_choice_4_2_end = None
        self.first_choice_4_3_end = None
        self.first_choice_4_4_end = None

        self.second_choice_4_1_end = None
        self.second_choice_4_2_end = None
        self.second_choice_4_3_end = None
        self.second_choice_4_4_end = None

        self.third_choice_4_1_end = None
        self.third_choice_4_2_end = None
        self.third_choice_4_3_end = None
        self.third_choice_4_4_end = None

        self.fourth_choice_4_1_end = None
        self.fourth_choice_4_2_end = None
        self.fourth_choice_4_3_end = None
        self.fourth_choice_4_4_end = None

        self.title_1 = None
        self.first_choice_1 = None
        self.second_choice_1 = None
        self.third_choice_1 = None
        self.fourth_choice_1 = None

        self.title_1_1 = None
        self.first_choice_1_1 = None
        self.second_choice_1_1 = None
        self.third_choice_1_1 = None
        self.fourth_choice_1_1 = None

        self.title_1_2 = None
        self.first_choice_1_2 = None
        self.second_choice_1_2 = None
        self.third_choice_1_2 = None
        self.fourth_choice_1_2 = None

        self.title_1_3 = None
        self.first_choice_1_3 = None
        self.second_choice_1_3 = None
        self.third_choice_1_3 = None
        self.fourth_choice_1_3 = None

        self.title_1_4 = None
        self.first_choice_1_4 = None
        self.second_choice_1_4 = None
        self.third_choice_1_4 = None
        self.fourth_choice_1_4 = None

        self.title_2 = None
        self.first_choice_2 = None
        self.second_choice_2 = None
        self.third_choice_2 = None
        self.fourth_choice_2 = None

        self.title_2_1 = None
        self.first_choice_2_1 = None
        self.second_choice_2_1 = None
        self.third_choice_2_1 = None
        self.fourth_choice_2_1 = None

        self.title_2_2 = None
        self.first_choice_2_2 = None
        self.second_choice_2_2 = None
        self.third_choice_2_2 = None
        self.fourth_choice_2_2 = None

        self.title_2_3 = None
        self.first_choice_2_3 = None
        self.second_choice_2_3 = None
        self.third_choice_2_3 = None
        self.fourth_choice_2_3 = None

        self.title_2_4 = None
        self.first_choice_2_4 = None
        self.second_choice_2_4 = None
        self.third_choice_2_4 = None
        self.fourth_choice_2_4 = None

        self.title_3 = None
        self.first_choice_3 = None
        self.second_choice_3 = None
        self.third_choice_3 = None
        self.fourth_choice_3 = None

        self.title_3_1 = None
        self.first_choice_3_1 = None
        self.second_choice_3_1 = None
        self.third_choice_3_1 = None
        self.fourth_choice_3_1 = None

        self.title_3_2 = None
        self.first_choice_3_2 = None
        self.second_choice_3_2 = None
        self.third_choice_3_2 = None
        self.fourth_choice_3_2 = None

        self.title_3_3 = None
        self.first_choice_3_3 = None
        self.second_choice_3_3 = None
        self.third_choice_3_3 = None
        self.fourth_choice_3_3 = None

        self.title_3_4 = None
        self.first_choice_3_4 = None
        self.second_choice_3_4 = None
        self.third_choice_3_4 = None
        self.fourth_choice_3_4 = None

        self.title_4 = None
        self.first_choice_4 = None
        self.second_choice_4 = None
        self.third_choice_4 = None
        self.fourth_choice_4 = None

        self.title_4_1 = None
        self.first_choice_4_1 = None
        self.second_choice_4_1 = None
        self.third_choice_4_1 = None
        self.fourth_choice_4_1 = None

        self.title_4_2 = None
        self.first_choice_4_2 = None
        self.second_choice_4_2 = None
        self.third_choice_4_2 = None
        self.fourth_choice_4_2 = None

        self.title_4_3 = None
        self.first_choice_4_3 = None
        self.second_choice_4_3 = None
        self.third_choice_4_3 = None
        self.fourth_choice_4_3 = None

        self.title_4_4 = None
        self.first_choice_4_4 = None
        self.second_choice_4_4 = None
        self.third_choice_4_4 = None
        self.fourth_choice_4_4 = None

    def next_dialogue(self, choice):
        if choice == "1":
            self.player_choose_one()
        if choice == "2":
            self.player_choose_two()
        if choice == "3":
            self.player_choose_three()
        if choice == "4":
            self.player_choose_four()

    def player_choose_one(self):
        if self.game.dialogueBoxes.counter == 1:
            self.title = self.title_1
            self.first_choice = self.first_choice_1
            self.second_choice = self.second_choice_1
            self.third_choice = self.third_choice_1
            self.fourth_choice = self.fourth_choice_1
        if self.game.dialogueBoxes.counter == 2:
            if self.game.dialogueBoxes.first_choice == 2:
                self.title = self.title_1_1
                self.first_choice = self.first_choice_1_1
                self.second_choice = self.second_choice_1_1
                self.third_choice = self.third_choice_1_1
                self.fourth_choice = self.fourth_choice_1_1
            if self.game.dialogueBoxes.first_choice == 2:
                self.title = self.title_2_1
                self.first_choice = self.first_choice_2_1
                self.second_choice = self.second_choice_2_1
                self.third_choice = self.third_choice_2_1
                self.fourth_choice = self.fourth_choice_2_1
            if self.game.dialogueBoxes.first_choice == 3:
                self.title = self.title_3_1
                self.first_choice = self.first_choice_3_1
                self.second_choice = self.second_choice_3_1
                self.third_choice = self.third_choice_3_1
                self.fourth_choice = self.fourth_choice_3_1
            if self.game.dialogueBoxes.first_choice == 4:
                self.title = self.title_4_1
                self.first_choice = self.first_choice_4_1
                self.second_choice = self.second_choice_4_1
                self.third_choice = self.third_choice_4_1
                self.fourth_choice = self.fourth_choice_4_1

    def player_choose_two(self):
        if self.game.dialogueBoxes.counter == 1:
            self.title = self.title_2
            self.first_choice = self.first_choice_2
            self.second_choice = self.second_choice_2
            self.third_choice = self.third_choice_2
            self.fourth_choice = self.fourth_choice_2
        if self.game.dialogueBoxes.counter == 2:
            if self.game.dialogueBoxes.first_choice == 1:
                self.title = self.title_1_2
                self.first_choice = self.first_choice_1_2
                self.second_choice = self.second_choice_1_2
                self.third_choice = self.third_choice_1_2
                self.fourth_choice = self.fourth_choice_1_2
            if self.game.dialogueBoxes.first_choice == 2:
                self.title = self.title_2_2
                self.first_choice = self.first_choice_2_2
                self.second_choice = self.second_choice_2_2
                self.third_choice = self.third_choice_2_2
                self.fourth_choice = self.fourth_choice_2_2
            if self.game.dialogueBoxes.first_choice == 3:
                self.title = self.title_3_2
                self.first_choice = self.first_choice_3_2
                self.second_choice = self.second_choice_3_2
                self.third_choice = self.third_choice_3_2
                self.fourth_choice = self.fourth_choice_3_2
            if self.game.dialogueBoxes.first_choice == 4:
                self.title = self.title_4_2
                self.first_choice = self.first_choice_4_2
                self.second_choice = self.second_choice_4_2
                self.third_choice = self.third_choice_4_2
                self.fourth_choice = self.fourth_choice_4_2

    def player_choose_three(self):
        if self.game.dialogueBoxes.counter == 1:
            self.title = self.title_3
            self.first_choice = self.first_choice_3
            self.second_choice = self.second_choice_3
            self.third_choice = self.third_choice_3
            self.fourth_choice = self.fourth_choice_3
        if self.game.dialogueBoxes.counter == 2:
            if self.game.dialogueBoxes.first_choice == 1:
                self.title = self.title_1_3
                self.first_choice = self.first_choice_1_3
                self.second_choice = self.second_choice_1_3
                self.third_choice = self.third_choice_1_3
                self.fourth_choice = self.fourth_choice_1_3
            if self.game.dialogueBoxes.first_choice == 2:
                self.title = self.title_2_3
                self.first_choice = self.first_choice_2_3
                self.second_choice = self.second_choice_2_3
                self.third_choice = self.third_choice_2_3
                self.fourth_choice = self.fourth_choice_2_3
            if self.game.dialogueBoxes.first_choice == 3:
                self.title = self.title_3_3
                self.first_choice = self.first_choice_3_3
                self.second_choice = self.second_choice_3_3
                self.third_choice = self.third_choice_3_3
                self.fourth_choice = self.fourth_choice_3_3
            if self.game.dialogueBoxes.first_choice == 4:
                self.title = self.title_4_3
                self.first_choice = self.first_choice_4_3
                self.second_choice = self.second_choice_4_3
                self.third_choice = self.third_choice_4_3
                self.fourth_choice = self.fourth_choice_4_3

    def player_choose_four(self):
        if self.game.dialogueBoxes.counter == 1:
            self.title = self.title_4
            self.first_choice = self.first_choice_4
            self.second_choice = self.second_choice_4
            self.third_choice = self.third_choice_4
            self.fourth_choice = self.fourth_choice_4
        if self.game.dialogueBoxes.counter == 2:
            if self.game.dialogueBoxes.first_choice == 1:
                self.title = self.title_1_4
                self.first_choice = self.first_choice_1_4
                self.second_choice = self.second_choice_1_4
                self.third_choice = self.third_choice_1_4
                self.fourth_choice = self.fourth_choice_1_4
            if self.game.dialogueBoxes.first_choice == 2:
                self.title = self.title_2_4
                self.first_choice = self.first_choice_2_4
                self.second_choice = self.second_choice_2_4
                self.third_choice = self.third_choice_2_4
                self.fourth_choice = self.fourth_choice_2_4
            if self.game.dialogueBoxes.first_choice == 3:
                self.title = self.title_3_4
                self.first_choice = self.first_choice_3_4
                self.second_choice = self.second_choice_3_4
                self.third_choice = self.third_choice_3_4
                self.fourth_choice = self.fourth_choice_3_4
            if self.game.dialogueBoxes.first_choice == 4:
                self.title = self.title_4_4
                self.first_choice = self.first_choice_4_4
                self.second_choice = self.second_choice_4_4
                self.third_choice = self.third_choice_4_4
                self.fourth_choice = self.fourth_choice_4_4

    @classmethod
    def computer(cls, game, x, y):
        computer = cls(game, x, y)
        computer.width = TILE_SIZE
        computer.height = TILE_SIZE

        computer.title = COMPUTER_title
        computer.first_choice = COMPUTER_first_choice
        computer.second_choice = COMPUTER_second_choice
        computer.third_choice = COMPUTER_third_choice
        computer.fourth_choice = COMPUTER_fourth_choice

        computer.title_1 = COMPUTER_title_1
        computer.first_choice_1 = COMPUTER_first_choice_1
        computer.second_choice_1 = COMPUTER_second_choice_1
        computer.third_choice_1 = COMPUTER_third_choice_1
        computer.fourth_choice_1 = COMPUTER_fourth_choice_1

        computer.title_2 = COMPUTER_title_2
        computer.first_choice_2 = COMPUTER_first_choice_2
        computer.second_choice_2 = COMPUTER_second_choice_2
        computer.third_choice_2 = COMPUTER_third_choice_2
        computer.fourth_choice_2 = COMPUTER_fourth_choice_2

        computer.title_3 = COMPUTER_title_3
        computer.first_choice_3 = COMPUTER_first_choice_3
        computer.second_choice_3 = COMPUTER_second_choice_3
        computer.third_choice_3 = COMPUTER_third_choice_3
        computer.fourth_choice_3 = COMPUTER_fourth_choice_3

        computer.title_3_1 = COMPUTER_title_3_1
        computer.first_choice_3_1 = COMPUTER_first_choice_3_1
        computer.second_choice_3_1 = COMPUTER_second_choice_3_1
        computer.third_choice_3_1 = COMPUTER_third_choice_3_1
        computer.fourth_choice_3_1 = COMPUTER_fourth_choice_3_1

        computer.title_3_2 = COMPUTER_title_3_2
        computer.first_choice_3_2 = COMPUTER_first_choice_3_2
        computer.second_choice_3_2 = COMPUTER_second_choice_3_2
        computer.third_choice_3_2 = COMPUTER_third_choice_3_2
        computer.fourth_choice_3_2 = COMPUTER_fourth_choice_3_2

        computer.title_4 = COMPUTER_title_4
        computer.first_choice_4 = COMPUTER_first_choice_4
        computer.second_choice_4 = COMPUTER_second_choice_4
        computer.third_choice_4 = COMPUTER_third_choice_4
        computer.fourth_choice_4 = COMPUTER_fourth_choice_4

        computer.first_choice_end = False
        computer.second_choice_end = False
        computer.third_choice_end = False
        computer.fourth_choice_end = False

        computer.first_choice_1_end = True
        computer.second_choice_1_end = True
        computer.third_choice_1_end = True
        computer.fourth_choice_1_end = True

        computer.first_choice_2_end = True
        computer.second_choice_2_end = True
        computer.third_choice_2_end = True
        computer.fourth_choice_2_end = True

        computer.first_choice_3_end = False
        computer.second_choice_3_end = False
        computer.third_choice_3_end = True
        computer.fourth_choice_3_end = True

        computer.first_choice_3_1_end = True
        computer.second_choice_3_1_end = True
        computer.third_choice_3_1_end = True
        computer.fourth_choice_3_1_end = True

        computer.first_choice_3_2_end = True
        computer.second_choice_3_2_end = True
        computer.third_choice_3_2_end = True
        computer.fourth_choice_3_2_end = True

        computer.first_choice_4_end = True
        computer.second_choice_4_end = True
        computer.third_choice_4_end = True
        computer.fourth_choice_4_end = True

        computer.image = pygame.Surface((computer.width, computer.height))
        computer.image.set_colorkey((0, 0, 0))

        return computer

    @classmethod
    def computer2(cls, game, x, y):
        computer2 = cls(game, x, y)
        computer2.width = TILE_SIZE
        computer2.height = TILE_SIZE

        computer2.title = COMPUTER_title
        computer2.first_choice = COMPUTER_first_choice
        computer2.second_choice = COMPUTER_second_choice
        computer2.third_choice = COMPUTER_third_choice
        computer2.fourth_choice = COMPUTER_fourth_choice

        computer2.title_1 = COMPUTER_title_1
        computer2.first_choice_1 = COMPUTER_first_choice_1
        computer2.second_choice_1 = COMPUTER_second_choice_1
        computer2.third_choice_1 = COMPUTER_third_choice_1
        computer2.fourth_choice_1 = COMPUTER_fourth_choice_1

        computer2.title_2 = COMPUTER_title_2
        computer2.first_choice_2 = COMPUTER_first_choice_2
        computer2.second_choice_2 = COMPUTER_second_choice_2
        computer2.third_choice_2 = COMPUTER_third_choice_2
        computer2.fourth_choice_2 = COMPUTER_fourth_choice_2

        computer2.title_3 = COMPUTER_title_3
        computer2.first_choice_3 = COMPUTER_first_choice_3
        computer2.second_choice_3 = COMPUTER_second_choice_3
        computer2.third_choice_3 = COMPUTER_third_choice_3
        computer2.fourth_choice_3 = COMPUTER_fourth_choice_3

        computer2.title_3_1 = COMPUTER_title_3_1
        computer2.first_choice_3_1 = COMPUTER_first_choice_3_1
        computer2.second_choice_3_1 = COMPUTER_second_choice_3_1
        computer2.third_choice_3_1 = COMPUTER_third_choice_3_1
        computer2.fourth_choice_3_1 = COMPUTER_fourth_choice_3_1

        computer2.title_3_2 = COMPUTER_title_3_2
        computer2.first_choice_3_2 = COMPUTER2_first_choice_3_2
        computer2.second_choice_3_2 = COMPUTER_second_choice_3_2
        computer2.third_choice_3_2 = COMPUTER_third_choice_3_2
        computer2.fourth_choice_3_2 = COMPUTER_fourth_choice_3_2

        computer2.title_4 = COMPUTER_title_4
        computer2.first_choice_4 = COMPUTER2_first_choice_4
        computer2.second_choice_4 = COMPUTER2_second_choice_4
        computer2.third_choice_4 = COMPUTER2_third_choice_4
        computer2.fourth_choice_4 = COMPUTER_fourth_choice_4

        computer2.title_4_3 = COMPUTER2_title_4_3
        computer2.first_choice_4_3 = COMPUTER2_first_choice_4_3
        computer2.second_choice_4_3 = COMPUTER2_second_choice_4_3
        computer2.third_choice_4_3 = COMPUTER2_third_choice_4_3
        computer2.fourth_choice_4_3 = COMPUTER2_fourth_choice_4_3

        computer2.first_choice_end = False
        computer2.second_choice_end = False
        computer2.third_choice_end = False
        computer2.fourth_choice_end = False

        computer2.first_choice_1_end = True
        computer2.second_choice_1_end = True
        computer2.third_choice_1_end = True
        computer2.fourth_choice_1_end = True

        computer2.first_choice_2_end = True
        computer2.second_choice_2_end = True
        computer2.third_choice_2_end = True
        computer2.fourth_choice_2_end = True

        computer2.first_choice_3_end = False
        computer2.second_choice_3_end = False
        computer2.third_choice_3_end = True
        computer2.fourth_choice_3_end = True

        computer2.first_choice_3_1_end = True
        computer2.second_choice_3_1_end = True
        computer2.third_choice_3_1_end = True
        computer2.fourth_choice_3_1_end = True

        computer2.first_choice_3_2_end = True
        computer2.second_choice_3_2_end = True
        computer2.third_choice_3_2_end = True
        computer2.fourth_choice_3_2_end = True

        computer2.first_choice_4_end = True
        computer2.second_choice_4_end = True
        computer2.third_choice_4_end = False
        computer2.fourth_choice_4_end = True

        computer2.first_choice_4_3_end = True
        computer2.second_choice_4_3_end = True
        computer2.third_choice_4_3_end = True
        computer2.fourth_choice_4_3_end = True

        computer2.image = pygame.Surface((computer2.width, computer2.height))
        computer2.image.set_colorkey((0, 0, 0))

        return computer2

    @classmethod
    def computer3(cls, game, x, y):
        computer3 = cls(game, x, y)
        computer3.width = TILE_SIZE
        computer3.height = TILE_SIZE

        computer3.title = COMPUTER_title
        computer3.first_choice = COMPUTER_first_choice
        computer3.second_choice = COMPUTER_second_choice
        computer3.third_choice = COMPUTER_third_choice
        computer3.fourth_choice = COMPUTER_fourth_choice

        computer3.title_1 = COMPUTER_title_1
        computer3.first_choice_1 = COMPUTER_first_choice_1
        computer3.second_choice_1 = COMPUTER_second_choice_1
        computer3.third_choice_1 = COMPUTER_third_choice_1
        computer3.fourth_choice_1 = COMPUTER_fourth_choice_1

        computer3.title_2 = COMPUTER_title_2
        computer3.first_choice_2 = COMPUTER_first_choice_2
        computer3.second_choice_2 = COMPUTER_second_choice_2
        computer3.third_choice_2 = COMPUTER_third_choice_2
        computer3.fourth_choice_2 = COMPUTER_fourth_choice_2

        computer3.title_3 = COMPUTER_title_3
        computer3.first_choice_3 = COMPUTER_first_choice_3
        computer3.second_choice_3 = COMPUTER_second_choice_3
        computer3.third_choice_3 = COMPUTER_third_choice_3
        computer3.fourth_choice_3 = COMPUTER_fourth_choice_3

        computer3.title_3_1 = COMPUTER_title_3_1
        computer3.first_choice_3_1 = COMPUTER_first_choice_3_1
        computer3.second_choice_3_1 = COMPUTER_second_choice_3_1
        computer3.third_choice_3_1 = COMPUTER_third_choice_3_1
        computer3.fourth_choice_3_1 = COMPUTER_fourth_choice_3_1

        computer3.title_3_2 = COMPUTER3_title_3_2
        computer3.first_choice_3_2 = COMPUTER3_first_choice_3_2
        computer3.second_choice_3_2 = COMPUTER3_second_choice_3_2
        computer3.third_choice_3_2 = COMPUTER_third_choice_3_2
        computer3.fourth_choice_3_2 = COMPUTER_fourth_choice_3_2

        computer3.title_4 = COMPUTER_title_4
        computer3.first_choice_4 = COMPUTER2_first_choice_4
        computer3.second_choice_4 = COMPUTER2_second_choice_4
        computer3.third_choice_4 = COMPUTER2_third_choice_4
        computer3.fourth_choice_4 = COMPUTER_fourth_choice_4

        computer3.title_4_3 = COMPUTER2_title_4_3
        computer3.first_choice_4_3 = COMPUTER2_first_choice_4_3
        computer3.second_choice_4_3 = COMPUTER2_second_choice_4_3
        computer3.third_choice_4_3 = COMPUTER2_third_choice_4_3
        computer3.fourth_choice_4_3 = COMPUTER2_fourth_choice_4_3

        computer3.first_choice_end = False
        computer3.second_choice_end = False
        computer3.third_choice_end = False
        computer3.fourth_choice_end = False

        computer3.first_choice_1_end = True
        computer3.second_choice_1_end = True
        computer3.third_choice_1_end = True
        computer3.fourth_choice_1_end = True

        computer3.first_choice_2_end = True
        computer3.second_choice_2_end = True
        computer3.third_choice_2_end = True
        computer3.fourth_choice_2_end = True

        computer3.first_choice_3_end = False
        computer3.second_choice_3_end = False
        computer3.third_choice_3_end = True
        computer3.fourth_choice_3_end = True

        computer3.first_choice_3_1_end = True
        computer3.second_choice_3_1_end = True
        computer3.third_choice_3_1_end = True
        computer3.fourth_choice_3_1_end = True

        computer3.first_choice_3_2_end = True
        computer3.second_choice_3_2_end = True
        computer3.third_choice_3_2_end = True
        computer3.fourth_choice_3_2_end = True

        computer3.first_choice_4_end = True
        computer3.second_choice_4_end = True
        computer3.third_choice_4_end = False
        computer3.fourth_choice_4_end = True

        computer3.first_choice_4_3_end = True
        computer3.second_choice_4_3_end = True
        computer3.third_choice_4_3_end = True
        computer3.fourth_choice_4_3_end = True

        computer3.image = pygame.Surface((computer3.width, computer3.height))
        computer3.image.set_colorkey((0, 0, 0))

        return computer3

    @classmethod
    def computer4(cls, game, x, y):
        computer4 = cls(game, x, y)
        computer4.width = TILE_SIZE
        computer4.height = TILE_SIZE

        computer4.title = COMPUTER_title
        computer4.first_choice = COMPUTER_first_choice
        computer4.second_choice = COMPUTER_second_choice
        computer4.third_choice = COMPUTER_third_choice
        computer4.fourth_choice = COMPUTER_fourth_choice

        computer4.title_1 = COMPUTER_title_1
        computer4.first_choice_1 = COMPUTER_first_choice_1
        computer4.second_choice_1 = COMPUTER_second_choice_1
        computer4.third_choice_1 = COMPUTER_third_choice_1
        computer4.fourth_choice_1 = COMPUTER_fourth_choice_1

        computer4.title_2 = COMPUTER_title_2
        computer4.first_choice_2 = COMPUTER_first_choice_2
        computer4.second_choice_2 = COMPUTER_second_choice_2
        computer4.third_choice_2 = COMPUTER_third_choice_2
        computer4.fourth_choice_2 = COMPUTER_fourth_choice_2

        computer4.title_3 = COMPUTER_title_3
        computer4.first_choice_3 = COMPUTER_first_choice_3
        computer4.second_choice_3 = COMPUTER_second_choice_3
        computer4.third_choice_3 = COMPUTER_third_choice_3
        computer4.fourth_choice_3 = COMPUTER_fourth_choice_3

        computer4.title_3_1 = COMPUTER_title_3_1
        computer4.first_choice_3_1 = COMPUTER_first_choice_3_1
        computer4.second_choice_3_1 = COMPUTER_second_choice_3_1
        computer4.third_choice_3_1 = COMPUTER_third_choice_3_1
        computer4.fourth_choice_3_1 = COMPUTER_fourth_choice_3_1

        computer4.title_3_2 = COMPUTER3_title_3_2
        computer4.first_choice_3_2 = COMPUTER4_first_choice_3_2
        computer4.second_choice_3_2 = COMPUTER_second_choice_3_2
        computer4.third_choice_3_2 = COMPUTER_third_choice_3_2
        computer4.fourth_choice_3_2 = COMPUTER_fourth_choice_3_2

        computer4.title_4 = COMPUTER_title_4
        computer4.first_choice_4 = COMPUTER2_first_choice_4
        computer4.second_choice_4 = COMPUTER2_second_choice_4
        computer4.third_choice_4 = COMPUTER2_third_choice_4
        computer4.fourth_choice_4 = COMPUTER_fourth_choice_4

        computer4.title_4_3 = COMPUTER2_title_4_3
        computer4.first_choice_4_3 = COMPUTER2_first_choice_4_3
        computer4.second_choice_4_3 = COMPUTER2_second_choice_4_3
        computer4.third_choice_4_3 = COMPUTER2_third_choice_4_3
        computer4.fourth_choice_4_3 = COMPUTER2_fourth_choice_4_3

        computer4.first_choice_end = False
        computer4.second_choice_end = False
        computer4.third_choice_end = False
        computer4.fourth_choice_end = False

        computer4.first_choice_1_end = True
        computer4.second_choice_1_end = True
        computer4.third_choice_1_end = True
        computer4.fourth_choice_1_end = True

        computer4.first_choice_2_end = True
        computer4.second_choice_2_end = True
        computer4.third_choice_2_end = True
        computer4.fourth_choice_2_end = True

        computer4.first_choice_3_end = False
        computer4.second_choice_3_end = False
        computer4.third_choice_3_end = True
        computer4.fourth_choice_3_end = True

        computer4.first_choice_3_1_end = True
        computer4.second_choice_3_1_end = True
        computer4.third_choice_3_1_end = True
        computer4.fourth_choice_3_1_end = True

        computer4.first_choice_3_2_end = True
        computer4.second_choice_3_2_end = True
        computer4.third_choice_3_2_end = True
        computer4.fourth_choice_3_2_end = True

        computer4.first_choice_4_end = True
        computer4.second_choice_4_end = True
        computer4.third_choice_4_end = False
        computer4.fourth_choice_4_end = True

        computer4.first_choice_4_3_end = True
        computer4.second_choice_4_3_end = True
        computer4.third_choice_4_3_end = True
        computer4.fourth_choice_4_3_end = True

        computer4.image = pygame.Surface((computer4.width, computer4.height))
        computer4.image.set_colorkey((0, 0, 0))

        return computer4

    @classmethod
    def computer5(cls, game, x, y):
        computer5 = cls(game, x, y)
        computer5.width = TILE_SIZE
        computer5.height = TILE_SIZE

        computer5.title = COMPUTER_title
        computer5.first_choice = COMPUTER_first_choice
        computer5.second_choice = COMPUTER_second_choice
        computer5.third_choice = COMPUTER_third_choice
        computer5.fourth_choice = COMPUTER_fourth_choice

        computer5.title_1 = COMPUTER_title_1
        computer5.first_choice_1 = COMPUTER_first_choice_1
        computer5.second_choice_1 = COMPUTER_second_choice_1
        computer5.third_choice_1 = COMPUTER_third_choice_1
        computer5.fourth_choice_1 = COMPUTER_fourth_choice_1

        computer5.title_2 = COMPUTER_title_2
        computer5.first_choice_2 = COMPUTER_first_choice_2
        computer5.second_choice_2 = COMPUTER_second_choice_2
        computer5.third_choice_2 = COMPUTER_third_choice_2
        computer5.fourth_choice_2 = COMPUTER_fourth_choice_2

        computer5.title_3 = COMPUTER_title_3
        computer5.first_choice_3 = COMPUTER_first_choice_3
        computer5.second_choice_3 = COMPUTER_second_choice_3
        computer5.third_choice_3 = COMPUTER_third_choice_3
        computer5.fourth_choice_3 = COMPUTER_fourth_choice_3

        computer5.title_3_1 = COMPUTER_title_3_1
        computer5.first_choice_3_1 = COMPUTER_first_choice_3_1
        computer5.second_choice_3_1 = COMPUTER_second_choice_3_1
        computer5.third_choice_3_1 = COMPUTER_third_choice_3_1
        computer5.fourth_choice_3_1 = COMPUTER_fourth_choice_3_1

        computer5.title_3_2 = COMPUTER3_title_3_2
        computer5.first_choice_3_2 = COMPUTER4_first_choice_3_2
        computer5.second_choice_3_2 = COMPUTER_second_choice_3_2
        computer5.third_choice_3_2 = COMPUTER_third_choice_3_2
        computer5.fourth_choice_3_2 = COMPUTER_fourth_choice_3_2

        computer5.title_4 = COMPUTER_title_4
        computer5.first_choice_4 = COMPUTER2_first_choice_4
        computer5.second_choice_4 = COMPUTER2_second_choice_4
        computer5.third_choice_4 = COMPUTER2_third_choice_4
        computer5.fourth_choice_4 = COMPUTER_fourth_choice_4

        computer5.title_4_3 = COMPUTER5_title_4_3
        computer5.first_choice_4_3 = COMPUTER5_first_choice_4_3
        computer5.second_choice_4_3 = COMPUTER5_second_choice_4_3
        computer5.third_choice_4_3 = COMPUTER5_third_choice_4_3
        computer5.fourth_choice_4_3 = COMPUTER5_fourth_choice_4_3

        computer5.first_choice_end = False
        computer5.second_choice_end = False
        computer5.third_choice_end = False
        computer5.fourth_choice_end = False

        computer5.first_choice_1_end = True
        computer5.second_choice_1_end = True
        computer5.third_choice_1_end = True
        computer5.fourth_choice_1_end = True

        computer5.first_choice_2_end = True
        computer5.second_choice_2_end = True
        computer5.third_choice_2_end = True
        computer5.fourth_choice_2_end = True

        computer5.first_choice_3_end = False
        computer5.second_choice_3_end = False
        computer5.third_choice_3_end = True
        computer5.fourth_choice_3_end = True

        computer5.first_choice_3_1_end = True
        computer5.second_choice_3_1_end = True
        computer5.third_choice_3_1_end = True
        computer5.fourth_choice_3_1_end = True

        computer5.first_choice_3_2_end = True
        computer5.second_choice_3_2_end = True
        computer5.third_choice_3_2_end = True
        computer5.fourth_choice_3_2_end = True

        computer5.first_choice_4_end = True
        computer5.second_choice_4_end = True
        computer5.third_choice_4_end = False
        computer5.fourth_choice_4_end = True

        computer5.first_choice_4_3_end = True
        computer5.second_choice_4_3_end = True
        computer5.third_choice_4_3_end = True
        computer5.fourth_choice_4_3_end = True

        computer5.image = pygame.Surface((computer5.width, computer5.height))
        computer5.image.set_colorkey((0, 0, 0))

        return computer5

    @classmethod
    def computer6(cls, game, x, y):
        computer6 = cls(game, x, y)
        computer6.width = TILE_SIZE
        computer6.height = TILE_SIZE

        computer6.title = COMPUTER_title
        computer6.first_choice = COMPUTER_first_choice
        computer6.second_choice = COMPUTER_second_choice
        computer6.third_choice = COMPUTER_third_choice
        computer6.fourth_choice = COMPUTER_fourth_choice

        computer6.title_1 = COMPUTER_title_1
        computer6.first_choice_1 = COMPUTER_first_choice_1
        computer6.second_choice_1 = COMPUTER_second_choice_1
        computer6.third_choice_1 = COMPUTER_third_choice_1
        computer6.fourth_choice_1 = COMPUTER_fourth_choice_1

        computer6.title_2 = COMPUTER_title_2
        computer6.first_choice_2 = COMPUTER6_first_choice_2
        computer6.second_choice_2 = COMPUTER6_second_choice_2
        computer6.third_choice_2 = COMPUTER_third_choice_2
        computer6.fourth_choice_2 = COMPUTER_fourth_choice_2

        computer6.title_3 = COMPUTER_title_3
        computer6.first_choice_3 = COMPUTER_first_choice_3
        computer6.second_choice_3 = COMPUTER_second_choice_3
        computer6.third_choice_3 = COMPUTER_third_choice_3
        computer6.fourth_choice_3 = COMPUTER_fourth_choice_3

        computer6.title_3_1 = COMPUTER_title_3_1
        computer6.first_choice_3_1 = COMPUTER_first_choice_3_1
        computer6.second_choice_3_1 = COMPUTER_second_choice_3_1
        computer6.third_choice_3_1 = COMPUTER_third_choice_3_1
        computer6.fourth_choice_3_1 = COMPUTER_fourth_choice_3_1

        computer6.title_3_2 = COMPUTER3_title_3_2
        computer6.first_choice_3_2 = COMPUTER4_first_choice_3_2
        computer6.second_choice_3_2 = COMPUTER_second_choice_3_2
        computer6.third_choice_3_2 = COMPUTER_third_choice_3_2
        computer6.fourth_choice_3_2 = COMPUTER_fourth_choice_3_2

        computer6.title_4 = COMPUTER_title_4
        computer6.first_choice_4 = COMPUTER2_first_choice_4
        computer6.second_choice_4 = COMPUTER2_second_choice_4
        computer6.third_choice_4 = COMPUTER2_third_choice_4
        computer6.fourth_choice_4 = COMPUTER_fourth_choice_4

        computer6.title_4_3 = COMPUTER5_title_4_3
        computer6.first_choice_4_3 = COMPUTER5_first_choice_4_3
        computer6.second_choice_4_3 = COMPUTER5_second_choice_4_3
        computer6.third_choice_4_3 = COMPUTER5_third_choice_4_3
        computer6.fourth_choice_4_3 = COMPUTER5_fourth_choice_4_3

        computer6.first_choice_end = False
        computer6.second_choice_end = False
        computer6.third_choice_end = False
        computer6.fourth_choice_end = False

        computer6.first_choice_1_end = True
        computer6.second_choice_1_end = True
        computer6.third_choice_1_end = True
        computer6.fourth_choice_1_end = True

        computer6.first_choice_2_end = True
        computer6.second_choice_2_end = True
        computer6.third_choice_2_end = True
        computer6.fourth_choice_2_end = True

        computer6.first_choice_3_end = False
        computer6.second_choice_3_end = False
        computer6.third_choice_3_end = True
        computer6.fourth_choice_3_end = True

        computer6.first_choice_3_1_end = True
        computer6.second_choice_3_1_end = True
        computer6.third_choice_3_1_end = True
        computer6.fourth_choice_3_1_end = True

        computer6.first_choice_3_2_end = True
        computer6.second_choice_3_2_end = True
        computer6.third_choice_3_2_end = True
        computer6.fourth_choice_3_2_end = True

        computer6.first_choice_4_end = True
        computer6.second_choice_4_end = True
        computer6.third_choice_4_end = False
        computer6.fourth_choice_4_end = True

        computer6.first_choice_4_3_end = True
        computer6.second_choice_4_3_end = True
        computer6.third_choice_4_3_end = True
        computer6.fourth_choice_4_3_end = True

        computer6.image = pygame.Surface((computer6.width, computer6.height))
        computer6.image.set_colorkey((0, 0, 0))

        return computer6

    @classmethod
    def computer7(cls, game, x, y):
        computer7 = cls(game, x, y)
        computer7.width = TILE_SIZE
        computer7.height = TILE_SIZE

        computer7.title = COMPUTER_title
        computer7.first_choice = COMPUTER_first_choice
        computer7.second_choice = COMPUTER_second_choice
        computer7.third_choice = COMPUTER_third_choice
        computer7.fourth_choice = COMPUTER_fourth_choice

        computer7.title_1 = COMPUTER_title_1
        computer7.first_choice_1 = COMPUTER_first_choice_1
        computer7.second_choice_1 = COMPUTER_second_choice_1
        computer7.third_choice_1 = COMPUTER_third_choice_1
        computer7.fourth_choice_1 = COMPUTER_fourth_choice_1

        computer7.title_2 = COMPUTER7_title_2
        computer7.first_choice_2 = COMPUTER7_first_choice_2
        computer7.second_choice_2 = COMPUTER6_second_choice_2
        computer7.third_choice_2 = COMPUTER_third_choice_2
        computer7.fourth_choice_2 = COMPUTER_fourth_choice_2

        computer7.title_3 = COMPUTER_title_3
        computer7.first_choice_3 = COMPUTER_first_choice_3
        computer7.second_choice_3 = COMPUTER_second_choice_3
        computer7.third_choice_3 = COMPUTER_third_choice_3
        computer7.fourth_choice_3 = COMPUTER_fourth_choice_3

        computer7.title_3_1 = COMPUTER_title_3_1
        computer7.first_choice_3_1 = COMPUTER_first_choice_3_1
        computer7.second_choice_3_1 = COMPUTER_second_choice_3_1
        computer7.third_choice_3_1 = COMPUTER_third_choice_3_1
        computer7.fourth_choice_3_1 = COMPUTER_fourth_choice_3_1

        computer7.title_3_2 = COMPUTER3_title_3_2
        computer7.first_choice_3_2 = COMPUTER4_first_choice_3_2
        computer7.second_choice_3_2 = COMPUTER_second_choice_3_2
        computer7.third_choice_3_2 = COMPUTER_third_choice_3_2
        computer7.fourth_choice_3_2 = COMPUTER_fourth_choice_3_2

        computer7.title_4 = COMPUTER_title_4
        computer7.first_choice_4 = COMPUTER2_first_choice_4
        computer7.second_choice_4 = COMPUTER2_second_choice_4
        computer7.third_choice_4 = COMPUTER2_third_choice_4
        computer7.fourth_choice_4 = COMPUTER_fourth_choice_4

        computer7.title_4_3 = COMPUTER5_title_4_3
        computer7.first_choice_4_3 = COMPUTER5_first_choice_4_3
        computer7.second_choice_4_3 = COMPUTER5_second_choice_4_3
        computer7.third_choice_4_3 = COMPUTER5_third_choice_4_3
        computer7.fourth_choice_4_3 = COMPUTER5_fourth_choice_4_3

        computer7.first_choice_end = False
        computer7.second_choice_end = False
        computer7.third_choice_end = False
        computer7.fourth_choice_end = False

        computer7.first_choice_1_end = True
        computer7.second_choice_1_end = True
        computer7.third_choice_1_end = True
        computer7.fourth_choice_1_end = True

        computer7.first_choice_2_end = True
        computer7.second_choice_2_end = True
        computer7.third_choice_2_end = True
        computer7.fourth_choice_2_end = True

        computer7.first_choice_3_end = False
        computer7.second_choice_3_end = False
        computer7.third_choice_3_end = True
        computer7.fourth_choice_3_end = True

        computer7.first_choice_3_1_end = True
        computer7.second_choice_3_1_end = True
        computer7.third_choice_3_1_end = True
        computer7.fourth_choice_3_1_end = True

        computer7.first_choice_3_2_end = True
        computer7.second_choice_3_2_end = True
        computer7.third_choice_3_2_end = True
        computer7.fourth_choice_3_2_end = True

        computer7.first_choice_4_end = True
        computer7.second_choice_4_end = True
        computer7.third_choice_4_end = False
        computer7.fourth_choice_4_end = True

        computer7.first_choice_4_3_end = True
        computer7.second_choice_4_3_end = True
        computer7.third_choice_4_3_end = True
        computer7.fourth_choice_4_3_end = True

        computer7.image = pygame.Surface((computer7.width, computer7.height))
        computer7.image.set_colorkey((0, 0, 0))

        return computer7

    @classmethod
    def Mom(cls, game, x, y):
        mom = cls(game, x, y)
        mom.width = TILE_SIZE
        mom.height = TILE_SIZE

        mom.title = MOM_title
        mom.first_choice = MOM_first_choice
        mom.second_choice = MOM_second_choice
        mom.third_choice = MOM_third_choice
        mom.fourth_choice = MOM_fourth_choice

        mom.title_1 = MOM_title_1
        mom.first_choice_1 = MOM_first_choice_1
        mom.second_choice_1 = MOM_second_choice_1
        mom.third_choice_1 = MOM_third_choice_1
        mom.fourth_choice_1 = MOM_fourth_choice_1

        mom.title_2 = MOM_title_2
        mom.first_choice_2 = MOM_first_choice_2
        mom.second_choice_2 = MOM_second_choice_2
        mom.third_choice_2 = MOM_third_choice_2
        mom.fourth_choice_2 = MOM_fourth_choice_2

        mom.first_choice_end = False
        mom.second_choice_end = False
        mom.third_choice_end = True
        mom.fourth_choice_end = True

        mom.first_choice_1_end = True
        mom.second_choice_1_end = True
        mom.third_choice_1_end = True
        mom.fourth_choice_1_end = True

        mom.first_choice_2_end = True
        mom.second_choice_2_end = True
        mom.third_choice_2_end = True
        mom.fourth_choice_2_end = True

        mom.image = pygame.Surface((mom.width, mom.height))
        mom.image.set_colorkey((0, 0, 0))

        return mom

    @classmethod
    def Mom2(cls, game, x, y):
        mom2 = cls(game, x, y)
        mom2.width = TILE_SIZE
        mom2.height = TILE_SIZE

        mom2.title = MOM_title
        mom2.first_choice = MOM_first_choice
        mom2.second_choice = MOM_second_choice
        mom2.third_choice = MOM2_third_choice
        mom2.fourth_choice = MOM_fourth_choice

        mom2.title_1 = MOM_title_1
        mom2.first_choice_1 = MOM_first_choice_1
        mom2.second_choice_1 = MOM_second_choice_1
        mom2.third_choice_1 = MOM_third_choice_1
        mom2.fourth_choice_1 = MOM_fourth_choice_1

        mom2.title_2 = MOM_title_2
        mom2.first_choice_2 = MOM_first_choice_2
        mom2.second_choice_2 = MOM_second_choice_2
        mom2.third_choice_2 = MOM_third_choice_2
        mom2.fourth_choice_2 = MOM_fourth_choice_2

        mom2.title_3 = MOM2_title_3
        mom2.first_choice_3 = MOM2_first_choice_3
        mom2.second_choice_3 = MOM2_second_choice_3
        mom2.third_choice_3 = MOM2_third_choice_3
        mom2.fourth_choice_3 = MOM2_fourth_choice_3

        mom2.first_choice_end = False
        mom2.second_choice_end = False
        mom2.third_choice_end = False
        mom2.fourth_choice_end = True

        mom2.first_choice_1_end = True
        mom2.second_choice_1_end = True
        mom2.third_choice_1_end = True
        mom2.fourth_choice_1_end = True

        mom2.first_choice_2_end = True
        mom2.second_choice_2_end = True
        mom2.third_choice_2_end = True
        mom2.fourth_choice_2_end = True

        mom2.first_choice_3_end = True
        mom2.second_choice_3_end = True
        mom2.third_choice_3_end = True
        mom2.fourth_choice_3_end = True

        mom2.image = pygame.Surface((mom2.width, mom2.height))
        mom2.image.set_colorkey((0, 0, 0))

        return mom2

    @classmethod
    def Guard(cls, game, x, y):
        guard = cls(game, x, y)
        guard.width = TILE_SIZE
        guard.height = TILE_SIZE
        guard.name = 'guard'

        guard.title = GUARD_title
        guard.first_choice = GUARD_first_choice
        guard.second_choice = GUARD_second_choice
        guard.third_choice = GUARD_third_choice
        guard.fourth_choice = GUARD_fourth_choice

        guard.first_choice_end = True
        guard.second_choice_end = True
        guard.third_choice_end = True
        guard.fourth_choice_end = True

        guard.image = pygame.Surface((guard.width, guard.height))
        guard.image.set_colorkey((0, 0, 0))

        return guard

    @classmethod
    def Guard2(cls, game, x, y):
        guard2 = cls(game, x, y)
        guard2.width = TILE_SIZE
        guard2.height = TILE_SIZE
        guard2.name = 'guard2'

        guard2.title = GUARD_title
        guard2.first_choice = GUARD_first_choice
        guard2.second_choice = GUARD2_second_choice
        guard2.third_choice = GUARD_third_choice
        guard2.fourth_choice = GUARD_fourth_choice

        guard2.title_2 = GUARD2_title_2
        guard2.first_choice_2 = GUARD2_first_choice_2
        guard2.second_choice_2 = GUARD2_second_choice_2
        guard2.third_choice_2 = GUARD2_third_choice_2
        guard2.fourth_choice_2 = GUARD2_fourth_choice_2

        guard2.first_choice_end = True
        guard2.second_choice_end = False
        guard2.third_choice_end = True
        guard2.fourth_choice_end = True

        guard2.first_choice_2_end = True
        guard2.second_choice_2_end = True
        guard2.third_choice_2_end = True
        guard2.fourth_choice_2_end = True

        guard2.image = pygame.Surface((guard2.width, guard2.height))
        guard2.image.set_colorkey((0, 0, 0))

        return guard2

    @classmethod
    def Police(cls, game, x, y):
        police = cls(game, x, y)
        police.width = TILE_SIZE
        police.height = TILE_SIZE
        police.name = 'police'

        police.title = POLICE_title
        police.first_choice = POLICE_first_choice
        police.second_choice = POLICE_second_choice
        police.third_choice = POLICE_third_choice
        police.fourth_choice = POLICE_fourth_choice

        police.first_choice_end = True
        police.second_choice_end = True
        police.third_choice_end = True
        police.fourth_choice_end = True

        police.image = pygame.Surface((police.width, police.height))
        police.image.set_colorkey((0, 0, 0))

        return police

    @classmethod
    def Police2(cls, game, x, y):
        police = cls(game, x, y)
        police.width = TILE_SIZE
        police.height = TILE_SIZE
        police.name = 'police2'

        police.title = POLICE_title
        police.first_choice = POLICE2_first_choice
        police.second_choice = POLICE_second_choice
        police.third_choice = POLICE_third_choice
        police.fourth_choice = POLICE_fourth_choice

        police.first_choice_end = True
        police.second_choice_end = True
        police.third_choice_end = True
        police.fourth_choice_end = True

        police.image = pygame.Surface((police.width, police.height))
        police.image.set_colorkey((0, 0, 0))

        return police

    @classmethod
    def Stay_back(cls, game, x, y):
        stay_back = cls(game, x, y)
        stay_back.width = TILE_SIZE
        stay_back.height = TILE_SIZE
        stay_back.name = 'stay back'

        stay_back.title = STAY_BACK_title
        stay_back.first_choice = STAY_BACK_first_choice
        stay_back.second_choice = LEAVE
        stay_back.third_choice = LEAVE
        stay_back.fourth_choice = LEAVE

        stay_back.first_choice_end = True
        stay_back.second_choice_end = True
        stay_back.third_choice_end = True
        stay_back.fourth_choice_end = True

        stay_back.image = pygame.Surface((stay_back.width, stay_back.height))
        stay_back.image.set_colorkey((0, 0, 0))

        return stay_back

    @classmethod
    def Clue_paper(cls, game, x, y):
        clue_paper = cls(game, x, y)
        clue_paper.width = TILE_SIZE
        clue_paper.height = TILE_SIZE
        clue_paper.name = 'clue paper'

        clue_paper.title = CLUE_PAPER
        clue_paper.first_choice = TAKE
        clue_paper.second_choice = LEAVE
        clue_paper.third_choice = LEAVE
        clue_paper.fourth_choice = LEAVE

        clue_paper.first_choice_end = True
        clue_paper.second_choice_end = True
        clue_paper.third_choice_end = True
        clue_paper.fourth_choice_end = True

        clue_paper.image = pygame.Surface((clue_paper.width, clue_paper.height))
        clue_paper.image.set_colorkey((0, 0, 0))

        return clue_paper

    @classmethod
    def Mask(cls, game, x, y):
        mask = cls(game, x, y)
        mask.width = TILE_SIZE
        mask.height = TILE_SIZE
        mask.name = 'mask'

        mask.title = MASK
        mask.first_choice = TAKE
        mask.second_choice = LEAVE
        mask.third_choice = LEAVE
        mask.fourth_choice = LEAVE

        mask.first_choice_end = True
        mask.second_choice_end = True
        mask.third_choice_end = True
        mask.fourth_choice_end = True

        mask.image = pygame.Surface((mask.width, mask.height))
        mask.image.set_colorkey((0, 0, 0))

        return mask

    @classmethod
    def Alcohol(cls, game, x, y):
        alcohol = cls(game, x, y)
        alcohol.width = TILE_SIZE
        alcohol.height = TILE_SIZE
        alcohol.name = 'alcohol'

        alcohol.title = ALCOHOL
        alcohol.first_choice = TAKE
        alcohol.second_choice = LEAVE
        alcohol.third_choice = LEAVE
        alcohol.fourth_choice = LEAVE

        alcohol.first_choice_end = True
        alcohol.second_choice_end = True
        alcohol.third_choice_end = True
        alcohol.fourth_choice_end = True

        alcohol.image = pygame.Surface((alcohol.width, alcohol.height))
        alcohol.image.set_colorkey((0, 0, 0))

        return alcohol

    @classmethod
    def Forehead_thermometer(cls, game, x, y):
        forehead_thermometer = cls(game, x, y)
        forehead_thermometer.width = TILE_SIZE
        forehead_thermometer.height = TILE_SIZE
        forehead_thermometer.name = 'forehead thermometer'

        forehead_thermometer.title = FOREHEAD_THERMOMETER
        forehead_thermometer.first_choice = TAKE
        forehead_thermometer.second_choice = LEAVE
        forehead_thermometer.third_choice = LEAVE
        forehead_thermometer.fourth_choice = LEAVE

        forehead_thermometer.first_choice_end = True
        forehead_thermometer.second_choice_end = True
        forehead_thermometer.third_choice_end = True
        forehead_thermometer.fourth_choice_end = True

        forehead_thermometer.image = pygame.Surface((forehead_thermometer.width, forehead_thermometer.height))
        forehead_thermometer.image.set_colorkey((0, 0, 0))
        return forehead_thermometer

    @classmethod
    def Face_shield(cls, game, x, y):
        face_shield = cls(game, x, y)
        face_shield.width = TILE_SIZE
        face_shield.height = TILE_SIZE
        face_shield.name = 'face shield'

        face_shield.title = FACE_SHIELD
        face_shield.first_choice = TAKE
        face_shield.second_choice = LEAVE
        face_shield.third_choice = LEAVE
        face_shield.fourth_choice = LEAVE

        face_shield.first_choice_end = True
        face_shield.second_choice_end = True
        face_shield.third_choice_end = True
        face_shield.fourth_choice_end = True

        face_shield.image = pygame.Surface((face_shield.width, face_shield.height))
        face_shield.image.set_colorkey((0, 0, 0))

        return face_shield

    @classmethod
    def Bauta(cls, game, x, y):
        bauta = cls(game, x, y)
        bauta.width = TILE_SIZE
        bauta.height = TILE_SIZE
        bauta.name = 'bauta'

        bauta.title = BAUTA
        bauta.first_choice = TAKE
        bauta.second_choice = LEAVE
        bauta.third_choice = LEAVE
        bauta.fourth_choice = LEAVE

        bauta.first_choice_end = True
        bauta.second_choice_end = True
        bauta.third_choice_end = True
        bauta.fourth_choice_end = True

        bauta.image = pygame.Surface((bauta.width, bauta.height))
        bauta.image.set_colorkey((0, 0, 0))

        return bauta

    @classmethod
    def Cloak(cls, game, x, y):
        cloak = cls(game, x, y)
        cloak.width = TILE_SIZE
        cloak.height = TILE_SIZE
        cloak.name = 'cloak'

        cloak.title = CLOAK
        cloak.first_choice = TAKE
        cloak.second_choice = LEAVE
        cloak.third_choice = LEAVE
        cloak.fourth_choice = LEAVE

        cloak.first_choice_end = True
        cloak.second_choice_end = True
        cloak.third_choice_end = True
        cloak.fourth_choice_end = True

        cloak.image = pygame.Surface((cloak.width, cloak.height))
        cloak.image.set_colorkey((0, 0, 0))

        return cloak

    @classmethod
    def Vaccine(cls, game, x, y):
        vaccine = cls(game, x, y)
        vaccine.width = TILE_SIZE
        vaccine.height = TILE_SIZE
        vaccine.name = 'vaccine'

        vaccine.title = VACCINE
        vaccine.first_choice = TAKE
        vaccine.second_choice = LEAVE
        vaccine.third_choice = LEAVE
        vaccine.fourth_choice = LEAVE

        vaccine.first_choice_end = True
        vaccine.second_choice_end = True
        vaccine.third_choice_end = True
        vaccine.fourth_choice_end = True

        vaccine.image = pygame.Surface((vaccine.width, vaccine.height))
        vaccine.image.set_colorkey((0, 0, 0))

        return vaccine

    @classmethod
    def Gloves(cls, game, x, y):
        gloves = cls(game, x, y)
        gloves.width = TILE_SIZE
        gloves.height = TILE_SIZE
        gloves.name = 'gloves'

        gloves.title = GLOVES
        gloves.first_choice = TAKE
        gloves.second_choice = LEAVE
        gloves.third_choice = LEAVE
        gloves.fourth_choice = LEAVE

        gloves.first_choice_end = True
        gloves.second_choice_end = True
        gloves.third_choice_end = True
        gloves.fourth_choice_end = True

        gloves.image = pygame.Surface((gloves.width, gloves.height))
        gloves.image.set_colorkey((0, 0, 0))

        return gloves

    @classmethod
    def Booklet(cls, game, x, y):
        booklet = cls(game, x, y)
        booklet.width = TILE_SIZE
        booklet.height = TILE_SIZE
        booklet.name = 'booklet'

        booklet.title = BOOKLET
        booklet.first_choice = TAKE
        booklet.second_choice = LEAVE
        booklet.third_choice = LEAVE
        booklet.fourth_choice = LEAVE

        booklet.first_choice_end = True
        booklet.second_choice_end = True
        booklet.third_choice_end = True
        booklet.fourth_choice_end = True

        booklet.image = pygame.Surface((booklet.width, booklet.height))
        booklet.image.set_colorkey((0, 0, 0))

        return booklet

    @classmethod
    def Switch(cls, game, x, y):
        switch = cls(game, x, y)
        switch.width = TILE_SIZE
        switch.height = TILE_SIZE
        switch.name = 'switch'

        switch.title = SWITCH
        switch.first_choice = TAKE
        switch.second_choice = LEAVE
        switch.third_choice = LEAVE
        switch.fourth_choice = LEAVE

        switch.first_choice_end = True
        switch.second_choice_end = True
        switch.third_choice_end = True
        switch.fourth_choice_end = True

        switch.image = pygame.Surface((switch.width, switch.height))
        switch.image.set_colorkey((0, 0, 0))

        return switch

    @classmethod
    def Blinkers(cls, game, x, y):
        blinkers = cls(game, x, y)
        blinkers.width = TILE_SIZE
        blinkers.height = TILE_SIZE
        blinkers.name = 'blinkers'

        blinkers.title = BLINKERS
        blinkers.first_choice = TAKE
        blinkers.second_choice = LEAVE
        blinkers.third_choice = LEAVE
        blinkers.fourth_choice = LEAVE

        blinkers.first_choice_end = True
        blinkers.second_choice_end = True
        blinkers.third_choice_end = True
        blinkers.fourth_choice_end = True

        blinkers.image = pygame.Surface((blinkers.width, blinkers.height))
        blinkers.image.set_colorkey((0, 0, 0))

        return blinkers

    @classmethod
    def Handkerchief(cls, game, x, y):
        handkerchief = cls(game, x, y)
        handkerchief.width = TILE_SIZE
        handkerchief.height = TILE_SIZE
        handkerchief.name = 'handkerchief'

        handkerchief.title = HANDKERCHIEF
        handkerchief.first_choice = TAKE
        handkerchief.second_choice = LEAVE
        handkerchief.third_choice = LEAVE
        handkerchief.fourth_choice = LEAVE

        handkerchief.first_choice_end = True
        handkerchief.second_choice_end = True
        handkerchief.third_choice_end = True
        handkerchief.fourth_choice_end = True

        handkerchief.image = pygame.Surface((handkerchief.width, handkerchief.height))
        handkerchief.image.set_colorkey((0, 0, 0))

        return handkerchief

    @classmethod
    def Health_ID_card(cls, game, x, y):
        health_ID_card = cls(game, x, y)
        health_ID_card.width = TILE_SIZE
        health_ID_card.height = TILE_SIZE
        health_ID_card.name = 'health ID card'

        health_ID_card.title = HEALTH_ID_CARD
        health_ID_card.first_choice = TAKE
        health_ID_card.second_choice = LEAVE
        health_ID_card.third_choice = LEAVE
        health_ID_card.fourth_choice = LEAVE

        health_ID_card.first_choice_end = True
        health_ID_card.second_choice_end = True
        health_ID_card.third_choice_end = True
        health_ID_card.fourth_choice_end = True

        health_ID_card.image = pygame.Surface((health_ID_card.width, health_ID_card.height))
        health_ID_card.image.set_colorkey((0, 0, 0))

        return health_ID_card


class DialogueSpotGroup:
    def __init__(self, game):
        self.game = game
        self.dialogueSpots_list = []
        self.in_dialogue = False
        self.player_at_dialogueSpot = False
        self.in_used = []

    def refresh_dialogueSpots(self):
        self.dialogueSpots_list.clear()
        self.in_used.clear()
        for i, row in enumerate(self.game.map_in_use):
            for j, column in enumerate(row):
                if column == "c":
                    if self.game.scene_5_1_complete:
                        self.generate_dialogueSpot('computer7', j, i)
                    elif self.game.scene_4_complete:
                        self.generate_dialogueSpot('computer6', j, i)
                    elif self.game.scene_4_2_complete:
                        self.generate_dialogueSpot('computer5', j, i)
                    elif self.game.scene_3_complete:
                        self.generate_dialogueSpot('computer4', j, i)
                    elif self.game.scene_3_1_complete:
                        self.generate_dialogueSpot('computer3', j, i)
                    elif self.game.scene_2_complete:
                        self.generate_dialogueSpot('computer2', j, i)
                    else:
                        self.generate_dialogueSpot('computer', j, i)
                if self.game.scene_1_1_complete:
                    if not self.game.scene_2_1_complete:
                        if column == '-':
                            self.generate_dialogueSpot('stay back', j, i)
                    if not self.game.scene_1_3_complete:
                        if self.game.scene_1_2_complete:
                            if column == "m":
                                self.generate_dialogueSpot('Mom2', j, i)
                        else:
                            if column == "m":
                                self.generate_dialogueSpot('Mom', j, i)
                    if not self.game.scene_5_3_complete:
                        if not self.game.scene_4_1_complete:
                            if column == "d":
                                self.generate_dialogueSpot('Guard', j, i)
                        else:
                            if column == "d":
                                self.generate_dialogueSpot('Guard2', j, i)
                        if column == "v":
                            self.generate_dialogueSpot('police', j, i)
                    else:
                        if column == "v":
                            self.generate_dialogueSpot('police2', j, i)

                    for item in self.game.items.items_list:
                        if column == "i":
                            if item.name == 'clue paper':
                                self.generate_dialogueSpot('clue paper', j, i)
                        if column == "q":
                            if item.name == 'mask':
                                self.generate_dialogueSpot('mask', j, i)
                        if column == "l":
                            if item.name == 'alcohol':
                                self.generate_dialogueSpot('alcohol', j, i)
                        if column == "o":
                            if item.name == 'cloak':
                                self.generate_dialogueSpot('cloak', j, i)
                        if column == "t":
                            if item.name == 'health ID card':
                                self.generate_dialogueSpot('health ID card', j, i)
                        if column == "s":
                            if item.name == 'forehead thermometer':
                                self.generate_dialogueSpot('forehead thermometer', j, i)
                        if column == "j":
                            if item.name == 'blinkers':
                                self.generate_dialogueSpot('blinkers', j, i)
                        if column == "<":
                            if item.name == 'switch':
                                self.generate_dialogueSpot('switch', j, i)
                        if column == "?":
                            if item.name == 'booklet':
                                self.generate_dialogueSpot('booklet', j, i)
                        if column == "]":
                            if item.name == 'bauta':
                                self.generate_dialogueSpot('bauta', j, i)
                        if column == "}":
                            if item.name == 'vaccine':
                                self.generate_dialogueSpot('vaccine', j, i)
                        if column == "』":
                            if item.name == 'gloves':
                                self.generate_dialogueSpot('gloves', j, i)
                        if column == "」":
                            if item.name == 'face shield':
                                self.generate_dialogueSpot('face shield', j, i)
                        if column == "神":
                            if item.name == 'handkerchief':
                                self.generate_dialogueSpot('handkerchief', j, i)

    def generate_dialogueSpot(self, name, x, y):
        new_spot = None
        if name is None:
            return
        if name == 'computer':
            new_spot = DialogueSpot.computer(self.game, x, y)
        if name == 'computer2':
            new_spot = DialogueSpot.computer2(self.game, x, y)
        if name == 'computer3':
            new_spot = DialogueSpot.computer3(self.game, x, y)
        if name == 'computer4':
            new_spot = DialogueSpot.computer4(self.game, x, y)
        if name == 'computer5':
            new_spot = DialogueSpot.computer5(self.game, x, y)
        if name == 'computer6':
            new_spot = DialogueSpot.computer6(self.game, x, y)
        if name == 'computer7':
            new_spot = DialogueSpot.computer7(self.game, x, y)
        if name == 'Mom':
            new_spot = DialogueSpot.Mom(self.game, x, y)
        if name == 'Mom2':
            new_spot = DialogueSpot.Mom2(self.game, x, y)
        if name == 'Guard':
            new_spot = DialogueSpot.Guard(self.game, x, y)
        if name == 'Guard2':
            new_spot = DialogueSpot.Guard2(self.game, x, y)
        if name == 'police':
            new_spot = DialogueSpot.Police(self.game, x, y)
        if name == 'police2':
            new_spot = DialogueSpot.Police2(self.game, x, y)
        if name == 'clue paper':
            new_spot = DialogueSpot.Clue_paper(self.game, x, y)
        if name == 'mask':
            new_spot = DialogueSpot.Mask(self.game, x, y)
        if name == 'alcohol':
            new_spot = DialogueSpot.Alcohol(self.game, x, y)
        if name == 'forehead thermometer':
            new_spot = DialogueSpot.Forehead_thermometer(self.game, x, y)
        if name == 'baby_wipe':
            new_spot = DialogueSpot.Baby_wipe(self.game, x, y)
        if name == 'face shield':
            new_spot = DialogueSpot.Face_shield(self.game, x, y)
        if name == 'bauta':
            new_spot = DialogueSpot.Bauta(self.game, x, y)
        if name == 'cloak':
            new_spot = DialogueSpot.Cloak(self.game, x, y)
        if name == 'vaccine':
            new_spot = DialogueSpot.Vaccine(self.game, x, y)
        if name == 'gloves':
            new_spot = DialogueSpot.Gloves(self.game, x, y)
        if name == 'booklet':
            new_spot = DialogueSpot.Booklet(self.game, x, y)
        if name == 'switch':
            new_spot = DialogueSpot.Switch(self.game, x, y)
        if name == 'blinkers':
            new_spot = DialogueSpot.Blinkers(self.game, x, y)
        if name == 'handkerchief':
            new_spot = DialogueSpot.Handkerchief(self.game, x, y)
        if name == 'health ID card':
            new_spot = DialogueSpot.Health_ID_card(self.game, x, y)
        if name == 'stay back':
            new_spot = DialogueSpot.Stay_back(self.game, x, y)
        self.dialogueSpots_list.append(new_spot)

    def get_in_used_dialogueSpot(self):
        for player in self.game.players.players_list:
            for dialogueSpot in self.dialogueSpots_list:
                hit = dialogueSpot.rect.colliderect(player.rect)
                if hit:
                    self.player_at_dialogueSpot = True
                    self.in_used.append(dialogueSpot)
                    self.game.NPCs.move_detection()

    def update(self):
        self.player_at_dialogueSpot = False
        self.get_in_used_dialogueSpot()
        if not self.player_at_dialogueSpot:
            self.in_used.clear()

    def draw(self, screen):
        for dialogueSpot in self.dialogueSpots_list:
            screen.blit(dialogueSpot.image, dialogueSpot.rect)


class Door:
    def __init__(self, game, x, y, map1, map2):
        self.game = game

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.tilemap_self = map1
        self.tilemap_street = map2

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((0, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    @classmethod
    def home(cls, game, x, y, map1, map2):
        home = cls(game, x, y, map1, map2)
        home.width = TILE_SIZE
        home.height = TILE_SIZE
        home.image = pygame.Surface((home.width, home.height))
        home.image.fill((0, 0, 0))
        home.tilemap_self = map1
        home.tilemap_street = map2
        return home

    @classmethod
    def school(cls, game, x, y, map1, map2):
        school = cls(game, x, y, map1, map2)
        school.width = TILE_SIZE
        school.height = TILE_SIZE
        school.image = pygame.Surface((school.width, school.height))
        school.image.fill((0, 0, 0))
        school.tilemap_self = map1
        school.tilemap_street = map2
        return school

    @classmethod
    def police_station(cls, game, x, y, map1, map2):
        police_station = cls(game, x, y, map1, map2)
        police_station.width = TILE_SIZE
        police_station.height = TILE_SIZE
        police_station.image = pygame.Surface((police_station.width, police_station.height))
        police_station.image.fill((0, 0, 0))
        police_station.tilemap_self = map1
        police_station.tilemap_street = map2
        return police_station


class DoorGroup:
    def __init__(self, game):
        self.doors_list = []
        self.game = game
        self.player_at_door = False
        self.next_map = None
        self.police_entered = False



    def generate_door(self, name, x, y):
        new_door = None
        if name is None:
            return
        if name == 'home':
            if not self.game.scene_5_3_complete:
                new_door = Door.home(self.game, x, y, tilemap_4, tilemap_2)
            else:
                new_door = Door.home(self.game, x, y, tilemap_4, tilemap_9)
        if name == 'school':
            if not self.game.scene_5_3_complete:
                if not self.game.scene_2_2_complete:
                    new_door = Door.school(self.game, x, y, tilemap_3, tilemap_5)
                else:
                    new_door = Door.school(self.game, x, y, tilemap_6, tilemap_5)
            else:
                new_door = Door.school(self.game, x, y, tilemap_3, tilemap_10)
        if name == 'police station':
            if self.game.map_in_use == tilemap_7:
                self.police_entered = True
            if self.police_entered:
                if not self.game.scene_5_3_complete:
                    new_door = Door.police_station(self.game, x, y, tilemap_12, tilemap_8)
                else:
                    new_door = Door.police_station(self.game, x, y, tilemap_12, tilemap_11)
            else:
                if not self.game.scene_5_3_complete:
                    new_door = Door.police_station(self.game, x, y, tilemap_7, tilemap_8)
                else:
                    new_door = Door.police_station(self.game, x, y, tilemap_7, tilemap_11)
        self.doors_list.append(new_door)

    def detect_player(self):
        for player in self.game.players.players_list:
            for door in self.doors_list:
                hit = door.rect.colliderect(player.rect)
                if hit:
                    self.player_at_door = True
                    if self.game.players.in_street:
                        self.next_map = door.tilemap_self
                    elif not self.game.players.in_street:
                        self.next_map = door.tilemap_street

    def refresh_door(self):
        self.doors_list.clear()
        for i, row in enumerate(self.game.map_in_use):
            for j, column in enumerate(row):
                if column == "1":
                    self.generate_door('home', j, i)
                if column == "2":
                    self.generate_door('school', j, i)
                if column == "3":
                    self.generate_door('police station', j, i)

    def map_change(self):
        if self.player_at_door:
            self.game.door_sound.play()
            self.game.players.players_list.clear()
            self.game.NPCs.NPCs_list.clear()
            self.game.grounds.grounds_list.clear()
            self.game.blocks.blocks_list.clear()
            self.game.dialogueSpots.dialogueSpots_list.clear()
            self.game.doors.doors_list.clear()
            self.game.items.items_list.clear()
            self.game.map_in_use = self.next_map
            self.game.create_tilemap()
            self.game.players.in_street = not self.game.players.in_street

    def update(self):
        self.refresh_door()
        self.detect_player()
        self.map_change()
        self.player_at_door = False

    def draw(self, screen):
        for door in self.doors_list:
            screen.blit(door.image, door.rect)


class Item:
    def __init__(self, game, x ,y):
        self.game = game
        self.name = None
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        self.protection = 0

        self.image = pygame.Surface((self.width, self.height))
        self.image.set_colorkey((0, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    @classmethod
    def Mask(cls, game, x, y):
        mask = cls(game, x, y)
        mask.x = TILE_SIZE
        mask.y = TILE_SIZE
        mask.width = TILE_SIZE
        mask.height = TILE_SIZE
        mask.name = 'mask'
        mask.protection = 100
        mask.image = mask.game.item_spritesheet.get_sprite(0, 0, mask.width, mask.height)
        return mask

    @classmethod
    def Alcohol(cls, game, x, y):
        alcohol = cls(game, x, y)
        alcohol.x = TILE_SIZE
        alcohol.y = TILE_SIZE
        alcohol.width = TILE_SIZE
        alcohol.height = TILE_SIZE
        alcohol.name = 'alcohol'
        alcohol.protection = 50
        alcohol.image = alcohol.game.item_spritesheet.get_sprite(32, 0, alcohol.width, alcohol.height)
        return alcohol

    @classmethod
    def Forehead_thermometer(cls, game, x, y):
        forehead_thermometer = cls(game, x, y)
        forehead_thermometer.x = TILE_SIZE
        forehead_thermometer.y = TILE_SIZE
        forehead_thermometer.width = TILE_SIZE
        forehead_thermometer.height = TILE_SIZE
        forehead_thermometer.protection = 30
        forehead_thermometer.name = 'forehead thermometer'
        forehead_thermometer.image = forehead_thermometer.game.item_spritesheet.get_sprite(3 * TILE_SIZE, 0,
                                                                                           forehead_thermometer.width,
                                                                                           forehead_thermometer.height)
        return forehead_thermometer

    @classmethod
    def Email(cls, game, x, y):
        email = cls(game, x, y)
        email.x = TILE_SIZE
        email.y = TILE_SIZE
        email.width = TILE_SIZE
        email.height = TILE_SIZE
        email.name = 'email'
        email.image = email.game.item_spritesheet.get_sprite(0, TILE_SIZE, email.width, email.height)
        return email

    @classmethod
    def Face_shield(cls, game, x, y):
        face_shield = cls(game, x, y)
        face_shield.x = TILE_SIZE
        face_shield.y = TILE_SIZE
        face_shield.width = TILE_SIZE
        face_shield.height = TILE_SIZE
        face_shield.protection = 30
        face_shield.name = 'face shield'
        face_shield.image = face_shield.game.item_spritesheet.get_sprite(2 * TILE_SIZE, TILE_SIZE, face_shield.width,
                                                                         face_shield.height)
        return face_shield

    @classmethod
    def Bauta(cls, game, x, y):
        bauta = cls(game, x, y)
        bauta.x = TILE_SIZE
        bauta.y = TILE_SIZE
        bauta.width = TILE_SIZE
        bauta.height = TILE_SIZE
        bauta.protection = -9999
        bauta.name = 'bauta'
        bauta.image = bauta.game.item_spritesheet.get_sprite(3 * TILE_SIZE, TILE_SIZE, bauta.width, bauta.height)
        return bauta

    @classmethod
    def Cloak(cls, game, x, y):
        cloak = cls(game, x, y)
        cloak.x = TILE_SIZE
        cloak.y = TILE_SIZE
        cloak.width = TILE_SIZE
        cloak.height = TILE_SIZE
        cloak.protection = 18
        cloak.name = 'cloak'
        cloak.image = cloak.game.item_spritesheet.get_sprite(0, 2 * TILE_SIZE, cloak.width, cloak.height)
        return cloak

    @classmethod
    def Vaccine(cls, game, x, y):
        vaccine = cls(game, x, y)
        vaccine.x = TILE_SIZE
        vaccine.y = TILE_SIZE
        vaccine.width = TILE_SIZE
        vaccine.height = TILE_SIZE
        vaccine.protection = 50
        vaccine.name = 'vaccine'
        vaccine.image = vaccine.game.item_spritesheet.get_sprite(TILE_SIZE, 2 * TILE_SIZE, vaccine.width,
                                                                 vaccine.height)
        return vaccine


    @classmethod
    def Gloves(cls, game, x, y):
        gloves = cls(game, x, y)
        gloves.x = TILE_SIZE
        gloves.y = TILE_SIZE
        gloves.width = TILE_SIZE
        gloves.height = TILE_SIZE
        gloves.protection = 20
        gloves.name = 'gloves'
        gloves.image = gloves.game.item_spritesheet.get_sprite(3 * TILE_SIZE, 2 * TILE_SIZE, gloves.width,
                                                               gloves.height)
        return gloves


    @classmethod
    def Booklet(cls, game, x, y):
        booklet = cls(game, x, y)
        booklet.x = TILE_SIZE
        booklet.y = TILE_SIZE
        booklet.width = TILE_SIZE
        booklet.height = TILE_SIZE
        booklet.protection = 100
        booklet.name = 'booklet'
        booklet.image = booklet.game.item_spritesheet.get_sprite(TILE_SIZE, 3 * TILE_SIZE, booklet.width,
                                                                               booklet.height)
        return booklet

    @classmethod
    def Switch(cls, game, x, y):
        switch = cls(game, x, y)
        switch.x = TILE_SIZE
        switch.y = TILE_SIZE
        switch.width = TILE_SIZE
        switch.height = TILE_SIZE
        switch.protection = -10
        switch.name = 'switch'
        switch.image = switch.game.item_spritesheet.get_sprite(2 * TILE_SIZE, 3 * TILE_SIZE, switch.width,
                                                               switch.height)
        return switch

    @classmethod
    def Blinkers(cls, game, x, y):
        blinkers = cls(game, x, y)
        blinkers.x = TILE_SIZE
        blinkers.y = TILE_SIZE
        blinkers.width = TILE_SIZE
        blinkers.height = TILE_SIZE
        blinkers.protection = 5
        blinkers.name = 'blinkers'
        blinkers.image = blinkers.game.item_spritesheet.get_sprite(3 * TILE_SIZE, 3 * TILE_SIZE, blinkers.width,
                                                                   blinkers.height)
        return blinkers


    @classmethod
    def Handkerchief(cls, game, x, y):
        handkerchief = cls(game, x, y)
        handkerchief.x = TILE_SIZE
        handkerchief.y = TILE_SIZE
        handkerchief.width = TILE_SIZE
        handkerchief.height = TILE_SIZE
        handkerchief.name = 'handkerchief'
        handkerchief.protection = 9999
        handkerchief.image = handkerchief.game.item_spritesheet.get_sprite(TILE_SIZE, 4 * TILE_SIZE, handkerchief.width,
                                                                           handkerchief.height)
        return handkerchief

    @classmethod
    def Health_ID_card(cls, game, x, y):
        health_ID_card = cls(game, x, y)
        health_ID_card.x = TILE_SIZE
        health_ID_card.y = TILE_SIZE
        health_ID_card.width = TILE_SIZE
        health_ID_card.height = TILE_SIZE
        health_ID_card.protection = 4
        health_ID_card.name = 'health ID card'
        health_ID_card.image = health_ID_card.game.item_spritesheet.get_sprite(2 * TILE_SIZE, 4 * TILE_SIZE,
                                                                               health_ID_card.width,
                                                                               health_ID_card.height)
        return health_ID_card

    @classmethod
    def Clue_paper(cls, game, x, y):
        clue_paper = cls(game, x, y)
        clue_paper.x = TILE_SIZE
        clue_paper.y = TILE_SIZE
        clue_paper.width = TILE_SIZE
        clue_paper.height = TILE_SIZE
        clue_paper.name = 'clue paper'
        clue_paper.image = clue_paper.game.item_spritesheet.get_sprite(64, 0, clue_paper.width, clue_paper.height)
        return clue_paper

    @classmethod
    def Mail(cls, game, x, y):
        mail = cls(game, x, y)
        mail.x = TILE_SIZE
        mail.y = TILE_SIZE
        mail.width = TILE_SIZE
        mail.height = TILE_SIZE
        mail.name = 'clue paper'
        mail.image = mail.game.item_spritesheet.get_sprite(0, TILE_SIZE, mail.width, mail.height)
        return mail


class ItemGroup:
    def __init__(self, game):
        self.items_list = []
        self.game = game

    def generate_item(self, name, x, y):
        new_item = None
        if name is None:
            return
        if name == 'mask':
            new_item = Item.Mask(self.game, x, y)
        if name == 'alcohol':
            new_item = Item.Alcohol(self.game, x, y)
        if name == 'clue paper':
            new_item = Item.Clue_paper(self.game, x, y)
        if name == 'forehead thermometer':
            new_item = Item.Forehead_thermometer(self.game, x, y)
        if name == 'email':
            new_item = Item.Email(self.game, x, y)
        if name == 'face shield':
            new_item = Item.Face_shield(self.game, x, y)
        if name == 'cloak':
            new_item = Item.Cloak(self.game, x, y)
        if name == 'bauta':
            new_item = Item.Bauta(self.game, x, y)
        if name == 'vaccine':
            new_item = Item.Vaccine(self.game, x, y)
        if name == 'gloves':
            new_item = Item.Gloves(self.game, x, y)
        if name == 'booklet':
            new_item = Item.Booklet(self.game, x, y)
        if name == 'switch':
            new_item = Item.Switch(self.game, x, y)
        if name == 'blinkers':
            new_item = Item.Blinkers(self.game, x, y)
        if name == 'handkerchief':
            new_item = Item.Handkerchief(self.game, x, y)
        if name == 'health ID card':
            new_item = Item.Health_ID_card(self.game, x, y)
        self.items_list.append(new_item)

    def draw(self, screen):
        for item in self.items_list:
            screen.blit(item.image, item.rect)

    def detect_pick_up_item(self):
        dialogueSpot = self.game.dialogueSpots.in_used
        for arrow in self.game.arrows.arrows_list:
            if arrow.rect.y == ARROW_CHOOSE_ONE_Y:
                for item in self.items_list:
                    if dialogueSpot[0].name == item.name:
                        self.game.players.items_list.append(item)
                        self.game.get_sound.play()
                        self.game.players.protection += item.protection
                        item.rect = self.game.bag.bag_item_list[0]
                        self.game.bag.bag_item_list.pop(0)
                        self.items_list.pop(self.items_list.index(item))
                        if item.name == 'clue paper':
                            pygame.mixer.music.load(self.game.chase_music)
                            pygame.mixer.music.set_volume(0.3)
                            pygame.mixer.music.play(-1)


class Bag:
    def __init__(self, game):
        self.game = game
        self.displaying = False
        self.x = BAG_X
        self.y = BAG_Y
        self.width = 11*TILE_SIZE
        self.height = 11*TILE_SIZE
        self.protection_text = Font().get_text('texts/protection.txt')
        self.protection_text_image = Font().get_image(self.protection_text)

        self.protection_text_image = pygame.font.Font("texts/NotoSerifCJKtc-Regular.otf", 20).render(self.protection_text
                                                                                                     , True, (250, 66, 60),
                                                                                                     (144, 187, 221))

        self.image = game.bag_spritesheet.get_sprite(0, 0, self.width, self.height)


        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.bag_item_list = [(BAG_X + 90, BAG_Y + 92), (BAG_X + 137, BAG_Y + 92), (BAG_X + 184, BAG_Y + 92),
                              (BAG_X + 231, BAG_Y + 92), (BAG_X + 90, BAG_Y + 132), (BAG_X + 137, BAG_Y + 132),
                              (BAG_X + 184, BAG_Y + 132), (BAG_X + 231, BAG_Y + 132), (BAG_X + 90, BAG_Y + 172),
                              (BAG_X + 137, BAG_Y + 172), (BAG_X + 184, BAG_Y + 172), (BAG_X + 231, BAG_Y + 172),
                              (BAG_X + 90, BAG_Y + 212), (BAG_X + 137, BAG_Y + 212), (BAG_X + 184, BAG_Y + 212),
                              (BAG_X + 231, BAG_Y + 172), (BAG_X + 90, BAG_Y + 252), (BAG_X + 137, BAG_Y + 252),
                              (BAG_X + 184, BAG_Y + 252), (BAG_X + 231, BAG_Y + 252), (BAG_X + 90, BAG_Y + 292),
                              (BAG_X + 137, BAG_Y + 292), (BAG_X + 184, BAG_Y + 292), (BAG_X + 231, BAG_Y + 292)]

    def bag_in_use(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_b]:
            self.displaying = True
        else:
            self.displaying = False
        return self.displaying

    def draw(self, screen):
        protection = str(self.game.players.protection)
        protection_image = pygame.font.Font("texts/NotoSerifCJKtc-Regular.otf", 20).render(protection, True,
                                                                                                (250, 66, 60),
                                                                                                (144, 187, 221))
        if self.bag_in_use():
            screen.blit(self.image, (BAG_X, BAG_Y))
            screen.blit(self.protection_text_image, (BAG_X + 90, BAG_Y + 60))
            screen.blit(protection_image, (BAG_X + 200, BAG_Y + 60))
            for item in self.game.players.items_list:
                screen.blit(item.image, item.rect)


class Bullet:
    def __init__(self, game, x, y):
        self.game = game
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.image = self.game.bullet.get_sprite(0, 0, self.width, self.height)
        self.image.set_colorkey((0, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.path = BULLET_PATH
        self.path_pos = 0

        self.x_change = 0
        self.y_change = 0
        self.speed = 8

        self.max_count = TILE_SIZE / self.speed
        self.move_goal_x = 41*TILE_SIZE
        self.move_goal_y = None
        self.moving = True


    def move(self):
        if self.moving:
            if self.rect.x == self.move_goal_x and self.rect.y == self.move_goal_y:
                self.moving = False
                self.x_change = 0
                self.y_change = 0
            else:
                if self.path[self.path_pos] == 'x+':
                    self.x_change += self.speed
                elif self.path[self.path_pos] == 'x-':
                    self.x_change -= self.speed
                if self.path[self.path_pos] == 'y+':
                    self.y_change += self.speed
                elif self.path[self.path_pos] == 'y-':
                    self.y_change -= self.speed

            self.path_pos += 1

    @classmethod
    def Shot_by_boss(cls, game, x, y):
        bullet = cls(game, x, y)
        bullet.move_goal_y = 12*TILE_SIZE
        return bullet

    @classmethod
    def Shot_by_gov(cls, game, x, y):
        bullet = cls(game, x, y)
        bullet.move_goal_y = 14 * TILE_SIZE
        return bullet


class BulletGroup:
    def __init__(self, game):
        self.game = game
        self.bullets_list = []
        self.counter = 0

    def generate_bullet(self, name):
        new_bullet = None
        if name is None:
            return
        # 木頭地板
        if name == 'shot by boss':
            new_bullet = Bullet.Shot_by_boss(self.game, 7, 12)
        # 草地地板
        if name == 'shot by gov':
            new_bullet = Bullet.Shot_by_gov(self.game, 7, 14)
        self.bullets_list.append(new_bullet)

    def draw(self, screen):
        for bullet in self.bullets_list:
            screen.blit(bullet.image, bullet.rect)

    def update(self):
        if (self.game.map_in_use == tilemap_9 and self.game.plots.plot_15_played) or\
            (self.game.map_in_use == tilemap_10 and self.game.plots.plot_15_played) or\
            (self.game.map_in_use == tilemap_11 and self.game.plots.plot_15_played):
            if not self.counter % 41 and self.counter % 82:
                self.generate_bullet('shot by boss')
                self.game.shot_sound.play()
            if not self.counter % 82:
                self.generate_bullet('shot by gov')
                self.game.shot_sound.play()
            self.counter += 1
        else:
            self.bullets_list.clear()

        for bullet in self.bullets_list:
            bullet.move()
            bullet.rect.x += bullet.x_change
            bullet.rect.y += bullet.y_change
            bullet.x_change = 0
            bullet.y_change = 0
        for player in self.game.players.players_list:
            for bullet in self.bullets_list:
                hit = bullet.rect.colliderect(player)
                if hit:
                    self.game.killed_sound.play()
                    self.game.plots.get_shot = True



