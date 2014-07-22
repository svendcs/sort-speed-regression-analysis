import sys
import re

initialization_phase = 0
run_files = 0
first_phase = 0
second_phase = 0
third_phase = 0

for i in range(1, len(sys.argv)) :
	f = open(sys.argv[i]) # open for reading

	# Report file line
	contents = f.readline()

	# Data size line
	m = re.search('\d+MiB', f.readline())
	size = m.group(0)

	# Memory size line
	m = re.search('\d+MiB', f.readline())
	memory = m.group(0)

	# Initialization phase line
	m = re.search('\d+', f.readline())
	initialization_phase += int(m.group(0))

	# First phase line
	m = re.search('\d+', f.readline())
	first_phase += int(m.group(0))

	# Run files line
	m = re.search('\d+', f.readline())
	run_files += int(m.group(0))

	# Second phase line
	m = re.search('\d+', f.readline())
	second_phase += int(m.group(0))

	# Third phase line
	m = re.search('\d+', f.readline())
	third_phase += int(m.group(0))

print "Data: %s"%(size)
print "Memory: %s"%(memory)

total = initialization_phase + first_phase + second_phase + third_phase
count = len(sys.argv) - 1
print "Initialization phase average: %s"%(initialization_phase/count)
print "First phase average: %s"%(first_phase/count)
print "Second phase average: %s"%(second_phase/count)
print "Third phase average: %s"%(third_phase/count)
print "Total phase average: %s"%(total/count)
print "# run files average: %s"%(run_files/count)
