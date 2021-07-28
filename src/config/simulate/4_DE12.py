import numpy as np

config = {
    "eta": 1,  # 結合損
    "alpha": 52.96,  # 伝搬損失係数
    "K": np.array(
        [0.23070162327425536, 0.04303787885935956, 0.05200462550992102, 0.0788036186199243, 0.5554112953743447]
    ),  # 結合率
    "L": np.array(
        [5.495454545454545e-05, 8.243181818181816e-05, 5.495454545454545e-05, 8.243181818181816e-05]
    ),  # リング周長
    "n_eff": 2.2,  # 実行屈折率
    "n_g": 4.4,  # 群屈折率
    "center_wavelength": 1550e-9,
    "lambda_limit": np.arange(1520e-9, 1560e-9, 1e-12),
}
