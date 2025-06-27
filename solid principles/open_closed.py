"""
📌 Question:
Create a class DiscountCalculator that computes discounts.
Then add two types of discounts — SeasonalDiscount and LoyaltyDiscount — without modifying DiscountCalculator, only by extending behavior.
(Use inheritance or composition, your choice.)
"""

# MARK: Abstract + Inherit
from abc import ABC, abstractmethod
from typing import Dict


class DiscountCalculator(ABC):
    def __init__(self, discount: float):
        self.discount = discount

    @abstractmethod
    def compute(self) -> Dict[int, float]:
        pass


class SeasonalDiscount(DiscountCalculator):
    def compute(self):
        months = 12
        season_interval = 3
        discount = {}
        for month in range(0, months, season_interval):
            discount[month] = self.discount
        return discount


class LoyaltyDiscount(DiscountCalculator):
    def __init__(self, discount, frequency):
        super().__init__(discount)
        self.frequency = frequency

    def compute(self):
        discount = {}
        if self.frequency < 20:
            return discount
        if self.frequency == 20:
            discount[self.frequency] = self.discount * 2
        else:
            discount[self.frequency] = self.discount
        return discount


discounts = [SeasonalDiscount(20), LoyaltyDiscount(30, 50)]
for discount in discounts:
    print(discount.compute())


# MARK: Composition

class DiscountEngine:
    def __init__(self, strategy: DiscountCalculator):
        self.strategy = strategy

    def calculate_discount(self):
        return self.strategy.compute()


discounts2 = [SeasonalDiscount(20), LoyaltyDiscount(30, 50)]
for discount in discounts2:
    engine = DiscountEngine(discount)
    print(engine.calculate_discount())

# MARK: Strategy Pattern ^
