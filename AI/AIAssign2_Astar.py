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

    start_game_state = GameState(start_state, 0, heuristic_func(start_state))
    priority_queue.put(start_game_state)

    while not priority_queue.empty():
        current_state = priority_queue.get()

        if current_state.state == goal_state:
            return current_state.state

        visited.add(current_state.state)

        # Generate next possible states
        next_states = generate_next_states(current_state.state)

        for next_state in next_states:
            cost = current_state.cost + 1
            heuristic = heuristic_func(next_state)
            next_game_state = GameState(next_state, cost, heuristic)

            if next_state not in visited:
                priority_queue.put(next_game_state)

    return None


def heuristic_func(state):
    # Calculate the estimated cost from the current state to the goal state
    # Return the heuristic value
    goal_state = sorted(state)
    misplaced_count = sum(state[i] != goal_state[i] for i in range(len(state)))
    return misplaced_count


def generate_next_states(state):
    next_states = []

    # Generate next states by swapping adjacent digits
    for i in range(len(state) - 1):
        next_state = list(state)
        next_state[i], next_state[i + 1] = next_state[i + 1], next_state[i]
        next_states.append("".join(next_state))

    return next_states


def main():
    # Take input from the user
    start_state = input("Enter the start state: ")
    goal_state = input("Enter the goal state: ")

    # Run A* algorithm
    result = a_star(start_state, goal_state, heuristic_func)

    if result is not None:
        print("Goal state found:", result)
    else:
        print("Goal state not reachable.")


if __name__ == "__main__":
    main()
