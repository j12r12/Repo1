import pandas as pd

class Read_csv():

    """
    Class to read_csv with ISO-8859-1 encoding, dayfirst=True and parse_dates = True by default.
    """

    """
    You can set an index when creating the class, just add the column name. 
    The form should be as follows: bob = Read_csv(data, index).store().
    .store() just returns the dataframe in the object instance you've created.
    """

    def __init__(self, data, index=None):
        
        self.data = data
        self.index = index
        self.df = pd.read_csv(self.data, encoding="ISO-8859-1",
                              dayfirst=True, parse_dates=True, index_col=self.index)

    def store(self):

        return self.df
