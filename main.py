import game
import numpy as np

number_of_rounds = 5

# game1 = game.Game()
# game1.play(cpu_vs_cpu=True, alpha_beta_vs_min_max=True, empty_adjacent_cells_node_choice_player_1=True, empty_adjacent_cells_node_choice_player_2=True)

# ******************************MIN-MAX vs MIN-MAX******************************

# **001** MIN-MAX 1 heurystyka / 1 heurystyka vs MIN-MAX 1 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_min_max=True, rating_method_one_player_one=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_one_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
    print("Policzyłem: " + str(i))
print("**001** MIN-MAX 1 heurystyka / 1 heurystyka vs MIN-MAX 1 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **002** MIN-MAX 1 heurystyka / 1 heurystyka vs MIN-MAX 2 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_min_max=True, rating_method_one_player_one=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_two_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**002** MIN-MAX 1 heurystyka / 1 heurystyka vs MIN-MAX 2 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **003** MIN-MAX 1 heurystyka / 1 heurystyka vs MIN-MAX 3 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_min_max=True, rating_method_one_player_one=True, empty_adjacent_cells_node_choice_player_1=True, empty_adjacent_cells_node_choice_player_2=True)
print("**003** MIN-MAX 1 heurystyka / 1 heurystyka vs MIN-MAX 3 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **004** MIN-MAX 1 heurystyka / 1 heurystyka vs MIN-MAX 1 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_min_max=True, rating_method_one_player_one=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_one_player_two=True, random_node_choice_player_2=True)
print("**004** MIN-MAX 1 heurystyka / 1 heurystyka vs MIN-MAX 1 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **005** MIN-MAX 1 heurystyka / 1 heurystyka vs MIN-MAX 2 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_min_max=True, rating_method_one_player_one=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_two_player_two=True, random_node_choice_player_2=True)
print("**005** MIN-MAX 1 heurystyka / 1 heurystyka vs MIN-MAX 2 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **006** MIN-MAX 1 heurystyka / 1 heurystyka vs MIN-MAX 3 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_min_max=True, rating_method_one_player_one=True, empty_adjacent_cells_node_choice_player_1=True, random_node_choice_player_2=True)
print("**006** MIN-MAX 1 heurystyka / 1 heurystyka vs MIN-MAX 3 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **007** MIN-MAX 2 heurystyka / 1 heurystyka vs MIN-MAX 1 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_min_max=True, rating_method_two_player_one=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_one_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**007** MIN-MAX 2 heurystyka / 1 heurystyka vs MIN-MAX 1 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **008** MIN-MAX 2 heurystyka / 1 heurystyka vs MIN-MAX 2 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_min_max=True, rating_method_two_player_one=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_two_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**008** MIN-MAX 2 heurystyka / 1 heurystyka vs MIN-MAX 2 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **009** MIN-MAX 2 heurystyka / 1 heurystyka vs MIN-MAX 3 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_min_max=True, rating_method_two_player_one=True, empty_adjacent_cells_node_choice_player_1=True, empty_adjacent_cells_node_choice_player_2=True)
print("**009** MIN-MAX 2 heurystyka / 1 heurystyka vs MIN-MAX 3 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **010** MIN-MAX 2 heurystyka / 1 heurystyka vs MIN-MAX 1 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_min_max=True, rating_method_two_player_one=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_one_player_two=True, random_node_choice_player_2=True)
print("**010** MIN-MAX 2 heurystyka / 1 heurystyka vs MIN-MAX 1 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **011** MIN-MAX 2 heurystyka / 1 heurystyka vs MIN-MAX 2 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_min_max=True, rating_method_two_player_one=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_two_player_two=True, random_node_choice_player_2=True)
print("**011** MIN-MAX 2 heurystyka / 1 heurystyka vs MIN-MAX 2 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **012** MIN-MAX 2 heurystyka / 1 heurystyka vs MIN-MAX 3 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_min_max=True, rating_method_two_player_one=True, empty_adjacent_cells_node_choice_player_1=True, random_node_choice_player_2=True)
print("**012** MIN-MAX 2 heurystyka / 1 heurystyka vs MIN-MAX 3 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **013** MIN-MAX 3 heurystyka / 1 heurystyka vs MIN-MAX 1 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_min_max=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_one_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**013** MIN-MAX 3 heurystyka / 1 heurystyka vs MIN-MAX 1 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **014** MIN-MAX 3 heurystyka / 1 heurystyka vs MIN-MAX 2 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_min_max=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_two_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**014** MIN-MAX 3 heurystyka / 1 heurystyka vs MIN-MAX 2 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **015** MIN-MAX 3 heurystyka / 1 heurystyka vs MIN-MAX 3 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_min_max=True, empty_adjacent_cells_node_choice_player_1=True, empty_adjacent_cells_node_choice_player_2=True)
print("**015** MIN-MAX 3 heurystyka / 1 heurystyka vs MIN-MAX 3 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **016** MIN-MAX 3 heurystyka / 1 heurystyka vs MIN-MAX 1 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_min_max=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_one_player_two=True, random_node_choice_player_2=True)
print("**016** MIN-MAX 3 heurystyka / 1 heurystyka vs MIN-MAX 1 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **017** MIN-MAX 3 heurystyka / 1 heurystyka vs MIN-MAX 2 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_min_max=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_two_player_two=True, random_node_choice_player_2=True)
print("**017** MIN-MAX 3 heurystyka / 1 heurystyka vs MIN-MAX 2 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **018** MIN-MAX 3 heurystyka / 1 heurystyka vs MIN-MAX 3 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_min_max=True, empty_adjacent_cells_node_choice_player_1=True, random_node_choice_player_2=True)
print("**018** MIN-MAX 3 heurystyka / 1 heurystyka vs MIN-MAX 3 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **019** MIN-MAX 1 heurystyka / 2 heurystyka vs MIN-MAX 1 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_min_max=True, rating_method_one_player_one=True, random_node_choice_player_1=True, rating_method_one_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**019** MIN-MAX 1 heurystyka / 2 heurystyka vs MIN-MAX 1 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **020** MIN-MAX 1 heurystyka / 2 heurystyka vs MIN-MAX 2 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_min_max=True, rating_method_one_player_one=True, random_node_choice_player_1=True, rating_method_two_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**020** MIN-MAX 1 heurystyka / 2 heurystyka vs MIN-MAX 2 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **021** MIN-MAX 1 heurystyka / 2 heurystyka vs MIN-MAX 3 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_min_max=True, rating_method_one_player_one=True, random_node_choice_player_1=True, empty_adjacent_cells_node_choice_player_2=True)
print("**021** MIN-MAX 1 heurystyka / 2 heurystyka vs MIN-MAX 3 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **022** MIN-MAX 1 heurystyka / 2 heurystyka vs MIN-MAX 1 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_min_max=True, rating_method_one_player_one=True, random_node_choice_player_1=True, rating_method_one_player_two=True, random_node_choice_player_2=True)
print("**022** MIN-MAX 1 heurystyka / 2 heurystyka vs MIN-MAX 1 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **023** MIN-MAX 1 heurystyka / 2 heurystyka vs MIN-MAX 2 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_min_max=True, rating_method_one_player_one=True, random_node_choice_player_1=True, rating_method_two_player_two=True, random_node_choice_player_2=True)
print("**023** MIN-MAX 1 heurystyka / 2 heurystyka vs MIN-MAX 2 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **024** MIN-MAX 1 heurystyka / 2 heurystyka vs MIN-MAX 3 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_min_max=True, rating_method_one_player_one=True, random_node_choice_player_1=True, random_node_choice_player_2=True)
print("**024** MIN-MAX 1 heurystyka / 2 heurystyka vs MIN-MAX 3 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **025** MIN-MAX 2 heurystyka / 2 heurystyka vs MIN-MAX 1 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_min_max=True, rating_method_two_player_one=True, random_node_choice_player_1=True, rating_method_one_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**025** MIN-MAX 2 heurystyka / 2 heurystyka vs MIN-MAX 1 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **026** MIN-MAX 2 heurystyka / 2 heurystyka vs MIN-MAX 2 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_min_max=True, rating_method_two_player_one=True, random_node_choice_player_1=True, rating_method_two_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**026** MIN-MAX 2 heurystyka / 2 heurystyka vs MIN-MAX 2 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **027** MIN-MAX 2 heurystyka / 2 heurystyka vs MIN-MAX 3 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_min_max=True, rating_method_two_player_one=True, random_node_choice_player_1=True, empty_adjacent_cells_node_choice_player_2=True)
print("**027** MIN-MAX 2 heurystyka / 2 heurystyka vs MIN-MAX 3 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **028** MIN-MAX 2 heurystyka / 2 heurystyka vs MIN-MAX 1 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_min_max=True, rating_method_two_player_one=True, random_node_choice_player_1=True, rating_method_one_player_two=True, random_node_choice_player_2=True)
print("**028** MIN-MAX 2 heurystyka / 2 heurystyka vs MIN-MAX 1 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **029** MIN-MAX 2 heurystyka / 2 heurystyka vs MIN-MAX 2 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_min_max=True, rating_method_two_player_one=True, random_node_choice_player_1=True, rating_method_two_player_two=True, random_node_choice_player_2=True)
print("**029** MIN-MAX 2 heurystyka / 2 heurystyka vs MIN-MAX 2 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **030** MIN-MAX 2 heurystyka / 2 heurystyka vs MIN-MAX 3 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_min_max=True, rating_method_two_player_one=True, random_node_choice_player_1=True, random_node_choice_player_2=True)
print("**030** MIN-MAX 2 heurystyka / 2 heurystyka vs MIN-MAX 3 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **031** MIN-MAX 3 heurystyka / 2 heurystyka vs MIN-MAX 1 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_min_max=True, random_node_choice_player_1=True, rating_method_one_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**031** MIN-MAX 3 heurystyka / 2 heurystyka vs MIN-MAX 1 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **032** MIN-MAX 3 heurystyka / 2 heurystyka vs MIN-MAX 2 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_min_max=True, random_node_choice_player_1=True, rating_method_two_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**032** MIN-MAX 3 heurystyka / 2 heurystyka vs MIN-MAX 2 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **033** MIN-MAX 3 heurystyka / 2 heurystyka vs MIN-MAX 3 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_min_max=True, random_node_choice_player_1=True, empty_adjacent_cells_node_choice_player_2=True)
print("**033** MIN-MAX 3 heurystyka / 2 heurystyka vs MIN-MAX 3 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **034** MIN-MAX 3 heurystyka / 2 heurystyka vs MIN-MAX 1 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_min_max=True, random_node_choice_player_1=True, rating_method_one_player_two=True, random_node_choice_player_2=True)
print("**034** MIN-MAX 3 heurystyka / 2 heurystyka vs MIN-MAX 1 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **035** MIN-MAX 3 heurystyka / 2 heurystyka vs MIN-MAX 2 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_min_max=True, random_node_choice_player_1=True, rating_method_two_player_two=True, random_node_choice_player_2=True)
print("**035** MIN-MAX 3 heurystyka / 2 heurystyka vs MIN-MAX 2 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **036** MIN-MAX 3 heurystyka / 2 heurystyka vs MIN-MAX 3 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_min_max=True, random_node_choice_player_1=True, random_node_choice_player_2=True)
print("**036** MIN-MAX 3 heurystyka / 2 heurystyka vs MIN-MAX 3 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# ************************************************************MIN-MAX vs ALPHA-BETA************************************************************

# **037** MIN-MAX 1 heurystyka / 1 heurystyka vs ALPHA-BETA 1 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_alpha_beta=True, rating_method_one_player_one=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_one_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**037** MIN-MAX 1 heurystyka / 1 heurystyka vs ALPHA-BETA 1 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **038** MIN-MAX 1 heurystyka / 1 heurystyka vs ALPHA-BETA 2 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_alpha_beta=True, rating_method_one_player_one=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_two_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**038** MIN-MAX 1 heurystyka / 1 heurystyka vs ALPHA-BETA 2 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **039** MIN-MAX 1 heurystyka / 1 heurystyka vs ALPHA-BETA 3 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_alpha_beta=True, rating_method_one_player_one=True, empty_adjacent_cells_node_choice_player_1=True, empty_adjacent_cells_node_choice_player_2=True)
print("**039** MIN-MAX 1 heurystyka / 1 heurystyka vs ALPHA-BETA 3 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **040** MIN-MAX 1 heurystyka / 1 heurystyka vs ALPHA-BETA 1 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_alpha_beta=True, rating_method_one_player_one=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_one_player_two=True, random_node_choice_player_2=True)
print("**040** MIN-MAX 1 heurystyka / 1 heurystyka vs ALPHA-BETA 1 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **041** MIN-MAX 1 heurystyka / 1 heurystyka vs ALPHA-BETA 2 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_alpha_beta=True, rating_method_one_player_one=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_two_player_two=True, random_node_choice_player_2=True)
print("**041** MIN-MAX 1 heurystyka / 1 heurystyka vs ALPHA-BETA 2 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **042** MIN-MAX 1 heurystyka / 1 heurystyka vs ALPHA-BETA 3 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_alpha_beta=True, rating_method_one_player_one=True, empty_adjacent_cells_node_choice_player_1=True, random_node_choice_player_2=True)
print("**042** MIN-MAX 1 heurystyka / 1 heurystyka vs ALPHA-BETA 3 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **043** MIN-MAX 2 heurystyka / 1 heurystyka vs ALPHA-BETA 1 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_alpha_beta=True, rating_method_two_player_one=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_one_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**043** MIN-MAX 2 heurystyka / 1 heurystyka vs ALPHA-BETA 1 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **044** MIN-MAX 2 heurystyka / 1 heurystyka vs ALPHA-BETA 2 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_alpha_beta=True, rating_method_two_player_one=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_two_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**044** MIN-MAX 2 heurystyka / 1 heurystyka vs ALPHA-BETA 2 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **045** MIN-MAX 2 heurystyka / 1 heurystyka vs ALPHA-BETA 3 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_alpha_beta=True, rating_method_two_player_one=True, empty_adjacent_cells_node_choice_player_1=True, empty_adjacent_cells_node_choice_player_2=True)
print("**045** MIN-MAX 2 heurystyka / 1 heurystyka vs ALPHA-BETA 3 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **046** MIN-MAX 2 heurystyka / 1 heurystyka vs ALPHA-BETA 1 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_alpha_beta=True, rating_method_two_player_one=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_one_player_two=True, random_node_choice_player_2=True)
print("**046** MIN-MAX 2 heurystyka / 1 heurystyka vs ALPHA-BETA 1 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **047** MIN-MAX 2 heurystyka / 1 heurystyka vs ALPHA-BETA 2 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_alpha_beta=True, rating_method_two_player_one=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_two_player_two=True, random_node_choice_player_2=True)
print("**047** MIN-MAX 2 heurystyka / 1 heurystyka vs ALPHA-BETA 2 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **048** MIN-MAX 2 heurystyka / 1 heurystyka vs ALPHA-BETA 3 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_alpha_beta=True, rating_method_two_player_one=True, empty_adjacent_cells_node_choice_player_1=True, random_node_choice_player_2=True)
print("**048** MIN-MAX 2 heurystyka / 1 heurystyka vs ALPHA-BETA 3 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **049** MIN-MAX 3 heurystyka / 1 heurystyka vs ALPHA-BETA 1 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_alpha_beta=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_one_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**049** MIN-MAX 3 heurystyka / 1 heurystyka vs ALPHA-BETA 1 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **050** MIN-MAX 3 heurystyka / 1 heurystyka vs ALPHA-BETA 2 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_alpha_beta=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_two_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**050** MIN-MAX 3 heurystyka / 1 heurystyka vs ALPHA-BETA 2 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **051** MIN-MAX 3 heurystyka / 1 heurystyka vs ALPHA-BETA 3 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_alpha_beta=True, empty_adjacent_cells_node_choice_player_1=True, empty_adjacent_cells_node_choice_player_2=True)
print("**051** MIN-MAX 3 heurystyka / 1 heurystyka vs ALPHA-BETA 3 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **052** MIN-MAX 3 heurystyka / 1 heurystyka vs ALPHA-BETA 1 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_alpha_beta=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_one_player_two=True, random_node_choice_player_2=True)
print("**052** MIN-MAX 3 heurystyka / 1 heurystyka vs ALPHA-BETA 1 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **053** MIN-MAX 3 heurystyka / 1 heurystyka vs ALPHA-BETA 2 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_alpha_beta=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_two_player_two=True, random_node_choice_player_2=True)
print("**053** MIN-MAX 3 heurystyka / 1 heurystyka vs ALPHA-BETA 2 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **054** MIN-MAX 3 heurystyka / 1 heurystyka vs ALPHA-BETA 3 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_alpha_beta=True, empty_adjacent_cells_node_choice_player_1=True, random_node_choice_player_2=True)
print("**054** MIN-MAX 3 heurystyka / 1 heurystyka vs ALPHA-BETA 3 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **055** MIN-MAX 1 heurystyka / 2 heurystyka vs ALPHA-BETA 1 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_alpha_beta=True, rating_method_one_player_one=True, random_node_choice_player_1=True, rating_method_one_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**055** MIN-MAX 1 heurystyka / 2 heurystyka vs ALPHA-BETA 1 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **056** MIN-MAX 1 heurystyka / 2 heurystyka vs ALPHA-BETA 2 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_alpha_beta=True, rating_method_one_player_one=True, random_node_choice_player_1=True, rating_method_two_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**056** MIN-MAX 1 heurystyka / 2 heurystyka vs ALPHA-BETA 2 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **057** MIN-MAX 1 heurystyka / 2 heurystyka vs ALPHA-BETA 3 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_alpha_beta=True, rating_method_one_player_one=True, random_node_choice_player_1=True, empty_adjacent_cells_node_choice_player_2=True)
print("**057** MIN-MAX 1 heurystyka / 2 heurystyka vs ALPHA-BETA 3 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **058** MIN-MAX 1 heurystyka / 2 heurystyka vs ALPHA-BETA 1 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_alpha_beta=True, rating_method_one_player_one=True, random_node_choice_player_1=True, rating_method_one_player_two=True, random_node_choice_player_2=True)
print("**058** MIN-MAX 1 heurystyka / 2 heurystyka vs ALPHA-BETA 1 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **059** MIN-MAX 1 heurystyka / 2 heurystyka vs ALPHA-BETA 2 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_alpha_beta=True, rating_method_one_player_one=True, random_node_choice_player_1=True, rating_method_two_player_two=True, random_node_choice_player_2=True)
print("**059** MIN-MAX 1 heurystyka / 2 heurystyka vs ALPHA-BETA 2 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **060** MIN-MAX 1 heurystyka / 2 heurystyka vs ALPHA-BETA 3 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_alpha_beta=True, rating_method_one_player_one=True, random_node_choice_player_1=True, random_node_choice_player_2=True)
print("**060** MIN-MAX 1 heurystyka / 2 heurystyka vs ALPHA-BETA 3 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **061** MIN-MAX 2 heurystyka / 2 heurystyka vs ALPHA-BETA 1 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_alpha_beta=True, rating_method_two_player_one=True, random_node_choice_player_1=True, rating_method_one_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**061** MIN-MAX 2 heurystyka / 2 heurystyka vs ALPHA-BETA 1 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **062** MIN-MAX 2 heurystyka / 2 heurystyka vs ALPHA-BETA 2 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_alpha_beta=True, rating_method_two_player_one=True, random_node_choice_player_1=True, rating_method_two_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**062** MIN-MAX 2 heurystyka / 2 heurystyka vs ALPHA-BETA 2 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **063** MIN-MAX 2 heurystyka / 2 heurystyka vs ALPHA-BETA 3 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_alpha_beta=True, rating_method_two_player_one=True, random_node_choice_player_1=True, empty_adjacent_cells_node_choice_player_2=True)
print("**063** MIN-MAX 2 heurystyka / 2 heurystyka vs ALPHA-BETA 3 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **064** MIN-MAX 2 heurystyka / 2 heurystyka vs ALPHA-BETA 1 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_alpha_beta=True, rating_method_two_player_one=True, random_node_choice_player_1=True, rating_method_one_player_two=True, random_node_choice_player_2=True)
print("**064** MIN-MAX 2 heurystyka / 2 heurystyka vs ALPHA-BETA 1 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **065** MIN-MAX 2 heurystyka / 2 heurystyka vs ALPHA-BETA 2 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_alpha_beta=True, rating_method_two_player_one=True, random_node_choice_player_1=True, rating_method_two_player_two=True, random_node_choice_player_2=True)
print("**065** MIN-MAX 2 heurystyka / 2 heurystyka vs ALPHA-BETA 2 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **066** MIN-MAX 2 heurystyka / 2 heurystyka vs ALPHA-BETA 3 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_alpha_beta=True, rating_method_two_player_one=True, random_node_choice_player_1=True, random_node_choice_player_2=True)
print("**066** MIN-MAX 2 heurystyka / 2 heurystyka vs ALPHA-BETA 3 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **067** MIN-MAX 3 heurystyka / 2 heurystyka vs ALPHA-BETA 1 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_alpha_beta=True, random_node_choice_player_1=True, rating_method_one_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**067** MIN-MAX 3 heurystyka / 2 heurystyka vs ALPHA-BETA 1 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **068** MIN-MAX 3 heurystyka / 2 heurystyka vs ALPHA-BETA 2 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_alpha_beta=True, random_node_choice_player_1=True, rating_method_two_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**068** MIN-MAX 3 heurystyka / 2 heurystyka vs ALPHA-BETA 2 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **069** MIN-MAX 3 heurystyka / 2 heurystyka vs ALPHA-BETA 3 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_alpha_beta=True, random_node_choice_player_1=True, empty_adjacent_cells_node_choice_player_2=True)
print("**069** MIN-MAX 3 heurystyka / 2 heurystyka vs ALPHA-BETA 3 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **070** MIN-MAX 3 heurystyka / 2 heurystyka vs ALPHA-BETA 1 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_alpha_beta=True, random_node_choice_player_1=True, rating_method_one_player_two=True, random_node_choice_player_2=True)
print("**070** MIN-MAX 3 heurystyka / 2 heurystyka vs ALPHA-BETA 1 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **071** MIN-MAX 3 heurystyka / 2 heurystyka vs ALPHA-BETA 2 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_alpha_beta=True, random_node_choice_player_1=True, rating_method_two_player_two=True, random_node_choice_player_2=True)
print("**071** MIN-MAX 3 heurystyka / 2 heurystyka vs ALPHA-BETA 2 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **072** MIN-MAX 3 heurystyka / 2 heurystyka vs ALPHA-BETA 3 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, min_max_vs_alpha_beta=True, random_node_choice_player_1=True, random_node_choice_player_2=True)
print("**072** MIN-MAX 3 heurystyka / 2 heurystyka vs ALPHA-BETA 3 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# ************************************************************ALPHA-BETA vs MIN-MAX************************************************************

# **073** ALPHA-BETA 1 heurystyka / 1 heurystyka vs MIN-MAX 1 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_min_max=True, rating_method_one_player_one=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_one_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**073** ALPHA-BETA 1 heurystyka / 1 heurystyka vs MIN-MAX 1 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **074** ALPHA-BETA 1 heurystyka / 1 heurystyka vs MIN-MAX 2 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_min_max=True, rating_method_one_player_one=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_two_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**074** ALPHA-BETA 1 heurystyka / 1 heurystyka vs MIN-MAX 2 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **075** ALPHA-BETA 1 heurystyka / 1 heurystyka vs MIN-MAX 3 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_min_max=True, rating_method_one_player_one=True, empty_adjacent_cells_node_choice_player_1=True, empty_adjacent_cells_node_choice_player_2=True)
print("**075** ALPHA-BETA 1 heurystyka / 1 heurystyka vs MIN-MAX 3 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **076** ALPHA-BETA 1 heurystyka / 1 heurystyka vs MIN-MAX 1 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_min_max=True, rating_method_one_player_one=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_one_player_two=True, random_node_choice_player_2=True)
print("**076** ALPHA-BETA 1 heurystyka / 1 heurystyka vs MIN-MAX 1 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **077** ALPHA-BETA 1 heurystyka / 1 heurystyka vs MIN-MAX 2 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_min_max=True, rating_method_one_player_one=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_two_player_two=True, random_node_choice_player_2=True)
print("**077** ALPHA-BETA 1 heurystyka / 1 heurystyka vs MIN-MAX 2 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **078** ALPHA-BETA 1 heurystyka / 1 heurystyka vs MIN-MAX 3 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_min_max=True, rating_method_one_player_one=True, empty_adjacent_cells_node_choice_player_1=True, random_node_choice_player_2=True)
print("**078** ALPHA-BETA 1 heurystyka / 1 heurystyka vs MIN-MAX 3 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **079** ALPHA-BETA 2 heurystyka / 1 heurystyka vs MIN-MAX 1 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_min_max=True, rating_method_two_player_one=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_one_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**079** ALPHA-BETA 2 heurystyka / 1 heurystyka vs MIN-MAX 1 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **080** ALPHA-BETA 2 heurystyka / 1 heurystyka vs MIN-MAX 2 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_min_max=True, rating_method_two_player_one=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_two_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**080** ALPHA-BETA 2 heurystyka / 1 heurystyka vs MIN-MAX 2 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **081** ALPHA-BETA 2 heurystyka / 1 heurystyka vs MIN-MAX 3 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_min_max=True, rating_method_two_player_one=True, empty_adjacent_cells_node_choice_player_1=True, empty_adjacent_cells_node_choice_player_2=True)
print("**081** ALPHA-BETA 2 heurystyka / 1 heurystyka vs MIN-MAX 3 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **082** ALPHA-BETA 2 heurystyka / 1 heurystyka vs MIN-MAX 1 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_min_max=True, rating_method_two_player_one=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_one_player_two=True, random_node_choice_player_2=True)
print("**082** ALPHA-BETA 2 heurystyka / 1 heurystyka vs MIN-MAX 1 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **083** ALPHA-BETA 2 heurystyka / 1 heurystyka vs MIN-MAX 2 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_min_max=True, rating_method_two_player_one=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_two_player_two=True, random_node_choice_player_2=True)
print("**083** ALPHA-BETA 2 heurystyka / 1 heurystyka vs MIN-MAX 2 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **084** ALPHA-BETA 2 heurystyka / 1 heurystyka vs MIN-MAX 3 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_min_max=True, rating_method_two_player_one=True, empty_adjacent_cells_node_choice_player_1=True, random_node_choice_player_2=True)
print("**084** ALPHA-BETA 2 heurystyka / 1 heurystyka vs MIN-MAX 3 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **085** ALPHA-BETA 3 heurystyka / 1 heurystyka vs MIN-MAX 1 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_min_max=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_one_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**085** ALPHA-BETA 3 heurystyka / 1 heurystyka vs MIN-MAX 1 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **086** ALPHA-BETA 3 heurystyka / 1 heurystyka vs MIN-MAX 2 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_min_max=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_two_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**086** ALPHA-BETA 3 heurystyka / 1 heurystyka vs MIN-MAX 2 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **087** ALPHA-BETA 3 heurystyka / 1 heurystyka vs MIN-MAX 3 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_min_max=True, empty_adjacent_cells_node_choice_player_1=True, empty_adjacent_cells_node_choice_player_2=True)
print("**087** ALPHA-BETA 3 heurystyka / 1 heurystyka vs MIN-MAX 3 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **088** ALPHA-BETA 3 heurystyka / 1 heurystyka vs MIN-MAX 1 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_min_max=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_one_player_two=True, random_node_choice_player_2=True)
print("**088** ALPHA-BETA 3 heurystyka / 1 heurystyka vs MIN-MAX 1 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **089** ALPHA-BETA 3 heurystyka / 1 heurystyka vs MIN-MAX 2 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_min_max=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_two_player_two=True, random_node_choice_player_2=True)
print("**089** ALPHA-BETA 3 heurystyka / 1 heurystyka vs MIN-MAX 2 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **090** ALPHA-BETA 3 heurystyka / 1 heurystyka vs MIN-MAX 3 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_min_max=True, empty_adjacent_cells_node_choice_player_1=True, random_node_choice_player_2=True)
print("**090** ALPHA-BETA 3 heurystyka / 1 heurystyka vs MIN-MAX 3 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **091** ALPHA-BETA 1 heurystyka / 2 heurystyka vs MIN-MAX 1 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_min_max=True, rating_method_one_player_one=True, random_node_choice_player_1=True, rating_method_one_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**091** ALPHA-BETA 1 heurystyka / 2 heurystyka vs MIN-MAX 1 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **092** ALPHA-BETA 1 heurystyka / 2 heurystyka vs MIN-MAX 2 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_min_max=True, rating_method_one_player_one=True, random_node_choice_player_1=True, rating_method_two_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**092** ALPHA-BETA 1 heurystyka / 2 heurystyka vs MIN-MAX 2 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **093** ALPHA-BETA 1 heurystyka / 2 heurystyka vs MIN-MAX 3 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_min_max=True, rating_method_one_player_one=True, random_node_choice_player_1=True, empty_adjacent_cells_node_choice_player_2=True)
print("**093** ALPHA-BETA 1 heurystyka / 2 heurystyka vs MIN-MAX 3 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **094** ALPHA-BETA 1 heurystyka / 2 heurystyka vs MIN-MAX 1 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_min_max=True, rating_method_one_player_one=True, random_node_choice_player_1=True, rating_method_one_player_two=True, random_node_choice_player_2=True)
print("**094** ALPHA-BETA 1 heurystyka / 2 heurystyka vs MIN-MAX 1 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **095** ALPHA-BETA 1 heurystyka / 2 heurystyka vs MIN-MAX 2 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_min_max=True, rating_method_one_player_one=True, random_node_choice_player_1=True, rating_method_two_player_two=True, random_node_choice_player_2=True)
print("**095** ALPHA-BETA 1 heurystyka / 2 heurystyka vs MIN-MAX 2 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **096** ALPHA-BETA 1 heurystyka / 2 heurystyka vs MIN-MAX 3 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_min_max=True, rating_method_one_player_one=True, random_node_choice_player_1=True, random_node_choice_player_2=True)
print("**096** ALPHA-BETA 1 heurystyka / 2 heurystyka vs MIN-MAX 3 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **097** ALPHA-BETA 2 heurystyka / 2 heurystyka vs MIN-MAX 1 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_min_max=True, rating_method_two_player_one=True, random_node_choice_player_1=True, rating_method_one_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**097** ALPHA-BETA 2 heurystyka / 2 heurystyka vs MIN-MAX 1 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **098** ALPHA-BETA 2 heurystyka / 2 heurystyka vs MIN-MAX 2 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_min_max=True, rating_method_two_player_one=True, random_node_choice_player_1=True, rating_method_two_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**098** ALPHA-BETA 2 heurystyka / 2 heurystyka vs MIN-MAX 2 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **099** ALPHA-BETA 2 heurystyka / 2 heurystyka vs MIN-MAX 3 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_min_max=True, rating_method_two_player_one=True, random_node_choice_player_1=True, empty_adjacent_cells_node_choice_player_2=True)
print("**099** ALPHA-BETA 2 heurystyka / 2 heurystyka vs MIN-MAX 3 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **100** ALPHA-BETA 2 heurystyka / 2 heurystyka vs MIN-MAX 1 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_min_max=True, rating_method_two_player_one=True, random_node_choice_player_1=True, rating_method_one_player_two=True, random_node_choice_player_2=True)
print("**100** ALPHA-BETA 2 heurystyka / 2 heurystyka vs MIN-MAX 1 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **101** ALPHA-BETA 2 heurystyka / 2 heurystyka vs MIN-MAX 2 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_min_max=True, rating_method_two_player_one=True, random_node_choice_player_1=True, rating_method_two_player_two=True, random_node_choice_player_2=True)
print("**101** ALPHA-BETA 2 heurystyka / 2 heurystyka vs MIN-MAX 2 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **102** ALPHA-BETA 2 heurystyka / 2 heurystyka vs MIN-MAX 3 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_min_max=True, rating_method_two_player_one=True, random_node_choice_player_1=True, random_node_choice_player_2=True)
print("**102** ALPHA-BETA 2 heurystyka / 2 heurystyka vs MIN-MAX 3 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **103** ALPHA-BETA 3 heurystyka / 2 heurystyka vs MIN-MAX 1 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_min_max=True, random_node_choice_player_1=True, rating_method_one_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**103** ALPHA-BETA 3 heurystyka / 2 heurystyka vs MIN-MAX 1 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **104** ALPHA-BETA 3 heurystyka / 2 heurystyka vs MIN-MAX 2 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_min_max=True, random_node_choice_player_1=True, rating_method_two_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**104** ALPHA-BETA 3 heurystyka / 2 heurystyka vs MIN-MAX 2 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **105** ALPHA-BETA 3 heurystyka / 2 heurystyka vs MIN-MAX 3 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_min_max=True, random_node_choice_player_1=True, empty_adjacent_cells_node_choice_player_2=True)
print("**105** ALPHA-BETA 3 heurystyka / 2 heurystyka vs MIN-MAX 3 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **106** ALPHA-BETA 3 heurystyka / 2 heurystyka vs MIN-MAX 1 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_min_max=True, random_node_choice_player_1=True, rating_method_one_player_two=True, random_node_choice_player_2=True)
print("**106** ALPHA-BETA 3 heurystyka / 2 heurystyka vs MIN-MAX 1 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **107** ALPHA-BETA 3 heurystyka / 2 heurystyka vs MIN-MAX 2 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_min_max=True, random_node_choice_player_1=True, rating_method_two_player_two=True, random_node_choice_player_2=True)
print("**107** ALPHA-BETA 3 heurystyka / 2 heurystyka vs MIN-MAX 2 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **108** ALPHA-BETA 3 heurystyka / 2 heurystyka vs MIN-MAX 3 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_min_max=True, random_node_choice_player_1=True, random_node_choice_player_2=True)
print("**108** ALPHA-BETA 3 heurystyka / 2 heurystyka vs MIN-MAX 3 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# ************************************************************ALPHA-BETA vs ALPHA-BETA************************************************************

# **109** ALPHA-BETA 1 heurystyka / 1 heurystyka vs ALPHA-BETA 1 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_alpha_beta=True, rating_method_one_player_one=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_one_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**109** ALPHA-BETA 1 heurystyka / 1 heurystyka vs ALPHA-BETA 1 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **110** ALPHA-BETA 1 heurystyka / 1 heurystyka vs ALPHA-BETA 2 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_alpha_beta=True, rating_method_one_player_one=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_two_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**110** ALPHA-BETA 1 heurystyka / 1 heurystyka vs ALPHA-BETA 2 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **111** ALPHA-BETA 1 heurystyka / 1 heurystyka vs ALPHA-BETA 3 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_alpha_beta=True, rating_method_one_player_one=True, empty_adjacent_cells_node_choice_player_1=True, empty_adjacent_cells_node_choice_player_2=True)
print("**111** ALPHA-BETA 1 heurystyka / 1 heurystyka vs ALPHA-BETA 3 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **112** ALPHA-BETA 1 heurystyka / 1 heurystyka vs ALPHA-BETA 1 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_alpha_beta=True, rating_method_one_player_one=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_one_player_two=True, random_node_choice_player_2=True)
print("**112** ALPHA-BETA 1 heurystyka / 1 heurystyka vs ALPHA-BETA 1 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **113** ALPHA-BETA 1 heurystyka / 1 heurystyka vs ALPHA-BETA 2 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_alpha_beta=True, rating_method_one_player_one=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_two_player_two=True, random_node_choice_player_2=True)
print("**113** ALPHA-BETA 1 heurystyka / 1 heurystyka vs ALPHA-BETA 2 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **114** ALPHA-BETA 1 heurystyka / 1 heurystyka vs ALPHA-BETA 3 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_alpha_beta=True, rating_method_one_player_one=True, empty_adjacent_cells_node_choice_player_1=True, random_node_choice_player_2=True)
print("**114** ALPHA-BETA 1 heurystyka / 1 heurystyka vs ALPHA-BETA 3 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **115** ALPHA-BETA 2 heurystyka / 1 heurystyka vs ALPHA-BETA 1 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_alpha_beta=True, rating_method_two_player_one=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_one_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**115** ALPHA-BETA 2 heurystyka / 1 heurystyka vs ALPHA-BETA 1 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **116** ALPHA-BETA 2 heurystyka / 1 heurystyka vs ALPHA-BETA 2 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_alpha_beta=True, rating_method_two_player_one=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_two_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**116** ALPHA-BETA 2 heurystyka / 1 heurystyka vs ALPHA-BETA 2 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **117** ALPHA-BETA 2 heurystyka / 1 heurystyka vs ALPHA-BETA 3 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_alpha_beta=True, rating_method_two_player_one=True, empty_adjacent_cells_node_choice_player_1=True, empty_adjacent_cells_node_choice_player_2=True)
print("**117** ALPHA-BETA 2 heurystyka / 1 heurystyka vs ALPHA-BETA 3 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **118** ALPHA-BETA 2 heurystyka / 1 heurystyka vs ALPHA-BETA 1 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_alpha_beta=True, rating_method_two_player_one=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_one_player_two=True, random_node_choice_player_2=True)
print("**118** ALPHA-BETA 2 heurystyka / 1 heurystyka vs ALPHA-BETA 1 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **119** ALPHA-BETA 2 heurystyka / 1 heurystyka vs ALPHA-BETAALPHA-BETA 2 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_alpha_beta=True, rating_method_two_player_one=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_two_player_two=True, random_node_choice_player_2=True)
print("**119** ALPHA-BETA 2 heurystyka / 1 heurystyka vs ALPHA-BETA 2 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **120** ALPHA-BETA 2 heurystyka / 1 heurystyka vs ALPHA-BETA 3 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_alpha_beta=True, rating_method_two_player_one=True, empty_adjacent_cells_node_choice_player_1=True, random_node_choice_player_2=True)
print("**120** ALPHA-BETA 2 heurystyka / 1 heurystyka vs ALPHA-BETA 3 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **121** ALPHA-BETA 3 heurystyka / 1 heurystyka vs ALPHA-BETA 1 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_alpha_beta=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_one_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**121** ALPHA-BETA 3 heurystyka / 1 heurystyka vs ALPHA-BETA 1 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **122** ALPHA-BETA 3 heurystyka / 1 heurystyka vs ALPHA-BETA 2 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_alpha_beta=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_two_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**122** ALPHA-BETA 3 heurystyka / 1 heurystyka vs ALPHA-BETA 2 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **123** ALPHA-BETA 3 heurystyka / 1 heurystyka vs ALPHA-BETA 3 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_alpha_beta=True, empty_adjacent_cells_node_choice_player_1=True, empty_adjacent_cells_node_choice_player_2=True)
print("**123** ALPHA-BETA 3 heurystyka / 1 heurystyka vs ALPHA-BETA 3 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **124** ALPHA-BETA 3 heurystyka / 1 heurystyka vs ALPHA-BETA 1 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_alpha_beta=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_one_player_two=True, random_node_choice_player_2=True)
print("**124** ALPHA-BETA 3 heurystyka / 1 heurystyka vs ALPHA-BETA 1 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **125** ALPHA-BETA 3 heurystyka / 1 heurystyka vs ALPHA-BETA 2 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_alpha_beta=True, empty_adjacent_cells_node_choice_player_1=True, rating_method_two_player_two=True, random_node_choice_player_2=True)
print("**125** ALPHA-BETA 3 heurystyka / 1 heurystyka vs ALPHA-BETA 2 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **126** ALPHA-BETA 3 heurystyka / 1 heurystyka vs ALPHA-BETA 3 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_alpha_beta=True, empty_adjacent_cells_node_choice_player_1=True, random_node_choice_player_2=True)
print("**126** ALPHA-BETA 3 heurystyka / 1 heurystyka vs ALPHA-BETA 3 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **127** ALPHA-BETA 1 heurystyka / 2 heurystyka vs ALPHA-BETA 1 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_alpha_beta=True, rating_method_one_player_one=True, random_node_choice_player_1=True, rating_method_one_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**127** ALPHA-BETA 1 heurystyka / 2 heurystyka vs ALPHA-BETA 1 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **128** ALPHA-BETA 1 heurystyka / 2 heurystyka vs ALPHA-BETA 2 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_alpha_beta=True, rating_method_one_player_one=True, random_node_choice_player_1=True, rating_method_two_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**128** ALPHA-BETA 1 heurystyka / 2 heurystyka vs ALPHA-BETA 2 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **129** ALPHA-BETA 1 heurystyka / 2 heurystyka vs ALPHA-BETA 3 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_alpha_beta=True, rating_method_one_player_one=True, random_node_choice_player_1=True, empty_adjacent_cells_node_choice_player_2=True)
print("**129** ALPHA-BETA 1 heurystyka / 2 heurystyka vs ALPHA-BETA 3 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **130** ALPHA-BETA 1 heurystyka / 2 heurystyka vs ALPHA-BETA 1 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_alpha_beta=True, rating_method_one_player_one=True, random_node_choice_player_1=True, rating_method_one_player_two=True, random_node_choice_player_2=True)
print("**130** ALPHA-BETA 1 heurystyka / 2 heurystyka vs ALPHA-BETA 1 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **131** ALPHA-BETA 1 heurystyka / 2 heurystyka vs ALPHA-BETA 2 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_alpha_beta=True, rating_method_one_player_one=True, random_node_choice_player_1=True, rating_method_two_player_two=True, random_node_choice_player_2=True)
print("**131** ALPHA-BETA 1 heurystyka / 2 heurystyka vs ALPHA-BETA 2 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **132** ALPHA-BETA 1 heurystyka / 2 heurystyka vs ALPHA-BETA 3 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_alpha_beta=True, rating_method_one_player_one=True, random_node_choice_player_1=True, random_node_choice_player_2=True)
print("**132** ALPHA-BETA 1 heurystyka / 2 heurystyka vs ALPHA-BETA 3 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **133** ALPHA-BETA 2 heurystyka / 2 heurystyka vs ALPHA-BETA 1 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_alpha_beta=True, rating_method_two_player_one=True, random_node_choice_player_1=True, rating_method_one_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**133** ALPHA-BETA 2 heurystyka / 2 heurystyka vs ALPHA-BETA 1 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **134** ALPHA-BETA 2 heurystyka / 2 heurystyka vs ALPHA-BETA 2 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_alpha_beta=True, rating_method_two_player_one=True, random_node_choice_player_1=True, rating_method_two_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**134** ALPHA-BETA 2 heurystyka / 2 heurystyka vs ALPHA-BETA 2 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **135** ALPHA-BETA 2 heurystyka / 2 heurystyka vs ALPHA-BETA 3 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_alpha_beta=True, rating_method_two_player_one=True, random_node_choice_player_1=True, empty_adjacent_cells_node_choice_player_2=True)
print("**135** ALPHA-BETA 2 heurystyka / 2 heurystyka vs ALPHA-BETA 3 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **136** ALPHA-BETA 2 heurystyka / 2 heurystyka vs ALPHA-BETA 1 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_alpha_beta=True, rating_method_two_player_one=True, random_node_choice_player_1=True, rating_method_one_player_two=True, random_node_choice_player_2=True)
print("**136** ALPHA-BETA 2 heurystyka / 2 heurystyka vs ALPHA-BETA 1 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **137** ALPHA-BETA 2 heurystyka / 2 heurystyka vs ALPHA-BETA 2 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_alpha_beta=True, rating_method_two_player_one=True, random_node_choice_player_1=True, rating_method_two_player_two=True, random_node_choice_player_2=True)
print("**137** ALPHA-BETA 2 heurystyka / 2 heurystyka vs ALPHA-BETA 2 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **138** ALPHA-BETA 2 heurystyka / 2 heurystyka vs ALPHA-BETA 3 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_alpha_beta=True, rating_method_two_player_one=True, random_node_choice_player_1=True, random_node_choice_player_2=True)
print("**138** ALPHA-BETA 2 heurystyka / 2 heurystyka vs ALPHA-BETA 3 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **139** ALPHA-BETA 3 heurystyka / 2 heurystyka vs ALPHA-BETA 1 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_alpha_beta=True, random_node_choice_player_1=True, rating_method_one_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**139** ALPHA-BETA 3 heurystyka / 2 heurystyka vs ALPHA-BETA 1 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **140** ALPHA-BETA 3 heurystyka / 2 heurystyka vs ALPHA-BETA 2 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_alpha_beta=True, random_node_choice_player_1=True, rating_method_two_player_two=True, empty_adjacent_cells_node_choice_player_2=True)
print("**140** ALPHA-BETA 3 heurystyka / 2 heurystyka vs ALPHA-BETA 2 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **141** ALPHA-BETA 3 heurystyka / 2 heurystyka vs ALPHA-BETA 3 heurystyka / 1 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_alpha_beta=True, random_node_choice_player_1=True, empty_adjacent_cells_node_choice_player_2=True)
print("**141** ALPHA-BETA 3 heurystyka / 2 heurystyka vs ALPHA-BETA 3 heurystyka / 1 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **142** ALPHA-BETA 3 heurystyka / 2 heurystyka vs ALPHA-BETA 1 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_alpha_beta=True, random_node_choice_player_1=True, rating_method_one_player_two=True, random_node_choice_player_2=True)
print("**142** ALPHA-BETA 3 heurystyka / 2 heurystyka vs ALPHA-BETA 1 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **143** ALPHA-BETA 3 heurystyka / 2 heurystyka vs ALPHA-BETA 2 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_alpha_beta=True, random_node_choice_player_1=True, rating_method_two_player_two=True, random_node_choice_player_2=True)
print("**143** ALPHA-BETA 3 heurystyka / 2 heurystyka vs ALPHA-BETA 2 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))

# **144** ALPHA-BETA 3 heurystyka / 2 heurystyka vs ALPHA-BETA 3 heurystyka / 2 heurystyka

scoreboard = np.zeros((number_of_rounds,), dtype=int)
for i in range(number_of_rounds):
    game1 = game.Game()
    scoreboard[i] = game1.play(cpu_vs_cpu=True, alpha_beta_vs_alpha_beta=True, random_node_choice_player_1=True, random_node_choice_player_2=True)
print("**144** ALPHA-BETA 3 heurystyka / 2 heurystyka vs ALPHA-BETA 3 heurystyka / 2 heurystyka  ==>  " + str(np.count_nonzero(scoreboard == 1)) + " : " + str(np.count_nonzero(scoreboard == 2)))
