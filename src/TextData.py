import pandas as pd


class TextData:
    def __init__(self, file_path):
        self.data = None
        self.file_path = file_path

    def read_csv(self):
        self.data = pd.read_csv(self.file_path, delimiter=';')
        return self

    def output_csv(self, output_path):
        if self.data is not None:
            # index=False prevents pandas to write row index
            self.data.to_csv(output_path, sep=";", index=False)
            print("CSV file written to " + output_path)
        return self

    def drop_attributes(self, attributes):
        # axis=1 drops columns, axis=0 drops rows
        self.data = self.data.drop(attributes, axis=1)
        return self

    # Replace values of a column by a new value
    def replace_column_values(self, column_name, old_values, new_value):
        self.data[column_name] = self.data[column_name].replace(old_values, new_value)
        return self

    def convert_columns_to_string(self, columns):
        for column in columns:
            self.data[column] = self.data[column].astype(str).str.strip()
        return self

    def convert_columns_to_int(self, columns):
        for column in columns:
            self.data[column] = self.data[column].astype(int)
        return self
