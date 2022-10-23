import pyexcel.cookbook as pc
import sys
import time

print("Process Start")

start_time = time.time()

input_file = sys.argv[1]
result_file = sys.argv[2]


pc.merge_all_to_a_book([input_file],result_file)

print("Process Done")
end_time = time.time()

print("The Job Took" + str(end_time - start_time) + " seconds.")


