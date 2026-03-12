from .formula_team import FormulaTeam
class RedBullTeam(FormulaTeam):
    def __init__(self, budget):
        super().__init__(budget)
        self.expenses = 250000

    def calculate_revenue_after_race(self, race_pos):
        revenue = 0

        sponsors = {
            "Oracle": {1: 1_500_000, 2: 800_000},
            "Honda": {8: 20_000, 10: 10_000}
        }

        for sponsor_positions in sponsors.values():
            eligible_positions = [pos for pos in sponsor_positions if race_pos <= pos]
            if eligible_positions:
                best_position = min(eligible_positions)
                revenue += sponsor_positions[best_position]

        revenue -= 250_000
        self.budget += revenue

        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"