# Import the csv module
import csv
# Import counter module
from collections import counter
# Import datetime module
from datetime import datetime

# Create the file object: csvfile
csvfile = open('crime_sampler.csv', 'r')

# Create an empty list: crime_data
crime_data = []

# Loop over a csv reader on the file object
for row in csv.reader(csvfile):

    # Append the date, type of crime, location description, and arrest
    crime_data.append((row[0], row[2], row[4], row[5]))
    
# Remove the first element from crime_data
crime_data.pop(0)

# Print the first 10 records
print(crime_data[:10])

# Create a Counter Object: crimes_by_month
crimes_by_month = Counter()

# Loop over the crime_data list
for row in crime_data:
    
    # Convert the first element of each item into a Python Datetime Object
    date = datetime.strptime(row[0], '%m/%d/%Y %I:%M:%S %p')
    
    # Increment the counter for the month of the row by one
    crimes_by_month[date.month] += 1
    
# Print the 3 most common months for crime
print(crimes_by_month.most_common(3))
