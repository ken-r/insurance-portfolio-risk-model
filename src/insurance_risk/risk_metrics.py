from dataclasses import dataclass
import numpy as np
from numpy.typing import NDArray

@dataclass
class LossSummary:
    """Summary statistics for simulated portfolio losses.

    Attributes:
        mean: Average loss.
        median: Median loss.
        var_95: 95th percentile of losses (95% VaR).
        var_99: 99th percentile of losses (99% VaR).
        es_95: Average loss in the worst 5% of outcomes (95% ES).
        es_99: Average loss in the worst 1% of outcomes (99% ES).
    """
    mean: float
    median: float
    var_95: float
    var_99: float
    es_95: float
    es_99: float


def summarize_losses(losses: NDArray[np.float64]):
    mean = losses.mean()
    median = np.median(losses)
    p95, p99 = np.percentile(losses, [95, 99])
    es_95 = losses[losses >= p95].mean()
    es_99 = losses[losses >= p99].mean()

    return LossSummary(
        mean=mean,
        median=median,
        var_95=p95,
        var_99=p99,
        es_95=es_95,
        es_99=es_99,
    )
