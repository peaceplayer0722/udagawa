import numpy as np

config = {
    "eta": 1,  # 結合損
    "alpha": 52.96,  # 伝搬損失係数
    "K": np.array([0.10160936406648989, 0.011395812979615644, 0.14949515586294948]),  # 結合効率
    "L": np.array([2.83163416e-05, 4.24745123e-05]),  # リング周長
    "n_eff": 3.3938,  # 実行屈折率
    "n_g": 4.2,  # 群屈折率
    "lambda_limit": np.arange(1525e-9, 1575e-9, 1e-12),  # 波長レンジ
}
