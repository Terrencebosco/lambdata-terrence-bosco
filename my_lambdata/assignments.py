import pandas as pd


def add_abbrev_stat_column(my_df):
    '''
    add a column of state names

    params is df

    return df with state addrrev
    '''
    
    
    new_df = my_df.copy()

    names_map ={'CA':'Cali','CO':'Colo','CT':'Conn'}
    
    new_df['name'] = new_df['abbrev'].map(names_map)
    
    return new_df



if __name__ == "__main__":
    df = pd.DataFrame({'abbrev':['CA','CO','CT','DC','TX']})
    print(df.head())

    mapped_df = add_abbrev_stat_column(df)
    print(mapped_df.head())

    df2 = pd.DataFrame({'Other_col':[1,2,2]})
    df2.head()

    breakpoint()