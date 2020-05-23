import argparse
import geopandas as gpd
import shapely
import arctern
import pandas as pd
import time
import os

data_path = "/home/zc/CLionProjects/GeoSeriesTest/data"
output_path = "/home/zc/CLionProjects/GeoSeriesTest/output"


def test_single_col(csv_path, func_name):
    df = pd.read_csv(csv_path, delimiter='|', header=None)
    data_shapely = df[0].apply(shapely.wkt.loads)
    data = gpd.GeoSeries(data_shapely)
    start_time = time.time()
    try:
        exec("data.%s" % func_name)
    except AttributeError:
        print("geopandas has no attribute ", func_name)
        pass
    end_time = time.time()
    with open(output_path + "/geopandas/" + data_num_path + "/" + func_name + ".txt", 'a+') as f:
        f.writelines("geopandas %s time is:" % func_name + str(end_time - start_time))
    arctern_data = arctern.GeoSeries(df[0])
    start_time = time.time()
    try:
        exec("arctern_data.%s" % func_name)
    except AttributeError:
        print("arctern has no attribute ", func_name)
        pass
    end_time = time.time()
    with open(output_path + "/arctern/" + data_num_path + "/" + func_name + ".txt", 'a+') as f:
        f.writelines("arctern %s time is:" % func_name + str(end_time - start_time))


def test_double_cols(csv_path, func_name):
    df = pd.read_csv(csv_path, delimiter='|', header=None)
    data_shapely_1 = df[0].apply(shapely.wkt.loads)
    data_shapely_2 = df[1].apply(shapely.wkt.loads)
    data_col1 = gpd.GeoSeries(data_shapely_1)
    data_col2 = gpd.GeoSeries(data_shapely_2)
    start_time = time.time()
    try:
        exec("data_col1.%s(data_col2)" % func_name)
    except AttributeError:
        print("geopandas has no attribute ", func_name)
        pass
    end_time = time.time()
    with open(output_path + "/geopandas/" + data_num_path + "/" + func_name + ".txt", 'a+') as f:
        f.writelines("geopandas %s time is:" % func_name + str(end_time - start_time))
    arctern_data_col1 = arctern.GeoSeries(df[0])
    arctern_data_col2 = arctern.GeoSeries(df[1])
    start_time = time.time()
    try:
        exec("arctern_data_col1.%s(arctern_data_col2)" % func_name)
    except AttributeError:
        print("arctern has no attribute ", func_name)
        pass
    end_time = time.time()
    with open(output_path + "/arctern/" + data_num_path + "/" + func_name + ".txt", 'a+') as f:
        f.writelines("arctern %s time is:" % func_name + str(end_time - start_time))


def test_point(csv_path, func_name):
    df = pd.read_csv(csv_path, delimiter='|', header=None)
    data_shapely_x = df[0].apply(shapely.wkt.loads)
    data_shapely_y = df[1].apply(shapely.wkt.loads)
    data_x = gpd.GeoSeries(data_shapely_x)
    data_y = gpd.GeoSeries(data_shapely_y)
    start_time = time.time()
    try:
        exec("gpd.GeoSeries.%s(data_x, data_y)" % func_name)
    except AttributeError:
        print("geopandas has no attribute ", func_name)
        pass
    end_time = time.time()
    with open(output_path + "/geopandas/" + data_num_path + "/" + func_name + ".txt", 'a+') as f:
        f.writelines("geopandas %s time is:" % func_name + str(end_time - start_time))
    arctern_data_x = arctern.GeoSeries(df[0])
    arctern_data_y = arctern.GeoSeries(df[1])
    start_time = time.time()
    try:
        exec("arctern.GeoSeries.%s(arctern_data_x, arctern_data_y)" % func_name)
    except AttributeError:
        print("arctern has no attribute ", func_name)
        pass
    end_time = time.time()
    with open(output_path + "/arctern/" + data_num_path + "/" + func_name + ".txt", 'a+') as f:
        f.writelines("arctern %s time is:" % func_name + str(end_time - start_time))


