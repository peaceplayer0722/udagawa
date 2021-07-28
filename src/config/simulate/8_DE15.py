import numpy as np

config = {
    "eta": 0.996,  # 結合損
    "alpha": 52.96,  # 伝搬損失係数
    "K": np.array(
        [
            0.2456973861767161,
            0.05286603992625161,
            0.35446704896186804,
            0.9898419719743882,
            0.5085988434650281,
            0.06840974588265497,
            0.05838387317242322,
            0.11893124787100318,
            0.6239367304036265,
        ]
    ),  # 結合率
    "L": np.array(
        [
            5.754611350109022e-05,
            5.754611350109022e-05,
            8.631917025163532e-05,
            8.631917025163532e-05,
            8.631917025163532e-05,
            8.631917025163532e-05,
            8.631917025163532e-05,
            8.631917025163532e-05,
        ]
    ),  # リング周長
    "n_eff": 3.3938,  # 実行屈折率
    "n_g": 4.2,  # 群屈折率
    "center_wavelength": 1550e-9,
    # 'lambda_limit': np.arange(1520e-9, 1560e-9, 1e-12)
}
