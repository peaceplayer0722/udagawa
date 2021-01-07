from ..model import Model
import numpy as np

def generate_model(crosstalk, rank):
    m = Model('crosstalk{}'.format(crosstalk))
    d1 = np.arange(-60, 0, 0.5)
    d2 = np.arange(-60, crosstalk, 0.5)
    y = np.hstack((
        np.repeat(-60, (m.FSR - m.length_of_3db_band) / 6 / 1e-12 - d2.size),
        d2,
        np.repeat(crosstalk, (m.FSR - m.length_of_3db_band) / 6 / 1e-12),
        d2[::-1],
        np.repeat(-60, (m.FSR - m.length_of_3db_band) / 6 / 1e-12 - d2.size - d1.size),
        d1,
        np.repeat(0, m.length_of_3db_band / 1e-12),
        d1[::-1],
        np.repeat(-60, (m.FSR - m.length_of_3db_band) / 6 / 1e-12 - d2.size - d1.size),
        d2,
        np.repeat(crosstalk, (m.FSR - m.length_of_3db_band) / 6 / 1e-12),
        d2[::-1],
        np.repeat(-60, (m.FSR - m.length_of_3db_band) / 6 / 1e-12 - d2.size)
    ))
    m.set_y(y)
    m.set_rank(rank)

    return m

data = [
    *[
        generate_model(i, 3)
        for i in range(-5, -30, -1)
    ],
    *[
        generate_model(i, 2)
        for i in range(-30, -40, -1)
    ],
    *[
        generate_model(i, 1)
        for i in range(-40, -60, -1)
    ]
]
