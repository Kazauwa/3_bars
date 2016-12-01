import json
import sys


def sort_bar_distance(bar):
        bar_long = float(bar.get('Longitude_WGS84'))
        bar_lat = float(bar.get('Latitude_WGS84'))
        difference = abs(longitude - bar_long) + abs(latitude - bar_lat)
        return difference


def load_data(filepath):
    with open(filepath, 'r') as reader:
        raw_bars = reader.read()
    return json.loads(raw_bars)


def get_biggest_bar(data):
    return max(data, key=lambda x: x.get('SeatsCount'))


def get_smallest_bar(data):
    return min(data, key=lambda x: x.get('SeatsCount'))


def get_closest_bar(data, longitude, latitude):
    return min(data, key=sort_bar_distance)


if __name__ == '__main__':
    bars = load_data(input('Input path to json file: '))
    biggest = get_biggest_bar(bars)
    print('\nThe biggest bar is {0} with {1} seats. The address is:\n {2}\n'.format(biggest.get('Name'),
                                                                                    biggest.get('SeatsCount'),
                                                                                    biggest.get('Address')))
    smallest = get_smallest_bar(bars)
    print('The smallest bar is {0} with {1} seats. The address is:\n {2}\n'.format(smallest.get('Name'),
                                                                                   smallest.get('SeatsCount'),
                                                                                   smallest.get('Address')))
    if len(sys.argv) > 2:
        longitude = float(sys.argv[1])
        latitude = float(sys.argv[2])
        closest = get_closest_bar(bars, longitude, latitude)
        print('The closest bar is {0}. The address is:\n {1}\n'.format(closest.get('Name'),
                                                                       closest.get('Address')))
