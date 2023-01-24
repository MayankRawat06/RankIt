import pandas as pd
import numpy as np

def topsis(file_name, weights, impacts):
    w = list(int(i) for i in weights.split(','))
    im = list(i for i in impacts.split(','))

    if (len(w) != len(im)):
        raise Exception('Number of elements in Weights and Impacts should be same')
    try:
        data = pd.read_csv(file_name)
    except FileNotFoundError:
        raise Exception('File not Found')
    else:
        df = data.iloc[:, 1:].values
        m = len(data)
        n = len(data.columns) - 1
        if (n < 3):
            raise Exception('Less than 3 Columns')
        rss = []
        for j in range(0, n):
            s = 0
            for i in range(0, m):
                s += np.square(df[i, j])
            rss.append(np.sqrt(s))

        for j in range(0, n):
            df[:, j] /= rss[j]
            df[:, j] *= w[j]
        best = []
        worst = []
        for j in range(0, n):
            if (im[j] == '+'):
                best.append(max(df[:, j]))
                worst.append(min(df[:, j]))
            elif (im[j] == '-'):
                best.append(min(df[:, j]))
                worst.append(max(df[:, j]))
            else:
                raise Exception('Signs in Impact can be either + or - only')

        ebest = []
        eworst = []
        for i in range(0, m):
            ssdb = 0
            ssdw = 0
            for j in range(0, n):
                ssdb += np.square(df[i, j] - best[j])
                ssdw += np.square(df[i, j] - worst[j])
            rssdb = np.sqrt(ssdb)
            rssdw = np.sqrt(ssdw)
            ebest.append(rssdb)
            eworst.append(rssdw)

        p = []

        for i in range(0, m):
            measure = eworst[i] / (eworst[i] + ebest[i])
            p.append(measure * 100)

        data['Topsis Score'] = p
        data['Rank'] = data['Topsis Score'].rank(ascending=False)

        return data