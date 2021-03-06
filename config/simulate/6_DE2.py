import numpy as np

config = {
    "eta": 0.996,  # 結合損
    "alpha": 52.96,  # 伝搬損失係数
    "K": np.array([0.54662281, 0.10321745, 0.08215906, 0.07981861, 0.08597901, 0.04467645, 0.24152085]),  # 結合率
    "L": np.array(
        [8.35788791e-05, 8.35788791e-05, 5.57192528e-05, 8.35788791e-05, 5.57192528e-05, 5.57192528e-05]
    ),  # リング周長
    "n_eff": 3.3938,  # 実行屈折率
    "n_g": 4.2,  # 群屈折率
    "center_wavelength": 1550e-9,
    "lambda_limit": np.arange(1525e-9, 1555e-9, 1e-12),
}
