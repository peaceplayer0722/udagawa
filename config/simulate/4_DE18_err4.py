import numpy as np

# (6.323746691398936, [0.13129521534584263, 0.03140404790304265, 0.03714736397846521, 0.02247427292639586, 0.46619736750352564], [2.748169016920735e-05, 0.00010992725641177333, 2.748539337057154e-05, 2.7477992937474902e-05])

config = {
    "eta": 0.996,
    "alpha": 52.96,
    "K": [0.11869986696322209, 0.03185966107086482, 0.03390999170032763, 0.023451899815998205, 0.4137724660750513],
    "L": [2.7636733102582754e-05, 0.00011039479509582315, 2.7436069758000086e-05, 2.7524206405574425e-05],
    "n_eff": 2.2,
    "n_g": 4.4,
    "center_wavelength": 1.55e-06,
    "lambda_limit": np.arange(1520e-9, 1560e-9, 1e-12),
    "label": "{}{\\(4^\\textrm{th}(E=5.6)\\)}",
}