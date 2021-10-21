import numpy as np

# (6.323746691398936, [0.13129521534584263, 0.03140404790304265, 0.03714736397846521, 0.02247427292639586, 0.46619736750352564], [2.748169016920735e-05, 0.00010992725641177333, 2.748539337057154e-05, 2.7477992937474902e-05])

config = {
    "eta": 0.996,
    "alpha": 52.96,
    "K": [0.12395188629725941, 0.030807624452130217, 0.03493053701137464, 0.02301971078881386, 0.44123167392946],
    "L": [2.7477272727272726e-05, 0.0001099090909090909, 2.7477272727272726e-05, 2.7477272727272726e-05],
    "n_eff": 2.2,
    "n_g": 4.4,
    "center_wavelength": 1.55e-06,
    "lambda_limit": np.arange(1520e-9, 1560e-9, 1e-12),
    "label": "{}{\\(4^\\textrm{th}(E=5.6)\\)}",
}
