import pandas as pd


class DataFrame:
    __Data = None

    @property
    def frame(self):
        return self.__Data

    @frame.setter
    def frame(self, data: pd.DataFrame):
        if isinstance(self.__Data, pd.DataFrame):
            self.__Data.append(item for item in data)
        else:
            self.__Data = data

    def getFieldNames(self):
        return self.__Data.columns.values

    def getPandasDFInfo(self):
        return self.__Data.info()

    def removeColumn(self, index: int):
        pass

    def setDefaultColumnsName(self):
        pass

    @staticmethod
    def saveContent(data: pd.DataFrame, fileName: str):
        data.to_csv(fileName, encoding='utf-8', index=False)

    @staticmethod
    def getContentFromFile(path: str):
        try:
            df = pd.read_csv(path)
        except IOError:
            raise Exception("An IOError has occurred!")
        return df
