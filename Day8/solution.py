from typing import Tuple, List, Set
from queue import PriorityQueue
from itertools import combinations
from UnionFind import UnionFind
from math import prod
INPUT_FILE = r'Day8\input.txt'

Coordinate = List[Tuple[int, int, int]]

def parse_input(filename: str) -> Coordinate:
    with open(filename, 'r') as file:
        return [tuple(map(int, line.split(','))) for line in file]

def compute_squared_distance(left: Coordinate, right: Coordinate):
    return sum((a - b) ** 2 for a, b in zip(left, right))

def create_distance_heap(coordinates: List[Coordinate]) -> PriorityQueue[Tuple[float, Tuple[int, int]]]:
    distances = PriorityQueue()
    for pair in combinations(range(len(coordinates)), 2):
        distances.put((compute_squared_distance(coordinates[pair[0]], coordinates[pair[1]]), pair))
    return distances

def build_circuits_iterations(coordinates: List[Coordinate], coordinate_pairs: PriorityQueue[Tuple[float, Tuple[Coordinate, Coordinate]]]) -> UnionFind:
    circuits = UnionFind(len(coordinates))
    for i in range(1000):
        _, (a, b) = coordinate_pairs.get()
        circuits.unite(a, b)
    return circuits

def build_full_circuits(coordinates: List[Coordinate], coordinate_pairs: PriorityQueue[Tuple[float, Tuple[Coordinate, Coordinate]]]) -> Tuple[Coordinate, Coordinate]:
    circuits = UnionFind(len(coordinates))
    while True:
        _, (a, b) = coordinate_pairs.get()
        circuits.unite(a, b)
        if circuits.get_component_count() == 1:
            return (coordinates[a], coordinates[b])

def product_of_three_largest_circuits(filename: str) -> int:
    coordinates = parse_input(filename)
    sorted_coordinate_pairs = create_distance_heap(coordinates)
    circuits = build_circuits_iterations(coordinates, sorted_coordinate_pairs)
    circuits_sizes = sorted(circuits.get_component_sizes(), reverse=True)
    return prod(circuits_sizes[0:3])

def product_of_last_x_coords(filename: str) -> int:
    coordinates = parse_input(filename)
    sorted_coordinate_pairs = create_distance_heap(coordinates)
    a, b = build_full_circuits(coordinates, sorted_coordinate_pairs)
    return a[0] * b[0]

if __name__ == '__main__':
    print(product_of_three_largest_circuits(INPUT_FILE))
    print(product_of_last_x_coords(INPUT_FILE))
    