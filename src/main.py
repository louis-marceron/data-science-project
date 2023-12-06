# with automatically closes the file once the block ends
from src.TextData import TextData

data = TextData('../data/2022/usagers-2022.csv')

data.read_csv('../data/2022/usagers-2022.csv')\
    .drop_attributes(['Num_Acc'])\
    .output_csv('./mydata')
