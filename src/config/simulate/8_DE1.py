import numpy as np

config = {
    "eta": 1,  # 結合損
    "alpha": 52.96,  # 伝搬損失係数
    "K": np.array(
        [
            0.6333908028993347,
            0.219505842742294,
            0.2103524554061157,
            0.1755628894073955,
            0.2517069303591533,
            0.21938976634326562,
            0.2226932630359006,
            0.2565993188688389,
            0.5633955567427729,
        ]
    ),  # 結合率
    "L": np.array([0.0001393, 0.0001393, 0.0001393, 0.0001393, 0.00011144, 0.00011144, 0.0001393, 0.0001393]),  # リング周長
    "n_eff": 3.3938,  # 実行屈折率
    "n_g": 4.2,  # 群屈折率
    "center_wavelength": 1550e-9,
    # 'lambda_limit': np.arange(1525e-9, 1575e-9, 1e-12)
}
