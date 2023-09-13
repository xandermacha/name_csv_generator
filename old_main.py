import csv, random


last_name_initial = open('letters.csv', 'rt')

column_name = 'Author'
with open('new_names.csv', 'w' , newline= '') as f:
    fieldsname = [column_name]
    writer = csv.DictWriter(f, fieldnames=fieldsname)
    writer.writeheader()
    writer.writerow({column_name: 'Mike B.'})

with open('new_names.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row[column_name])
    
    
with open('names.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['Name'])
        
with open('letters.csv', 'r') as letter:
    reader = csv.reader(letter)
    last_inital_pick = random.choice(list(reader))
    print(''.join(last_inital_pick))
    