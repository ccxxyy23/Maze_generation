import random
import pyxel

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = [[0 if x % 2 == 1 and y % 2 == 1\
                     else 1 for x in range(width)] for y in range(height)]
        self.map[1][0] = 0  # entry
        self.map[height - 2][width - 1] = 0  # exit
        self.visited = []
        # right up left down
        self.dx = [1, 0, -1, 0]
        self.dy = [0, -1, 0, 1]
        self.start = [1, 1]
        self.visited.append(self.start)
        self.wall_list = []
        self.get_neighbor_wall(self.start, self.wall_list)
    
    # generate the maze once, just for testing
    def generate(self):
        start = [1, 1]
        self.visited.append(start)
        wall_list = []
        self.get_neighbor_wall(start, wall_list)
        while wall_list:
            wall_position = random.choice(wall_list)
            neighbor_road = self.get_neighbor_road(wall_position)
            wall_list.remove(wall_position)
            # one of two roads have been visited or both are visited
            self.deal_with_not_visited(neighbor_road[0], wall_position, wall_list)
            self.deal_with_not_visited(neighbor_road[1], wall_position, wall_list)
    
    # only generate the next frame
    def next_frame(self):
        if not self.wall_list:
            return False
        
        while self.wall_list:
            wall_position = random.choice(self.wall_list)
            neighbor_road = self.get_neighbor_road(wall_position)
            self.wall_list.remove(wall_position)
            # one of two roads have been visited or both are visited
            vis1 = self.deal_with_not_visited(neighbor_road[0], wall_position, self.wall_list)
            vis2 = self.deal_with_not_visited(neighbor_road[1], wall_position, self.wall_list)
            if vis1 + vis2 == 1:
                break
            
        return True
    
    def get_neighbor_wall(self, start, wall_list):
        x, y = start[0], start[1]
        for i in range(4):
            x_new = x + self.dx[i]
            y_new = y + self.dy[i]
            if 0 < x_new < self.height - 1 and 0 < y_new < self.width - 1 and self.map[x_new][y_new] == 1:
                wall_list.append((x_new, y_new))


    def get_neighbor_road(self, wall_position):
        x, y = wall_position[0], wall_position[1]
        neighbor_road = []
        for i in range(4):
            x_new = x + self.dx[i]
            y_new = y + self.dy[i]
            if 0 < x_new < self.height - 1 and 0 < y_new < self.width - 1 and self.map[x_new][y_new] == 0:
                neighbor_road.append((x_new, y_new))
        return neighbor_road
    

    def print_map(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                print(self.map[i][j], end = ' ')
            print()
    
    
    def deal_with_not_visited(self, nr, wall_position, wall_list):
        if nr in self.visited:
            return 0
        self.visited.append(nr)
        x, y = wall_position[0], wall_position[1]
        self.map[x][y] = 0 #打通
        self.get_neighbor_wall(nr, wall_list)
        return 1
    


#maze = Maze(5, 5)
#maze.print_map()
#print()
#maze.generate()
#maze.print_map()




