# TODO: import enlarge

# from my_mod import enlarge

# another way to import / need init file
from my_lambdata.my_mod import enlarge

from pandas import DataFrame

df = DataFrame({'col_1': [1,2,3,4,5,6,7]})

print(df.head())

print('Hello world!')

print(enlarge(8))