# Project name: Hackovid
# Course: Python game programming
# Group: 3-1
# Game type: role-playing game
# Engineer: Watson Chao
# Institute: department of Engineering Science - NCKU
# File: config.py

# 設定視窗大小和視窗單位
WIN_WIDTH = 1280
WIN_HEIGHT = 800
TILE_SIZE = 32
# 設定禎數
FPS = 60
# 設定地圖層
ARROW_LAYER = 4
DIALOGUE_BOX_LAYER = 3
PLAYER_LAYER = 2
BLOCK_LAYER = 1
# 設定角色速度
PLAYER_SPEED = 5
BAG_X = 900
BAG_Y = 50
# 設定對話框大小及位置
PLOT_BOX_X = 240
PLOT_BOX_Y = 540
PLOT_BOX_WIDTH = 800
PLOT_BOX_HEIGHT = 200
# 設定文字大小及位置
TEXT_BOX_X = 290
TEXT_BOX_Y = 620
TEXT_BOX_WIDTH = 600
TEXT_BOX_HEIGHT = 120
# 設定
HINT_BOX_X = 340
HINT_BOX_Y = 680
HINT_BOX_WIDTH = 600
HINT_BOX_HEIGHT = 20

HINT_BOX_TYPE_Y = 440
TYPE_BOX_X = 240
TYPE_BOX_Y = 300
TYPE_BOX_WIDTH = 800
TYPE_BOX_HEIGHT = 200

TYPING_AREA_X = 340
TYPING_AREA_Y = 380
TYPING_AREA_WIDTH = 600
TYPING_AREA_HEIGHT = 20


TITLE_TYPE_BOX_X = 290
TITLE_TYPE_BOX_Y = 320
TITLE_TYPE_BOX_WIDTH = 600
TITLE_TYPE_BOX_HEIGHT = 25

SUBTITLE_TYPE_BOX_X = 320
SUBTITLE_TYPE_BOX_Y = 350
SUBTITLE_TYPE_BOX_WIDTH = 600
SUBTITLE_TYPE_BOX_HEIGHT = 25

# 設定對話點大小及位置
DIALOGUE_BOX_X = 240
DIALOGUE_BOX_Y = 540
DIALOGUE_BOX_WIDTH = 800
DIALOGUE_BOX_HEIGHT = 200
# 設定標題大小及位置
TITLE_BOX_X = 290
TITLE_BOX_Y = 560
TITLE_BOX_WIDTH = 600
TITLE_BOX_HEIGHT = 25
# 設定選項指示初始位置
ARROW_X = 290
ARROW_Y = 601
# 設定選項指示大小及位置
ARROW_CHOOSE_ONE_Y = 601
ARROW_CHOOSE_TWO_Y = 631
ARROW_CHOOSE_THREE_Y = 661
ARROW_CHOOSE_FOUR_Y = 691
ARROW_WIDTH = 10
ARROW_HEIGHT = 10

# 設定選項1指示大小及位置
CHOICE_ONE_BOX_X = 340
CHOICE_ONE_BOX_Y = 590
CHOICE_ONE_BOX_WIDTH = 600
CHOICE_ONE_BOX_HEIGHT = 20
# 設定選項2指示大小及位置
CHOICE_TWO_BOX_X = 340
CHOICE_TWO_BOX_Y = 620
CHOICE_TWO_BOX_WIDTH = 600
CHOICE_TWO_BOX_HEIGHT = 20
# 設定選項3指示大小及位置
CHOICE_THREE_BOX_X = 340
CHOICE_THREE_BOX_Y = 650
CHOICE_THREE_BOX_WIDTH = 600
CHOICE_THREE_BOX_HEIGHT = 20
# 設定選項4指示大小及位置
CHOICE_FOUR_BOX_X = 340
CHOICE_FOUR_BOX_Y = 680
CHOICE_FOUR_BOX_WIDTH = 600
CHOICE_FOUR_BOX_HEIGHT = 20
# 設定選項指示大小
CHOOSING_ARROW_WIDTH = 20
CHOOSING_ARROW_HEIGHT = 20

MOM_PATH = ['x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+',
            'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+',
            'x+', 'x+', 'x+', 'x+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+',
            'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+',
            'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', '']

