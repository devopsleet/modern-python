import pandas as pd

# Read the CSV file
df = pd.read_csv('C:/Users/gasin/OneDrive/Documents/Emails.csv')

# Extract the unique emails
unique_emails = df['Email'].drop_duplicates()

# Save the unique emails to a new CSV file
unique_emails.to_csv('unique_emails.csv', index=False)

print("Unique emails have been saved to 'unique_emails.csv'.")
