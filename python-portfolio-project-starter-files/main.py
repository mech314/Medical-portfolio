import csv

class DataAnalyzer:
    def __init__(self, csv_data):
        self.csv_data = csv_data

    def calc_avr_age(self):
        """Calculates the average age of the clients"""
        with open(self.csv_data, 'r') as datafile:
            data_dict = csv.DictReader(datafile)
            ages = [int(row['age']) for row in data_dict]
        if ages:
            average_age = sum(ages) / len(ages)
            print(f'Number of customers: {len(ages)} with the average age of the client: {round(average_age)}')
        else:
            print('No data available to calculate average age.')

    def max_region(self):
        """Calculates where the customers come from"""
        with open(self.csv_data, 'r') as datafile:
            data_dict = csv.DictReader(datafile)
            region_count = {}
            for row in data_dict:
                region = row['region']
                region_count[region] = region_count.get(region, 0) + 1
            if region_count:
                max_region = max(region_count, key=region_count.get)
                print(f'Most of the customers ({region_count[max_region]}) come from {max_region}')
            else:
                print('No data available to determine the region with most customers.')

    def smoker_cost(self):
        """Calculates the differnece in price for smokers and non smokers"""
        with open(self.csv_data, 'r') as datafile:
            data_dict = csv.DictReader(datafile)
            smoker_costs = [float(row['charges']) for row in data_dict if row['smoker'] == 'yes']
            nonsmoker_costs = [float(row['charges']) for row in data_dict if row['smoker'] == 'no']
        if smoker_costs and nonsmoker_costs:
            avg_smoker_cost = sum(smoker_costs) / len(smoker_costs)
            avg_nonsmoker_cost = sum(nonsmoker_costs) / len(nonsmoker_costs)
            print(f'Smokers on average pay ${avg_smoker_cost:.2f} while non-smokers pay only ${round(avg_nonsmoker_cost)}')
        else:
            print('No data available to calculate smoker and non-smoker costs.')

    def average_age_with_child(self):
        """Calculates average age for people with at least one child"""
        with open(self.csv_data, 'r') as datafile:
            data_dict = csv.DictReader(datafile)
            ages_with_children = [int(row['age']) for row in data_dict if int(row['children']) > 0]
        if ages_with_children:
            average_age_with_child = sum(ages_with_children) / len(ages_with_children)
            print(f'Average age for individuals who have at least one child is {round(average_age_with_child)}')
        else:
            print('No data available to calculate average age for individuals with children.')

if __name__ == "__main__":
    analyzer = DataAnalyzer('python-portfolio-project-starter-files/insurance.csv')
    analyzer.calc_avr_age()
    analyzer.max_region()
    analyzer.smoker_cost()
    analyzer.average_age_with_child()
