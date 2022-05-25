from config.model import OptimizationConfig

config = OptimizationConfig(
    eta=0.996,      #結合損
    alpha=52.96,    # 伝搬損失係数
    n_eff=2.2,      #実行屈折率
    n_g=4.4,        #群屈折率
    number_of_rings=2,      #リング次数
    center_wavelength=1550e-9,      #中央波長
    FSR=20e-9,      #共振波長間隔
    length_of_3db_band=1e-9,        #3dB波長帯域     
    max_crosstalk=-30,      #クロストークの最大許容値
    H_p=-20,        #通過域の下限
    H_s=-60,        #阻止域の上限
    H_i=-10,        #挿入損失の最低許容値
    r_max=5,        #リプルの最大許容値
    weight=[1.0, 3.5, 1.0, 5.0, 3.5, 1.0, 1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
    #重みパラメータ
    min_ring_length=50e-6,      #最小リング長
    number_of_generations=3,      #DEの世代の数
    strategy=[0.03, 0.07, 0.2, 0.7],        #?
)