GOVERNMENT_OFFICIAL_PATH = ['y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+',
                            'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+',
                            'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-','x-', 'x-',
                            'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-',
                            'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'y-', 'y-', 'y-', 'y-', 'y-',
                            'y-', 'y-', 'y-', 'y-', 'y-', 'y-', 'y-','y-', 'y-', 'y-', 'y-', 'y-', 'y-',  'y-', '']


BOSS_PATH = ['y-', 'y-', 'y-', 'y-', 'y-', 'y-', 'y-', 'y-', 'y-', 'y-', 'y-', 'y-', 'y-', 'y-', 'y-', 'y-',
             'y-', 'y-', 'y-', 'y-', 'y-', 'y-', 'y-', 'y-', 'y-', 'y-', 'y-', 'y-', 'y-', 'y-', 'y-', 'y-',
             'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-',
             'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-',
             'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-',
             'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+',
             'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+',
             'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+',
             'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', 'y+', '']


GUARD_PATH = ['y-', 'y-', 'y-', 'y-', 'y-', 'y-', 'y-', 'y-', 'y-', 'y-', 'y-', 'y-', 'y-', 'y-', 'y-', 'y-',
              'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-', 'x-', '']

BULLET_PATH = ['x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+',
               'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+',
               'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+',
               'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+',
               'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+',
               'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+',
               'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+',
               'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+',
               'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', 'x+', '']

tilemap = [
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
    'B..CCC..S...A...owE.E.E.B..L.J.T..JA.J.B',
    'B...c...////.... o/.....B..............B',
    'B......./P./....../.....B..............B',
    'Bt....../../......//////B..............B',
    'Brt...../../............B..G/......F/..B',
    'B.K//...................B..//......//..B',
    'B.H/....................B..G/..q...F/..B',
    'B.......................B..//.qaq..//..B',
    'B.......................B..//..q...//..B',
    'B..WWWW...WWWW...WWWW...B....I..I......B',
    'B.......................B..............B',
    'B.......................B....JA.A.J....B',
    'B.......................B..............B',
    'B.......................B..G/......F/..B',
    'B..........................//......//..B',
    'B..R//....R//....R//.......//......//..B',
    'B......................................B',
    'BBBBBBBBBBBBBBBBBBBBBBBBB..............B',
    'MMMMMMMMMMMMMMMMMMMMMMMMB......JAnA.A.JB',
    'MMMMMMMMMMMMMMMMMMMMMMMMB........l.....B',
    'MMMMMMMMMMMMMMMMMMMMMMMMB......m!......B',
    'MMMMMMMMMMMMMMMMMMMMMMMMB..............B',
    'MMMMMMMMMMMMMMMMMMMMMMMMB..............B',
    'MMMMMMMMMMMMMMMMMMMMMMMMBBBBBBBBBBBB.1.B',
]

tilemap_2 = [
    '........................................',
    '.U.....................Q................',
    '........................................',
    '........................................',
    '........................................',
    '................Y.......................',
    '....//////...Z......X.....//////....Z...',
    '..../.2.//........X......./OOO3/.Y....Y.',
    '..../OOO/.....Z...........///OO/..X.Z...',
    '....//OO/.y.............../OOOO/.....Z..',
    '..../OOO/......x.x.x.x..../OOOO/x.x.....',
    '..Y./OOO///////////////////OOOO////x....',
    '..../OOOOOOOOOOOOOOOOOOOOOOOOOOOOOO/x.x.',
    '..Y./OOOOOOOOOOOOOOOOOOOOOOdOOdOOOO/....',
    '..../OOOOOOOOOOOOOOOOOOOOOOOOOOOOO神...1.',
    '..../zzzY//Y//OOOOY///zzzz/////OO神強.....',
    '.V.........../OOOO/.........../OOO神...1.',
    '...........X./OOOOX.........../OO$O.....',
    '............./OOOO/.......b.../OOOO/..1.',
    '........Y..Z./OOOOZ.........../OOOO/....',
    '............./OOOO/............////.....',
    '..1.//////////OOOO/.....................',
    './POOOOOOOOOOOOOOO/.....................',
    './OOOOOOOOOOOOOOOO/.....................',
    './////////////////......................',
]

