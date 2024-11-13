import pandas as pd

df = pd.read_csv("C:/Users/gadzi/OneDrive/Desktop/PowerBI Python Cleaning/data/bestsellers.csv")

df.columns = df.columns.str.strip()


#duplicates = df[df['Name'].duplicated(keep=False)]

#Dropping the duplicated names
df = df.drop_duplicates(subset='Name', keep='first')

#Removing the whitespaces within the Name data
df['Name'] = df['Name'].str.strip()
df['Author'] = df['Author'].str.strip()
df['Genre'] = df['Genre'].str.strip()

#print("Duplicated names:")
#print(duplicates)

#Saving the clean data
cleaned_file_path = "C:/Users/gadzi/OneDrive/Desktop/PowerBI Python Cleaning/data/Clean Bestsellers.csv"
df.to_csv(cleaned_file_path, index= False)

print(df.head())
print(df.info())
print(df.columns)
print(df)