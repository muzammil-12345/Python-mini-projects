'''
 Day 17: Student Report generator
 Topics Covered:
 1. CSV files
 2. Reading CSV files
 3. Writing to CSV files
 4. Using the CSV module
 5. Mini-proect: Student report generator
'''
# What is CSV file?
''' CSV (Comma seperated values) are plan text files
that stores tabular data, Each line represents a row 
and each value is seperated by comma. Commonly used
in spreadsheets, databases and data analysis.
'''

import csv
# Reading csv files

with open('Students.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Writing to CSV files
with open('marks.csv','w') as file:
    writer = csv.writer(file)
    writer.writerow(['Name','English','Math','Urdu'])
    writer.writerow(['Alice',45,50,34])
    writer.writerow(['John',34,31,56])

# Writing into a dictionary

with open('new_studs','w') as file:
    writer = csv.DictWriter(file, fieldnames=['Name','English','Math','Urdu'])
    writer.writeheader()
    writer.writerow({'Name':'Eve', 'English':57,'Math':55,'Urdu':31})

# --- Mini-project: Students report Generator ---

# Step 1: Read student data and calculate averages
def process_student_data(input_file, output_file):
    try:
        with open(input_file, 'r', newline='') as inflie:
            reader = csv.DictReader(inflie)
            student_reports = []

            for row in reader:
                name = row['Name']
                Math = int(row['Math'])
                English = int(row['English'])
                Science = int(row['Science'])
                average = round((Math + English + Science) / 3, 2)
                Status = 'Pass' if average >= 60 else 'Fail'

                student_reports.append({
                    'Name': name,
                    'English': English,
                    'Math': Math,
                    'Science': Science,
                    'Average': average,
                    'Status': Status
                })

        # Step 2: Process the data to a new csv file
        with open(output_file, 'w', newline='') as outfile:
            fieldnames = ['Name', 'English', 'Math', 'Science', 'Average', 'Status']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(student_reports)

        print(f'Students report generated in {output_file} successfully.')
    except FileNotFoundError:
        print(f"Error: File {input_file} not found.")
    except KeyError:
        print("Error: Invalid column names in the input")
    except Exception as e:
        print(f'An error occured {e}')

# Step 3: Main program
input_file = 'students.csv'
output_file = 'student_report.csv'
process_student_data(input_file, output_file)        