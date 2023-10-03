import logging
import math
from queue import PriorityQueue
import heapq

logging.basicConfig(level=logging.INFO)  # Set the desired log level (e.g., DEBUG)
log = logging.getLogger(__name__)


class Item:
    """
        this is the use of object-oriented programming to perform A* Algorithm
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

    def __str__(self):
        return f"Item: {self.item}, X: {self.x_location}, Y: {self.y_location}," \
               f" G-Score: {self.g_score}, Heuristic: {self.heuristic}"

    def __eq__(self, other):
        if isinstance(other, Item):
            return (
                    self.item == other.item and
                    self.x_location == other.x_location and
                    self.y_location == other.y_location
            )
        return False

    def __hash__(self):
        # Hash based on item, x_location, and y_location
        return hash((self.item, self.x_location, self.y_location))

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


class Item2:
    def __init__(self, heuristic, g_score, item):
        self.item = item
        self.heuristic = heuristic
        self.g_score = g_score

    def set_g_score(self, g_score):
        self.g_score = g_score

    def get_item(self):
        return self.item

    def get_heuristic(self):
        return self.heuristic

    def get_g_score(self):
        return self.g_score

    def __str__(self):
        return f"Item2{{item={self.item}, heuristic={self.heuristic}, g_score={self.g_score}}}"

    def __lt__(self, other):
        return (self.heuristic + self.g_score) < (other.heuristic + other.g_score)


def xy_distance(starting_point, node):
    x_distance = abs(starting_point.get_x_location() - node.get_x_location())
    y_distance = abs(starting_point.get_y_location() - node.get_y_location())
    return x_distance, y_distance


def a_star_h_and_g_unknown(graph, start, goal, heuristic_function, g_score_generator):
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

    log.info(" Updating heuristics ")
    if heuristic_function == "manhattan":
        graph = set_taxicab_distances(graph, goal)
    elif heuristic_function == "euclidean":
        graph = set_euclidean_distances(graph, goal)
    else:
        log.error("Heuristic function is undefined")
        raise ValueError
    tunnel = PriorityQueue()
    visited = set()
    tunnel.put(start)

    while not tunnel.empty():
        item = tunnel.get()
        if item not in visited:
            if g_score_generator == "manhattan":
                log.info(f"g_score_generator set as {g_score_generator}")
                set_g_scores(item, start, lambda starting_point, node: sum(xy_distance(starting_point, node)))
            elif g_score_generator == "euclidean":
                log.info(f"g_score_generator set as {g_score_generator}")
                set_g_scores(item, start, lambda starting_point, node: int(
                    round(math.sqrt(sum(x ** 2 for x in xy_distance(starting_point, node))))))
            else:
                log.error("G score is undefined")
                raise ValueError
            log.info(f"Visiting {item}")
            visited.add(item)
            if item == goal:
                log.info(f"Found goal node {item}")
                return item
            neighbors = graph.get(item, [])
            for neighbor in neighbors:
                tunnel.put(neighbor)
    log.error("Goal node cannot be found")
    raise ValueError


def a_star2(graph, start, goal):
    tunnel = []
    init_cost = 0
    visited = set()
    heapq.heappush(tunnel, start)

    while tunnel:
        item = heapq.heappop(tunnel)
        if item not in visited:
            if item == goal:
                return item

            children = graph.get(item, [])
            final_init_cost = init_cost
            for t_item in children:
                t_item.set_g_score(t_item.get_g_score() + final_init_cost)
            tunnel.extend(children)
            visited.add(item)
            init_cost = item.get_g_score()

    raise ValueError("Element not accessible")