tilemap_3 = [
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
    'B........JBus...L......D.............C.B',
    'B.........Bs...........................B',
    'B......................................B',
    'B......................................B',
    'B......................................B',
    'B........JB............................B',
    'B....P....B...e/...e/...e/...e/...e/...B',
    'B.........B............................B',
    'BBBB2.2.BBB...H/...H/...H/.....H/.H/...B',
    'MMMMMMMMMMB..........-.........j.......B',
    'MMMMMMMMMMB...e/...e/#..e/...e/hj.e/...B',
    'MMMMMMMMMMB....................j.......B',
    'MMMMMMMMMMB.....H/.H/@..H/...H/...H/...B',
    'MMMMMMMMMMB.....?..........<...........B',
    'MMMMMMMMMMB...e/>?.e/-..e/.,.e/...e/...B',
    'MMMMMMMMMMB.i...?..........<...........B',
    'MMMMMMMMMMB.k.H/...H/...H/.H/.....H/...B',
    'MMMMMMMMMMB.i..........................B',
    'MMMMMMMMMMB............................B',
    'MMMMMMMMMMB............................B',
    'MMMMMMMMMMB............................B',
    'MMMMMMMMMMBf.f.f.f.f.f.f.f.f.f.f.f.f.f.B',
    'MMMMMMMMMMB............................B',
    'MMMMMMMMMMBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
]

tilemap_4 = [
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
    'B..CCC..S...A.....E.E.E.B..L.J.T..JA.J.B',
    'B...c...////....../.....B..............B',
    'B......./../....../.....B..............B',
    'B......./../......//////B..............B',
    'B......./../............B..G.......F...B',
    'B.K//...................B..............B',
    'B.H/....................B..G.......F...B',
    'B.......................B..............B',
    'B.......................B..............B',
    'B..WWWW...WWWW...WWWW...B....I..I......B',
    'B.......................B..............B',
    'B.......................B....JA.A.J....B',
    'B.......................B..............B',
    'B.......................B..G.......F...B',
    'B......................................B',
    'B..R//....R//....R//...................B',
    'B......................................B',
    'BBBBBBBBBBBBBBBBBBBBBBBBB..............B',
    'MMMMMMMMMMMMMMMMMMMMMMMMB......JA.A.A.JB',
    'MMMMMMMMMMMMMMMMMMMMMMMMB..............B',
    'MMMMMMMMMMMMMMMMMMMMMMMMB..............B',
    'MMMMMMMMMMMMMMMMMMMMMMMMB............P.B',
    'MMMMMMMMMMMMMMMMMMMMMMMMB..............B',
    'MMMMMMMMMMMMMMMMMMMMMMMMBBBBBBBBBBBB.1.B',
]

tilemap_5 = [
    '........................................',
    '.U.....................Q................',
    '........................................',
    '........................................',
    '........................................',
    '................Y.......................',
    '....//////...Z......X.....//////....Z...',
    '..../.2.//........X......./OOO3/.Y....Y.',
    '..../OOO/.....Z...........///OO/..X.Z...',
    '....//PO/.y.............../OOOO/.....Z..',
    '..../OOO/......x.x.x.x..../OOOO/x.x.....',
    '..Y./OOO///////////////////OOOO////x....',
    '..../OOOOOOOOOOOOOOOOOOOOOOOOOOOOOO/x.x.',
    '..Y./OOOOOOOOOOOOOOOOOOOOOOdOOdOOOO/....',
    '..../OOOOOOOOOOOOOOOOOOOOOOOOOOOOO神...1.',
    '..../zzzY//Y//OOOOY///zzzz/////OO神強.....',
    '.V.........../OOOO/.........../OOO神...1.',
    '...........X./OOOOX.........../OO$O.....',
    '............./OOOO/.......b.../OOOO/..1.',
    '........Y..Z./OOOOZ.........../OOOO/....',
    '............./OOOO/............////.....',
    '..1.//////////OOOO/.....................',
    './OOOOOOOOOOOOOOOO/.....................',
    './OOOOOOOOOOOOOOOO/.....................',
    './////////////////......................',
]

