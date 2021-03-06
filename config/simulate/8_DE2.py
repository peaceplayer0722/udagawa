import numpy as np

config = {
    "eta": 1,  # 結合損
    "alpha": 52.96,  # 伝搬損失係数
    "K": np.array(
        [
            0.6488653245312135,
            0.21799642358394317,
            0.6743285658297639,
            0.6958112212486283,
            0.17514909873454032,
            0.08301412133391256,
            0.0731174788843163,
            0.100880638091841,
            0.45484152504689734,
        ]
    ),  # 結合率
    "L": np.array(
        [
            8.494902469208556e-05,
            8.494902469208556e-05,
            0.0007079085391007131,
            8.494902469208556e-05,
            8.494902469208556e-05,
            8.494902469208556e-05,
            8.494902469208556e-05,
            8.494902469208556e-05,
        ]
    ),  # リング周長
    "n_eff": 3.3938,  # 実行屈折率
    "n_g": 4.2,  # 群屈折率
    "center_wavelength": 1550e-9,
    # 'lambda_limit': np.arange(1525e-9, 1575e-9, 1e-12)
}
