import pandas as pd


def getContent(path: str):
    """
    Gets content from reading file as pandas data frame.
    :param path: file path
    :return: pandas df
    """
    try:
        df = pd.read_csv(path, sep=' ', delimiter='\t')
        return df
    except IOError:
        print("An IOError has occurred!")
        return None


def saveContent(df: pd.DataFrame, fileName: str):
    """
    Save content from pandas data frame as csv file
    :param df: data frame
    :param fileName: name saved file
    :return: None
    """
    df.to_csv(fileName, encoding='utf-8', index=False)