tilemap_6 = [
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
    'B........JB.....L......D.............C.B',
    'B.........B............................B',
    'B......................................B',
    'B......................................B',
    'B......................................B',
    'B........JB............................B',
    'B....P....B...e/...e/...e/...e/...e/...B',
    'B.........B............................B',
    'BBBB2.2.BBB...H/...H/...H/.....H/.H/...B',
    'MMMMMMMMMMB............................B',
    'MMMMMMMMMMB...e/...e/...e/...e/...e/...B',
    'MMMMMMMMMMB............................B',
    'MMMMMMMMMMB.....H/.H/...H/...H/...H/...B',
    'MMMMMMMMMMB............................B',
    'MMMMMMMMMMB...e/...e/...e/...e/...e/...B',
    'MMMMMMMMMMB............................B',
    'MMMMMMMMMMB...H/...H/...H/.H/.....H/...B',
    'MMMMMMMMMMB............................B',
    'MMMMMMMMMMB............................B',
    'MMMMMMMMMMB............................B',
    'MMMMMMMMMMB............................B',
    'MMMMMMMMMMBf.f.f.f.f.f.f.f.f.f.f.f.f.f.B',
    'MMMMMMMMMMB............................B',
    'MMMMMMMMMMBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
]

tilemap_7 = [
    'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM',
    'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM',
    'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM',
    'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM',
    'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM',
    'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM',
    'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM',
    'MMMMMBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBMMMMM',
    'MMMMMBG/....F/..T/..L『..「W.%..%...BMMMMM',
    'MMMMMB//....//.......』..」/........BMMMMM',
    'MMMMMB//....//..A/.......K//K//K//BMMMMM',
    'MMMMMBG/*.^.F/.......].....v..v...BMMMMM',
    'MMMMMB//....//......][]...........BMMMMM',
    'MMMMMB//....//.......]............BMMMMM',
    'MMMMMBBBBBBBBBBBBBB}..............BMMMMM',
    'MMMMMMMMMMMMMMMMMMB{}...........P.BMMMMM',
    'MMMMMMMMMMMMMMMMMMBR//.R//.R//....BMMMMM',
    'MMMMMMMMMMMMMMMMMMBBBBBBBBBBBB3.3.BMMMMM',
    'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM',
    'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM',
    'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM',
    'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM',
    'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM',
    'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM',
    'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM',
]

tilemap_8 = [
    '........................................',
    '.U.....................Q................',
    '........................................',
    '........................................',
    '........................................',
    '................Y.......................',
    '....//////...Z......X.....//////....Z...',
    '..../.2.//........X......./OOO3/.Y....Y.',
    '..../OOO/.....Z...........///OO/..X.Z...',
    '....//OO/.y.............../OOPO/.....Z..',
    '..../OOO/......x.x.x.x..../OOdO/x.x.....',
    '..Y./OOO///////////////////OOOO////x....',
    '..../OOOOOOOOOOOOOOOOOOOOOOOOOOOOOO/x.x.',
    '..Y./OOOOOOOOOOOOOOOOOOOOOOdOOdOOOO/....',
    '..../OOOOOOOOOOOOOOOOOOOOOOOOOOOOO神...1.',
    '..../zzzY//Y//OOOOY///zzzz/////OO神強.....',
    '.V.........../OOOO/.........../OOO神...1.',
    '...........X./OOOOX.........../OO$O.....',
    '............./OOOO/.......b.../OOOO/..1.',
    '........Y..Z./OOOOZ.........../OOOO/....',
    '............./OOOO/............////.....',
    '..1.//////////OOOO/.....................',
    './OOOOOOOOOOOOOOOO/.....................',
    './OOOOOOOOOOOOOOOO/.....................',
    './////////////////......................',
]

tilemap_9 = [
    '........................................',
    '.U.....................Q................',
    '........................................',
    '........................................',
    '........................................',
    '................Y.......................',
    '....//////...Z......X.....//////....Z...',
    '..../.2.//........X......./OOO3/.Y....Y.',
    '..../OOO/.....Z...........///OO/..X.Z...',
    '....//OO/.y.............../OOOO/.....Z..',
    '..../OOO/......x.x.x.x..../OOOO/x.x.....',
    '..Y./#OO///////////////////OOOO////x....',
    '..../OOOOOOOOOOOOOOOOOOOOOOOOOOOOOO/x.x.',
    '..Y./@OOOOOOOOOOOOOOOOOOOOOOOOOOOOO/....',
    '..../OOOOOOOOOOOOOOOOOOOOOOOOOOOOOO/..1.',
    '..../zzzY//Y//OOOOY///zzzz/////OOOO/....',
    '.V.........../OOOO/.........../OOOO/..1.',
    '...........X./OOOOX.........../OO$O/....',
    '............./OOOO/.......b.../OOOO/..1.',
    '........Y..Z./OOOOZ.........../OOOO/....',
    '............./OOOO/............////.....',
    '..1.//////////OOOO/.....................',
    './POOOOOOOOOOOOOOO/.....................',
    './OOOOOOOOOOOOOOOO/.....................',
    './////////////////......................',
]

