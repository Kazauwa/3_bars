import json
import sys


def load_data(filepath):
    with open(filepath, 'r') as reader:
        data = reader.read()
    return json.loads(data)


def get_biggest_bar(data):
    biggest = data[0]
    for bar in data[1:]:
        if biggest.get('SeatsCount') < bar.get('SeatsCount'):
            biggest = bar
    return biggest


def get_smallest_bar(data):
    smallest = data[0]
    for bar in data[1:]:
        if smallest.get('SeatsCount') > bar.get('SeatsCount'):
            smallest = bar
    return smallest


def get_closest_bar(data, longitude, latitude):
    closest = data[0]
    smallest_difference = 999
    for bar in data[1:]:
        bar_long = float(bar.get('Longitude_WGS84'))
        bar_lat = float(bar.get('Latitude_WGS84'))
        current_difference = abs(longitude - bar_long) + abs(latitude - bar_lat)
        if current_difference < smallest_difference:
            closest = bar
            smallest_difference = current_difference
    return closest


if __name__ == '__main__':
    data = load_data(input('Input path to json file: '))
    biggest = get_biggest_bar(data)
    print('\nThe biggest bar is {0} with {1} seats. The address is:\n {2}\n'.format(biggest.get('Name'),
                                                                                    biggest.get('SeatsCount'),
                                                                                    biggest.get('Address')))
    smallest = get_smallest_bar(data)
    print('The smallest bar is {0} with {1} seats. The address is:\n {2}\n'.format(smallest.get('Name'),
                                                                                   smallest.get('SeatsCount'),
                                                                                   smallest.get('Address')))
    if len(sys.argv) > 2:
        closest = get_closest_bar(data, float(sys.argv[1]), float(sys.argv[2]))
        print('The closest bar is {0}. The address is:\n {1}\n'.format(closest.get('Name'),
                                                                       closest.get('Address')))
