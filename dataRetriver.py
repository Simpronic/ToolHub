import pandas as pd
import configparser as cp
import sys
import os
class Retriver:

    def __getCFGPath(self):
        if(getattr(sys,'frozen',False)):
            return os.path.join(sys._MEIPASS,'configs','config.cfg')
        else:
            return os.path.join(os.path.dirname(__file__),"configs","config.cfg")

    def __getCSVPath(self):
        if(getattr(sys,'frozen',False)):
            return os.path.join(sys._MEIPASS,'configs','tools.csv')
        else:
            return os.path.join(os.path.dirname(__file__),"configs","tools.csv")

    def __checkCSVCompatibility(self,Colums):
       field_value = self.config.get('CSVCONFIG', 'colums').split(',')
       if not set(Colums).issubset(set(field_value)):
          raise Exception("Not compatible Fields") 

    def __init__(self,csv_path):
        self.csv_df = None
        self.config = cp.ConfigParser()
        self.config.read(self.__getCFGPath())
        try:
         self.csv_df = pd.read_csv(self.__getCSVPath())
         self.__checkCSVCompatibility( self.csv_df.columns)
        except Exception as e:
            print(str(e))
            exit()

    def getCsvData(self):
       self.csv_df['Id'] = range(1, len(self.csv_df) + 1)
       return self.csv_df
    