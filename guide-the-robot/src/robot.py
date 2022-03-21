DEFAULT_MAZE = [
    ["*", "*", "*", ".", "*"],
    ["*", "*", "*", ".", "*"],
    ["*", ".", ".", ".", "*"],
    ["*", ".", "*", "*", "*"],
    ["*", ".", "*", "*", "*"],
    ["*", ".", "*", "*", "*"]
]

DEFAULT_START_AND_END = [
    (5, 1),
    (0, 3)
]

class Robot():
    
    def __init__(self):
        self.maze = DEFAULT_MAZE
        self.starting_pos = DEFAULT_START_AND_END[0]
        self.ending_pos = DEFAULT_START_AND_END[1]
        self.current_pos = self.starting_pos
        self.mark_pos = ','
        self.visited = []
        
    def set_maze(self, maze):
        self.maze = maze 
    
    def _get_position(self, elem):
        return [(ix, iy) for ix, row in enumerate(self.maze) for iy, i in enumerate(row) if i == elem][0]


    # While it's more idiomatic to provide one move function and parameterise,
    # Providing 4 will be more instructive for students to solve the robot maze
    # 
    # Errors are caught silenty and kids are provided with 'CODES'

    def _catch_and_move_robot(self, new_pos):
    
        try:
            if self.maze[new_pos[0]][new_pos[1]] == '.':
                self.current_pos = new_pos
                self.visited.append(new_pos)
                if self.current_pos == self.ending_pos:
                    return "FINISHED"
                else:
                    return "OK"
            else:
                return "NO_PATH"
        except IndexError:
            # Robot has tried to fall off the 'maze'
            return "NO_PATH"

    def move_up(self):
        proposed_move = (self.current_pos[0] - 1, self.current_pos[1])
        return self._catch_and_move_robot(proposed_move)

    def move_right(self):
        proposed_move = (self.current_pos[0], self.current_pos[1] + 1)
        return self._catch_and_move_robot(proposed_move)
    
    def move_left(self):
        proposed_move = (self.current_pos[0], self.current_pos[1] - 1)
        return self._catch_and_move_robot(proposed_move)

    def move_down(self):
        proposed_move = (self.current_pos[0] + 1, self.current_pos[1])
        return self._catch_and_move_robot(proposed_move)
 
    def _use_camera(self):
        '''

        '''
        scan_positions = [
            (self.current_pos[0] - 1, self.current_pos[1]),
            (self.current_pos[0], self.current_pos[1] + 1),
            (self.current_pos[0], self.current_pos[1] - 1),
            (self.current_pos[0] + 1, self.current_pos[1])
        ]

        for idx in range(0, len(scan_positions)):
            x, y = scan_positions[idx]
            # For beginners you should design mazes so that this always returns
            if self.maze[x][y] == '.':
                return idx, scan_positions[idx]
            

    def _has_visited_pos(self, pos):
        '''
        Think carefully before excluding this from workflows

        It makes maze solving much harder for beginners
        '''
        if pos in self.visited:
            return True 
        else:
            return False


    def look_around(self):
        '''
        Returns the direction of the next free space in order up -> right -> left -> down.

        
        '''
        visited_pos = True
        while visited_pos:
            free_idx, free_pos = self._use_camera()
            visited_pos = self._has_visited_pos(free_pos)
        
        if free_idx == 0:
            return 'PATH_UP'
        elif free_idx == 1:
            return 'PATH_RIGHT'
        elif free_idx == 2:
            return 'PATH_LEFT'
        elif free_idx == 3:
            return 'PATH_DOWN'
        else:
            return "NO_PATH_SEEN"
        
        




