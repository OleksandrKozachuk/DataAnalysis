import pandas as pd


class DataFrame:
    __data = None

    def __init__(self):
        pass

    def getDataFrame(self):
        return self.__data

    def getFieldNames(self):
        return self.__data.columns

    def getContent(self, path: str):
        """
        Gets content from reading file as pandas data frame.
        :param path: file path
        """
        try:
            self.__data = pd.read_csv(path, sep=' ', delimiter='\t')
        except IOError:
            raise Exception("An IOError has occurred!")

    def saveContent(self, fileName: str):
        """
        Save content as csv file
        :param fileName: name saved file
        :return: None
        """
        self.__data.to_csv(fileName, encoding='utf-8', index=False)

    def updateData(self):
        pass

    def removeData(self):
        pass

    def setDefaultColumnsName(self):
        pass
