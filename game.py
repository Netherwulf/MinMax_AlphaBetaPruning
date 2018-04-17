import numpy as np
import random


class Game(object):

    def __init__(self):
        self.board = np.zeros((7, 7), dtype=int)
        self.points_per_row_column_diagonal = np.zeros((16, 2), dtype=int)
        self.players_points = np.zeros((2, 1), dtype=int)
        pass

    def play(self, human_player_one=False):
        while 0 in self.board:
            if human_player_one:
                print(self.board)
                chosen_x, chosen_y = [int(x) for x in input("Podaj współrzędne x i y wybranego pola oddzielone spacją: ").split()]
                while self.board[chosen_x][chosen_y] != 0:
                    chosen_x, chosen_y = [int(x) for x in
                                          input("Podaj współrzędne x i y wybranego pola oddzielone spacją: ").split()]
                self.board[chosen_x][chosen_y] = 1
                # pierwszy gracz ma ostatni ruch
                if 0 not in self.board:
                    break
                free_fields = np.where(self.board == 0)
                computer_chosen_index = random.randint(0, free_fields[0].length - 1)
                self.board[free_fields[0][computer_chosen_index]][free_fields[1][computer_chosen_index]] = 2
            if not human_player_one:
                free_fields = np.where(self.board == 0)
                computer_chosen_index = random.randint(0, free_fields[0].length - 1)
                self.board[free_fields[0][computer_chosen_index]][free_fields[1][computer_chosen_index]] = 2
                if 0 not in self.board:
                    break
                print(self.board)
                chosen_x, chosen_y = [int(x) for x in
                                      input("Podaj współrzędne x i y wybranego pola oddzielone spacją: ").split()]
                while self.board[chosen_x][chosen_y] != 0:
                    chosen_x, chosen_y = [int(x) for x in
                                          input("Podaj współrzędne x i y wybranego pola oddzielone spacją: ").split()]
                self.board[chosen_x][chosen_y] = 1
        print("Gra dobiegła końca!")
        print("Punkty gracza 1: " + self.players_points[0])
        print("Punkty gracza 2: " + self.players_points[1])

    def check_results(self, row, column):
        if 0 not in self.board[:, column]:
            same_values = np.array([])
            for i in self.board[:, column]:
                if same_values.size == 0 or same_values[-1] == i:
                    same_values = np.append(same_values, i)
                else:
                    if same_values.size >= 2:
                        self.points_per_row_column_diagonal[7+column][same_values[0]] += same_values.size
                        self.players_points[same_values[0]] += same_values.size
                    same_values = np.array([])
        if 0 not in self.board[row, :]:
            same_values = np.array([])
            for i in self.board[row, :]:
                if same_values.size == 0 or same_values[-1] == i:
                    same_values = np.append(same_values, i)
                else:
                    if same_values.size >= 2:
                        self.points_per_row_column_diagonal[row][same_values[0]] += same_values.size
                        self.players_points[same_values[0]] += same_values.size
                    same_values = np.array([])
        if 0 not in self.board.diagonal():
            same_values = np.array([])
            for i in self.board.diagonal():
                if same_values.size == 0 or same_values[-1] == i:
                    same_values = np.append(same_values, i)
                else:
                    if same_values.size >= 2:
                        self.points_per_row_column_diagonal[14][same_values[0]] += same_values.size
                        self.players_points[same_values[0]] += same_values.size
                    same_values = np.array([])
        if 0 not in np.diag(np.fliplr(self.board)):
            same_values = np.array([])
            for i in np.diag(np.fliplr(self.board)):
                if same_values.size == 0 or same_values[-1] == i:
                    same_values = np.append(same_values, i)
                else:
                    if same_values.size >= 2:
                        self.points_per_row_column_diagonal[15][same_values[0]] += same_values.size
                        self.players_points[same_values[0]] += same_values.size
                    same_values = np.array([])
