import game
import numpy as np


game1 = game.Game()
# game1.play(cpu_vs_cpu=True, alpha_beta_vs_min_max=True, empty_adjacent_cells_node_choice_player_1=True, empty_adjacent_cells_node_choice_player_2=True)

# ******************************MIN-MAX vs MIN-MAX******************************

# **001** MIN-MAX 1 heurystyka / 1 heurystyka vs MIN-MAX 1 heurystyka / 1 heurystyka

# **002** MIN-MAX 1 heurystyka / 1 heurystyka vs MIN-MAX 2 heurystyka / 1 heurystyka

# **003** MIN-MAX 1 heurystyka / 1 heurystyka vs MIN-MAX 3 heurystyka / 1 heurystyka

# **004** MIN-MAX 1 heurystyka / 1 heurystyka vs MIN-MAX 1 heurystyka / 2 heurystyka

# **005** MIN-MAX 1 heurystyka / 1 heurystyka vs MIN-MAX 2 heurystyka / 2 heurystyka

# **006** MIN-MAX 1 heurystyka / 1 heurystyka vs MIN-MAX 3 heurystyka / 2 heurystyka

# **007** MIN-MAX 2 heurystyka / 1 heurystyka vs MIN-MAX 1 heurystyka / 1 heurystyka

# **008** MIN-MAX 2 heurystyka / 1 heurystyka vs MIN-MAX 2 heurystyka / 1 heurystyka

# **009** MIN-MAX 2 heurystyka / 1 heurystyka vs MIN-MAX 3 heurystyka / 1 heurystyka

# **010** MIN-MAX 2 heurystyka / 1 heurystyka vs MIN-MAX 1 heurystyka / 2 heurystyka

# **011** MIN-MAX 2 heurystyka / 1 heurystyka vs MIN-MAX 2 heurystyka / 2 heurystyka

# **012** MIN-MAX 2 heurystyka / 1 heurystyka vs MIN-MAX 3 heurystyka / 2 heurystyka

# **013** MIN-MAX 3 heurystyka / 1 heurystyka vs MIN-MAX 1 heurystyka / 1 heurystyka

# **014** MIN-MAX 3 heurystyka / 1 heurystyka vs MIN-MAX 2 heurystyka / 1 heurystyka

# **015** MIN-MAX 3 heurystyka / 1 heurystyka vs MIN-MAX 3 heurystyka / 1 heurystyka

# **016** MIN-MAX 3 heurystyka / 1 heurystyka vs MIN-MAX 1 heurystyka / 2 heurystyka

# **017** MIN-MAX 3 heurystyka / 1 heurystyka vs MIN-MAX 2 heurystyka / 2 heurystyka

# **018** MIN-MAX 3 heurystyka / 1 heurystyka vs MIN-MAX 3 heurystyka / 2 heurystyka

# **019** MIN-MAX 1 heurystyka / 2 heurystyka vs MIN-MAX 1 heurystyka / 1 heurystyka

# **020** MIN-MAX 1 heurystyka / 2 heurystyka vs MIN-MAX 2 heurystyka / 1 heurystyka

# **021** MIN-MAX 1 heurystyka / 2 heurystyka vs MIN-MAX 3 heurystyka / 1 heurystyka

# **022** MIN-MAX 1 heurystyka / 2 heurystyka vs MIN-MAX 1 heurystyka / 2 heurystyka

# **023** MIN-MAX 1 heurystyka / 2 heurystyka vs MIN-MAX 2 heurystyka / 2 heurystyka

# **024** MIN-MAX 1 heurystyka / 2 heurystyka vs MIN-MAX 3 heurystyka / 2 heurystyka

# **025** MIN-MAX 2 heurystyka / 2 heurystyka vs MIN-MAX 1 heurystyka / 1 heurystyka

# **026** MIN-MAX 2 heurystyka / 2 heurystyka vs MIN-MAX 2 heurystyka / 1 heurystyka

# **027** MIN-MAX 2 heurystyka / 2 heurystyka vs MIN-MAX 3 heurystyka / 1 heurystyka

# **028** MIN-MAX 2 heurystyka / 2 heurystyka vs MIN-MAX 1 heurystyka / 2 heurystyka

