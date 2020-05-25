for ((data_num = 3; data_num < 7; data_num++))
do
	echo $data_num
	for ((i = 0; i < 5; i++))
	do
		python3 main.py -f st_envelope_aggr -n $data_num
		python3 main.py -f st_union_aggr -n $data_num
		python3 main.py -f st_make_valid -n $data_num
	done
done
