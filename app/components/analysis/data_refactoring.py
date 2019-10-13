import numpy as np
import pandas as pd


def countOptimalBins(N: int):
    if N < 100:
        if N % 2 == 0:
            num_b = np.sqrt(N) - 1
        else:
            num_b = np.sqrt(N)
    else:
        if N % 2 == 0:
            num_b = np.cbrt(N) - 1
        else:
            num_b = np.cbrt(N)

    return int(np.floor(num_b))


def standardize(data: pd.DataFrame):
    names = data.columns.values
    _values = data[names]

    means = _values.mean()
    stds = _values.std()

    for name in names:
        data[name] = (data[name] - means[name]) / stds[name]
    # change columns names
    data.columns = ["standardized_{0}".format(name) for name in data.columns]

    return data


def shift(data: pd.DataFrame):
    names = data.columns.values
    means = data[names].mean()

    for name in names:
        data[name] += means[name]
    # change columns names
    data.columns = ["shifted_{0}".format(name) for name in data.columns]

    return data


def log(data: pd.DataFrame):
    for name in data.columns.values:
        currentData = data[name]

        if np.issubdtype(currentData.dtype, np.floating) and (currentData >= 0).all:
            data[name] = np.log(currentData)

    # change columns names
    data.columns = ["logged_{0}".format(name) for name in data.columns]

    return data


def removeAbnormal(data: pd.DataFrame, alpha: float):
    N, dim = data.shape
    bins = countOptimalBins(N)

    def _getStep(col: np.ndarray):
        return (np.max(col) - np.min(col)) / bins

    def _getDimClassIndexes(rowValue: np.float64, minCol: np.float64, colStep: np.float64):
        return np.trunc((rowValue - minCol) / colStep)

    def _convertNSysToDecimal(observationIndexes: list):
        return int(np.sum(
            np.array(
                [value * np.int(np.power(dim, i)) for i, value in enumerate(reversed(
                    observationIndexes))]
            )
        ))

    def _getObservationIndex(row: list):
        npDf = data.values.reshape(dim, N)
        result = []

        for i, col in enumerate(npDf):
            minCol = np.amin(col)
            stepCol = _getStep(col)

            res = _getDimClassIndexes(row[i], minCol, stepCol)
            result.append(res)

        return _convertNSysToDecimal(result)

    def _buildDistribution():
        cube = {}
        for i, row in enumerate(data.values):
            index = _getObservationIndex(row)
            if index not in cube.keys():
                cube[index] = [0, i]
            cube[index][0] += 1

        return cube

    def _cleanData(cube: dict):
        for key in cube.keys():
            absFreq = cube[key][0]
            relFreq = absFreq / N

            if relFreq < alpha:
                indexRow = cube[key][1]
                data.drop(indexRow, inplace=True)

    nDimCube = _buildDistribution()
    _cleanData(nDimCube)

    # change columns names
    data.columns = ["non_abnormal_{0}".format(name) for name in data.columns]

    return data
