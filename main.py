import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap

def randWalk(s):
    #initialise with 0 = unvisited and 1 = visited
    grid = [[0 for _ in range(s)] for _ in range(s)]
    
    x,y = 0, 0
    grid[y][x] = 1
    visitedCount = 1
    total = s ** 2
    
    path = [(x, y)]
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    fig, ax = plt.subplots(figsize=(8,8))
    ax.set_xlim(-0.5, s-0.5)
    ax.set_ylim(-0.5, s-0.5)
    ax.set_title(f'2D Random Walk({s}x{s})')
    ax.set_aspect('equal')
    ax.grid(True)
    cmap = ListedColormap(['white', 'blue'])
    img = ax.imshow(grid, cmap, origin='lower', extent=(-0.5, s-0.5, -0.5, s-0.5))
    line, = ax.plot([], [], 'r-', lw=1)
    point, = ax.plot([], [], 'ro')
    
    def init():
        line.set_data([], [])
        point.set_data([], [])
        return img, line, point
    
    def update(frame):
        nonlocal x, y, visitedCount
        
        if visitedCount < total:
            dx, dy = random.choice(moves)
            newX = max(0, min(s-1, x+dx))
            newY = max(0, min(s-1,y+dy))
            
            if newX != x or newY != y:
                x, y = newX, newY
                if grid[y][x] == 0:
                    grid[y][x] = 1
                    visitedCount += 1
                path.append((x,y))
                img.set_array(grid)
                
                if len(path) > 1:
                    xs, ys = zip(*path)
                    line.set_data(xs, ys)
                    
                point.set_data([x], [y])
                
                print(f'\rProgress: {visitedCount}/{total} cells visited ({100 * visitedCount/total:.2f}%)', end='')
                
                if visitedCount == total:
                    print('\nAll cells visited. Simulation Over.')
                    
        return img, line, point
    
    ani = FuncAnimation(fig, update, frames=range(1000000), init_func=init, blit=True, interval=50, repeat=False)
    plt.show()
    
    return path

if __name__ == '__main__':
    try:
        s = int(input('Enter grid size (e.g., 50 for a 50x50 grid)'))
        if s <= 0:
            raise ValueError('Grid size must be positive')
        
        print('Starting simulation...')
        print('(close the window to stop the simulation)')
        
        path = randWalk(s)
    except ValueError as e:
        print(f'Invalid input: {e}')
    except KeyboardInterrupt:
        print('Simulation stopped by User.')