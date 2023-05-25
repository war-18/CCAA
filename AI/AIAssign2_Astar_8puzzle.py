from queue import PriorityQueue


class GameState:
    def __init__(self, state, cost, heuristic):
        self.state = state
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)


def a_star(start_state, goal_state, heuristic_func):
    visited = set()
    priority_queue = PriorityQueue()

    start_game_state = GameState(start_state, 0, heuristic_func(start_state, goal_state))
    priority_queue.put(start_game_state)

    while not priority_queue.empty():
        current_state = priority_queue.get()

        if current_state.state == goal_state:
            return current_state.state

        visited.add(tuple(current_state.state))

        # Generate next possible states
        next_states = generate_next_states(current_state.state)

        for next_state in next_states:
            cost = current_state.cost + 1
            heuristic = heuristic_func(next_state, goal_state)
            next_game_state = GameState(next_state, cost, heuristic)

            if tuple(next_state) not in visited:
                priority_queue.put(next_game_state)

    return None


def heuristic_func(state, goal_state):
    misplaced_count = sum(state[i] != goal_state[i] for i in range(len(state)))
    return misplaced_count


def generate_next_states(state):
    next_states = []
    empty_tile_index = state.index(0)
    row, col = empty_tile_index // 3, empty_tile_index % 3

    # Possible moves: left, right, up, down
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for move in moves:
        new_row, new_col = row + move[0], col + move[1]

        # Check if the new position is within the grid
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = state[:]
            new_index = new_row * 3 + new_col

            # Swap the empty tile with the neighboring tile
            new_state[empty_tile_index], new_state[new_index] = new_state[new_index], new_state[empty_tile_index]
            next_states.append(new_state)

    return next_states


def main():
    # Take input from the user for the start state and goal state
    start_state = list(map(int, input("Enter the start state (space-separated): ").split()))
    goal_state = list(map(int, input("Enter the goal state (space-separated): ").split()))

    # Run A* algorithm
    result = a_star(start_state, goal_state, heuristic_func)

    if result is not None:
        print("Goal state found:", result)
    else:
        print("Goal state not reachable.")


if __name__ == "__main__":
    main()
