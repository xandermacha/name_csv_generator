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


field_names = ['product_handle','state','rating', 'title', 'author', 'email',
               'location','body', 'imageUrl', 'reply', 'created_at', 'replied_at']
def write_to_newcsv(dict):
   
    with open('new_names.csv', 'a',newline='' ) as f:
        dictwriter_obj = DictWriter(f, fieldnames=field_names)
        dictwriter_obj.writerow(dict)
        f.close()
        

# Paths to your CSV files
first_names_file = 'name_list_60k.csv'
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
        
        name_dict = {"product_handle": 'autoair' ,"state":'published',"rating": rating, "title": '', "author": full_name, "email": '', 
                     "location": '', "body": ' ', "imageUrl": '', "reply": '', "created_at": '', "replied_at": '' }
        name_list.append(name_dict)
    else:
        return None  # All first names have been used

# Initialize a list to keep track of the selected names
index = [0]

# Example of how to generate the list of dictionaries
for _ in range(4000):  # Generate more than 26 names
    get_random_name()

# Print the generated list of dictionaries
for name in name_list:
    write_to_newcsv(name)
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
