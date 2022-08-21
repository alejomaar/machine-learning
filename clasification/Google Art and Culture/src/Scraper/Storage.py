import pandas as pd

class Storage:
    """Store, read and export data in webscraping process
    """    
    
    def __init__(self):
        self.storage = []
            
    def add(self, url:str="NULL",data:str="NULL",category:str="NULL"):
        """Add new register into storage

        Parameters
        ----------
        url : str
            Url of de image picture
        data : str
            Data related of a picture
        category : str
            color category     
        """
        register = {
            'url': str(url),
            'data': str(data),
            'category': str(category)
        }
        self.storage.append(register)
    
    def get_data(self):
        return self.storage
    
    def export(self,name):
        """Name of export file 
        
        NOTE: The filename should be extension .csv

        Parameters
        ----------
        name : str
            name of export file    
        """
        df = pd.DataFrame(self.storage)
        df.to_csv(name, index = False)