# **029** MIN-MAX 2 heurystyka / 2 heurystyka vs MIN-MAX 2 heurystyka / 2 heurystyka

# **030** MIN-MAX 2 heurystyka / 2 heurystyka vs MIN-MAX 3 heurystyka / 2 heurystyka

# **031** MIN-MAX 3 heurystyka / 2 heurystyka vs MIN-MAX 1 heurystyka / 1 heurystyka

# **032** MIN-MAX 3 heurystyka / 2 heurystyka vs MIN-MAX 2 heurystyka / 1 heurystyka

# **033** MIN-MAX 3 heurystyka / 2 heurystyka vs MIN-MAX 3 heurystyka / 1 heurystyka

# **034** MIN-MAX 3 heurystyka / 2 heurystyka vs MIN-MAX 1 heurystyka / 2 heurystyka

# **035** MIN-MAX 3 heurystyka / 2 heurystyka vs MIN-MAX 2 heurystyka / 2 heurystyka

# **036** MIN-MAX 3 heurystyka / 2 heurystyka vs MIN-MAX 3 heurystyka / 2 heurystyka

# ******************************MIN-MAX vs ALPHA-BETA******************************

# **037** MIN-MAX 1 heurystyka / 1 heurystyka vs ALPHA-BETA 1 heurystyka / 1 heurystyka

# **038** MIN-MAX 1 heurystyka / 1 heurystyka vs ALPHA-BETA 2 heurystyka / 1 heurystyka

# **039** MIN-MAX 1 heurystyka / 1 heurystyka vs ALPHA-BETA 3 heurystyka / 1 heurystyka

# **040** MIN-MAX 1 heurystyka / 1 heurystyka vs ALPHA-BETA 1 heurystyka / 2 heurystyka

# **041** MIN-MAX 1 heurystyka / 1 heurystyka vs ALPHA-BETA 2 heurystyka / 2 heurystyka

# **042** MIN-MAX 1 heurystyka / 1 heurystyka vs ALPHA-BETA 3 heurystyka / 2 heurystyka

# **043** MIN-MAX 2 heurystyka / 1 heurystyka vs ALPHA-BETA 1 heurystyka / 1 heurystyka

# **044** MIN-MAX 2 heurystyka / 1 heurystyka vs ALPHA-BETA 2 heurystyka / 1 heurystyka

# **045** MIN-MAX 2 heurystyka / 1 heurystyka vs ALPHA-BETA 3 heurystyka / 1 heurystyka

# **046** MIN-MAX 2 heurystyka / 1 heurystyka vs ALPHA-BETA 1 heurystyka / 2 heurystyka

# **047** MIN-MAX 2 heurystyka / 1 heurystyka vs ALPHA-BETA 2 heurystyka / 2 heurystyka

# **048** MIN-MAX 2 heurystyka / 1 heurystyka vs ALPHA-BETA 3 heurystyka / 2 heurystyka

# **049** MIN-MAX 3 heurystyka / 1 heurystyka vs ALPHA-BETA 1 heurystyka / 1 heurystyka

# **050** MIN-MAX 3 heurystyka / 1 heurystyka vs ALPHA-BETA 2 heurystyka / 1 heurystyka

# **051** MIN-MAX 3 heurystyka / 1 heurystyka vs ALPHA-BETA 3 heurystyka / 1 heurystyka

# **052** MIN-MAX 3 heurystyka / 1 heurystyka vs ALPHA-BETA 1 heurystyka / 2 heurystyka

# **053** MIN-MAX 3 heurystyka / 1 heurystyka vs ALPHA-BETA 2 heurystyka / 2 heurystyka

# **054** MIN-MAX 3 heurystyka / 1 heurystyka vs ALPHA-BETA 3 heurystyka / 2 heurystyka

# **055** MIN-MAX 1 heurystyka / 2 heurystyka vs ALPHA-BETA 1 heurystyka / 1 heurystyka

# **056** MIN-MAX 1 heurystyka / 2 heurystyka vs ALPHA-BETA 2 heurystyka / 1 heurystyka

# **057** MIN-MAX 1 heurystyka / 2 heurystyka vs ALPHA-BETA 3 heurystyka / 1 heurystyka

# **058** MIN-MAX 1 heurystyka / 2 heurystyka vs ALPHA-BETA 1 heurystyka / 2 heurystyka

