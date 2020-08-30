

import pandas as pd

class DataFrameProcessor():
    def __init__(self, df):
        self.df = df

    def add_state_names_column(self):
        '''
        add a column of state names

        params is df

        return df with state addrrev
        '''
        names_map ={'CA':'Cali','CO':'Colo','CT':'Conn'}
        
        # this will return a copy
        # new_df = self.df.copy()
        # new_df['name'] = new_df['abbrev'].map(names_map)
        # return new_df

        # this will transform/mutate the existing dataframe
        self.df['names'] = self.df['abbrev'].map(names_map)

if __name__ == "__main__":
    df = pd.DataFrame({'abbrev':['CA','CO','CT','DC','TX']})
    
    # old way with out oop
    # mapped_df = add_state_name_column(df)
    # print(mapped_df.head())


    processor = DataFrameProcessor(df=df)
    print(processor.df.head())
    processor.add_state_names_column()
    print(processor.df.head())