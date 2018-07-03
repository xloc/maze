import random

class Maze(object):
    def __init__(self, width, height):
        self.width, self.height = width, height

        # cell x,y | <- vertical wall x,y
        # ---------
        # ^ horizontal wall x,y
        self.horizontal_walls = [[True for y in range(height)] for x in range(width)]
        self.vertical_walls = [[True for y in range(height)] for x in range(width)]

    def show(self):
        import matplotlib.pyplot as plt
        def draw_line(x1, y1, x2, y2):
            return plt.plot([x1, x2], [y1, y2], 'k')
            
        w, h = self.width, self.height
        
        plt.axis('equal')
        plt.title('Maze')

        # Draw box
        draw_line(0,0,w,0)  # down
        draw_line(0,h,w,h)  # up
        draw_line(0,0,0,h)  # left
        draw_line(w,0,w,h)  # right

        # Draw walls
        for x in range(self.width):
            for y in range(self.height):
                if self.horizontal_walls[x][y]:
                    draw_line(x, y+1, x+1, y+1)
                if self.vertical_walls[x][y]:
                    draw_line(x+1, y, x+1, y+1)

        plt.show()

    def break_wall(self, x1, y1, x2, y2):
        if abs(x1-x2) == 1 and y1 == y2:
            self.vertical_walls[min(x1, x2)][y1] = False
        elif x1 == x2 and abs(y1-y2) == 1:
            self.horizontal_walls[x1][min(y1, y2)] = False
        else:
            assert False, 'Cannot break the wall'

def generate_maze(mz):
    cell_accessed = set()
    def random_pace_from(x, y):
        for dx, dy in random.sample([[0,1],[0,-1], [1,0], [-1,0]], 4):
            nx, ny = x+dx, y+dy
            if (nx, ny) not in cell_accessed and nx in range(mz.width) and ny in range(mz.height):
                cell_accessed.add((nx, ny))
                yield nx, ny

    def dfs(x, y):
        for next in random_pace_from(x, y):
            mz.break_wall(x, y, *next)
            dfs(*next)
    
    dfs(0, 0)


if __name__ == '__main__':
    mz = Maze(width=10, height=10)
    generate_maze(mz)

    mz.show()