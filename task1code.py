import pandas as pd

file_path=r"C:\Users\mehal\Downloads\netflix_titles.csv.zip"
df=pd.read_csv(file_path)

print(df.isnull().sum())
df=df.dropna()


# 2. Remove duplicate rows
df = df.drop_duplicates()


# 6. Check and fix data types
df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')  # Convert to numeric

# 5. Rename column headers
df.columns = df.columns.str.lower().str.replace(' ', '_')

#Standardize country names
df['country'] = df['country'].str.title().str.strip()

#Save cleaned dataset
df.to_csv("cleaned_data.csv", index=False)
