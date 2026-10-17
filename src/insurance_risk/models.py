from dataclasses import dataclass

@dataclass
class LineOfBusiness:
    """An insurance line

    Attributes:
        name: The name of the line.
        exposure: The total amount of coverage, measured in policy-years (one policy covered for one year equals one policy-year).
        claim_frequency: The expected number of claims per exposure unit (policy-year).
        claim_severity_mean: The mean amount of an individual claim.
        claim_severity_std: The standard deviation of individual claim amounts.
    """
    name: str
    exposure: float
    claim_frequency: float
    claim_severity_mean: float
    claim_severity_std: float

@dataclass
class Portfolio:
    """A collection of insurance lines included in a loss simulation.

    Attributes:
        lines: The lines of business in the portfolio.
    """

    lines: list[LineOfBusiness]
