class Stats:
    def __init__(self, values_added, values_stats):
        """
        Constructor for initialize an object of Stats class.
        :param values_added: list of added values.
        :param values_stats: dict of values with their stats.
        """
        self.values_added = values_added
        self.values_stats = values_stats

    def less(self, value):
        """
        Accepts an input value and check all less values added in values list.
        :param value: value to evaluate.
        :return: less values.
        """
        try:
            return self.values_stats[value]['left']
        except Exception as e:
            if value not in self.values_added:
                print('Input value was not be added before.')
            else:
                print(f'Exception found on less method: {e}')

    def between(self, min_value, max_value):
        """
        Accepts two input values and check all between values added in values list.
        Include min and max value.
        :param min_value: minimum value to evaluate.
        :param max_value: maximum value to evaluate.
        :return: between values.
        """
        try:
            return len(self.values_added) - \
                   self.values_stats[min_value]['left'] - \
                   self.values_stats[max_value]['right']
        except Exception as e:
            if min_value or max_value not in self.values_added:
                print('Some of values were not be added before.')
            else:
                print(f'Exception found on between method: {e}')

    def greater(self, value):
        """
        Accepts an input value and check all greater values added in values list.
        :param value: value to evaluate.
        :return: greater values.
        """
        try:
            return self.values_stats[value]['right']
        except Exception as e:
            if value not in self.values_added:
                print('Input value was not be added before.')
            else:
                print(f'Exception found on between method: {e}')
