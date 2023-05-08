import multiprocessing
import time
import helper

city_list = ["Kyiv", "Vancouver", "Paris", "New york", "Berlin"]
city_list_with_data = []


def create_city_coordinates_list_by_process(city_lst):
    processes = []

    for city in city_lst:
        p = multiprocessing.Process(target=helper.find_and_add_city_coordinates, args=(city, city_list_with_data))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    return city_list_with_data


def find_city_with_max_temp_by_process(city_lst):
    start_process_time = time.time()

    create_city_coordinates_list_by_process(city_lst)

    processes = []

    for city in city_list_with_data:
        p = multiprocessing.Process(target=helper.get_average_temperature_by_city, args=(city,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    max_temp = max(city_list_with_data, key=lambda x: x['average_temperature'])

    end_process_time = time.time()

    process_duration = end_process_time - start_process_time

    return max_temp, process_duration


print("City with max temp =>", find_city_with_max_temp_by_process(city_list)[0])
print("Process_duration =>", find_city_with_max_temp_by_process(city_list)[1])
