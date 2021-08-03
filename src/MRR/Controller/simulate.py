import numpy as np
import numpy.typing as npt

from config.model import SimulationConfig
from MRR.Evaluator import Evaluator
from MRR.gragh import Gragh
from MRR.logger import Logger
from MRR.Simulator import Ring, TransferFunction


class Simulator:
    def __init__(self, is_focus: bool = False) -> None:
        self.logger = Logger()
        self.xs: list[npt.NDArray[np.float64]] = []
        self.ys: list[npt.NDArray[np.float64]] = []
        self.number_of_rings: int = 0
        self.graph = Gragh(is_focus)

    def simulate(self, config: SimulationConfig) -> None:
        mrr = TransferFunction(config.L, config.K, config)
        mrr.print_parameters()
        print("K:", config.K.tolist())
        print("L:", config.L.tolist())
        ring = Ring(config)
        N = ring.calculate_N(config.L)
        FSR = ring.calculate_practical_FSR(N)

        if config.lambda_limit_is_defined:
            x = config.lambda_limit
            y = mrr.simulate(x)
        else:
            x = ring.calculate_x(FSR)
            y = mrr.simulate(x)
            evaluator = Evaluator(x, y, config)
            result = evaluator.evaluate_band()
            print(result)

        self.logger.save_data_as_csv(x, y, config.name)
        self.logger.typeset_pgfplots_graph(config.name)
        self.graph.create()
        self.graph.plot(x, y, config.label)

    def show(self) -> None:
        self.graph.show(self.logger.generate_image_path())
