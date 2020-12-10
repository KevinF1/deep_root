import numpy as np


def create_noised_deterministic_trend(trend, noise_lvl, size=100, delta=1):
    max_step = size * delta
    x = np.arange(0, max_step, delta)
    y_trend = trend * x
    y_noise = np.random.normal(scale=noise_lvl, size=size)
    y = y_trend + y_noise
    return y
