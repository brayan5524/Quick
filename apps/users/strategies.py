import pandas as pd
from abc import ABC, abstractmethod

class FileStrategy(ABC):
    @abstractmethod
    def process(self, file_path):
        pass

class CSVStrategy(FileStrategy):
    def process(self, file_path):
        return pd.read_csv(file_path, delimiter=';').to_dict(orient='records')

class ExcelStrategy(FileStrategy):
    def process(self, file_path):
        return pd.read_excel(file_path).to_dict(orient='records')