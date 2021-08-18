import numpy as np

config = {
    "eta": 0.996,  # 結合損
    "alpha": 52.96,  # 伝搬損失係数
    "K": np.array(
        [
            0.18902787044079716,
            0.038284178907437905,
            0.04153039594481933,
            0.1616603404381629,
            0.5169600653266402,
            0.33319818665453804,
            0.2239807639568177,
            0.29223707699395196,
            0.365288226591892,
            0.406083404745424,
            0.43075327182701306,
            0.623872140983909,
            0.9460630350634363,
        ]
    ),  # 結合率
    "L": np.array(
        [
            8.243181818181816e-05,
            8.243181818181816e-05,
            8.243181818181816e-05,
            0.00038468181818181814,
            0.00038468181818181814,
            0.00019234090909090907,
            0.00019234090909090907,
            0.00019234090909090907,
            0.00019234090909090907,
            0.00019234090909090907,
            0.00019234090909090907,
            0.00019234090909090907,
        ]
    ),  # リング周長
    "n_eff": 2.2,  # 実行屈折率
    "n_g": 4.4,  # 群屈折率
    "center_wavelength": 1550e-9,
    "lambda_limit": np.arange(1520e-9, 1560e-9, 1e-12),
    "label": r"{}{\(12^\textrm{th}\)}",
}

"""
p=[0.03,0.07,0.2,0.7]
-0.0    4
-0.0    4
-0.0    4
-0.0    4
4.091631984319461       4
4.091631984319461       4
4.091631984319461       4
4.091631984319461       4
4.169124153165209       4
4.173179106468703       4
4.181671411823726       4
4.181671411823726       3
4.181671411823726       4
4.181671411823726       4
4.181671411823726       2
4.181671411823726       4
4.181671411823726       4
4.181671411823726       3
4.181671411823726       4
4.181671411823726       4
4.181671411823726       4
4.181671411823726       4
4.181671411823726       4
4.181671411823726       1
4.181671411823726       3
4.181671411823726       4
8.386953273240296       3
8.386953273240296       4
8.386953273240296       4
8.386953273240296       3
8.386953273240296       3
8.386953273240296       4
8.386953273240296       3
8.386953273240296       4
8.386953273240296       4
8.386953273240296       4
8.386953273240296       4
8.386953273240296       1
8.386953273240296       4
8.386953273240296       4
8.60484189089214        4
8.60484189089214        4
8.60484189089214        4
8.612628318989376       1
8.612628318989376       4
8.692420326087374       3
8.692420326087374       4
9.452681395738182       4
9.452681395738182       4
9.452681395738182       4
9.452681395738182       4
9.452681395738182       4
12.934153408902937      3
12.934153408902937      4
12.934153408902937      4
12.934153408902937      4
12.934153408902937      4
12.934153408902937      4
12.934153408902937      4
12.934153408902937      3
12.934153408902937      4
12.934153408902937      4
12.934153408902937      4
12.934153408902937      4
12.934153408902937      1
12.934153408902937      4
12.934153408902937      4
12.934153408902937      4
12.934153408902937      2
12.934153408902937      4
12.934153408902937      4
12.934153408902937      3
12.934153408902937      4
12.934153408902937      4
12.934153408902937      4
12.934153408902937      4
12.934153408902937      4
12.934153408902937      4
12.934153408902937      4
12.934153408902937      4
12.934153408902937      4
12.934153408902937      4
12.934153408902937      4
"""
