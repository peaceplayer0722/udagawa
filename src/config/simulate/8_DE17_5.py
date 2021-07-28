import numpy as np

config = {
    "eta": 0.996,  # 結合損
    "alpha": 52.96,  # 伝搬損失係数
    "K": np.array(
        [
            0.3272398771381704,
            0.10676634947204956,
            0.015485427279088266,
            0.053333644072596116,
            0.14222227600831278,
            0.7326125666803643,
            0.5910844076281513,
            0.05460700990889374,
            0.30762237545316246,
        ]
    ),  # 結合率
    "L": np.array(
        [
            8.243181818181816e-05,
            8.243181818181816e-05,
            5.495454545454545e-05,
            5.495454545454545e-05,
            8.243181818181816e-05,
            8.243181818181816e-05,
            5.495454545454545e-05,
            5.495454545454545e-05,
        ]
    ),  # リング周長
    "n_eff": 2.2,  # 実行屈折率
    "n_g": 4.4,  # 群屈折率
    "center_wavelength": 1550e-9,
    # 'lambda_limit': np.arange(1520e-9, 1560e-9, 1e-12)
}
