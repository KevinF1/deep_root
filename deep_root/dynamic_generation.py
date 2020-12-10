import numpy as np


def create_noised_deterministic_trend(noise_lvl, start, trend=1, size=100, delta=1):
    max_step = size * delta
    x = np.arange(0, max_step, delta)
    y_trend = trend * x + start
    y_noise = np.random.normal(scale=noise_lvl, size=size)
    y_noise[0] = 0
    y = y_trend + y_noise
    return y


def create_noised_stochastic_trend(noise_lvl, start=1, size=100):
    y_noise = np.random.normal(scale=noise_lvl, size=size)
    y = np.zeros((size,))
    y[0] = start
    for i in np.arange(1, size, 1):
        y[i] = y[i-1] + y_noise[i]
    return y
