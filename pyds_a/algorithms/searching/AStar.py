import logging
import math
from queue import PriorityQueue

# Define a custom logger
log = logging.getLogger("Astar")


class Item:
    """
        this is the use of object oriented programming to perform A* Algorithm
        item -> Node Object
        X_location -> object location on X axis
        Y_location -> object location on Y axis
        g_score -> path cost
        heuristic -> heuristic of the Item object
    """

    def __init__(self, item, x_location, y_location):
        self.item = item
        self.heuristic = 0
        self.g_score = 0
        self.x_location = x_location
        self.y_location = y_location

    def get_item(self):
        return self.item

    def set_heuristic(self, heuristic):
        self.heuristic = heuristic

    def set_g_score(self, g_score):
        self.g_score = g_score

    def get_x_location(self):
        return self.x_location

    def get_y_location(self):
        return self.y_location

    def __lt__(self, other):
        # Define comparison for priority this is the compare to option
        return (self.heuristic + self.g_score) < (other.heuristic + other.g_score)


def xy_distance(starting_point, node):
    x_distance = abs(starting_point.get_x_location() - node.get_x_location())
    y_distance = abs(starting_point.get_y_location() - node.get_y_location())
    return x_distance, y_distance


def a_star(graph, start, goal, heuristic_function, g_score_generator):
    log.info("A* initialized")
    log.info(f"Start node: {start} Goal: {goal}")

    def set_g_scores(node, initial_node, g_score_calculator):
        # Calculates the G score for the Node
        g_score = g_score_calculator(initial_node, node)
        node.set_g_score(g_score)

    def set_taxicab_distances(use_graph, end_node):
        for node in use_graph:
            x_distance, y_distance = xy_distance(node, end_node)
            taxicab_distance = x_distance + y_distance
            node.set_heuristic(taxicab_distance)
        return use_graph

    def set_euclidean_distances(use_graph, end_node):
        for node in use_graph:
            x_distance, y_distance = xy_distance(node, end_node)
            euclidean_distance = math.sqrt(x_distance ** 2 + y_distance ** 2)
            node.set_heuristic(int(euclidean_distance))  # Assuming heuristic is an integer
        return use_graph

    if heuristic_function == "manhattan":
        graph = set_taxicab_distances(graph, goal)
    elif heuristic_function == "euclidean":
        graph = set_euclidean_distances(graph, goal)
    else:
        raise ValueError("Heuristic function is undefined")

    tunnel = PriorityQueue()
    visited = set()
    tunnel.put(start)

    while not tunnel.empty():
        item = tunnel.get()
        if item not in visited:
            if g_score_generator == "manhattan":
                log.info(f"g_score_generator set as {g_score_generator}")
                set_g_scores(item, start, lambda starting_point, neighbor: sum(xy_distance(starting_point, neighbor)))
            elif g_score_generator == "euclidean":
                log.info(f"g_score_generator set as {g_score_generator}")
                set_g_scores(item, start, lambda starting_point, neighbor: int(
                    round(math.sqrt(sum(x ** 2 for x in xy_distance(starting_point, neighbor))))))
            else:
                log.error("G score is undefined")
                raise ValueError()

            visited.add(item)
            if item == goal:
                return item
            neighbors = graph.get(item, [])
            for neighbor in neighbors:
                tunnel.put(neighbor)

    raise ValueError("Goal node cannot be found")


if __name__ == "__main__":
    # Create sample Item instances representing nodes in your graph
    itemA = Item("A", 0, 0)
    itemB = Item("B", 1, 1)
    itemC = Item("C", 2, 2)
    itemD = Item("D", 3, 3)

    # Define a graph with neighbors for each node
    graph = {
        itemA: [itemB, itemC],
        itemB: [itemA, itemD],
        itemC: [itemA, itemD],
        itemD: [itemB, itemC],
    }

    # Specify the start and goal nodes

    # Perform A* search with the Manhattan heuristic
    result_manhattan = a_star(graph, itemA, itemD, "manhattan", "manhattan")
    print(f"A* search result with Manhattan heuristic: {result_manhattan.get_item()}")

    # Perform A* search with the Euclidean heuristic
    result_euclidean = a_star(graph, itemA, itemD, "euclidean", "euclidean")
    print(f"A* search result with Euclidean heuristic: {result_euclidean.get_item()}")

    # Create sample Item instances representing nodes in your graph
    itemA = Item("A", 0, 0)
    itemB = Item("B", 1, 1)
    itemC = Item("C", 2, 2)
    itemD = Item("D", 3, 3)
    itemE = Item("E", 4, 4)
    itemF = Item("F", 5, 5)

    # Define a graph with neighbors for each node
    graph = {
        itemA: [itemB, itemC],
        itemB: [itemA, itemD],
        itemC: [itemA, itemD],
        itemD: [itemB, itemC, itemE],
        itemE: [itemD, itemF],
        itemF: [itemE],
    }

    # Specify the start and goal nodes
    start_node = itemA
    goal_node = itemF

    # Perform A* search with the Manhattan heuristic
    result_manhattan = a_star(graph, start_node, goal_node, "manhattan", "manhattan")
    if result_manhattan:
        print(f"A* search result with Manhattan heuristic: {result_manhattan.get_item()}")
    else:
        print("Goal node cannot be reached with Manhattan heuristic.")

    # Perform A* search with the Euclidean heuristic
    result_euclidean = a_star(graph, start_node, goal_node, "euclidean", "euclidean")
    if result_euclidean:
        print(f"A* search result with Euclidean heuristic: {result_euclidean.get_item()}")
    else:
        print("Goal node cannot be reached with Euclidean heuristic.")
