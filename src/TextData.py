import pandas as pd


class TextData:
    def __init__(self, file_path):
        self.data = None
        self.file_path = file_path
        self.output_separator = ","

    def read_csv(self):
        self.data = pd.read_csv(self.file_path, delimiter=';')
        return self

    def output_csv(self, output_path, separator=";"):
        if self.data is not None:
            # index=False prevents pandas to write row index
            self.data.to_csv(output_path, sep=separator, index=False)
            print("CSV file written to " + output_path)
        return self

    def drop_attributes(self, attributes):
        # axis=1 drops columns, axis=0 drops rows
        self.data = self.data.drop(attributes, axis=1)
        return self

    # Replace values of a column by a new value
    def replace_column_values2(self, column_name, old_values, new_value):
        try:
            if column_name not in self.data.columns:
                raise KeyError(f"Column '{column_name}' does not exist in the DataFrame.")
            self.data[column_name] = self.data[column_name].replace(old_values, new_value)
        except Exception as e:
            print(f"Error replacing column values: {e}")
        return self

    def convert_columns_to_string(self, columns):
        for column in columns:
            try:
                if column not in self.data.columns:
                    raise KeyError(f"Column '{column}' does not exist in the DataFrame.")
                self.data[column] = self.data[column].astype(str).str.strip()
            except Exception as e:
                print(f"Error converting column '{column}' to string: {e}")
        return self

    def convert_columns_to_int(self, columns):
        for column in columns:
            try:
                if column not in self.data.columns:
                    raise KeyError(f"Column '{column}' does not exist in the DataFrame.")
                self.data[column] = self.data[column].astype(int)
            except ValueError as e:
                print(f"Error converting column '{column}' to int: {e}")
            except Exception as e:
                print(f"Error: {e}")
        return self

    def rename_columns(self, columns):
        try:
            self.data = self.data.rename(columns=columns)
        except Exception as e:
            print(f"Error renaming columns: {e}")
        return self

    def replace_column_values(self, column_name, replacements):
        try:
            if column_name not in self.data.columns:
                raise KeyError(f"Column '{column_name}' does not exist in the DataFrame.")
            # Loop over the dictionary to replace each old value with the new value
            for old_value, new_value in replacements.items():
                self.data[column_name] = self.data[column_name].replace(old_value, new_value)
        except Exception as e:
            print(f"Error replacing column values: {e}")
        return self
