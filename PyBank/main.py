# OPEN CSV FOR READING
# Import the OS module
import os

# Import module for reading CSV file
import csv

# Connect path to CSV file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Read using CSV moduile to count number of months
with open(csvpath) as csvfile:

    # Specify delimiter and variable
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # Read each row of data after the header to calculate total months (source: https://www.adamsmith.haus/python/answers/how-to-count-the-number-of-lines-in-a-csv-file-in-python)
    total_months = 0
    sum = 0
    for row in csvreader:
        total_months += 1

# Calculate total (source: https://stackoverflow.com/questions/65151369/summing-a-column-in-a-csv-file-using-python)
total = 0
with open(csvpath) as csvfile:

    # Specify delimiter and variable
    data = csv.reader(csvfile)
    for row in data:
        if not str(row[1]).startswith('P'):
            total = total + int(row[1])

# Calculate average of Profit/Loss column
average = 0
average = average + total / total_months

# Format average to 2 decimal places (source: https://pythonguides.com/python-print-2-decimal-places/)
format_average = "{:.2f}".format(average)

# Calculate maximum and minimum changes in profits (source: https://stackoverflow.com/questions/70628607/how-to-find-the-date-of-min-and-max-outdoor-temp-and-output-the-min-and-max-to-a)
with open(csvpath) as csvfile:

    # Specify delimiter and variable
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # Read the first data row
    row = next(csvreader)

    # Initialize data
    mindate = maxdate = row[0]
    file_min = int(row[1])
    file_max = int(row[1])
    
    # Process the remaining rows
    for row in csvreader:
        row_min = int(row[1])
        row_max = int(row[1])
        if row_min < file_min:
            file_min = row_min
            mindate = row[0]
        if row_max > file_max:
            file_max = row_max
            maxdate = row[0]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# RESULTS

# Print spacing line and title
print('      ')
print("Financial Analysis")

# Print dividing line
print("------------------------------------------------------")

# Print analysis
print("Total Months: " + str(total_months))

print("Total: " + "$" + str(total))

print("Average Change: " + "$" + str(format_average))

print("Greatest Increase in Profits: " + maxdate + "  ($" + str(file_max) + ")")

print("Greatest Decrease in Profits: " + mindate + "  ($" + str(file_min) + ")")

# Print dividing line
print("------------------------------------------------------")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# EXPORT TO TEXT FILE

# Export a text file with results (source: https://www.pythontutorial.net/python-basics/python-write-text-file/)
lines = ['Financial Analysis', '------------------------------------------------------', 'Total Months: ' + str(total_months), 'Total: ' + '$' + str(total), 'Average Change: ' + '$' + str(format_average), 'Greatest Increase in Profits: ' + maxdate + '  ($' + str(file_max) + ')', 'Greatest Decrease in Profits: ' + mindate + '  ($' + str(file_min) + ')', '------------------------------------------------------']
with open('Analysis/analysis.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')