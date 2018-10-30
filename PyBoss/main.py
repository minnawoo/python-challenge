import unicodecsv
from datetime import datetime as dt
import us_state_abbrev

# Open csv file and read data into a list of dictionaries
with open('employee_data.csv', 'rb') as f:
    reader = unicodecsv.DictReader(f)
    employee_data = list(reader)

# Reformat employee data    
for row in employee_data:
    
    # Split name to first and last
    first_name, last_name = row['Name'].split(" ")
    
    # Rename 'Name' key to 'First Name' and replace full name with first name
    row['First Name'] = row.pop('Name')
    row['First Name'] = first_name
    
    # Add a 'Last Name' key and assign value
    row['Last Name'] = last_name
    
    # Reformat DOB from YYYY-MM-DD to MM/DD/YYYY
    date =  row['DOB']
    row['DOB'] = dt.strptime(date, '%Y-%m-%d').strftime('%m/%d/%Y')
    
    # Replace first five numbers of SN with asterisks
    old_SN = row['SSN']
    part_one, part_two, part_three = old_SN.split("-") # Split into three parts
    row['SSN'] = "***-**-" + part_three # Replace with ***-**-part_three

    # Reformat state to two-letter abbreviations
    old_state = row['State']
    row['State'] = us_state_abbrev.us_state_abbrev[old_state]

# Write out to a Output.csv file
import csv
with open('Output.csv', 'w') as csvfile:
    #fieldnames = list(employee_data[0].keys())
    fieldnames = ['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State']
    writer = csv.DictWriter(csvfile, fieldnames= fieldnames)
    writer.writeheader()
    writer.writerows(employee_data)