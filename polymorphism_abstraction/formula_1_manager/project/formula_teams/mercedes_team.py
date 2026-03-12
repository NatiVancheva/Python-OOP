from .formula_team import FormulaTeam
class MercedesTeam(FormulaTeam):
    def __init__(self, budget):
        super().__init__(budget)
        self.expenses = 200000

    def calculate_revenue_after_race(self, race_pos):
        revenue = 0

        sponsors = {
            "Petronas": {1: 1_000_000, 3: 500_000},
            "TeamViewer": {5: 100_000, 7: 50_000}
        }

        for sponsor_positions in sponsors.values():
            eligible_positions = [pos for pos in sponsor_positions if race_pos <= pos]
            if eligible_positions:
                best_position = min(eligible_positions)
                revenue += sponsor_positions[best_position]

        revenue -= 200_000
        self.budget += revenue

        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
        