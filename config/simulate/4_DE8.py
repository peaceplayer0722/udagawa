import numpy as np

config = {
    "eta": 1,  # 結合損
    "alpha": 52.96,  # 伝搬損失係数
    "K": np.array(
        [0.2634849707269228, 0.03753154680933346, 0.08686946565370768, 0.11478823521455123, 0.23979193361806478]
    ),  # 結合率
    "L": np.array([5.66326831e-05, 5.66326831e-05, 1.69898049e-04, 5.66326831e-05]),  # リング周長
    "n_eff": 3.3938,  # 実行屈折率
    "n_g": 4.2,  # 群屈折率
    "center_wavelength": 1550e-9,
    # 'lambda_limit': np.arange(1535e-9, 1565e-9, 1e-12)
}
