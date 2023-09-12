from maze_generation import Maze
import pyxel

class App:
    pixel = 6
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = Maze(self.width, self.height)
        pyxel.init(width * App.pixel, height * App.pixel)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_S) or pyxel.btnp(pyxel.KEY_D):
            self.maze.next_frame()
        if pyxel.btnp(pyxel.KEY_R):
            self.maze = Maze(self.width, self.height)

    def draw(self):
        # draw maze
        pyxel.cls(0)
        road_color = 7
        wall_color = 0
        start_point_color = 1
        end_point_color = 1
        for x in range(self.height):
            for y in range(self.width):
                color = road_color if self.maze.map[x][y] == 0 else wall_color
                pyxel.rect(y * App.pixel, x * App.pixel, App.pixel, App.pixel, color)
        pyxel.rect(0, App.pixel, App.pixel, App.pixel, start_point_color)
        pyxel.rect((self.width - 1) * App.pixel, (self.height - 2) * App.pixel, App.pixel, App.pixel, end_point_color)

App(23, 21)