import numpy as np
import matplotlib.pyplot as plt

from utils import city_randomizer, draw_cities, lexico_graphic, cities_converter, distance_calculator, draw_path


def main():
    n_cities = int(input("enter number of cities:  "))
    area_width = 500
    area_height = 500
    area = np.full((area_width, area_height, 3), 255, np.int16)
    city_locations = city_randomizer(n_cities, area_height, area_width)
    area = draw_cities(area, city_locations)

    paths = lexico_graphic(n_cities)
    best_distance = None
    best_path = None
    for path in paths:
        path = path+[path[0]]
        new_path = cities_converter(path, list(city_locations))
        distance = distance_calculator(new_path)
        if best_distance is not None and distance < best_distance or best_distance is None:
            best_distance = distance
            best_path = new_path.copy()
    area = draw_path(area, best_path, (255, 0, 0))
    plt.imshow(area)
    plt.title("")
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
