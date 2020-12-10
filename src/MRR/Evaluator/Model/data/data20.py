from ..model import Model
import numpy as np

data = Model('data20')
insertion_loss = -1
d = np.arange(-60, insertion_loss, 0.5)
y = np.hstack((
    np.repeat(-60, (data.FSR - data.length_of_3db_band) / 2 / 1e-12 - d.size),
    d,
    np.repeat(insertion_loss, data.length_of_3db_band / 1e-12),
    d[::-1],
    np.repeat(-60, (data.FSR - data.length_of_3db_band) / 2 / 1e-12 - d.size)
))
data.set_y(y)
data.set_rank(1)