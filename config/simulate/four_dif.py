import numpy as np

config = {
    "eta": 1,  # 結合損
    "alpha": 52.96,  # 伝搬損失係数
    "K": np.array(
        [0.16594145503371166, 0.015292083805988496, 0.008001728355588067, 0.010847545869912554, 0.30946179712989863]
    ),  # 結合効率
    "L": np.array([4.56715187e-05, 6.85072780e-05, 2.74029112e-05, 9.13430373e-05]),  # リング周長
    "n_eff": 3.3938,  # 実行屈折率
    "n_g": 4.2,  # 群屈折率
    "center_wavelength": 1550e-9,
    # 'lambda_limit': np.arange(1490e-9, 1560e-9, 1e-12)
}
