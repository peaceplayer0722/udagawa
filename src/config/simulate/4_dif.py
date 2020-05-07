import numpy as np

config = {
    'eta': 1,  # 結合損
    'alpha': 52.96,  # 伝搬損失係数
    'K': np.array([0.13436424, 0.84743374, 0.76377462, 0.25506903, 0.44543509]), # 結合率
    'L': np.array([0.00018269, 0.00018269, 0.00018269, 0.00018269]),  # リング周長
    'n': 3.3938,  # 屈折率
    'center_wavelength': 1550e-9
}
