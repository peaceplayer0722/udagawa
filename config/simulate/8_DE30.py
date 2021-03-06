import numpy as np

config = {
    "eta": 0.996,  # 結合損
    "alpha": 52.96,  # 伝搬損失係数
    "K": [
        0.42107999079401515,
        0.07252902882155426,
        0.048274497010866946,
        0.045531924363475584,
        0.05273694120925826,
        0.08358111970012377,
        0.2287384485219306,
        0.1568252299689027,
        0.4417495590584411,
    ],  # 結合率
    "L": [
        5.495454545454545e-05,
        7.327272727272726e-05,
        7.327272727272726e-05,
        7.327272727272726e-05,
        5.495454545454545e-05,
        5.495454545454545e-05,
        5.495454545454545e-05,
        5.495454545454545e-05,
    ],  # リング周長
    "n_eff": 2.2,  # 実行屈折率
    "n_g": 4.4,  # 群屈折率
    "center_wavelength": 1550e-9,
    "lambda_limit": np.arange(1510e-9, 1560e-9, 1e-12),
    "label": r"8th, E=13.99",
}
