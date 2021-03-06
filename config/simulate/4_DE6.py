import numpy as np

config = {
    "eta": 1,  # 結合損
    "alpha": 52.96,  # 伝搬損失係数
    "K": np.array(
        [0.03535271159564779, 0.010778618414470975, 0.01237925239335591, 0.01811167951680387, 0.5343396818184193]
    ),  # 結合率
    "L": np.array([0.00011418, 0.0005138, 0.00017127, 0.00034254]),  # リング周長
    "n_eff": 3.3938,  # 実行屈折率
    "n_g": 4.2,  # 群屈折率
    "center_wavelength": 1550e-9,
    # 'lambda_limit': np.arange(1535e-9, 1565e-9, 1e-12)
}
