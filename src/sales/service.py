class SalesService:

    def __init__(self, sales_repository):
        self.sales_repository = sales_repository

    def calculate_weekly_sales(self):
        return self.sales_repository.get_weekly_sales_count()

    def calculate_sales_probability(self, weight_factor=2):
        sales_by_day = self.sales_repository.get_sales_by_day()
        probabilities = {i: 0 for i in range(1, 8)}
        total_sales = sum([sales.total_sales for sales in sales_by_day])

        if total_sales > 0:
            for sales in sales_by_day:
                if sales.day_of_week == 2:
                    probabilities[sales.day_of_week] = (sales.total_sales * weight_factor) / total_sales
                else:
                    probabilities[sales.day_of_week] = sales.total_sales / total_sales

            total_probability = sum(probabilities.values())
            probabilities = {day: prob / total_probability for day, prob in probabilities.items()}

        return probabilities