def test_polygon_from_envelope(csv_path, func_name):
    df = pd.read_csv(csv_path, delimiter='|', header=None)
    data_shapely_min_x = df[0].apply(shapely.wkt.loads)
    data_shapely_min_y = df[1].apply(shapely.wkt.loads)
    data_shapely_max_x = df[2].apply(shapely.wkt.loads)
    data_shapely_max_y = df[3].apply(shapely.wkt.loads)
    data_min_x = gpd.GeoSeries(data_shapely_min_x)
    data_min_y = gpd.GeoSeries(data_shapely_min_y)
    data_max_x = gpd.GeoSeries(data_shapely_max_x)
    data_max_y = gpd.GeoSeries(data_shapely_max_y)
    start_time = time.time()
    try:
        exec("gpd.GeoSeries.%s(data_x, data_y)" % func_name)
    except AttributeError:
        print("geopandas has no attribute ", func_name)
        pass
    end_time = time.time()
    with open(output_path + "/geopandas/" + data_num_path + "/" + func_name + ".txt", 'a+') as f:
        f.writelines("geopandas %s time is:" % func_name + str(end_time - start_time))
    from pandas import Series
    arctern_data_min_x = Series(df[0])
    arctern_data_min_y = Series(df[1])
    arctern_data_max_x = Series(df[2])
    arctern_data_max_y = Series(df[3])
    start_time = time.time()
    try:
        exec("arctern.GeoSeries.polygon_from_envelope(arctern_data_min_x, arctern_data_min_y,"
             " arctern_data_max_x, arctern_data_max_y).to_wkt()")
    except AttributeError:
        print("arctern has no attribute ", func_name)
        pass
    end_time = time.time()
    with open(output_path + "/arctern/" + data_num_path + "/" + func_name + ".txt", 'a+') as f:
        f.writelines("arctern %s time is:" % func_name + str(end_time - start_time))


def test_transfrom(csv_path, func_name):
    df = pd.read_csv(csv_path, delimiter='|', header=None)
    data_shapely = df[0].apply(shapely.wkt.loads)
    data = gpd.GeoSeries(data_shapely, crs="EPSG:4326")
    start_time = time.time()
    try:
        exec("data.to_crs(\"EPSG:3857\").to_wkt()")
    except AttributeError:
        print("geopandas has no attribute ", func_name)
        pass
    end_time = time.time()
    with open(output_path + "/geopandas/" + data_num_path + "/" + func_name + ".txt", 'a+') as f:
        f.writelines("geopandas %s time is:" % func_name + str(end_time - start_time))
    arctern_data = arctern.GeoSeries(df[0], crs="EPSG:4326")
    start_time = time.time()
    try:
        exec("arctern_data.to_crs(\"EPSG:3857\").to_wkt()")
    except AttributeError:
        print("arctern has no attribute ", func_name)
        pass
    end_time = time.time()
    with open(output_path + "/arctern/" + data_num_path + "/" + func_name + ".txt", 'a+') as f:
        f.writelines("arctern %s time is:" % func_name + str(end_time - start_time))


def test_buffer(csv_path, func_name):
    df = pd.read_csv(csv_path, delimiter='|', header=None)
    data_shapely = df[0].apply(shapely.wkt.loads)
    data = gpd.GeoSeries(data_shapely)
    start_time = time.time()
    try:
        exec("data.buffer(1.2).to_wkt()")
    except AttributeError:
        print("geopandas has no attribute ", func_name)
        pass
    end_time = time.time()
    with open(output_path + "/geopandas/" + data_num_path + "/" + func_name + ".txt", 'a+') as f:
        f.writelines("geopandas %s time is:" % func_name + str(end_time - start_time))
    arctern_data = arctern.GeoSeries(df[0])
    start_time = time.time()
    try:
        exec("arctern_data.buffer(1.2).to_wkt()")
    except AttributeError:
        print("arctern has no attribute ", func_name)
        pass
    end_time = time.time()
    with open(output_path + "/arctern/" + data_num_path + "/" + func_name + ".txt", 'a+') as f:
        f.writelines("arctern %s time is:" % func_name + str(end_time - start_time))


