import numpy as np
import random


class Game(object):

    def __init__(self):
        self.board = np.zeros((7, 7), dtype=int)
        self.points_per_row_column_diagonal = np.zeros((16, 2), dtype=int)
        self.players_points = np.zeros(2, dtype=int)
        self.counted_lines = np.zeros(16, dtype=int)
        pass

    def play(self, human_player_one=False, cpu_vs_cpu=False):
        while 0 in self.board:
            if human_player_one and not cpu_vs_cpu:
                print(self.board)
                chosen_x, chosen_y = [int(x) for x in
                                      input("Podaj współrzędne x i y wybranego pola oddzielone spacją: ").split()]
                while 0 > chosen_x or chosen_x > 6 or 0 > chosen_y or chosen_y > 6 or self.board[chosen_x][chosen_y] != 0:
                    chosen_x, chosen_y = [int(x) for x in
                                          input("Podaj współrzędne x i y wybranego pola oddzielone spacją: ").split()]
                self.board[chosen_x][chosen_y] = 1
                self.check_results(chosen_x, chosen_y)
                # pierwszy gracz ma ostatni ruch
                if 0 not in self.board:
                    break
                free_fields = np.where(self.board == 0)
                computer_chosen_index = random.randint(0, free_fields[0].size - 1)
                self.board[free_fields[0][computer_chosen_index]][free_fields[1][computer_chosen_index]] = 2
                self.check_results(free_fields[0][computer_chosen_index], free_fields[1][computer_chosen_index])
            if not human_player_one and not cpu_vs_cpu:
                free_fields = np.where(self.board == 0)
                computer_chosen_index = random.randint(0, free_fields[0].size - 1)
                self.board[free_fields[0][computer_chosen_index]][free_fields[1][computer_chosen_index]] = 1
                self.check_results(free_fields[0][computer_chosen_index], free_fields[1][computer_chosen_index])
                if 0 not in self.board:
                    break
                print(self.board)
                chosen_x, chosen_y = [int(x) for x in
                                      input("Podaj współrzędne x i y wybranego pola oddzielone spacją: ").split()]
                while 0 > chosen_x or chosen_x > 6 or 0 > chosen_y or chosen_y > 6 or 0 != self.board[chosen_x][chosen_y]:
                    chosen_x, chosen_y = [int(x) for x in
                                          input("Podaj współrzędne x i y wybranego pola oddzielone spacją: ").split()]
                self.board[chosen_x][chosen_y] = 2
                self.check_results(chosen_x, chosen_y)
            if cpu_vs_cpu:
                # print(self.board)
                free_fields = np.where(self.board == 0)
                computer_chosen_index = random.randint(0, free_fields[0].size - 1)
                self.board[free_fields[0][computer_chosen_index]][free_fields[1][computer_chosen_index]] = 1
                self.check_results(free_fields[0][computer_chosen_index], free_fields[1][computer_chosen_index])
                if 0 not in self.board:
                    break
                free_fields = np.where(self.board == 0)
                computer_chosen_index = random.randint(0, free_fields[0].size - 1)
                self.board[free_fields[0][computer_chosen_index]][free_fields[1][computer_chosen_index]] = 2
                self.check_results(free_fields[0][computer_chosen_index], free_fields[1][computer_chosen_index])
        print(self.board)
        print("Gra dobiegła końca!")
        print("Punkty gracza 1: " + str(self.players_points[0]))
        print("Punkty gracza 2: " + str(self.players_points[1]))
        print("Wygrał gracz 1." if self.players_points[0] > self.players_points[1] else "Wygrał gracz 2.")
        print("Punkty w wierszach: " + "\n" + str(np.array([self.points_per_row_column_diagonal[i] for i in range(0, 7)])))
        print("Punkty w kolumnach: " + "\n" + str(np.array([self.points_per_row_column_diagonal[i] for i in range(7, 14)])))
        print("Punkty we współrzędnych: " + "\n" + str(np.array([self.points_per_row_column_diagonal[i] for i in range(14, 16)])))

    same_values = np.array([])

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
                            self.points_per_row_column_diagonal[7 + column][int(same_values[0])-1] += same_values.size
                            self.players_points[int(same_values[0])-1] += same_values.size
                        same_values = np.array([])
                        same_values = np.append(same_values, i)
                if number_of_iteration == 6 and same_values.size != 0:
                    if same_values.size >= 2:
                        self.points_per_row_column_diagonal[7 + column][int(same_values[0])-1] += same_values.size
                        self.players_points[int(same_values[0])-1] += same_values.size
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
                            self.points_per_row_column_diagonal[row][int(same_values[0])-1] += same_values.size
                            self.players_points[int(same_values[0])-1] += same_values.size
                        same_values = np.array([])
                        same_values = np.append(same_values, i)
                if number_of_iteration == 6 and same_values.size != 0:
                    if same_values.size >= 2:
                        self.points_per_row_column_diagonal[row][int(same_values[0])-1] += same_values.size
                        self.players_points[int(same_values[0])-1] += same_values.size
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
                            self.points_per_row_column_diagonal[14][int(same_values[0])-1] += same_values.size
                            self.players_points[int(same_values[0])-1] += same_values.size
                        same_values = np.array([])
                        same_values = np.append(same_values, i)
                if number_of_iteration == 6 and same_values.size != 0:
                    if same_values.size >= 2:
                        self.points_per_row_column_diagonal[14][int(same_values[0])-1] += same_values.size
                        self.players_points[int(same_values[0])-1] += same_values.size
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
                            self.points_per_row_column_diagonal[15][int(same_values[0])-1] += same_values.size
                            self.players_points[int(same_values[0])-1] += same_values.size
                        same_values = np.array([])
                        same_values = np.append(same_values, i)
                if number_of_iteration == 6 and same_values.size != 0:
                    if same_values.size >= 2:
                        self.points_per_row_column_diagonal[15][int(same_values[0])-1] += same_values.size
                        self.players_points[int(same_values[0])-1] += same_values.size
                    break
                number_of_iteration += 1