# **059** MIN-MAX 1 heurystyka / 2 heurystyka vs ALPHA-BETA 2 heurystyka / 2 heurystyka

# **060** MIN-MAX 1 heurystyka / 2 heurystyka vs ALPHA-BETA 3 heurystyka / 2 heurystyka

# **061** MIN-MAX 2 heurystyka / 2 heurystyka vs ALPHA-BETA 1 heurystyka / 1 heurystyka

# **062** MIN-MAX 2 heurystyka / 2 heurystyka vs ALPHA-BETA 2 heurystyka / 1 heurystyka

# **063** MIN-MAX 2 heurystyka / 2 heurystyka vs ALPHA-BETA 3 heurystyka / 1 heurystyka

# **064** MIN-MAX 2 heurystyka / 2 heurystyka vs ALPHA-BETA 1 heurystyka / 2 heurystyka

# **065** MIN-MAX 2 heurystyka / 2 heurystyka vs ALPHA-BETA 2 heurystyka / 2 heurystyka

# **066** MIN-MAX 2 heurystyka / 2 heurystyka vs ALPHA-BETA 3 heurystyka / 2 heurystyka

# **067** MIN-MAX 3 heurystyka / 2 heurystyka vs ALPHA-BETA 1 heurystyka / 1 heurystyka

# **068** MIN-MAX 3 heurystyka / 2 heurystyka vs ALPHA-BETA 2 heurystyka / 1 heurystyka

# **069** MIN-MAX 3 heurystyka / 2 heurystyka vs ALPHA-BETA 3 heurystyka / 1 heurystyka

# **070** MIN-MAX 3 heurystyka / 2 heurystyka vs ALPHA-BETA 1 heurystyka / 2 heurystyka

# **071** MIN-MAX 3 heurystyka / 2 heurystyka vs ALPHA-BETA 2 heurystyka / 2 heurystyka

# **072** MIN-MAX 3 heurystyka / 2 heurystyka vs ALPHA-BETA 3 heurystyka / 2 heurystyka

# ******************************ALPHA-BETA vs MIN-MAX******************************

# **073** ALPHA-BETA 1 heurystyka / 1 heurystyka vs MIN-MAX 1 heurystyka / 1 heurystyka

# **074** ALPHA-BETA 1 heurystyka / 1 heurystyka vs MIN-MAX 2 heurystyka / 1 heurystyka

# **075** ALPHA-BETA 1 heurystyka / 1 heurystyka vs MIN-MAX 3 heurystyka / 1 heurystyka

# **076** ALPHA-BETA 1 heurystyka / 1 heurystyka vs MIN-MAX 1 heurystyka / 2 heurystyka

# **077** ALPHA-BETA 1 heurystyka / 1 heurystyka vs MIN-MAX 2 heurystyka / 2 heurystyka

# **078** ALPHA-BETA 1 heurystyka / 1 heurystyka vs MIN-MAX 3 heurystyka / 2 heurystyka

# **079** ALPHA-BETA 2 heurystyka / 1 heurystyka vs MIN-MAX 1 heurystyka / 1 heurystyka

# **080** ALPHA-BETA 2 heurystyka / 1 heurystyka vs MIN-MAX 2 heurystyka / 1 heurystyka

# **081** ALPHA-BETA 2 heurystyka / 1 heurystyka vs MIN-MAX 3 heurystyka / 1 heurystyka

# **082** ALPHA-BETA 2 heurystyka / 1 heurystyka vs MIN-MAX 1 heurystyka / 2 heurystyka

# **083** ALPHA-BETA 2 heurystyka / 1 heurystyka vs MIN-MAX 2 heurystyka / 2 heurystyka

# **084** ALPHA-BETA 2 heurystyka / 1 heurystyka vs MIN-MAX 3 heurystyka / 2 heurystyka

# **085** ALPHA-BETA 3 heurystyka / 1 heurystyka vs MIN-MAX 1 heurystyka / 1 heurystyka

# **086** ALPHA-BETA 3 heurystyka / 1 heurystyka vs MIN-MAX 2 heurystyka / 1 heurystyka

# **087** ALPHA-BETA 3 heurystyka / 1 heurystyka vs MIN-MAX 3 heurystyka / 1 heurystyka

