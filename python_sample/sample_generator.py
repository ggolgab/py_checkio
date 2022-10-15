import time
import random
import os 


print("Process Start.")

start_time = time.time()

NUM_SAMPLES = 1000

alphabet_samples = "abcdefghizklmmnopqrstuvwxyz1234567890"

def random_string(length):
	result = ""
	for i in range(length):
		result += random.choice(alphabet_samples)
		return result

first_name_samples = "김이박최정강조윤장임"
middle_name_samples = "김이박최정강조윤장임"
last_name_samples = "김이박최정강조윤장임"

	

def random_name():
	result = ""
	result += random.choice(first_name_samples)
	result += random.choice(middle_name_samples)
	result += random.choice(last_name_samples)
	return result

os.mkdir("personal_info")

	
for i in range(NUM_SAMPLES):
	name = random_name()

	filename = "personal_info/"  + str(i) + "_" + name + ".txt"

	outfile =open(filename, "w")
	outfile.write("name : " + name + "\n")
	outfile.write("age : " + str(time.time())[-2:] + "\n")
	outfile.close()

print("Process Done.")

end_time = time.time()
print("the Job Took " + str(end_time - start_time) + " secotns.")

