import pandas as pd
import numpy as np

new_dataframe = pd.DataFrame()

numbers_of_columns = int(input("How many columns you'll be using? "))

columns_names = []

for i in range(numbers_of_columns):

    column_name = input(f"What's the name for column {i+1}: ")
    columns_names.append(column_name)

    #Asking for start and end numbers, that will define the range
    start_range, end_range = map(int, input(f"Enter the range of data for {column_name}(Example: '1 10' for values between 1 and 5): ").split())

    new_dataframe[column_name] = np.random.randint(start_range, end_range + 1, size=10)


new_dataframe.columns = columns_names

print(new_dataframe)

new_dataframe.to_csv('new_df.csv', index=False)
