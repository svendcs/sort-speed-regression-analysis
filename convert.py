import sys
import math

io_offset = 0
for line in open(sys.argv[1]) :
	if line[0] == "#" : continue

	row = line.split()

	try:
		time = int(row[0]) / 1000 # seconds
		cpu = int(float(row[1])) # (cpu time / real time) / %
		memory = int(float(row[2]) / 1024 / 1024) # MiB

		time_difference = float(row[0]) - last_time # milliseconds
		io_difference = float(row[3]) - last_io # bytes

		io = int(io_difference / time_difference / 1000) # MiB/s

		print "%d %d %d %d"%(time, cpu, memory, io)
	except (ValueError, OverflowError, NameError):
		pass

	last_io = float(row[3]);
	last_time = float(row[0]);