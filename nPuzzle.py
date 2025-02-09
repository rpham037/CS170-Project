from TreeNode import TreeNode
import heapq as min_heap_esque_queue  # because it sort of acts like a min heap

# Below are some built-in puzzles to allow quick testing.
trivial = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 0]]

veryEasy = [[1, 2, 3],
            [4, 5, 6],
            [7, 0, 8]]

easy = [[1, 2, 0],
        [4, 5, 3],
        [7, 8, 6]]

doable = [[0, 1, 2],
          [4, 5, 3],
          [7, 8, 6]]

oh_boy = [[8, 7, 1],
          [6, 0, 2],
          [5, 4, 3]]

eight_goal_state = [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 0]]


def main():
    puzzle_mode = input("Welcome to an 8-Puzzle Solver. Type '1' to use a default puzzle, or '2' to create your own." + '\n')
    if puzzle_mode == "1":
        select_and_init_algorithm(init_default_puzzle_mode())

    if puzzle_mode == "2":
        print("Enter your puzzle, using a zero to represent the blank. "
              "Please only enter valid 8-puzzles. Enter the puzzle delimiting "
              "the numbers with a space. RET only when finished." + '\n')
        puzzle_row_one = input("Enter the first row: ")
        puzzle_row_two = input("Enter the second row: ")
        puzzle_row_three = input("Enter the third row: ")

        puzzle_row_one = puzzle_row_one.split()
        puzzle_row_two = puzzle_row_two.split()
        puzzle_row_three = puzzle_row_three.split()

        for i in range(0, 3):
            puzzle_row_one[i] = int(puzzle_row_one[i])
            puzzle_row_two[i] = int(puzzle_row_two[i])
            puzzle_row_three[i] = int(puzzle_row_three[i])

        user_puzzle = [puzzle_row_one, puzzle_row_two, puzzle_row_three]
        select_and_init_algorithm(user_puzzle)

    return



def init_default_puzzle_mode():
    selected_difficulty = input(
        "You wish to use a default puzzle. Please enter a desired difficulty on a scale from 0 to 5." + '\n')
    if selected_difficulty == "0":
        print("Difficulty of 'Trivial' selected.")
        return trivial
    if selected_difficulty == "1":
        print("Difficulty of 'Very Easy' selected.")
        return veryEasy
    if selected_difficulty == "2":
        print("Difficulty of 'Easy' selected.")
        return easy
    if selected_difficulty == "3":
        print("Difficulty of 'Doable' selected.")
        return doable
    if selected_difficulty == "4":
        print("Difficulty of 'Oh Boy' selected.")
        return oh_boy
    if selected_difficulty == "5":
        print("Difficulty of 'Impossible' selected.")
        return impossible


def print_puzzle(puzzle):
    for i in range(0, 3):
        print(puzzle[i])
    print('\n')


def select_and_init_algorithm(puzzle):
    algorithm = input("Select algorithm. (1) for Uniform Cost Search, (2) for the Misplaced Tile Heuristic, "
                      "or (3) the Manhattan Distance Heuristic." + '\n')
    if algorithm == "1":
        uniform_cost_search(puzzle)
    elif algorithm == "2":
        a_star_search(puzzle, misplaced_tile_heuristic)
    elif algorithm == "3":
        a_star_search(puzzle, manhattan_distance_heuristic)

  
def misplaced_tile_heuristic(board):
    misplaced_count = 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != 0:
                if board[i][j] != eight_goal_state[i][j]:
                    misplaced_count += 1
    return misplaced_count


def manhattan_distance_heuristic(board):
    size = len(board)
    distance = 0
    for i in range(size):
        for j in range(size):
            tile = board[i][j]
            if tile != 0:
                goal_x, goal_y = divmod(tile - 1, size)
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance


def uniform_cost_search(puzzle):
    starting_node = TreeNode(None, puzzle, 0, 0) #Ensures heuristic is 0 and path cost is begins at start node
    working_queue = []
    repeated_states = dict()
    min_heap_esque_queue.heappush(working_queue, starting_node)
    num_nodes_expanded = 0
    max_queue_size = 0
    repeated_states[starting_node.board_to_tuple()] = "This is the parent board"

    stack_to_print = []  # the board states are stored in a stack

    while len(working_queue) > 0:
        max_queue_size = max(len(working_queue), max_queue_size)
        node_from_queue = min_heap_esque_queue.heappop(working_queue)
        repeated_states[node_from_queue.board_to_tuple()] = "This can be anything"
        num_nodes_expanded += 1

        #Prints traceback of the board
        if node_from_queue.solved():
            # Check if the current state of the board is the solution
            while len(stack_to_print) > 0:  # if the stack of nodes for the traceback
                print_puzzle(stack_to_print.pop())

            print("Number of nodes expanded:", num_nodes_expanded)
            print("Max queue size:", max_queue_size)
            return node_from_queue

        stack_to_print.append(node_from_queue.board)
        
        #Creating all possible moves from the current board
        for neighbor in node_from_queue.get_neighbors(node_from_queue.find_blank()):
            if neighbor.board_to_tuple() not in repeated_states:
                min_heap_esque_queue.heappush(working_queue, neighbor)



def a_star_search(puzzle, heuristic_type):
    starting_node = TreeNode(None, puzzle, 0, heuristic_type(puzzle))
    working_queue = []
    repeated_states = dict()
    min_heap_esque_queue.heappush(working_queue, starting_node)
    num_nodes_expanded = 0
    max_queue_size = 0
    repeated_states[starting_node.board_to_tuple()] = "This is the parent board"

    stack_to_print = []  # the board states are stored in a stack

    while len(working_queue) > 0:
        max_queue_size = max(len(working_queue), max_queue_size)
        node_from_queue = min_heap_esque_queue.heappop(working_queue)
        repeated_states[node_from_queue.board_to_tuple()] = "This can be anything"
        num_nodes_expanded += 1

        #Prints traceback of the board
        if node_from_queue.solved():
            # Check if the current state of the board is the solution
            while len(stack_to_print) > 0:  # if the stack of nodes for the traceback
                print_puzzle(stack_to_print.pop())

            print("Number of nodes expanded:", num_nodes_expanded)
            print("Max queue size:", max_queue_size)
            return node_from_queue

        stack_to_print.append(node_from_queue.board)
        
        #Creating all possible moves from the current board
        for neighbor in node_from_queue.get_neighbors(node_from_queue.find_blank()):
            if neighbor.board_to_tuple() not in repeated_states:
                min_heap_esque_queue.heappush(working_queue, neighbor)





if __name__ == "__main__":
    main()


# # Adding the new code snippet
# accusantium = doloremque(laudantium)
# print(totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi)
# def de architecto beatae vitae dicta sunt explicabo.
