import csv
import os

#search the image


# Define the path to your CSV file and image directory
csv_file_path = r'C:\Users\gasin\test.csv'
images_directory1 = r'C:\Users\gasin\Test'
images_directory2 = r'C:\Users\gasin\MarchPLAT'

# Read the CSV file
with open(csv_file_path, mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row if there is one

    for row in reader:
        if len(row) < 2:
            print(f"Skipping row {row} due to insufficient columns")
            continue

        column1 = row[0].strip()
        column2 = row[1].strip()

        # Search for images with column2 value

        for filename in os.listdir(images_directory1):
            if column1 in filename:
                old_file_path = os.path.join(images_directory1, filename)
                new_file_name = filename.replace(column1 + '.', column2 + '_')
                new_file_path = os.path.join(images_directory2, new_file_name)

                # Rename the file
                os.rename(old_file_path, new_file_path)
                print(f"Renamed {filename} to {new_file_name}")

print("Renaming process completed.")
