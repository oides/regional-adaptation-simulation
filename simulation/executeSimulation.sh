# Random Seeds
seeds=('42' '52' '62' '72' '82' '92' '91' '81' '71' '61') # '51' '41' '31' '21' '11' '13' '23' '33' '43' '53' '63' '73' '83' '93' '94' '84' '74' '64' '54' '44' '34' '24' '14' '15' '25' '35' '45' '55' '65' '75' '85' '95' '96' '86' '76' '66' '56' '46' '36' '26')

###################################
# Replications without control...
###################################
outputR=''
for ((i=0; i < ${#seeds[@]}; i++))
do
	# Executing simulation
	python overheadsimulation.py $((i + 1)) ${seeds[$i]} disable

	# Geting jobs number executed
	va=$(python _jobsExecutedUtil.py)

	outputR=$outputR' '$va

	echo 'Jobs number executed: ' $va
	echo
done

# Generate output file
rm -rf ../analysisR/reports/outputControlOff.csv
echo $outputR >> ../analysisR/reports/outputControlOff.csv

###################################
# Replications with control...
###################################
outputR=''
for ((i=0; i < ${#seeds[@]}; i++))
do
	# Executing simulation
	python overheadsimulation.py $((i + 1)) ${seeds[$i]} enable

	# Geting jobs number executed
	va=$(python _jobsExecutedUtil.py)

	outputR=$outputR' '$va

	echo 'Jobs number executed: ' $va
	echo
done

# Generate output file
rm -rf ../analysisR/reports/outputControlOn.csv
echo $outputR >> ../analysisR/reports/outputControlOn.csv