# **088** ALPHA-BETA 3 heurystyka / 1 heurystyka vs MIN-MAX 1 heurystyka / 2 heurystyka

# **089** ALPHA-BETA 3 heurystyka / 1 heurystyka vs MIN-MAX 2 heurystyka / 2 heurystyka

# **090** ALPHA-BETA 3 heurystyka / 1 heurystyka vs MIN-MAX 3 heurystyka / 2 heurystyka

# **091** ALPHA-BETA 1 heurystyka / 2 heurystyka vs MIN-MAX 1 heurystyka / 1 heurystyka

# **092** ALPHA-BETA 1 heurystyka / 2 heurystyka vs MIN-MAX 2 heurystyka / 1 heurystyka

# **093** ALPHA-BETA 1 heurystyka / 2 heurystyka vs MIN-MAX 3 heurystyka / 1 heurystyka

# **094** ALPHA-BETA 1 heurystyka / 2 heurystyka vs MIN-MAX 1 heurystyka / 2 heurystyka

# **095** ALPHA-BETA 1 heurystyka / 2 heurystyka vs MIN-MAX 2 heurystyka / 2 heurystyka

# **096** ALPHA-BETA 1 heurystyka / 2 heurystyka vs MIN-MAX 3 heurystyka / 2 heurystyka

# **097** ALPHA-BETA 2 heurystyka / 2 heurystyka vs MIN-MAX 1 heurystyka / 1 heurystyka

# **098** ALPHA-BETA 2 heurystyka / 2 heurystyka vs MIN-MAX 2 heurystyka / 1 heurystyka

# **099** ALPHA-BETA 2 heurystyka / 2 heurystyka vs MIN-MAX 3 heurystyka / 1 heurystyka

# **100** ALPHA-BETA 2 heurystyka / 2 heurystyka vs MIN-MAX 1 heurystyka / 2 heurystyka

# **101** ALPHA-BETA 2 heurystyka / 2 heurystyka vs MIN-MAX 2 heurystyka / 2 heurystyka

# **102** ALPHA-BETA 2 heurystyka / 2 heurystyka vs MIN-MAX 3 heurystyka / 2 heurystyka

# **103** ALPHA-BETA 3 heurystyka / 2 heurystyka vs MIN-MAX 1 heurystyka / 1 heurystyka

# **104** ALPHA-BETA 3 heurystyka / 2 heurystyka vs MIN-MAX 2 heurystyka / 1 heurystyka

# **105** ALPHA-BETA 3 heurystyka / 2 heurystyka vs MIN-MAX 3 heurystyka / 1 heurystyka

# **106** ALPHA-BETA 3 heurystyka / 2 heurystyka vs MIN-MAX 1 heurystyka / 2 heurystyka

# **107** ALPHA-BETA 3 heurystyka / 2 heurystyka vs MIN-MAX 2 heurystyka / 2 heurystyka

# **108** ALPHA-BETA 3 heurystyka / 2 heurystyka vs MIN-MAX 3 heurystyka / 2 heurystyka

# ******************************ALPHA-BETA vs ALPHA-BETA******************************

# **109** ALPHA-BETA 1 heurystyka / 1 heurystyka vs ALPHA-BETA 1 heurystyka / 1 heurystyka

# **110** ALPHA-BETA 1 heurystyka / 1 heurystyka vs ALPHA-BETA 2 heurystyka / 1 heurystyka

# **111** ALPHA-BETA 1 heurystyka / 1 heurystyka vs ALPHA-BETA 3 heurystyka / 1 heurystyka

# **112** ALPHA-BETA 1 heurystyka / 1 heurystyka vs ALPHA-BETA 1 heurystyka / 2 heurystyka

# **113** ALPHA-BETA 1 heurystyka / 1 heurystyka vs ALPHA-BETA 2 heurystyka / 2 heurystyka

# **114** ALPHA-BETA 1 heurystyka / 1 heurystyka vs ALPHA-BETA 3 heurystyka / 2 heurystyka

# **115** ALPHA-BETA 2 heurystyka / 1 heurystyka vs ALPHA-BETA 1 heurystyka / 1 heurystyka

# **116** ALPHA-BETA 2 heurystyka / 1 heurystyka vs ALPHA-BETA 2 heurystyka / 1 heurystyka

