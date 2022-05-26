import numpy as np
import numpy.typing as npt


def simulate_transfer_function(
    wavelength: npt.NDArray[np.float_],     #サンプリング波長
    L: npt.ArrayLike,                       #リング周長のリスト
    K: npt.ArrayLike,                       #結合率のリスト
    alpha: float,                           #電力透過率
    eta: float,                             #結合損
    n_eff: float,                           #実行屈折率
    n_g: float,                             #群屈折率
    center_wavelength: float,               #中心波長
) -> npt.NDArray[np.float_]:                #伝達関数のリストを出力
    y: npt.NDArray[np.float_] = 20 * np.log10(np.abs(_D(L, K, alpha, wavelength, eta, n_eff, n_g, center_wavelength)))
    return y.reshape(y.size)

'''
(K_n:float, 結合損:float)
-> C(K):2×2行列を計算
'''
def _C(K_k: float, eta: float) -> npt.NDArray[np.float_]:
    C: npt.NDArray[np.float_] = (
        1
        / (-1j * eta * np.sqrt(K_k))
        * np.array([[1, -eta * np.sqrt(eta - K_k)], [np.sqrt(eta - K_k) * eta, -(eta ** 2)]])
    )
    return C

'''
(電力透過率a:float,リング周長 L_n:float, 波長 wavelength:ndarray[float], 
 実行屈折率 n_eff:float,群屈折率 n_g:float, 中央波長center_wavelength:float)
->R(a,L,λ):2×2行列
'''
def _R(
    a_k: float,
    L_k: float,
    wavelength: npt.NDArray[np.float_],
    n_eff: float,
    n_g: float,
    center_wavelength: float,
) -> npt.NDArray[np.float_]:
    N_k = np.round(L_k * n_eff / center_wavelength)
    shifted_center_wavelength = L_k * n_eff / N_k
    x = (
        1j
        * np.pi
        * L_k
        * n_g
        * (wavelength - shifted_center_wavelength)
        / shifted_center_wavelength
        / shifted_center_wavelength
    )
    return np.array([[np.exp(x) / np.sqrt(a_k), 0], [0, np.exp(-x) * np.sqrt(a_k)]], dtype="object")


def _M(
    L: npt.ArrayLike,                       #リング周長のリスト
    K: npt.ArrayLike,                       #結合率のリスト
    alpha: float,                           #伝搬損失係数
    wavelength: npt.NDArray[np.float_],     #サンプリング波長
    eta: float,                             #結合損
    n_eff: float,                           #実行屈折率
    n_g: float,                             #群屈折率
    center_wavelength: float,               #中心波長
) -> npt.NDArray[np.float_]:                #伝達行列:2×2行列
    L_: npt.NDArray[np.float_] = np.array(L)[::-1]
    K_: npt.NDArray[np.float_] = np.array(K)[::-1]
    a: npt.NDArray[np.float_] = np.exp(-alpha * L_)
    product = np.identity(2)                #2×2の単位行列を生成
    for K_k, a_k, L_k in zip(K_[:-1], a, L_):
        product = np.dot(product, _C(K_k, eta))
        product = np.dot(product, _R(a_k, L_k, wavelength, n_eff, n_g, center_wavelength))
    product = np.dot(product, _C(K_[-1], eta))
    return product


def _D(
    L: npt.ArrayLike,                          #リング周長のリスト
    K: npt.ArrayLike,                          #結合率のリスト
    alpha: float,                              #伝搬損失係数
    wavelength: npt.NDArray[np.float_],        #サンプリング波長
    eta: float,                                #結合損
    n_eff: float,                              #実行屈折率
    n_g: float,                                #群屈折率
    center_wavelength: float,                  #中心波長
) -> npt.NDArray[np.float_]:                   #input-drop間の伝達関数を出力             
    D: npt.NDArray[np.float_] = 1 / _M(L, K, alpha, wavelength, eta, n_eff, n_g, center_wavelength)[0, 0]
    return D
