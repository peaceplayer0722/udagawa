import numpy as np

config = {
    "eta": 1,  # 結合損
    "alpha": 52.96,  # 伝搬損失係数
    "K": np.array(
        [0.2566612013110592, 0.03696843505677233, 0.018439736698312725, 0.005935495172525229, 0.15234758115973396]
    ),  # 結合率
    "L": np.array(
        [0.0001950173846425835, 0.0001950173846425835, 0.00011143850551004772, 5.571925275502386e-05]
    ),  # リング周長
    "n_eff": 3.3938,  # 実行屈折率
    "n_g": 4.2,  # 群屈折率
    "center_wavelength": 1550e-9,
    # 'lambda_limit': np.arange(1535e-9, 1565e-9, 1e-12)
}
