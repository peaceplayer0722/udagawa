import numpy as np

config = {
    "eta": 1,  # 結合損
    "alpha": 52.96,  # 伝搬損失係数
    "K": np.array(
        [0.29720933405703137, 0.2876060808496553, 0.5942811661707268, 0.09164118127740645, 0.2987256493494116]
    ),  # 結合率
    "L": np.array([0.00017127, 0.00034254, 0.00011418, 0.00011418]),  # リング周長
    "n_eff": 3.3938,  # 実行屈折率
    "n_g": 4.2,  # 群屈折率
    "center_wavelength": 1550e-9,
    # 'lambda_limit': np.arange(1535e-9, 1565e-9, 1e-12)
}
