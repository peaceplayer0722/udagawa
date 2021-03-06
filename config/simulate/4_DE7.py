import numpy as np

config = {
    "eta": 1,  # 結合損
    "alpha": 52.96,  # 伝搬損失係数
    "K": np.array(
        [0.348495030023752, 0.037089970898961655, 0.08906855569917516, 0.11595775554845839, 0.2088887545036368]
    ),  # 結合率
    "L": np.array([5.66326831e-05, 5.66326831e-05, 1.69898049e-04, 5.66326831e-05]),  # リング周長
    "n_eff": 3.3938,  # 実行屈折率
    "n_g": 4.2,  # 群屈折率
    "center_wavelength": 1550e-9,
    "lambda_limit": np.arange(1547e-9, 1553e-9, 1e-12),
}