# **117** ALPHA-BETA 2 heurystyka / 1 heurystyka vs ALPHA-BETA 3 heurystyka / 1 heurystyka

# **118** ALPHA-BETA 2 heurystyka / 1 heurystyka vs ALPHA-BETA 1 heurystyka / 2 heurystyka

# **119** ALPHA-BETA 2 heurystyka / 1 heurystyka vs ALPHA-BETA 2 heurystyka / 2 heurystyka

# **120** ALPHA-BETA 2 heurystyka / 1 heurystyka vs ALPHA-BETA 3 heurystyka / 2 heurystyka

# **121** ALPHA-BETA 3 heurystyka / 1 heurystyka vs ALPHA-BETA 1 heurystyka / 1 heurystyka

# **122** ALPHA-BETA 3 heurystyka / 1 heurystyka vs ALPHA-BETA 2 heurystyka / 1 heurystyka

# **123** ALPHA-BETA 3 heurystyka / 1 heurystyka vs ALPHA-BETA 3 heurystyka / 1 heurystyka

game1.play(cpu_vs_cpu=True, alpha_beta_vs_alpha_beta=True)

# **124** ALPHA-BETA 3 heurystyka / 1 heurystyka vs ALPHA-BETA 1 heurystyka / 2 heurystyka

# **125** ALPHA-BETA 3 heurystyka / 1 heurystyka vs ALPHA-BETA 2 heurystyka / 2 heurystyka

# **126** ALPHA-BETA 3 heurystyka / 1 heurystyka vs ALPHA-BETA 3 heurystyka / 2 heurystyka

# **127** ALPHA-BETA 1 heurystyka / 2 heurystyka vs ALPHA-BETA 1 heurystyka / 1 heurystyka

# **128** ALPHA-BETA 1 heurystyka / 2 heurystyka vs ALPHA-BETA 2 heurystyka / 1 heurystyka

# **129** ALPHA-BETA 1 heurystyka / 2 heurystyka vs ALPHA-BETA 3 heurystyka / 1 heurystyka

# **130** ALPHA-BETA 1 heurystyka / 2 heurystyka vs ALPHA-BETA 1 heurystyka / 2 heurystyka

# **131** ALPHA-BETA 1 heurystyka / 2 heurystyka vs ALPHA-BETA 2 heurystyka / 2 heurystyka

# **132** ALPHA-BETA 1 heurystyka / 2 heurystyka vs ALPHA-BETA 3 heurystyka / 2 heurystyka

# **133** ALPHA-BETA 2 heurystyka / 2 heurystyka vs ALPHA-BETA 1 heurystyka / 1 heurystyka

# **134** ALPHA-BETA 2 heurystyka / 2 heurystyka vs ALPHA-BETA 2 heurystyka / 1 heurystyka

# **135** ALPHA-BETA 2 heurystyka / 2 heurystyka vs ALPHA-BETA 3 heurystyka / 1 heurystyka

# **136** ALPHA-BETA 2 heurystyka / 2 heurystyka vs ALPHA-BETA 1 heurystyka / 2 heurystyka

# **137** ALPHA-BETA 2 heurystyka / 2 heurystyka vs ALPHA-BETA 2 heurystyka / 2 heurystyka

# **138** ALPHA-BETA 2 heurystyka / 2 heurystyka vs ALPHA-BETA 3 heurystyka / 2 heurystyka

# **139** ALPHA-BETA 3 heurystyka / 2 heurystyka vs ALPHA-BETA 1 heurystyka / 1 heurystyka

# **140** ALPHA-BETA 3 heurystyka / 2 heurystyka vs ALPHA-BETA 2 heurystyka / 1 heurystyka

# **141** ALPHA-BETA 3 heurystyka / 2 heurystyka vs ALPHA-BETA 3 heurystyka / 1 heurystyka

# **142** ALPHA-BETA 3 heurystyka / 2 heurystyka vs ALPHA-BETA 1 heurystyka / 2 heurystyka

# **143** ALPHA-BETA 3 heurystyka / 2 heurystyka vs ALPHA-BETA 2 heurystyka / 2 heurystyka

# **144** ALPHA-BETA 3 heurystyka / 2 heurystyka vs ALPHA-BETA 3 heurystyka / 2 heurystyka

