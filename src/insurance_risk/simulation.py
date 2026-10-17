import numpy as np

from .models import Portfolio

def simulate(portfolio: Portfolio, n_simulations=10_000, seed=13):
    """Simulates aggregate losses for a portfolio.

    Args:
        portfolio: The lines of business to simulate.
        n_simulations: Number of independent loss scenarios. Defaults to 10,000.
        seed: Seed for reproducibility. Defaults to 13.
    
    Returns:
        A NumPy array of total portfolio loss for each scenario.
    """
    rng = np.random.default_rng(seed)
    total_losses = np.zeros(n_simulations)

    for simulation_index in range(n_simulations):
        for line in portfolio.lines:
            expected_claims = line.exposure * line.claim_frequency
            n_claims = rng.poisson(expected_claims)
            mu, sigma = mean_std_to_lognormal_mu_sigma(
                line.claim_severity_mean, 
                line.claim_severity_std
                )

            claim_amounts = rng.lognormal(
                mean=mu,
                sigma=sigma,
                size=n_claims,
            )

            total_losses[simulation_index] += claim_amounts.sum()

    return total_losses

def mean_std_to_lognormal_mu_sigma(mean: float, std: float):
    """Returns the parameters of a lognormal distribution that give the desired mean and std.
    
    See `derivations.md` in the project root for the derivation.
    """

    variance_ratio = (std / mean) ** 2
    sigma_squared = np.log1p(variance_ratio)
    sigma = np.sqrt(sigma_squared)
    mu = np.log(mean) - sigma_squared / 2
    return mu, sigma
