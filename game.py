import numpy as np
import random
import time
from termcolor import colored


class Game(object):

    '''
    3 Heurystyki do oceny stanu planszy:
        1. Suma naszych punktów + liczba pustych pól przy naszych polach (każde puste pole liczy się tyle razy ile naszych pól z nim graniczy)
        2. Suma naszych punktów - punkty przeciwnika
        3. -1 * (Suma punktów przeciwnika + liczba pustych pól przy polach przeciwnika (każde puste pole liczy się tyle razy ile pól przeciwnika z nim graniczy))
    3 Heurystyki do wyboru kolejnego węzła:
        1. Funkcja oceniająca sprawdzająca węzły w kolejności liczby graniczących PUSTYCH pól -> szacowanie liczby dozwolonych ruchów (im więcej dozwolonych tym większa szansa na znalezienie najlepszego)
        2. Random
        3. Po kolei
    '''

    def __init__(self):
        self.board = np.zeros((7, 7), dtype=int)
        self.points_per_row_column_diagonal = np.zeros((16, 2), dtype=int)
        self.players_points = np.zeros(2, dtype=int)
        self.counted_lines = np.zeros(16, dtype=int)
        self.number_of_nodes_searched_player_1 = 0
        self.number_of_nodes_searched_player_2 = 0
        self.number_of_alpha_cuts_player_1 = 0
        self.number_of_alpha_cuts_player_2 = 0
        self.number_of_beta_cuts_player_1 = 0
        self.number_of_beta_cuts_player_2 = 0
        self.time_of_decision_player_1 = np.array([])
        self.time_of_decision_player_2 = np.array([])
        pass

    def play(self, human_player_one=False, cpu_vs_cpu=False, min_max_vs_alpha_beta=False, alpha_beta_vs_min_max=False,
             min_max_vs_min_max=False, alpha_beta_vs_alpha_beta=False, min_max_vs_human=False, rating_method_one_player_one=False, rating_method_one_player_two=False, rating_method_two_player_one=False, rating_method_two_player_two=False, random_node_choice_player_1=False, random_node_choice_player_2=False, empty_adjacent_cells_node_choice_player_1=False, empty_adjacent_cells_node_choice_player_2=False, present_results=False):
        while 0 in self.board:
            # Człowiek vs AI
            if human_player_one and not cpu_vs_cpu:
                self.print_board()
                chosen_x, chosen_y = [int(x) for x in
                                      input("Podaj współrzędne x i y wybranego pola oddzielone spacją: ").split()]
                while 0 > chosen_x or chosen_x > 6 or 0 > chosen_y or chosen_y > 6 or self.board[chosen_x][
                    chosen_y] != 0:
                    chosen_x, chosen_y = [int(x) for x in
                                          input("Podaj współrzędne x i y wybranego pola oddzielone spacją: ").split()]
                self.board[chosen_x][chosen_y] = 1
                self.check_results(chosen_x, chosen_y)
                # pierwszy gracz ma ostatni ruch
                if 0 not in self.board:
                    break
                # wykonywanie ruchu przez AI (pierwsze 3 wykonane losowo)
                if len(np.where(self.board != 0)[0]) < 6:
                    free_fields = np.where(self.board == 0)
                    computer_chosen_index = random.randint(0, free_fields[0].size - 1)
                    self.board[free_fields[0][computer_chosen_index]][free_fields[1][computer_chosen_index]] = 2
                    self.check_results(free_fields[0][computer_chosen_index], free_fields[1][computer_chosen_index])
                else:
                    # print("MYŚLĘ")
                    board = np.copy(self.board)
                    start_time = time.time()
                    computer_chosen_index = self.min_max(board, player=2, max_depth=3,
                                                         rating_method_one=rating_method_one_player_two, rating_method_two=rating_method_two_player_two, random_node_choice=random_node_choice_player_2, empty_adjacent_cells_node_choice=empty_adjacent_cells_node_choice_player_2) if min_max_vs_human else self.alpha_beta(
                        board, player=2, max_depth=3, rating_method_one=rating_method_one_player_two, rating_method_two=rating_method_two_player_two, random_node_choice=random_node_choice_player_2, empty_adjacent_cells_node_choice=empty_adjacent_cells_node_choice_player_2)
                    self.time_of_decision_player_2 = np.append(self.time_of_decision_player_2, np.array([time.time() - start_time]), axis=0)
                    self.board[computer_chosen_index[0]][computer_chosen_index[1]] = 2
                    self.check_results(computer_chosen_index[0], computer_chosen_index[1])
            # AI vs Człowiek
            if not human_player_one and not cpu_vs_cpu:
                # wykonywanie ruchu przez AI
                if len(np.where(self.board != 0)[0]) < 6:
                    free_fields = np.where(self.board == 0)
                    computer_chosen_index = random.randint(0, free_fields[0].size - 1)
                    self.board[free_fields[0][computer_chosen_index]][free_fields[1][computer_chosen_index]] = 1
                    self.check_results(free_fields[0][computer_chosen_index], free_fields[1][computer_chosen_index])
                else:
                    # print("MYŚLĘ")
                    board = np.copy(self.board)
                    start_time = time.time()
                    computer_chosen_index = self.min_max(board, player=1, max_depth=3,
                                                         rating_method_one=rating_method_one_player_one, rating_method_two=rating_method_two_player_one, random_node_choice=random_node_choice_player_1, empty_adjacent_cells_node_choice=empty_adjacent_cells_node_choice_player_1) if min_max_vs_human else self.alpha_beta(
                        board, player=1, max_depth=3, rating_method_one=rating_method_one_player_one, rating_method_two=rating_method_two_player_one,  random_node_choice=random_node_choice_player_1, empty_adjacent_cells_node_choice=empty_adjacent_cells_node_choice_player_1)
                    self.time_of_decision_player_1 = np.append(self.time_of_decision_player_1, np.array([time.time() - start_time]),
                                                               axis=0)
                    self.board[computer_chosen_index[0]][computer_chosen_index[1]] = 1
                    self.check_results(computer_chosen_index[0], computer_chosen_index[1])
                if 0 not in self.board:
                    break
                self.print_board()
                chosen_x, chosen_y = [int(x) for x in
                                      input("Podaj współrzędne x i y wybranego pola oddzielone spacją: ").split()]
                while 0 > chosen_x or chosen_x > 6 or 0 > chosen_y or chosen_y > 6 or 0 != self.board[chosen_x][
                    chosen_y]:
                    chosen_x, chosen_y = [int(x) for x in
                                          input("Podaj współrzędne x i y wybranego pola oddzielone spacją: ").split()]
                self.board[chosen_x][chosen_y] = 2
                self.check_results(chosen_x, chosen_y)
            # AI vs AI
            if cpu_vs_cpu:
                # self.print_board()
                # wykonywanie ruchu przez AI
                if len(np.where(self.board != 0)[0]) < 6:
                    free_fields = np.where(self.board == 0)
                    computer_chosen_index = random.randint(0, free_fields[0].size - 1)
                    self.board[free_fields[0][computer_chosen_index]][free_fields[1][computer_chosen_index]] = 1
                    self.check_results(free_fields[0][computer_chosen_index], free_fields[1][computer_chosen_index])
                else:
                    board = np.copy(self.board)
                    start_time = time.time()
                    computer_chosen_index = self.min_max(board, player=1, max_depth=2,
                                                         rating_method_one=rating_method_one_player_one, rating_method_two=rating_method_two_player_one, random_node_choice=random_node_choice_player_1, empty_adjacent_cells_node_choice=empty_adjacent_cells_node_choice_player_1) if min_max_vs_alpha_beta or min_max_vs_min_max else self.alpha_beta(
                        board, player=1, max_depth=3, rating_method_one=rating_method_one_player_one, rating_method_two=rating_method_two_player_one, random_node_choice=random_node_choice_player_1, empty_adjacent_cells_node_choice=empty_adjacent_cells_node_choice_player_1)
                    self.time_of_decision_player_1 = np.append(self.time_of_decision_player_1, np.array([time.time() - start_time]),
                                                               axis=0)
                    self.board[computer_chosen_index[0]][computer_chosen_index[1]] = 1
                    self.check_results(computer_chosen_index[0], computer_chosen_index[1])
                if 0 not in self.board:
                    break
                # self.print_board()
                # wykonywanie ruchu przez AI
                if len(np.where(self.board != 0)[0]) < 6:
                    free_fields = np.where(self.board == 0)
                    computer_chosen_index = random.randint(0, free_fields[0].size - 1)
                    self.board[free_fields[0][computer_chosen_index]][free_fields[1][computer_chosen_index]] = 2
                    self.check_results(free_fields[0][computer_chosen_index], free_fields[1][computer_chosen_index])
                else:
                    board = np.copy(self.board)
                    start_time = time.time()
                    computer_chosen_index = self.min_max(board, player=2, max_depth=2,
                                                         rating_method_one=rating_method_one_player_two, rating_method_two=rating_method_two_player_two, random_node_choice=random_node_choice_player_2, empty_adjacent_cells_node_choice=empty_adjacent_cells_node_choice_player_2) if alpha_beta_vs_min_max or min_max_vs_min_max else self.alpha_beta(
                        board, player=2, max_depth=3, rating_method_one=rating_method_one_player_two, rating_method_two=rating_method_two_player_two, random_node_choice=random_node_choice_player_2, empty_adjacent_cells_node_choice=empty_adjacent_cells_node_choice_player_2)
                    self.time_of_decision_player_2 = np.append(self.time_of_decision_player_2, np.array([time.time() - start_time]),
                                                               axis=0)
                    self.board[computer_chosen_index[0]][computer_chosen_index[1]] = 2
                    self.check_results(computer_chosen_index[0], computer_chosen_index[1])
        # prezentacja wyników końcowych
        if present_results:
            self.print_board()
            print("Gra dobiegła końca!")
            print("Punkty gracza 1: " + str(self.players_points[0]))
            print("Punkty gracza 2: " + str(self.players_points[1]))
            print("Wygrał gracz 1." if self.players_points[0] > self.players_points[1] else (
                "Wygrał gracz 2." if self.players_points[0] < self.players_points[1] else "Gra zakończyła się remisem!"))
            # print("Punkty w wierszach: " + "\n" + str(
            #     np.array([self.points_per_row_column_diagonal[i] for i in range(0, 7)])))
            # print("Punkty w kolumnach: " + "\n" + str(
            #     np.array([self.points_per_row_column_diagonal[i] for i in range(7, 14)])))
            # print("Punkty w przekątnych: " + "\n" + str(
            #     np.array([self.points_per_row_column_diagonal[i] for i in range(14, 16)])))

            if human_player_one and not cpu_vs_cpu:
                print("Liczba węzłów odwiedzona przez algorytm {algorithm}".format(algorithm="min-max: " if min_max_vs_human else "alfa-beta cięć: ") + str(self.number_of_nodes_searched_player_1))
                print("Średni czas podejmowania decyzji przez algorytm {algorithm}".format(algorithm="min-max: " if min_max_vs_human else "alfa-beta cięć: ") + str(np.average(self.time_of_decision_player_1)))
                if not min_max_vs_human:
                    print("Łaczna liczba alfa cięć wykonana przez algorytm: " + str(self.number_of_alpha_cuts_player_1))
                    print("Łaczna liczba beta cięć wykonana przez algorytm: " + str(self.number_of_beta_cuts_player_1))
                    print("Średnia liczba alfa cięć wykonana przez algorytm: " + str(self.number_of_alpha_cuts_player_1/25.0))
                    print("Średnia liczba beta cięć wykonana przez algorytm: " + str(self.number_of_beta_cuts_player_1/25.0))

            if not human_player_one and not cpu_vs_cpu:
                print("Liczba węzłów odwiedzona przez algorytm {algorithm}".format(algorithm="min-max: " if min_max_vs_human else "alfa-beta cięć: ") + str(self.number_of_nodes_searched_player_2))
                print("Średni czas podejmowania decyzji przez algorytm {algorithm}".format(algorithm="min-max: " if min_max_vs_human else "alfa-beta cięć: ") + str(np.average(self.time_of_decision_player_2)))
                if not min_max_vs_human:
                    print("Łaczna liczba alfa cięć wykonana przez algorytm: " + str(self.number_of_alpha_cuts_player_2))
                    print("Łaczna liczba beta cięć wykonana przez algorytm: " + str(self.number_of_beta_cuts_player_2))
                    print("Średnia liczba alfa cięć wykonana przez algorytm: " + str(self.number_of_alpha_cuts_player_2/24.0))
                    print("Średnia liczba beta cięć wykonana przez algorytm: " + str(self.number_of_beta_cuts_player_2/24.0))

            if cpu_vs_cpu:
                print("Liczba węzłów odwiedzona przez Gracza 1 (algorytm {algorithm}".format(
                    algorithm="min-max): " if min_max_vs_alpha_beta or min_max_vs_min_max else "alfa-beta cięć): ") + str(
                    self.number_of_nodes_searched_player_1))
                print("Liczba węzłów odwiedzona przez Gracza 2 (algorytm {algorithm}".format(
                    algorithm="min-max): " if alpha_beta_vs_min_max or min_max_vs_min_max else "alfa-beta cięć): ") + str(
                    self.number_of_nodes_searched_player_2))
                print("Średni czas podejmowania decyzji przez Gracza 1 (algorytm {algorithm}".format(
                    algorithm="min-max): " if min_max_vs_alpha_beta or min_max_vs_min_max else "alfa-beta cięć): ") + str(
                    np.average(self.time_of_decision_player_1)))
                print("Średni czas podejmowania decyzji przez Gracza 2 (algorytm {algorithm}".format(
                    algorithm="min-max): " if alpha_beta_vs_min_max or min_max_vs_min_max else "alfa-beta cięć): ") + str(
                    np.average(self.time_of_decision_player_2)))
                if not min_max_vs_alpha_beta and not min_max_vs_min_max:
                    print("Łaczna liczba alfa cięć wykonana przez Gracza 1 (algorytm alfa-beta cięć): " + str(self.number_of_alpha_cuts_player_1))
                if not alpha_beta_vs_min_max and not min_max_vs_min_max:
                    print("Łaczna liczba alfa cięć wykonana przez Gracza 2 (algorytm alfa-beta cięć): " + str(
                        self.number_of_alpha_cuts_player_2))
                if not min_max_vs_alpha_beta and not min_max_vs_min_max:
                    print("Łaczna liczba beta cięć wykonana przez Gracza 1 (algorytm alfa-beta cięć): " + str(self.number_of_beta_cuts_player_1))
                if not alpha_beta_vs_min_max and not min_max_vs_min_max:
                    print("Łaczna liczba beta cięć wykonana przez Gracza 2 (algorytm alfa-beta cięć): " + str(
                        self.number_of_beta_cuts_player_2))
                if not min_max_vs_alpha_beta and not min_max_vs_min_max:
                    print("Średnia liczba alfa cięć wykonana przez Gracza 1 (algorytm alfa-beta cięć): " + str(self.number_of_alpha_cuts_player_1 / 25.0))
                if not alpha_beta_vs_min_max and not min_max_vs_min_max:
                    print("Średnia liczba alfa cięć wykonana przez Gracza 2 (algorytm alfa-beta cięć): " + str(
                        self.number_of_alpha_cuts_player_2 / 25.0))
                if not min_max_vs_alpha_beta and not min_max_vs_min_max:
                    print("Średnia liczba beta cięć wykonana przez Gracza 1 (algorytm alfa-beta cięć): " + str(self.number_of_beta_cuts_player_1 / 25.0))
                if not alpha_beta_vs_min_max and not min_max_vs_min_max:
                    print("Średnia liczba beta cięć wykonana przez Gracza 2 (algorytm alfa-beta cięć): " + str(self.number_of_beta_cuts_player_2 / 25.0))
        return 1 if self.players_points[0] > self.players_points[1] else (
            2 if self.players_points[0] < self.players_points[1] else 3)
    # funkcja licząca punkty
    def check_results(self, row, column):
        global same_values
        # sprawdzenie i ewentualnie policzenie punktów w kolumnie
        if self.counted_lines[7 + column] == 0 and 0 not in self.board[:, column]:
            same_values = np.array([])
            self.counted_lines[7 + column] = 1
            number_of_iteration = 0
            for i in self.board[:, column]:
                if same_values.size == 0:
                    same_values = np.append(same_values, i)
                else:
                    if same_values[-1] == i:
                        same_values = np.append(same_values, i)
                    else:
                        if same_values.size >= 2:
                            self.points_per_row_column_diagonal[7 + column][int(same_values[0]) - 1] += same_values.size
                            self.players_points[int(same_values[0]) - 1] += same_values.size
                        same_values = np.array([])
                        same_values = np.append(same_values, i)
                if number_of_iteration == 6 and same_values.size != 0:
                    if same_values.size >= 2:
                        self.points_per_row_column_diagonal[7 + column][int(same_values[0]) - 1] += same_values.size
                        self.players_points[int(same_values[0]) - 1] += same_values.size
                    break
                number_of_iteration += 1

        # sprawdzenie i ewentualnie policzenie punktów w wierszu
        if self.counted_lines[row] == 0 and 0 not in self.board[row, :]:
            same_values = np.array([])
            self.counted_lines[row] = 1
            number_of_iteration = 0
            for i in self.board[row, :]:
                if same_values.size == 0:
                    same_values = np.append(same_values, i)
                else:
                    if same_values[-1] == i:
                        same_values = np.append(same_values, i)
                    else:
                        if same_values.size >= 2:
                            self.points_per_row_column_diagonal[row][int(same_values[0]) - 1] += same_values.size
                            self.players_points[int(same_values[0]) - 1] += same_values.size
                        same_values = np.array([])
                        same_values = np.append(same_values, i)
                if number_of_iteration == 6 and same_values.size != 0:
                    if same_values.size >= 2:
                        self.points_per_row_column_diagonal[row][int(same_values[0]) - 1] += same_values.size
                        self.players_points[int(same_values[0]) - 1] += same_values.size
                    break
                number_of_iteration += 1
        # sprawdzenie i ewentualnie policzenie punktów w lewej przekątnej
        if self.counted_lines[14] == 0 and 0 not in self.board.diagonal():
            same_values = np.array([])
            self.counted_lines[14] = 1
            number_of_iteration = 0
            for i in self.board.diagonal():
                if same_values.size == 0:
                    same_values = np.append(same_values, i)
                else:
                    if same_values[-1] == i:
                        same_values = np.append(same_values, i)
                    else:
                        if same_values.size >= 2:
                            self.points_per_row_column_diagonal[14][int(same_values[0]) - 1] += same_values.size
                            self.players_points[int(same_values[0]) - 1] += same_values.size
                        same_values = np.array([])
                        same_values = np.append(same_values, i)
                if number_of_iteration == 6 and same_values.size != 0:
                    if same_values.size >= 2:
                        self.points_per_row_column_diagonal[14][int(same_values[0]) - 1] += same_values.size
                        self.players_points[int(same_values[0]) - 1] += same_values.size
                    break
                number_of_iteration += 1
        # sprawdzenie i ewentualnie policzenie punktów w prawej przekątnej
        if self.counted_lines[15] == 0 and 0 not in np.diag(np.fliplr(self.board)):
            same_values = np.array([])
            self.counted_lines[15] = 1
            number_of_iteration = 0
            for i in np.diag(np.fliplr(self.board)):
                if same_values.size == 0:
                    same_values = np.append(same_values, i)
                else:
                    if same_values[-1] == i:
                        same_values = np.append(same_values, i)
                    else:
                        if same_values.size >= 2:
                            self.points_per_row_column_diagonal[15][int(same_values[0]) - 1] += same_values.size
                            self.players_points[int(same_values[0]) - 1] += same_values.size
                        same_values = np.array([])
                        same_values = np.append(same_values, i)
                if number_of_iteration == 6 and same_values.size != 0:
                    if same_values.size >= 2:
                        self.points_per_row_column_diagonal[15][int(same_values[0]) - 1] += same_values.size
                        self.players_points[int(same_values[0]) - 1] += same_values.size
                    break
                number_of_iteration += 1

    ###### MIN - MAX ######
    def min_max(self, board, player, max_depth, rating_method_one=False, rating_method_two=False, random_node_choice=False, empty_adjacent_cells_node_choice=False):
        moves = np.argwhere(board == 0)
        if random_node_choice:
            np.random.shuffle(moves)
        if empty_adjacent_cells_node_choice:
            cell_values = np.array([-1 * self.count_empty_adjacent_cells(board, move[0], move[1]) for move in moves])
            cells_choice_order = np.argsort(cell_values)
            sorted_moves = np.array(moves)[cells_choice_order]
            moves = sorted_moves
        best_move = moves[0]
        best_score = -np.inf
        if player == 1:
            next_player = 2
        else:
            next_player = 1
        for move in moves:
            clone = self.make_move_on_board(board, move, player)
            score = self.min_play(clone, next_player, player, max_depth, 0, rating_method_one, rating_method_two, random_node_choice, empty_adjacent_cells_node_choice)
            if score > best_score:
                # print("Nowy najlepszy wynik: " + str(score) + "Dla gracza: " + str(player))
                best_move = move
                best_score = score
        return best_move

    # min - max minimizer
    def min_play(self, board, cur_player, player, max_depth, current_depth, rating_method_one, rating_method_two, random_node_choice, empty_adjacent_cells_node_choice):
        if player == 1:
            self.number_of_nodes_searched_player_1 += 1
        else:
            self.number_of_nodes_searched_player_2 += 1
        if 0 not in board or current_depth == max_depth:
            return self.rate_table_state_by_our_points_and_empty_fields(board,
                                                                        player) if rating_method_one else (self.rate_table_state_by_our_points_and_opponent_points(
                board, player) if rating_method_two else self.rate_table_state_by_opponent_points_and_opponent_empty_cells(board, player))
        moves = np.argwhere(board == 0)
        if random_node_choice:
            np.random.shuffle(moves)
        if empty_adjacent_cells_node_choice:
            cell_values = np.array([-1 * self.count_empty_adjacent_cells(board, move[0], move[1]) for move in moves])
            cells_choice_order = np.argsort(cell_values)
            sorted_moves = np.array(moves)[cells_choice_order]
            moves = sorted_moves
        best_score = np.inf
        if cur_player == 1:
            next_player = 2
        else:
            next_player = 1
        for move in moves:
            clone = self.make_move_on_board(board, move, cur_player)
            score = self.max_play(clone, next_player, player, max_depth, current_depth + 1, rating_method_one, rating_method_two, random_node_choice, empty_adjacent_cells_node_choice)
            if score < best_score:
                best_move = move
                best_score = score
        return best_score

    # min - max maximizer
    def max_play(self, board, cur_player, player, max_depth, current_depth, rating_method_one, rating_method_two, random_node_choice, empty_adjacent_cells_node_choice):
        if player == 1:
            self.number_of_nodes_searched_player_1 += 1
        else:
            self.number_of_nodes_searched_player_2 += 1
        if 0 not in board or current_depth == max_depth:
            return self.rate_table_state_by_our_points_and_empty_fields(board,
                                                                        player) if rating_method_one else (
                self.rate_table_state_by_our_points_and_opponent_points(
                    board,
                    player) if rating_method_two else self.rate_table_state_by_opponent_points_and_opponent_empty_cells(
                    board, player))
        moves = np.argwhere(board == 0)
        if random_node_choice:
            np.random.shuffle(moves)
        if empty_adjacent_cells_node_choice:
            cell_values = np.array([-1 * self.count_empty_adjacent_cells(board, move[0], move[1]) for move in moves])
            cells_choice_order = np.argsort(cell_values)
            sorted_moves = np.array(moves)[cells_choice_order]
            moves = sorted_moves
        best_score = -np.inf
        if cur_player == 1:
            next_player = 2
        else:
            next_player = 1
        for move in moves:
            clone = self.make_move_on_board(board, move, cur_player)
            score = self.min_play(clone, next_player, player, max_depth, current_depth + 1, rating_method_one, rating_method_two, random_node_choice, empty_adjacent_cells_node_choice)
            if score > best_score:
                best_move = move
                best_score = score
        return best_score

    ###### ALFA - BETA CIĘCIE ######
    def alpha_beta(self, board, player, max_depth, rating_method_one=False, rating_method_two=False, random_node_choice=False, empty_adjacent_cells_node_choice=False):
        moves = np.argwhere(board == 0)
        if random_node_choice:
            np.random.shuffle(moves)
        if empty_adjacent_cells_node_choice:
            cell_values = np.array([-1 * self.count_empty_adjacent_cells(board, move[0], move[1]) for move in moves])
            cells_choice_order = np.argsort(cell_values)
            sorted_moves = np.array(moves)[cells_choice_order]
            moves = sorted_moves
        best_move = moves[0]
        best_score = -np.inf
        beta = np.inf
        if player == 1:
            next_player = 2
        else:
            next_player = 1
        for move in moves:
            clone = self.make_move_on_board(board, move, player)
            score = self.alpha_beta_minimizer(clone, best_score, beta, next_player, player, max_depth, 0,
                                              rating_method_one, rating_method_two, random_node_choice, empty_adjacent_cells_node_choice)
            if score > best_score:
                # print("Nowy najlepszy wynik: " + str(score) + "Dla gracza: " + str(player))
                best_move = move
                best_score = score
        return best_move

    # alfa - beta minimizer
    def alpha_beta_minimizer(self, board, alpha, beta, cur_player, player, max_depth, current_depth, rating_method_one, rating_method_two, random_node_choice, empty_adjacent_cells_node_choice):
        if player == 1:
            self.number_of_nodes_searched_player_1 += 1
        else:
            self.number_of_nodes_searched_player_2 += 1
        if 0 not in board or current_depth == max_depth:
            return self.rate_table_state_by_our_points_and_empty_fields(board,
                                                                        player) if rating_method_one else (
                self.rate_table_state_by_our_points_and_opponent_points(
                    board,
                    player) if rating_method_two else self.rate_table_state_by_opponent_points_and_opponent_empty_cells(
                    board, player))
        moves = np.argwhere(board == 0)
        if random_node_choice:
            np.random.shuffle(moves)
        if empty_adjacent_cells_node_choice:
            cell_values = np.array([-1 * self.count_empty_adjacent_cells(board, move[0], move[1]) for move in moves])
            cells_choice_order = np.argsort(cell_values)
            sorted_moves = np.array(moves)[cells_choice_order]
            moves = sorted_moves
        best_score = np.inf
        if cur_player == 1:
            next_player = 2
        else:
            next_player = 1
        for move in moves:
            clone = self.make_move_on_board(board, move, cur_player)
            score = self.alpha_beta_maximizer(clone, alpha, beta, next_player, player, max_depth, current_depth + 1,
                                              rating_method_one, rating_method_two, random_node_choice, empty_adjacent_cells_node_choice)
            if score < best_score:
                best_move = move
                best_score = score
            if best_score <= alpha:
                if player == 1:
                    self.number_of_alpha_cuts_player_1 += 1
                else:
                    self.number_of_alpha_cuts_player_2 += 1
                return best_score
            beta = min(beta, best_score)
        return best_score

    # alfa - beta maximizer
    def alpha_beta_maximizer(self, board, alpha, beta, cur_player, player, max_depth, current_depth, rating_method_one, rating_method_two, random_node_choice, empty_adjacent_cells_node_choice):
        if player == 1:
            self.number_of_nodes_searched_player_1 += 1
        else:
            self.number_of_nodes_searched_player_2 += 1
        if 0 not in board or current_depth == max_depth:
            return self.rate_table_state_by_our_points_and_empty_fields(board,
                                                                        player) if rating_method_one else (
                self.rate_table_state_by_our_points_and_opponent_points(
                    board,
                    player) if rating_method_two else self.rate_table_state_by_opponent_points_and_opponent_empty_cells(
                    board, player))
        moves = np.argwhere(board == 0)
        if random_node_choice:
            np.random.shuffle(moves)
        if empty_adjacent_cells_node_choice:
            cell_values = np.array([-1 * self.count_empty_adjacent_cells(board, move[0], move[1]) for move in moves])
            cells_choice_order = np.argsort(cell_values)
            sorted_moves = np.array(moves)[cells_choice_order]
            moves = sorted_moves
        best_score = -np.inf
        if cur_player == 1:
            next_player = 2
        else:
            next_player = 1
        for move in moves:
            clone = self.make_move_on_board(board, move, cur_player)
            score = self.alpha_beta_minimizer(clone, alpha, beta, next_player, player, max_depth, current_depth + 1,
                                              rating_method_one, rating_method_two, random_node_choice, empty_adjacent_cells_node_choice)
            if score > best_score:
                best_move = move
                best_score = score
            if best_score >= beta:
                if player == 1:
                    self.number_of_beta_cuts_player_1 += 1
                else:
                    self.number_of_beta_cuts_player_2 += 1
                return best_score
            alpha = max(alpha, best_score)
        return best_score

    # funkcja oceniająca stan planszy pod względem liczby pól, które należą do danego gracza i pól pustych, które graniczą z polami gracza
    def rate_table_state_by_our_points_and_empty_fields(self, board, player):
        value = 0

        my_cells_value = 0
        for my_cell in np.where(board == player):
            my_current_cell_value = 0

            if my_cell[0] > 0:
                if board[my_cell[0] - 1][my_cell[1]] == player:
                    my_current_cell_value += 1
            elif board[my_cell[0] + 1][my_cell[1]] == player:
                my_current_cell_value += 1
            if my_cell[1] > 0:
                if board[my_cell[0]][my_cell[1] - 1] == player:
                    my_current_cell_value += 1
            elif board[my_cell[0]][my_cell[1] + 1] == player:
                my_current_cell_value += 1

            my_cells_value += my_current_cell_value

        value += my_cells_value

        # policzenie punktów w lewej przekątnej
        my_cells_value = 0
        for index, value in enumerate(board.diagonal()):
            if index > 0:
                if board[index - 1][index - 1] == player:
                    my_cells_value += 1
            else:
                if board[index + 1][index + 1] == player:
                    my_cells_value += 1

        value += my_cells_value

        # policzenie punktów w prawej przekątnej
        my_cells_value = 0
        for index, value in enumerate(np.diag(np.fliplr(board))):
            if index > 0:
                if board[index - 1][index - 1] == player:
                    my_cells_value += 1
            else:
                if board[index + 1][index + 1] == player:
                    my_cells_value += 1

        value += my_cells_value

        # policzenie wartości pustych pól graniczących z polami gracza
        empty_cells_value = 0
        for empty_cell in np.argwhere(board == 0):
            current_empty_cell_value = 0

            if empty_cell[0] > 0:
                if board[empty_cell[0] - 1][empty_cell[1]] == player:
                    current_empty_cell_value += 1
            if empty_cell[0] < 6:
                if board[empty_cell[0] + 1][empty_cell[1]] == player:
                    current_empty_cell_value += 1
            if empty_cell[1] > 0:
                if board[empty_cell[0]][empty_cell[1] - 1] == player:
                    current_empty_cell_value += 1
            if empty_cell[1] < 6:
                if board[empty_cell[0]][empty_cell[1] + 1] == player:
                    current_empty_cell_value += 1

            empty_cells_value += current_empty_cell_value

        value += empty_cells_value

        return value

    # funkcja oceniająca stan planszy pod względem różnicy między punktami gracza a przeciwnika
    def rate_table_state_by_our_points_and_opponent_points(self, board, player):
        value = 0
        my_cells_value = 0
        for my_cell in np.where(board == player):
            my_current_cell_value = 0

            if my_cell[0] > 0:
                if board[my_cell[0] - 1][my_cell[1]] == player:
                    my_current_cell_value += 1
            elif board[my_cell[0] + 1][my_cell[1]] == player:
                my_current_cell_value += 1
            if my_cell[1] > 0:
                if board[my_cell[0]][my_cell[1] - 1] == player:
                    my_current_cell_value += 1
            elif board[my_cell[0]][my_cell[1] + 1] == player:
                my_current_cell_value += 1

            my_cells_value += my_current_cell_value

        value += my_cells_value

        if player == 1:
            opponent = 2
        else:
            opponent = 1

        his_cells_value = 0
        for his_cell in np.where(board == opponent):
            his_current_cell_value = 0

            if his_cell[0] > 0:
                if board[his_cell[0] - 1][his_cell[1]] == player:
                    his_current_cell_value += 1
            elif board[his_cell[0] + 1][his_cell[1]] == player:
                his_current_cell_value += 1
            if his_cell[1] > 0:
                if board[his_cell[0]][his_cell[1] - 1] == player:
                    his_current_cell_value += 1
            elif board[his_cell[0]][his_cell[1] + 1] == player:
                his_current_cell_value += 1

                his_cells_value += his_current_cell_value

        value -= his_cells_value

        # policzenie punktów w lewej przekątnej
        my_cells_value = 0
        his_cells_value = 0
        for index, value in enumerate(board.diagonal()):
            if index > 0:
                if board[index - 1][index - 1] == value:
                    if value == player:
                        my_cells_value += 1
                    else:
                        his_cells_value += 1
            else:
                if board[index + 1][index + 1] == value:
                    if value == player:
                        my_cells_value += 1
                    else:
                        his_cells_value += 1

        value += my_cells_value
        value -= his_cells_value

        # policzenie punktów w prawej przekątnej
        my_cells_value = 0
        his_cells_value = 0
        for index, value in enumerate(np.diag(np.fliplr(board))):
            if index > 0:
                if board[index - 1][index - 1] == value:
                    if value == player:
                        my_cells_value += 1
                    else:
                        his_cells_value += 1
            else:
                if board[index + 1][index + 1] == value:
                    if value == player:
                        my_cells_value += 1
                    else:
                        his_cells_value += 1

        value += my_cells_value
        value -= his_cells_value
        return value

    # funkcja oceniająca stan planszy pod względem punktów przeciwnika i wolnych pól, graniczących z polami przeciwnika
    def rate_table_state_by_opponent_points_and_opponent_empty_cells(self, board, player):
        if player == 1:
            opponent = 2
        else:
            opponent = 1

        value = 0

        his_cells_value = 0
        for his_cell in np.where(board == opponent):
            his_current_cell_value = 0

            if his_cell[0] > 0:
                if board[his_cell[0] - 1][his_cell[1]] == opponent:
                    his_current_cell_value += 1
            elif board[his_cell[0] + 1][his_cell[1]] == opponent:
                his_current_cell_value += 1
            if his_cell[1] > 0:
                if board[his_cell[0]][his_cell[1] - 1] == opponent:
                    his_current_cell_value += 1
            elif board[his_cell[0]][his_cell[1] + 1] == opponent:
                his_current_cell_value += 1

            his_cells_value += his_current_cell_value

        value += his_cells_value

        # policzenie punktów w lewej przekątnej
        his_cells_value = 0
        for index, value in enumerate(board.diagonal()):
            if index > 0:
                if board[index - 1][index - 1] == opponent:
                    his_cells_value += 1
            else:
                if board[index + 1][index + 1] == opponent:
                    his_cells_value += 1

        value += his_cells_value

        # policzenie punktów w prawej przekątnej
        his_cells_value = 0
        for index, value in enumerate(np.diag(np.fliplr(board))):
            if index > 0:
                if board[index - 1][index - 1] == opponent:
                    his_cells_value += 1
            else:
                if board[index + 1][index + 1] == opponent:
                    his_cells_value += 1

        value += his_cells_value

        # policzenie wartości pustych pól graniczących z polami gracza
        empty_cells_value = 0
        for empty_cell in np.argwhere(board == 0):
            current_empty_cell_value = 0

            if empty_cell[0] > 0:
                if board[empty_cell[0] - 1][empty_cell[1]] == opponent:
                    current_empty_cell_value += 1
            if empty_cell[0] < 6:
                if board[empty_cell[0] + 1][empty_cell[1]] == opponent:
                    current_empty_cell_value += 1
            if empty_cell[1] > 0:
                if board[empty_cell[0]][empty_cell[1] - 1] == opponent:
                    current_empty_cell_value += 1
            if empty_cell[1] < 6:
                if board[empty_cell[0]][empty_cell[1] + 1] == opponent:
                    current_empty_cell_value += 1

            empty_cells_value += current_empty_cell_value

        value += empty_cells_value

        return -1 * value

    # funkcje pomocnicze (utility functions)
    def make_move_on_board(self, board, move, player):
        new_board = np.copy(board)
        new_board[move[0]][move[1]] = player
        return new_board

    def print_board(self):
        print("---------------")
        print("  0 1 2 3 4 5 6")
        for index, row in enumerate(self.board):
            print(str(index) + ' ' + ' '.join(colored(element, 'cyan') if element == 1
                                              else colored(element, 'red') if element == 2 else colored(element,
                                                                                                        'green')
                                              for element in row))

    def count_empty_adjacent_cells(self, board, row, column):

        current_empty_cell_value = 0

        if row > 0 and board[row - 1][column] == 0:
            current_empty_cell_value += 1
        if row < 6 and board[row + 1][column] == 0:
            current_empty_cell_value += 1
        if column > 0 and board[row][column - 1] == 0:
            current_empty_cell_value += 1
        if column < 6 and board[row][column + 1] == 0:
            current_empty_cell_value += 1

        return current_empty_cell_value
