import math
import sys

import pygame

from Controller import *


class GUI:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 700))

    def player_vs_player(self):
        turn = 1
        font = pygame.font.SysFont("arial", 25)
        text = [font.render('Player 2 (white) turn', True, 'black'),
                font.render('Player 1 (black) turn', True, 'black')]
        controller = Controller()
        while True:
            self.screen.fill('green')
            for i in range(8):
                pygame.draw.line(self.screen, 'black', (0, 100 + i * 75), (600, 100 + i * 75))
            for i in range(1, 8):
                pygame.draw.line(self.screen, 'black', (i * 75, 100), (i * 75, 700))
            self.screen.blit(text[turn], (210, 10))
            scores = [font.render(f'Player 2 (white) score: {controller.PlayerScores[0]}', True, 'black'),
                      font.render(f'Player 1 (black) score: {controller.PlayerScores[1]}', True, 'black')]
            self.screen.blit(scores[0], (10, 50))
            self.screen.blit(scores[1], (350, 50))
            valid_moves = controller.getValidMoves(turn)
            for i in range(8):
                for j in range(8):
                    if (i + 1, j + 1) in valid_moves:
                        pygame.draw.rect(self.screen, 'red', pygame.Rect(j * 75 + 1, i * 75 + 101, 74, 74))
                    elif controller.board[i][j] == 'w':
                        pygame.draw.circle(self.screen, 'white', ((j) * 75 + 37, (i) * 75 + 137), 30)
                    elif controller.board[i][j] == 'b':
                        pygame.draw.circle(self.screen, 'black', ((j) * 75 + 37, (i) * 75 + 137), 30)
            if not valid_moves:
                if not controller.getValidMoves((turn + 1) % 2):
                    self.screen.fill('green')
                    winner_font = pygame.font.SysFont("blackarial", 40)
                    if controller.PlayerScores[0] > controller.PlayerScores[1]:
                        winner_text = winner_font.render('Player 2 (white) Wins', True, 'black')
                        x = 170
                        y = 220
                    elif controller.PlayerScores[0] < controller.PlayerScores[1]:
                        winner_text = winner_font.render('Player 1 (black) Wins', True, 'black')
                        x = 170
                        y = 220
                    else:
                        winner_text = winner_font.render('Draw', True, 'black')
                        x = 270
                        y = 220
                    mainmenu_text = winner_font.render('Main Menu', True, 'black')
                    self.screen.blit(winner_text, (x, y))
                    pygame.draw.rect(self.screen, 'blue', pygame.Rect(220, 320, 170, 50))
                    self.screen.blit(mainmenu_text, (230, 330))
                else:
                    turn = (turn + 1) % 2
                    continue
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:

                    click = pygame.mouse.get_pressed()[0]

                    if click:
                        if pygame.mouse.get_pos()[0] in range(220, 390) and pygame.mouse.get_pos()[1] in range(320,
                                                                                                               370) and not valid_moves and not controller.getValidMoves((turn + 1) % 2):
                            return
                        x = int((pygame.mouse.get_pos()[1] - 100) / 75) + 1
                        y = int((pygame.mouse.get_pos()[0]) / 75) + 1
                        if (x, y) in valid_moves:
                            controller.make_move(x, y, turn)
                            turn = (turn + 1) % 2
                            break

    def player_vs_computer_menu(self):
        font = pygame.font.SysFont("arialblack", 30)
        othelo_text = font.render("Othelo", True, 'black')
        easy_text = font.render("easy (depth = 1)", True, 'black')
        medium_text = font.render("medium (depth = 3)", True, 'black')
        hard_text = font.render("hard (depth = 5)", True, 'black')
        while True:
            self.screen.fill('lightgreen')
            pygame.draw.rect(self.screen, 'blue', pygame.Rect(170, 150, 285, 50))
            pygame.draw.rect(self.screen, 'blue', pygame.Rect(135, 250, 335, 50))
            pygame.draw.rect(self.screen, 'blue', pygame.Rect(165, 350, 280, 50))
            self.screen.blit(othelo_text, (260, 20))
            self.screen.blit(easy_text, (180, 150))
            self.screen.blit(medium_text, (145, 250))
            self.screen.blit(hard_text, (175, 350))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:

                    click = pygame.mouse.get_pressed()[0]

                    if click:
                        if pygame.mouse.get_pos()[0] in range(170, 455) and pygame.mouse.get_pos()[1] in range(150,
                                                                                                               200):
                            self.player_vs_computer(1)
                            return
                        if pygame.mouse.get_pos()[0] in range(135, 470) and pygame.mouse.get_pos()[1] in range(250,
                                                                                                               300):
                            self.player_vs_computer(3)
                            return
                        if pygame.mouse.get_pos()[0] in range(165, 445) and pygame.mouse.get_pos()[1] in range(350,
                                                                                                               400):
                            self.player_vs_computer(5)
                            return

    def player_vs_computer(self, depth):
        turn = 1
        font = pygame.font.SysFont("arial", 25)
        text = [font.render('Computer (white) turn', True, 'black'),
                font.render('Player (black) turn', True, 'black')]
        controller = Controller()
        while True:
            self.screen.fill('green')
            for i in range(8):
                pygame.draw.line(self.screen, 'black', (0, 100 + i * 75), (600, 100 + i * 75))
            for i in range(1, 8):
                pygame.draw.line(self.screen, 'black', (i * 75, 100), (i * 75, 700))
            self.screen.blit(text[turn], (210, 10))
            scores = [font.render(f'Computer (white) score: {controller.PlayerScores[0]}', True, 'black'),
                      font.render(f'Player (black) score: {controller.PlayerScores[1]}', True, 'black')]
            self.screen.blit(scores[0], (10, 50))
            self.screen.blit(scores[1], (350, 50))
            valid_moves = controller.getValidMoves(turn)
            for i in range(8):
                for j in range(8):
                    if (i + 1, j + 1) in valid_moves:
                        pygame.draw.rect(self.screen, 'red', pygame.Rect(j * 75 + 1, i * 75 + 101, 74, 74))
                    elif controller.board[i][j] == 'w':
                        pygame.draw.circle(self.screen, 'white', ((j) * 75 + 37, (i) * 75 + 137), 30)
                    elif controller.board[i][j] == 'b':
                        pygame.draw.circle(self.screen, 'black', ((j) * 75 + 37, (i) * 75 + 137), 30)
            if not valid_moves:
                if not controller.getValidMoves((turn + 1) % 2):
                    self.screen.fill('green')
                    winner_font = pygame.font.SysFont("blackarial", 40)
                    if controller.PlayerScores[0] > controller.PlayerScores[1]:
                        winner_text = winner_font.render('Computer (white) Wins', True, 'black')
                        x = 170
                        y = 220
                    elif controller.PlayerScores[0] < controller.PlayerScores[1]:
                        winner_text = winner_font.render('Player (black) Wins', True, 'black')
                        x = 170
                        y = 220
                    else:
                        winner_text = winner_font.render('Draw', True, 'black')
                        x = 270
                        y = 220
                    mainmenu_text = winner_font.render('Main Menu', True, 'black')
                    self.screen.blit(winner_text, (x, y))
                    pygame.draw.rect(self.screen, 'blue', pygame.Rect(220, 320, 170, 50))
                    self.screen.blit(mainmenu_text, (230, 330))
                else:
                    turn = (turn + 1) % 2
                    continue
            pygame.display.update()
            if turn == 0 and valid_moves:
                _, best_move = controller.minimax(controller, depth, float('-inf'), float('inf'), True)
                if best_move:
                    controller.board = best_move.board
                    controller.PlayerScores = best_move.PlayerScores
                else:
                    controller.make_move(valid_moves[0][0], valid_moves[0][1], turn)
                turn = (turn + 1) % 2
                continue
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:

                    click = pygame.mouse.get_pressed()[0]

                    if click:
                        if pygame.mouse.get_pos()[0] in range(220, 390) and pygame.mouse.get_pos()[1] in range(320,
                                                                                                               370) and not valid_moves and not controller.getValidMoves(
                            (turn + 1) % 2):
                            return
                        x = int((pygame.mouse.get_pos()[1] - 100) / 75) + 1
                        y = int((pygame.mouse.get_pos()[0]) / 75) + 1
                        if (x, y) in valid_moves:
                            controller.make_move(x, y, turn)
                            turn = (turn + 1) % 2
                            break

    def main_menu(self):
        font = pygame.font.SysFont("arialblack", 30)
        othelo_text = font.render("Othelo", True, 'black')
        playervsplayer_text = font.render("Player Vs Player", True, 'black')
        computervsplayer_text = font.render("Computer Vs Player", True, 'black')
        while True:
            self.screen.fill('lightgreen')
            pygame.draw.rect(self.screen, 'blue', pygame.Rect(170, 150, 285, 50))
            pygame.draw.rect(self.screen, 'blue', pygame.Rect(135, 250, 345, 50))
            self.screen.blit(othelo_text, (260, 20))
            self.screen.blit(playervsplayer_text, (180, 150))
            self.screen.blit(computervsplayer_text, (145, 250))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:

                    click = pygame.mouse.get_pressed()[0]

                    if click:
                        if pygame.mouse.get_pos()[0] in range(170, 455) and pygame.mouse.get_pos()[1] in range(150,
                                                                                                               200):
                            self.player_vs_player()
                        if pygame.mouse.get_pos()[0] in range(135, 480) and pygame.mouse.get_pos()[1] in range(250,
                                                                                                               300):
                            self.player_vs_computer_menu()
