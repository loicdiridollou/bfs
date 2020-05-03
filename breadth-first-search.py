import queue


def create_maze():
    maze = []
    maze.append(['O', '#', ' '])
    maze.append([' ', ' ', ' '])
    maze.append(['#', ' ', '#'])
    maze.append(['#', ' ', '#'])
    maze.append(['#', ' ', ' '])
    maze.append(['#', '#', 'X'])
    return maze


def print_maze(maze, path = ''):
    for j in maze:
        print(j)
    
    '''
    for x, pos in enumerate(path):
        if pos == 'O':
            start = x
    
    i = start
    j = 0
    pos = set()
    '''



def valid_path(maze, put):
    for x, pos in enumerate(maze[0]):
        if pos == 'O':
            start = x
    
    i = start
    j = 0

    

    for k in put:
        if k == 'L':
            j -= 1
        elif k == 'R':
            j += 1
        elif k == 'U':
            i -= 1
        else:
            i += 1

        
        if not (0 <= i < len(maze) and 0 <= j < len(maze[0])):
            return False
        elif maze[i][j] == '#':
            
            return False
        
    return True


def find_end(maze, put):
    for x, pos in enumerate(maze[0]):
        if pos == 'O':
            start = x
    
    i = start
    j = 0

    for k in put:
        if k == 'L':
            j -= 1
        elif k == 'R':
            j += 1
        elif k == 'U':
            i -= 1
        else:
            i += 1

    if maze[i][j] == 'X':
        print('Found')
        return True
        

    return False



def solve_maze(maze):
    nums = queue.Queue()
    nums.put('')
    path = ''
    i = 0
    while not find_end(maze, path):
        path = nums.get()
        for i in ['L', 'R', 'U', 'D']:
            put = path + i
            if valid_path(maze, put):
                nums.put(put)

            
            

maze = create_maze()
print_maze(maze)
solve_maze(maze)

#print(valid_path(maze, 'D'))
