import pandas as pd


class TextData:
    def __init__(self, data):
        self.data = data

    def read_csv(self, file_path):
        self.data = pd.read_csv(file_path, delimiter=';')
        return self

    def output_csv(self, file_path):
        if self.data is not None:
            # index=False prevents pandas to write row index
            self.data.to_csv(file_path, sep=";", index=False)
            print("CSV file written to " + file_path)
        return self

    def drop_attributes(self, attributes):
        # axis=1 drops columns, axis=0 drops rows
        self.data = self.data.drop(attributes, axis=1)
        return self

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
