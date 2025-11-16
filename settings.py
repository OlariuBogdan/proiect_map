# Display settings
DEFAULT_IMAGE_SIZE = (300, 300)
FPS = 120
HEIGHT = 1000
WIDTH = 1600
START_X, START_Y = 0, -300
X_OFFSET, Y_OFFSET = 20, 0

# Images
BG_IMAGE_PATH = 'graphics/0/bg.png'
GRID_IMAGE_PATH = 'graphics/0/gridline.png'
GAME_INDICES = [1, 2, 3] # 0 and 4 are outside of play area
SYM_PATH = 'graphics/0/symbols'

# Text
TEXT_COLOR = 'White'
# You need to provide your own font in the below directory
# I downloaded Kidspace font from https://www.dafont.com/kidspace.font
UI_FONT = 'graphics/font/kidspace.ttf'
UI_FONT_SIZE = 25
WIN_FONT_SIZE = 110


symbols = {
    'gagica': f"{SYM_PATH}/gagica copy.png", 
    'salba': f"{SYM_PATH}/salba de bani.png",
    'caruta': f"{SYM_PATH}/caruta copy.png",
    'tamburina': f"{SYM_PATH}/tamburina.png",
    'tiganu': f"{SYM_PATH}/tiganu.png",
    'acordeon': f"{SYM_PATH}/acordeon copy.png",
    'cal': f"{SYM_PATH}/cal nou  50 update copy.png"
}
