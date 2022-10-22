import os
import time

print("Process Start")

start_time = time.time()

directory = "personal_info"

outfile_name = "merged_ID.txt"

out_file = open(outfile_name,'w')

input_files = os.listdir(directory)

for filename in input_files:
	if ".txt" not in filename:
		continue
	file = open(directory + "/" + filename)
	content = file.read()
	out_file.write(content + "\n\n")
	file.close()


out_file.close()

print("Process Done.")
end_time = time.time()
print("The Job  Took" + str(end_time -start_time) + "seconds.")

