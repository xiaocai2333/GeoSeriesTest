import os


def calculate_time(file_path):
    time_list = []
    if not os.path.exists(file_path):
        return 0
    with open(file_path, "r") as f:
        for line in f.readlines():
            time_list.append(float(line.split(":")[-1]))
    s = 0
    for time in time_list:
        s += time
    return s / len(time_list)


def collect_time():
    data_num_list = os.listdir("output/arctern")
    func_list = os.listdir("output/arctern/10_3/")
    data_num_time = {}
    for data_num in data_num_list:
        test_case = {}
        for case in ["arctern", "geopandas"]:
            func_time = {}
            for func_file in func_list:
                func_time[func_file.replace(".txt", "")] = calculate_time(
                    "output/" + case + "/" + data_num + "/" + func_file)
            test_case[case] = func_time
        data_num_time[data_num] = test_case

    import json
    with open("all_test_time.json", "w+") as write_f:
        json_obj = json.dumps(data_num_time)
        write_f.write(json_obj)


if __name__ == "__main__":
    file_list = os.listdir("output/arctern/10_8")
    for file in file_list:
        time = calculate_time(os.path.join("output/arctern/10_8", file))
        print(file, time)
