import numpy as np

config = {
    "eta": 0.996,  # 結合損
    "alpha": 52.96,  # 伝搬損失係数
    "K": [
        0.9179087073095766,
        0.12475889347533353,
        0.0346215198212933,
        0.03481103072235542,
        0.028058021900943586,
        0.046810222091903886,
        0.050549801648881565,
        0.14964098196838277,
        0.6702657783292142,
    ],  # 結合率
    "L": [
        5.495454545454545e-05,
        5.495454545454545e-05,
        5.495454545454545e-05,
        5.495454545454545e-05,
        7.327272727272726e-05,
        7.327272727272726e-05,
        7.327272727272726e-05,
        7.327272727272726e-05,
    ],  # リング周長
    "n_eff": 2.2,  # 実行屈折率
    "n_g": 4.4,  # 群屈折率
    "center_wavelength": 1550e-9,
    "lambda_limit": np.arange(1510e-9, 1560e-9, 1e-12),
    "label": r"8th, E=13.99",
}