import numpy as np

config = {
    'eta': 0.996,  # 結合損
    'alpha': 52.96,  # 伝搬損失係数
    'K': np.array([
        0.34080834619745426, 0.058263995220206144, 0.06354668204751696, 0.035696044880658695, 0.01888770642479226, 0.022801840639856352, 0.25343132001078494
    ]),  # 結合率
    'L': np.array([
        0.0004396363636363636, 0.0004396363636363636, 8.243181818181816e-05, 0.0004396363636363636, 8.243181818181816e-05, 0.00032972727272727266
    ]),  # リング周長
    'n_eff': 2.2,  # 実行屈折率
    'n_g': 4.4,  # 群屈折率
    'center_wavelength': 1550e-9,
    'lambda': np.arange(1520e-9, 1560e-9, 1e-12)
}
