from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from numpy.typing import NDArray

from insurance_risk.models import LineOfBusiness, Portfolio
from insurance_risk.simulation import simulate
from insurance_risk.risk_metrics import LossSummary, summarize_losses

def print_summary(loss_summary: LossSummary):
    """Prints the loss summary."""
    print(f"Mean loss:                   {loss_summary.mean:,.0f}")
    print(f"Median loss:                 {loss_summary.median:,.0f}")
    print(f"95% Value at Risk (VaR):     {loss_summary.var_95:,.0f}")
    print(f"99% Value at Risk (VaR):     {loss_summary.var_99:,.0f}")
    print(f"95% Expected Shortfall (ES): {loss_summary.es_95:,.0f}")
    print(f"99% Expected Shortfall (ES): {loss_summary.es_99:,.0f}")

def plot_losses(losses: NDArray[np.float64], loss_summary: LossSummary, save_fig: str=False):
    """Plots the loss histogram and displays mean, 95%-VaR, and 99%-VaR."""
    hist_color = "blue"
    summary_color = "red"
    plt.hist(losses, bins=50, color=hist_color)
    plt.axvline(loss_summary.mean, color=summary_color, linestyle="-", label="Mean")
    plt.axvline(loss_summary.var_95, color=summary_color, linestyle="--", label="95% VaR")
    plt.axvline(loss_summary.var_99, color=summary_color, linestyle=":", label="99% VaR")
    plt.xlabel("Total portfolio loss")
    plt.ylabel("Number of simulations")
    plt.legend()

    if save_fig:
        output_dir = Path(__file__).resolve().parent / "output"
        output_dir.mkdir(exist_ok=True)
        plot_path = output_dir / "portfolio_loss_distribution.png"
        plt.savefig(plot_path, dpi=150, bbox_inches="tight")
        print(f"Plot saved to: {plot_path}")
        plt.show()

motor = LineOfBusiness(
    name="Motor",
    exposure=10_000,
    claim_frequency=0.08,
    claim_severity_mean=4_000,
    claim_severity_std=7_000,
)

home = LineOfBusiness(
    name="Home",
    exposure=7_500,
    claim_frequency=0.025,
    claim_severity_mean=2_000,
    claim_severity_std=3_000,
)

liability = LineOfBusiness(
    name="Liability",
    exposure=30_000,
    claim_frequency=0.001,
    claim_severity_mean=20_000,
    claim_severity_std=50_000
)

portfolio = Portfolio(lines=[motor, home, liability])
losses = simulate(portfolio, n_simulations=10_000, seed=13)
loss_summary = summarize_losses(losses)
print_summary(loss_summary)
plot_losses(losses=losses, loss_summary=loss_summary, save_fig=True)