tilemap_10 = [
    '........................................',
    '.U.....................Q................',
    '........................................',
    '........................................',
    '........................................',
    '................Y.......................',
    '....//////...Z......X.....//////....Z...',
    '..../.2.//........X......./OOO3/.Y....Y.',
    '..../OOO/.....Z...........///OO/..X.Z...',
    '....//PO/.y.............../OOOO/.....Z..',
    '..../OOO/......x.x.x.x..../OOOO/x.x.....',
    '..Y./#OO///////////////////OOOO////x....',
    '..../OOOOOOOOOOOOOOOOOOOOOOOOOOOOOO/x.x.',
    '..Y./@OOOOOOOOOOOOOOOOOOOOOOOOOOOOO/....',
    '..../OOOOOOOOOOOOOOOOOOOOOOOOOOOOOO/..1.',
    '..../zzzY//Y//OOOOY///zzzz/////OOOO/....',
    '.V.........../OOOO/.........../OOOO/..1.',
    '...........X./OOOOX.........../OO$O/....',
    '............./OOOO/.......b.../OOOO/..1.',
    '........Y..Z./OOOOZ.........../OOOO/....',
    '............./OOOO/............////.....',
    '..1.//////////OOOO/.....................',
    './OOOOOOOOOOOOOOOO/.....................',
    './OOOOOOOOOOOOOOOO/.....................',
    './////////////////......................',
]

tilemap_11 = [
    '........................................',
    '.U.....................Q................',
    '........................................',
    '........................................',
    '........................................',
    '................Y.......................',
    '....//////...Z......X.....//////....Z...',
    '..../.2.//........X......./OOO3/.Y....Y.',
    '..../OOO/.....Z...........///OO/..X.Z...',
    '....//OO/.y.............../OOPO/.....Z..',
    '..../OOO/......x.x.x.x..../OOOO/x.x.....',
    '..Y./#OO///////////////////OOOO////x....',
    '..../OOOOOOOOOOOOOOOOOOOOOOOOOOOOOO/x.x.',
    '..Y./@OOOOOOOOOOOOOOOOOOOOOOOOOOOOO/....',
    '..../OOOOOOOOOOOOOOOOOOOOOOOOOOOOOO/..1.',
    '..../zzzY//Y//OOOOY///zzzz/////OOOO/....',
    '.V.........../OOOO/.........../OOOO/..1.',
    '...........X./OOOOX.........../OO$O/....',
    '............./OOOO/.......b.../OOOO/..1.',
    '........Y..Z./OOOOZ.........../OOOO/....',
    '............./OOOO/............////.....',
    '..1.//////////OOOO/.....................',
    './OOOOOOOOOOOOOOOO/.....................',
    './OOOOOOOOOOOOOOOO/.....................',
    './////////////////......................',
]

tilemap_12 = [
    'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM',
    'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM',
    'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM',
    'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM',
    'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM',
    'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM',
    'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM',
    'MMMMMBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBMMMMM',
    'MMMMMBG/....F/..T/..L....W.%..%...BMMMMM',
    'MMMMMB//....//.........../........BMMMMM',
    'MMMMMB//....//..A/.......K//K//K//BMMMMM',
    'MMMMMBG/*.^.F/.......].....v..v...BMMMMM',
    'MMMMMB//....//......][]...........BMMMMM',
    'MMMMMB//....//.......]............BMMMMM',
    'MMMMMBBBBBBBBBBBBBB...............BMMMMM',
    'MMMMMMMMMMMMMMMMMMB.............P.BMMMMM',
    'MMMMMMMMMMMMMMMMMMBR//.R//.R//....BMMMMM',
    'MMMMMMMMMMMMMMMMMMBBBBBBBBBBBB3.3.BMMMMM',
    'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM',
    'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM',
    'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM',
    'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM',
    'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM',
    'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM',
    'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM',
]