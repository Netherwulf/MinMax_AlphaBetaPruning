import game
import numpy as np


game1 = game.Game()
game1.play(cpu_vs_cpu=True, alpha_beta_vs_alpha_beta=True, random_node_choice_player_1=True, random_node_choice_player_2=False)
# x = np.arange(9).reshape(3, 3)
# print(x)
# # print(np.where(x > 5))
# print(np.diag(np.fliplr(x)))
