# pricing.py

class PricingModel:
    def __init__(self, base_price: float):
        self.base_price = base_price
        self.max_discount = 0.30
        self.min_discount = 0.05

    def accept_or_counter(self, user_price: float):
        """Decides whether to accept the user's offer or counter it."""
        discounted_price = self.base_price * (1 - self.max_discount)
        if user_price >= discounted_price:
            return "accepted", user_price
        else:
            counter_offer = self.base_price * (1 - self.min_discount)
            return "countered", counter_offer
