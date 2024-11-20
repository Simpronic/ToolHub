import pandas as pd
import configparser as cp

class Retriver:

    def __checkCSVCompatibility(self,Colums):
       field_value = self.config.get('CSVCONFIG', 'colums').split(',')
       if not set(Colums).issubset(set(field_value)):
          raise Exception("Not compatible Fields") 

    def __init__(self,csv_path):
        self.csv_df = None
        self.config = cp.ConfigParser()
        self.config.read('configs/config.cfg')
        try:
         self.csv_df = pd.read_csv(csv_path)
         self.__checkCSVCompatibility( self.csv_df.columns)
        except Exception as e:
            print(str(e))
            exit()

    def getCsvData(self):
       self.csv_df['Id'] = range(1, len(self.csv_df) + 1)
       return self.csv_df
    