import threading
import time
import helper

city_list = ["Kyiv", "Vancouver", "Paris", "New york", "Berlin"]
city_list_with_data = []


def create_city_coordinates_list(city_lst):
    threads = []

    for city in city_lst:
        t = threading.Thread(target=helper.find_and_add_city_coordinates, args=(city, city_list_with_data))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    return city_list_with_data


def find_city_with_max_temp(city_lst):
    start_threads_time = time.time()

    threads = []

    create_city_coordinates_list(city_lst)

    for city in city_list_with_data:
        t = threading.Thread(target=helper.get_average_temperature_by_city, args=(city,))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    max_temp = max(city_list_with_data, key=lambda x: x['average_temperature'])

    end_threads_time = time.time()

    streams_duration = start_threads_time - end_threads_time

    return max_temp, streams_duration


print("City with max temp =>", find_city_with_max_temp(city_list)[0])
print("Streams_duration =>", find_city_with_max_temp(city_list)[1])

