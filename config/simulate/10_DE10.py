import numpy as np

config = {
    "eta": 0.996,  # 結合損
    "alpha": 52.96,  # 伝搬損失係数
    "K": [
        0.3716417232472473,
        0.017290441784985455,
        0.053145931958770265,
        0.3236036036769422,
        0.2474820164083541,
        0.9293027783407982,
        0.7439879399097385,
        0.032907838390978994,
        0.11301522856629537,
        0.14212858929477945,
        0.6289920951127447,
    ],  # 結合率
    "L": [
        0.00013738636363636362,
        0.00013738636363636362,
        8.243181818181816e-05,
        8.243181818181816e-05,
        8.243181818181816e-05,
        8.243181818181816e-05,
        8.243181818181816e-05,
        0.0002472954545454545,
        0.0002472954545454545,
        0.0002472954545454545,
    ],  # リング周長
    "n_eff": 2.2,  # 実行屈折率
    "n_g": 4.4,  # 群屈折率
    "center_wavelength": 1550e-9,
    "lambda_limit": np.arange(1520e-9, 1560e-9, 1e-12),
    "label": r"original",
}
