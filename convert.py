import sys
import math

io_offset = 0
for line in open(sys.argv[1]) :
	if line[0] == "#" : continue

	row = line.split()

	try:
		time = int(row[0])
		cpu = int(float(row[1]))
		memory = int(float(row[2]))
		io = int(float(row[3]) - io_offset)
	except (ValueError, OverflowError):
		continue

	print "%d %d %d %d"%(time, cpu, memory, io)

	io_offset = float(row[3]);