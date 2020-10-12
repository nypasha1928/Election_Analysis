# Add our dependencies.
import csv
import os

# Assign a varaible  to load a file from the path .
file_to_load = os.path.join("C:/Users/Amr/Election_Analysis/Resources/election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("C:/Users/Amr/Election_Analysis/Resources/analysis/election_analysis.txt")

# Open the elections results and read the file .
with open(file_to_load) as election_data:
   
   # To do:  read and analysis the data here.
   file_reader = csv.reader(election_data)
   
   # Read and print the header row.
   headers = next(file_reader)
   print(headers)   
   

   




   