maps = {

    'st_area': (
        'single_polygon.csv',
        'area',
        1
    ),

    'st_astext': (
        'single_polygon.csv',
        'to_wkt()',
        1
    ),

    'st_envelope_aggr': (
        'single_polygon.csv',
        'envelope_aggr',
        1
    ),

    'st_envelope': (
        'single_polygon.csv',
        'envelope',
        1
    ),

    'st_union_aggr': (
        'single_polygon.csv',
        'union_aggr',
        1
    ),

    'st_issimple': (
        'single_polygon.csv',
        'is_simple',
        1
    ),

    'st_transform': (
        'single_point.csv',
        'to_crs',
        5
    ),

    'st_buffer': (
        'single_point.csv',
        'buffer',
        6
    ),

    'st_length': (
        'single_linestring.csv',
        'length',
        1
    ),

    'st_isvalid': (
        'single_col.csv',
        'is_valid',
        1
    ),

    'st_npoints': (
        'single_col.csv',
        'npoints',
        1
    ),

    'st_centroid': (
        'single_col.csv',
        'centroid',
        1
    ),

    'st_convexhull': (
        'single_col.csv',
        'convexhull',
        1
    ),

    'st_geometry_type': (
        'single_col.csv',
        'geometry_type',
        1
    ),

    'st_simplify_preserve_topology': (
        'single_col.csv',
        'simplify_preserve_to_pology',
        1
    ),

    'st_make_valid': (
        'single_col.csv',
        'make_valid',
        1
    ),

    'st_intersection': (
        'double_col.csv',
        'intersection',
        2
    ),

    'st_intersects': (
        'double_col.csv',
        'intersects',
        2
    ),

    'st_overlaps': (
        'double_col.csv',
        'overlaps',
        2
    ),

    'st_contains': (
        'double_col.csv',
        'contains',
        2
    ),

    'st_equals': (
        'double_col.csv',
        'geom_equals',
        2
    ),

    'st_crosses': (
        'double_col.csv',
        'crosses',
        2
    ),

    'st_touches': (
        'double_col.csv',
        'touches',
        2
    ),

    'st_hausdorffdistance': (
        'double_col.csv',
        'hausdorff_distance',
        2
    ),

    'st_distance': (
        'st_distance.csv',
        'distance',
        2
    ),

    'st_within': (
        'st_within.csv',
        'within',
        2
    ),

    'st_curvetoline': (
        'st_curvetoline.csv',
        'curve_to_line',
        1
    ),

    'st_point': (
        'st_point.csv',
        'point',
        3
    ),

    'st_polygon_from_envelope': (
        'st_polygon_from_envelope.csv',
        'polygon_from_envelope',
        4
    ),

    'st_geomfromgeojson': (
        'st_geomfromgeojson.csv',
        'geom_from_geojson',
        1
    ),

}


def exec_fun(test_name):
    file_name, func_name, case_num = maps.get(test_name)
    csv_file = data_path + "/" + file_name
    print(func_name)
    if case_num == 1:
        test_single_col(csv_file, func_name)
    elif case_num == 2:
        test_double_cols(csv_file, func_name)
    elif case_num == 3:
        test_point(csv_file, func_name)
    elif case_num == 4:
        test_polygon_from_envelope(csv_file, file_name)
    elif case_num == 5:
        test_transfrom(csv_file, file_name)
    elif case_num == 6:
        test_buffer(csv_file, file_name)


def parser_args():
    parse = argparse.ArgumentParser()
    parse.add_argument('-f --test_func', dest='test_func', nargs=1)
    parse.add_argument('-n --data_num', dest='data_num', nargs=1)
    args = parse.parse_args()
    return args


if __name__ == "__main__":
    args = parser_args()
    data_num_path = args.data_num[0]
    test_func = args.test_func[0]

    if not os.path.exists(os.path.join(os.path.join(output_path, "geopandas"), data_num_path)):
        os.makedirs(os.path.join(os.path.join(output_path, "geopandas"), data_num_path))
    if not os.path.exists(os.path.join(os.path.join(output_path, "arctern"), data_num_path)):
        os.makedirs(os.path.join(os.path.join(output_path, "arctern"), data_num_path))

    data_path = data_path + "/" + data_num_path
    exec_fun(test_func)
