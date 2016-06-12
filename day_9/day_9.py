raw_puzzle_input = open('data', 'r')
raw_puzzle_input = list(raw_puzzle_input)
puzzle_input = [line.strip('\n').split(' ') for line in raw_puzzle_input[0:len(raw_puzzle_input) - 1]]


class Path:
    # A path from one city to another, with a given distance
    def __init__(self, start, end, distance):
        self.start = start
        self.end = end
        self.distance = distance


class Route:
    # A route to a given city, with a given cost
    def __init__(self, city, cost):
        self.city = city
        self.cost = cost


class City:
    # A City with a name, and a list of routes
    def __init__(self, name, routes):
        self.name = name
        self.routes = routes

class TodoEntry:
    # A todo entry with a city, and a path (a list of routes)
    def __init__(self, city_name, path):
        self.city = city_name
        self.path = path


def get_paths(raw_paths):
    paths = []
    for path in raw_paths:
        start = path[0]
        end = path[2]
        distance = path[4]
        paths.append(Path(start, end, distance))
    # Add reversed paths
    reversed_paths = [Path(entry.end, entry.start, entry.distance) for entry in paths]
    paths = paths + reversed_paths
    return paths


def print_path(path):
    print("Start: " + path.start)
    print("End: " + path.end)
    print("Distance: " + path.distance)


def print_paths(paths):
    for path in paths:
        print('--------------')
        print_path(path)


def print_routes(routes):
    for route in routes:
        print("Destination: " + route.city + "  Cost: " + str(route.cost))


def print_city(city):
    print("Name: " + city.name)
    print("Routes: ")
    print_routes(city.routes)


def print_cities(cities):
    for city in cities:
        print('-----------------')
        print_city(city)


def get_cities(paths):
    cities = []
    for path in paths:
        if path.start in [city.name for city in cities]:
            for city in cities:
                if path.start == city.name:
                    city.routes.append(Route(path.end, path.distance))
        else:
            cities.append(City(path.start, [Route(path.end, path.distance)]))
    return cities

def better_soln(soln, old_soln):
    if old_soln == []:
        return True
    elif sum(int(entry.cost) for entry in soln) > sum(int(entry.cost) for entry in old_soln):
        return True
    else:
        return False


def next_todo_entries(todo_entry, cities):
    entries = []
    for city in cities:
        if city.name == todo_entry.city:
            for route in city.routes:
                if route.city not in [entry.city for entry in todo_entry.path]:
                    entries.append(TodoEntry(route.city, todo_entry.path + [route]))
    return entries

def shortest_route_cost_all_cities(cities):
    print('Working......')
    todo = [TodoEntry(city.name, [Route(city.name, 0)]) for city in cities]
    present_soln = []

    while todo is not None:
        try:
            present_todo = todo[0]
        except:
            return sum(int(entry.cost) for entry in present_soln)
        if len(present_todo.path) == len(cities) - 1:
            if better_soln(present_todo.path, present_soln):
                present_soln = todo[0].path
                todo = todo[1:]
            else:
                todo = todo[1:]
        else:
            todo = next_todo_entries(todo[0], cities) + todo[1:]
    return present_soln


cities = get_cities(get_paths(puzzle_input))
cities = cities + [City('Straylight', [])]
# print('~~~~~~~~~~')
# print_cities(cities)

print('The shortest route would have a cost of %d ' % shortest_route_cost_all_cities(cities))