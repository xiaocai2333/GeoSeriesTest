for ((data_num = 3; data_num < 7; data_num++))
do
	echo $data_num
	for ((i = 0; i < 5; i++))
	do
		python3 main.py -f st_buffer -n $data_num
	done
done
