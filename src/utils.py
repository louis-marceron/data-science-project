import os.path

import pandas as pd

import pandas as pd


def validate_csv(input_path, delimiter=';'):
    try:
        # Try to read the CSV file
        df = pd.read_csv(input_path, delimiter=delimiter)

        total_rows = len(df)
        missing_value_rows = []
        inconsistent_column_rows = []

        # Identify rows with missing values
        missing_value_rows = df[df.isnull().any(axis=1)].index.tolist()
        missing_values_count = len(missing_value_rows)

        # Check for inconsistent column count
        with open(input_path, 'r') as file:
            header_cols = len(file.readline().split(delimiter))
            for line_number, line in enumerate(file, start=2):  # Start from 2 to account for the header
                if len(line.split(delimiter)) != header_cols:
                    inconsistent_column_rows.append(line_number)

        inconsistent_rows_count = len(inconsistent_column_rows)

        # Calculate percentages
        missing_values_percentage = (missing_values_count / total_rows) * 100
        inconsistent_rows_percentage = (inconsistent_rows_count / total_rows) * 100

        # Print results
        if missing_values_count > 0:
            print(
                f"Warning: {missing_values_count} rows ({missing_values_percentage:.2f}%) have missing values.")

        if inconsistent_rows_count > 0:
            print(
                f"Warning: {inconsistent_rows_count} rows ({inconsistent_rows_percentage:.2f}%) have an inconsistent number of columns.")

        if missing_values_count == 0 and inconsistent_rows_count == 0:
            print(os.path.basename(input_path) + " is a valid CSV.")
    except Exception as e:
        print(f"Error: Invalid CSV file. {e}")
