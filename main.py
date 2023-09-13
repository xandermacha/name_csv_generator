import csv
import random
from csv import DictWriter

# Function to read data from a CSV file and return a list of names
def read_csv(file_path):
    names = []
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:  # Check if the row is not empty
                names.append(row[0])  # Assuming the names are in the first column
    return names


field_names = ['PRODUCT_HANDLE','STATE','RATING', 'TITLE', 'AUTHOR', 'EMAIL',
               'LOCATION','BODY', 'IMGURL', 'REPLY', 'CREATED_AT', 'REPLIED_AT']
def write_to_newcsv(dict):
   
    with open('new_names.csv', 'a',newline='' ) as f:
        dictwriter_obj = DictWriter(f, fieldnames=field_names)
        dictwriter_obj.writerow(dict)
        f.close()
        

# Paths to your CSV files
first_names_file = 'first_names.csv'
last_names_file = 'last_names.csv'

# Read data from the CSV files
first_names = read_csv(first_names_file)
last_names = read_csv(last_names_file)

# Shuffle the last names list to randomize the order
random.shuffle(last_names)
random.shuffle(first_names)

# Initialize a list to keep track of the selected first names

name_list = []

# Function to get a random non-repeating full name and add it to the list as a dictionary
def get_random_name():
    if index[0] < len(first_names):
        first_name = first_names[index[0]]
        index[0] += 1
        last_name = random.choice(last_names)
        full_name = f"{first_name} {last_name}"
        
        # Determine the rating
        rating = 5 if random.random() < 0.75 else 4
        
        name_dict = {"PRODUCT_HANDLE": 'autoair' ,"STATE":'published',"RATING": rating, "TITLE": '', "AUTHOR": full_name, "EMAIL": '', 
                     "LOCATION": '', "BODY": ' ', "IMGURL": '', "REPLY": '', "CREATED_AT": '', "REPLIED_AT": '' }
        name_list.append(name_dict)
    else:
        return None  # All first names have been used

# Initialize a list to keep track of the selected names
index = [0]

# Example of how to generate the list of dictionaries
for _ in range(10):  # Generate more than 26 names
    get_random_name()

# Print the generated list of dictionaries
for name in name_list:
    print(name)
  



















#only generates random names
# selected_first_names = []

# # Function to get a random non-repeating full name
# def get_random_name():
#     if index[0] < len(first_names):
#         first_name = first_names[index[0]]
#         index[0] += 1
#         last_name = random.choice(last_names)
#         return f"{first_name} {last_name}"
#     else:
#         return None  # All first names have been used

# # Initialize a list to keep track of the selected names
# index = [0]

# # Example of how to get random non-repeating full names
# for _ in range(1900):  # Generate more than 26 names
#     random_name = get_random_name()
#     if random_name is not None:
#         write_to_newcsv(random_name)
#         print(random_name)
#     else:
#         print("All first names have been used.")
