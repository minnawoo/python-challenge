import unicodecsv
from datetime import datetime as dt
from operator import itemgetter

with open('budget_data.csv', 'rb') as f:
	reader = unicodecsv.DictReader(f)
	budget_data = list(reader)

# Add sortable date column
for row in budget_data:
    date =  row['Date']
    new_date = dt.strptime(date, '%b-%Y').strftime('%Y/%m')
    row['Sortable_date'] = new_date

# Sort by Sortable_date key
sorted_budget_data = sorted(budget_data, key=itemgetter('Sortable_date')) 

# Print to terminal
print("Financial Analysis")
print("----------------------------")

# Find and print the total number of months included in the dataset
prev_date = ""
num_months = 0
for row in sorted_budget_data:
    date = row['Date']
    if date != prev_date:
        num_months += 1
print(f"Total Months: {num_months}")

# Find and total total net amount of "Profit/Losses" over the entire period
sum = 0
for row in budget_data:
    sum += int(row['Profit/Losses'])
print(f"Total: ${sum}")

# Calculate and print the average change in "Profit/Losses" between months
# over the entire period
sum_changes = 0
previous_value = int(budget_data[0]['Profit/Losses'])
for row in budget_data:
    row['Change'] = int(row['Profit/Losses']) - previous_value
    sum_changes += row['Change']
    previous_value = int(row['Profit/Losses'])
avg_change = sum_changes/(len(budget_data) -1)
print("Average  Change: ${:.2f}".format(avg_change))

# Find and print the greatest increase in profits (date and amount) over the entire period
max_incr_value = 0
max_incr_date = ""
for row in budget_data:
    if int(row['Change']) > max_incr_value:
        max_incr_value = int(row['Change'])
        max_incr_date = row['Date']

print(f"Greatest Increase in Profits: {max_incr_date} (${max_incr_value})")

# Find and print the greatest decrease in losses (date and amount) over the entire period
max_decr_value = 0
max_decr_date = ""
for row in budget_data:
    if int(row['Change']) < max_decr_value:
        max_decr_value = int(row['Change'])
        max_decr_date = row['Date']

print(f"Greatest Decrease in Profits: {max_decr_date} (${max_decr_value})")

with open("Output.txt", "w") as text_file:
    text_file.write("Financial Analysis\n")
    text_file.write("----------------------------\n")
    text_file.write(f"Total Months: {num_months}\n")
    text_file.write(f"Total: ${sum}\n")
    text_file.write("Average  Change: ${:.2f}\n".format(avg_change))
    text_file.write(f"Greatest Increase in Profits: {max_incr_date} (${max_incr_value})\n")
    text_file.write(f"Greatest Decrease in Profits: {max_decr_date} (${max_decr_value})\n")