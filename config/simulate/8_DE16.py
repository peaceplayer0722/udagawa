import numpy as np

config = {
    "eta": 0.996,  # 結合損
    "alpha": 52.96,  # 伝搬損失係数
    "K": np.array(
        [
            0.20440301042463077,
            0.057034797177335575,
            0.32423368332211555,
            0.31536748721456764,
            0.04813897882916647,
            0.04149786830360708,
            0.21830751070796506,
            0.08468812525694289,
            0.29801533555206344,
        ]
    ),  # 結合率
    "L": np.array(
        [
            2.7477272727272726e-05,
            0.00013738636363636362,
            0.00013738636363636362,
            0.00013738636363636362,
            2.7477272727272726e-05,
            0.00013738636363636362,
            0.00013738636363636362,
            2.7477272727272726e-05,
        ]
    ),  # リング周長
    "n_eff": 2.2,  # 実行屈折率
    "n_g": 4.4,  # 群屈折率
    "center_wavelength": 1550e-9,
    "lambda_limit": np.arange(1520e-9, 1560e-9, 1e-12),
}
