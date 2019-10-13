import numpy as np
import pandas as pd


def pairCorrelationCoefficient(x, y, meanX: np.ndarray, meanY: np.ndarray, N: int) -> float:
    return np.mean([(x[i] - meanX) * (y[i] - meanY) for i in range(N)]) \
           / np.sqrt(np.var(x) * np.var(y))


def multiplicationVectorOnMatrix(A, v):
    result = []
    for i in range(len(v)):
        total = 0
        for j in range(len(v)):
            total += A[i][j] * v[j]
        result.append(total)
    return result


def getDispCovarianceMatrix(dataTable):
    countDimensions = len(dataTable)

    matrix = [np.zeros(countDimensions).tolist() for _ in range(countDimensions)]
    for i in range(countDimensions):
        lenColumn = len(dataTable[i])
        disp = dispersion(dataTable[i], lenColumn)

        for j in range(countDimensions):
            if i == j:
                matrix[i][j] = np.round(disp, 4)
            else:
                nextDisp = dispersion(dataTable[j], lenColumn)
                pairCorrelation = pairCorrelationCoefficient(dataTable[i], dataTable[j],
                                                             np.mean(dataTable[i]),
                                                             np.mean(dataTable[j]),
                                                             lenColumn)
                covariation = sqrt(nextDisp) * sqrt(disp) * pairCorrelation
                matrix[i][j] = np.round(covariation, 4)

    return matrix


def centralize(data):
    for i in range(len(data)):
        mean = np.mean(data[i])
        for j in range(len(data[0])):
            data[i][j] -= mean

    return data


def pca(data: pd.DataFrame):
    _, N = np.shape(data)
    centralizedData = centralize(data)
    correlationMatrix = getCorrelationMatrix(centralizedData)
    eigenval, eigenvec = np.linalg.eig(correlationMatrix)

    sigmas = eigenval / N
    indexes = np.where(sigmas >= 1)
    v = -eigenvec

    result = np.dot(v, centralizedData)
    result = np.delete(result, indexes, axis=0)

    return result, v


if __name__ == '__main__':
    x = np.arange(1, 11)
    y = 2 * x + np.random.randn(10) * 2
    X = np.vstack((x, y))

    pca_, v =pca(X)
    print(pca_)
    print(np.shape(pca_))