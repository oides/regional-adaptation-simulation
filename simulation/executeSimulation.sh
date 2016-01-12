# Replications...
for i in {1..20}
do
	# Executing simulation
	python overheadsimulation.py $i

	# Geting jobs number executed
	va=$(python _jobsExecutedUtil.py)

	echo 'Jobs number executed: ' $va
done
