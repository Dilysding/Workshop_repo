from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import requests


def moving_averaging(x,w):
    n = len(x)
    m = np.zeros(len(x) - w)
    m[0] = sum(x[:w]) / w
    for i in range(1, n - w):
        m[i] = m[i - 1] + (x[i + w] - x[i - 1]) / w
        
    return m

def trend(timeseries):
    trends = []
    nrmses = []
    for y in timeseries.T:
        x = np.arange(y.size) + 1
        mx = np.mean(x)
        my = np.mean(y)
        b = np.cov(y, x, bias=y.mean())[0, 1] / np.var(x)
        a = my - b * mx
        trend = a + b * x
        trends.append(trend)
    
        n = y.size
        mse = np.sum(np.abs(trend - y)) / n
        msemean = np.sum(np.abs(y - my)) / n
        nrmse = np.sqrt(mse / msemean)
        nrmses.append(nrmse)
        
    return trends, nrmses

fig, axes = plt.subplots(nrows=2)
for i, x in enumerate(timeseries.T):
    t = np.arange(x.size)
    axes[i].plot(t, x, linewidth=1)
    axes[i].plot(t[:-w], moving_averaged[i], linewidth=2)
    axes[i].plot(
        t, trends[i], linewidth=2, linestyle=":", label=f"nrmse={nrmses[i]:.3f}"
    )
    axes[i].set_ylabel(f"quantity {i + 1}")
    axes[i].legend()
plt.show()