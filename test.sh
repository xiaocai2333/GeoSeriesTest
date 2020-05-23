rm -rf output/arctern/*
rm -rf output/geopandas/*
for ((data_num = 3; data_num < 9; data_num++))
do
	echo $data_num
	for ((i = 0; i < 5; i++))
	do
		python3 main.py -f st_area -n $data_num
		python3 main.py -f st_astext -n $data_num
		python3 main.py -f st_envelope_aggr -n $data_num
		python3 main.py -f st_envelope -n $data_num
		python3 main.py -f st_union_aggr -n $data_num
		python3 main.py -f st_issimple -n $data_num
		python3 main.py -f st_transform -n $data_num
		python3 main.py -f st_buffer -n $data_num
		python3 main.py -f st_length -n $data_num
		python3 main.py -f st_isvalid -n $data_num
		python3 main.py -f st_npoints -n $data_num
		python3 main.py -f st_centroid -n $data_num
		python3 main.py -f st_convexhull -n $data_num
		python3 main.py -f st_geometry_type -n $data_num
		python3 main.py -f st_simplify_preserve_topology -n $data_num
		python3 main.py -f st_make_valid -n $data_num
		python3 main.py -f st_intersection -n $data_num
		python3 main.py -f st_intersects -n $data_num
		python3 main.py -f st_overlaps -n $data_num
		python3 main.py -f st_contains -n $data_num
		python3 main.py -f st_equals -n $data_num
		python3 main.py -f st_crosses -n $data_num
		python3 main.py -f st_touches -n $data_num
		python3 main.py -f st_hausdorffdistance -n $data_num
		python3 main.py -f st_distance -n $data_num
		python3 main.py -f st_within -n $data_num
		python3 main.py -f st_curvetoline -n $data_num
		python3 main.py -f st_point -n $data_num
		python3 main.py -f st_polygon_from_envelope -n $data_num
		python3 main.py -f st_geomfromgeojson -n $data_num
	done
done
