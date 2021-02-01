import numpy as np

config = {
    'eta': 0.996,  # 結合損
    'alpha': 52.96,  # 伝搬損失係数
    'K': np.array([
        0.24180925449654161, 0.04216995538665558, 0.07041288786112332, 0.0995501501692122, 0.14821275186266847, 0.050197256366153076, 0.04763963539888427, 0.11806501899600563, 0.40190334767661007
    ]),  # 結合率
    'L': np.array([
        0.0002472954545454545, 0.0002472954545454545, 0.00013738636363636362, 0.00013738636363636362, 0.0008243181818181817, 0.00013738636363636362, 0.0008243181818181817, 0.0002472954545454545
    ]),  # リング周長
    'n_eff': 2.2,  # 実行屈折率
    'n_g': 4.4,  # 群屈折率
    'center_wavelength': 1550e-9,
    'lambda': np.arange(1520e-9, 1560e-9, 1e-12)
}