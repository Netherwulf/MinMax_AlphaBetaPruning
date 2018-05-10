import game
import numpy as np


game1 = game.Game()
# game1.play(cpu_vs_cpu=True, alpha_beta_vs_min_max=True, empty_adjacent_cells_node_choice_player_1=True, empty_adjacent_cells_node_choice_player_2=True)
game1.play(cpu_vs_cpu=True, alpha_beta_vs_alpha_beta=True)
# game1.play(human_player_one=True)
