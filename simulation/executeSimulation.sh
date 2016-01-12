# Random Seeds
seeds=('42' '52' '62' '72' '82' '92' '91' '81' '71' '61' '51' '41' '31' '21' '11' '13' '23' '33' '43' '53')

# Replications...
for ((i=0; i < ${#seeds[@]}; i++))
do
	# Executing simulation
	j = $i + 1
	python overheadsimulation.py $((i + 1)) ${seeds[$i]}

	# Geting jobs number executed
	va=$(python _jobsExecutedUtil.py)

	echo 'Jobs number executed: ' $va
	echo
done
