import pyxel
import time
from pacman import Pacman
from maze import Maze
from ghost import Ghost

class App:
    def __init__(self):
        pyxel.init(240, 128)

        self.lives = 3
        self.game_paused = False
        self.game_finished = False
        self.ghosts = [ # initialize ghosts
            Ghost(32, 32, 0, 20, 4, 8, 8, 0, 1),
            Ghost(64, 32, 0, 4, 20, 8, 8, 0, 1),
            Ghost(32, 64, 0, 20, 20, 8, 8, 0, 1),
            Ghost(64, 64, 0, 4, 36, 8, 8, 0, 1)
        ]

        # predefined maze layouts
        self.mazes = [
            [
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
                [1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,0,0,0,0,0,1],
                [1,0,1,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1],
                [1,0,0,0,1,1,1,0,1,0,1,1,1,1,0,1,0,1,1,1,1,0,0,0,1,1,1,0,0,0,1],
                [1,1,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,1,0,1,1,1],
                [1,0,0,0,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,0,0,0,1],
                [1,0,1,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,0,1],
                [1,0,0,0,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1,0,0,0,1],
                [1,1,1,0,1,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,1,0,1,1,1],
                [1,0,0,0,1,1,1,0,1,0,1,1,1,1,0,1,0,1,1,1,1,0,1,0,1,1,1,0,0,0,1],
                [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1],
                [1,0,0,0,0,0,1,0,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1],
                [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
            ],
            [
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
                [1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,0,0,0,0,0,1],
                [1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1],
                [1,0,0,0,1,1,1,0,1,0,1,1,1,1,0,1,0,1,1,1,1,0,0,0,1,1,1,0,0,0,1],
                [1,1,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,1,0,1,1,1],
                [1,0,0,0,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,0,0,0,1],
                [1,0,1,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,0,1],
                [1,0,0,0,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1,0,0,0,1],
                [1,1,1,0,1,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,1,0,1,1,1],
                [1,0,0,0,1,0,0,0,1,0,1,1,1,1,0,1,0,1,1,1,1,0,1,0,0,0,1,0,0,0,1],
                [1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1],
                [1,0,0,0,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1],
                [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
            ],
            [
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
                [1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,0,0,0,0,0,1],
                [1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1],
                [1,0,0,0,1,1,1,0,1,0,1,1,1,1,0,1,0,1,1,1,1,0,0,0,1,1,1,0,0,0,1],
                [1,1,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,1,0,1,1,1],
                [1,0,0,0,1,0,1,0,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,0,0,0,1],
                [1,0,1,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,0,1],
                [1,0,0,0,1,0,1,1,1,1,1,0,1,0,0,1,0,0,1,0,1,0,1,1,1,0,1,0,0,0,1],
                [1,1,1,0,1,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,1,0,1,1,1],
                [1,0,0,0,1,0,0,0,1,0,1,1,1,1,0,1,0,1,1,1,1,0,1,0,0,0,1,0,0,0,1],
                [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1],
                [1,0,0,0,0,0,1,0,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,0,1,0,1,0,1],
                [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
            ]
        ]

        # create mazes
        self.current_maze_index = 0
        self.maze = Maze(
            maze_layout = self.mazes[self.current_maze_index],
            dot_color = pyxel.COLOR_YELLOW,
            big_dot_color = pyxel.COLOR_LIGHT_BLUE,
            wall_color = pyxel.COLOR_DARK_BLUE,
        )
        self.pacman = Pacman(x = 200, y = 16, speed = 2) # initialize pacman
        self.score = 0
        
        print(f"Pacman initialized at ({self.pacman.x}, {self.pacman.y})")
        
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.game_paused:
            # show 'game over' text on the screen (in draw method)
                if pyxel.btnp(pyxel.KEY_R):
                    self.restart_game()
                elif pyxel.btnp(pyxel.KEY_Q):                        
                    pyxel.quit()
                return
            
        # quit the game any time
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
                    
        self.pacman.handle_input()
        self.pacman.move(self.maze.maze_layout)
        
        # handle pacman power up
        if self.maze.maze_layout[self.pacman.y // 8][self.pacman.x // 8] == 2:
            self.pacman.eat_big_dot()
            for ghost in self.ghosts:
                ghost.become_vulnerable()
        
        # update pacman power-up time
        current_time = time.time()
        if self.pacman.power_up_active and self.pacman.power_up_timer + self.pacman.power_up_limit < current_time:
            self.pacman.power_up_active = False
            for ghost in self.ghosts:
                ghost.reset_vulnerability()
        
        # update ghosts
        for ghost in self.ghosts:
            ghost.update()
            if ghost.alive:    
                ghost.move(self.maze.maze_layout, self.pacman.x, self.pacman.y, self.pacman.power_up_active)
            
        for ghost in self.ghosts:
            if abs(ghost.x - self.pacman.x) < 8 and abs(ghost.y - self.pacman.y) < 8:
                if ghost.blinking and ghost.alive:
                    ghost.get_eaten()
                    self.score += 200   # add points for eating a ghost
                else:
                    self.reset_pacman_position()
                    break
        
        # collision detection with dots
        score_increment = self.maze.check_dot_collision(self.pacman.x // 8, self.pacman.y // 8, self.pacman)
        self.score += score_increment

        # check if maze is complete
        if self.maze.total_dots == 0:
            self.current_maze_index += 1
            if self.current_maze_index < len(self.mazes):
                self.maze = Maze(
                    maze_layout = self.mazes[self.current_maze_index],
                    dot_color = pyxel.COLOR_YELLOW,
                    big_dot_color = pyxel.COLOR_RED,
                    wall_color = pyxel.COLOR_DARK_BLUE,
                )
                self.pacman.x, self.pacman.y = 16, 16
            else:
                # ask if user wants to restart the game or quit
                self.game_finished = True
                if pyxel.btnp(pyxel.KEY_R):
                    self.restart_game()
                elif pyxel.btnp(pyxel.KEY_Q):                        
                    pyxel.quit()
                return
                
    def reset_pacman_position(self):
        self.lives -= 1
        if self.lives > 0:
            self.pacman.x, self.pacman.y = 200, 16 # reset to original position
        else:
            self.game_paused = True
    
    def restart_game(self):
        self.current_maze_index = 0
        self.maze = Maze(
            maze_layout = self.mazes[self.current_maze_index],
            dot_color = pyxel.COLOR_YELLOW,
            big_dot_color = pyxel.COLOR_LIGHT_BLUE,
            wall_color = pyxel.COLOR_DARK_BLUE,
        )
        self.pacman = Pacman(x = 200, y = 16, speed = 2)
        self.score = 0
        
        self.ghosts = [
            Ghost(32, 32, 0, 20, 4, 8, 8, 0, 1),
            Ghost(64, 32, 0, 4, 20, 8, 8, 0, 1),
            Ghost(32, 64, 0, 20, 20, 8, 8, 0, 1),
            Ghost(64, 64, 0, 4, 36, 8, 8, 0, 1)
        ]
        self.game_paused = False

    def draw(self):
        pyxel.cls(0)
        self.maze.draw()
        self.pacman.draw()
        
        # draw ghosts
        for ghost in self.ghosts:
            ghost.draw()

        # draw the score
        pyxel.text(5, 5, f"Score: {self.score}", pyxel.COLOR_WHITE)
        
        if self.pacman.power_up_active:
            pyxel.text(5, 20, "Power up active", pyxel.COLOR_GREEN)
        
        # draw 'Game Over' text
        if self.game_paused:
            pyxel.text(50, 60, 'GAME OVER', pyxel.COLOR_RED)
            pyxel.text(35, 80, "PRESS 'R' TO RESTART OR 'Q' TO QUIT", pyxel.COLOR_WHITE)
            pyxel.text(20, 100, f'YOUR SCORE: {self.score}', pyxel.COLOR_WHITE)
            
        if self.game_finished:
            pyxel.text(50, 60, "CONGRATULATIONS, YOU WON", pyxel.COLOR_RED)
            pyxel.text(35, 80, "PRESS 'R' TO RESTART OR 'Q' TO QUIT", pyxel.COLOR_WHITE)
            pyxel.text(20, 100, f'YOUR SCORE: {self.score}', pyxel.COLOR_WHITE)
            
        pyxel.text(5, 15, f"Lives: {self.lives}", pyxel.COLOR_WHITE)


App()
