# import csv

# # Create a list of lists to store the data.
# data = [
#     ["Roll_No", "Name_of_Student", "Telugu", "English", "Maths", "Science", "Social"],
#     [101, "sundeep", 90, 85, 80, 83, 75],
#     [102, "saradhi", 50, 60, 75, 54, 64],
#     [103, "ramesh", 95, 78, 68, 58, 78],
#     [104, "suresh", 55, 87, 68, 64, 59],
#     [105, "sathwik", 88, 84, 98, 73, 81],
#     [106, "abhiram", 73, 84, 91, 88, 84],
#     [107, "srinidhi", 90, 83, 74, 86, 94],
#     [108, "lakshmi", 75, 78, 85, 64, 53],
#     [109, "dinesh", 84, 85, 76, 94, 54],
#     [110, "harish", 83, 98, 81, 63, 79],
#     [111, "murali", 85, 86, 92, 75, 35],
#     [112, "vasu", 50, 54, 64, 87, 45],
#     [113, "kali", 89, 97, 69, 73, 82],
#     [114, "ramu", 25, 45, 60, 35, 48],
#     [115, "krishna", 1, 25, 65, 50, 55],
#     [116, "hari", 78, 89, 95, 67, 58],
#     [117, "pavan", 59, 52, 68, 68, 70],
#     [118, "ashok", 85, 86, 98, 78, 44],
#     [119, "govind", 89, 89, 95, 66, 95],
#     [120, "bhargav", 72, 78, 86, 64, 72],
# ]

# # Open a CSV file for writing.
# with open("data.csv", "w", newline="") as csvfile:

#     # Create a CSV writer object.
#     writer = csv.writer(csvfile)

#     # Write the data to the CSV file.
#     writer.writerows(data)




import csv

# Define the input and output file paths
input_file = "text_data.txt"
output_file = "grades.csv"

# Define the header for the CSV file
header = ["Roll_No", "Name_of_Student", "Telugu", "English", "Maths", "Science", "Social"]

# Read data from the text file and write to CSV
with open(input_file, "r") as file:
    with open(output_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        
        # Write the header to the CSV file
        writer.writerow(header)
        
        # Read each line from the text file, split it by comma, and write to CSV
        for line in file:
            row = line.strip().split(",")
            writer.writerow(row)

print("Conversion completed successfully.")
