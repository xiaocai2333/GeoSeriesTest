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


def collect_time_to_draw_map():
    data_num_list = os.listdir("output/arctern")
    data_num_time = {}
    arctern_file = open("arctern_for_html.txt", "w")
    geopandas_file = open("geopandas_for_html.txt", "w")
    for data_num in data_num_list:
        func_list = os.listdir("output/geopandas/" + data_num)
        arctern_time = []
        geopandas_time = []
        print(len(func_list))
        for func_file in func_list:
            arctern_time.append(calculate_time("output/arctern/" + data_num + "/" + func_file))
            geopandas_time.append(calculate_time("output/geopandas/" + data_num + "/" + func_file))
        arctern_file.writelines(data_num + ": " + str(arctern_time) + "\n")
        geopandas_file.writelines(data_num + ": " + str(geopandas_time) + "\n")

    arctern_file.writelines("func_list" + str([file.replace(".txt", "") for file in func_list]) + "\n")
    geopandas_file.writelines("func_list" + str([file.replace(".txt", "") for file in func_list]) + "\n")
    arctern_file.close()
    geopandas_file.close()


if __name__ == "__main__":

    collect_time()
    collect_time_to_draw_map()
