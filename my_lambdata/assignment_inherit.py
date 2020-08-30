# imports
from pandas import DataFrame

class CustomFrame(DataFrame):
    pass
    ## we may not need to do this since we are inheriting attr from parent (DataFrame)
    # def __init__(self, data, additional_attributes):
    #     super().__init__(data)
    #     self.additional_attributes = additional_attributes
        
    def add_state_names_column(self):

        names_map ={'CA':'Cali','CO':'Colo','CT':'Conn'}
        
        self['name'] = self['abbrev'].map(names_map)

if __name__ == "__main__":
    customframe = CustomFrame({'abbrev':['CA','CO','CT','DC','TX']})
    print(customframe.head())
    
    customframe.add_state_names_column()
    print(customframe.head())
