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
        if value not in self.values_added:
            raise ValueError('The entered value has not been added before.')
        else:
            return self.values_stats[value]['left']

    def between(self, min_value, max_value):
        """
        Accepts two input values and check all between values added in values list.
        Include min and max value.
        :param min_value: minimum value to evaluate.
        :param max_value: maximum value to evaluate.
        :return: between values.
        """
        if min_value not in self.values_added or max_value not in self.values_added:
            raise ValueError('The entered values have not been added before.')
        else:
            return len(self.values_added) - \
                   self.values_stats[min_value]['left'] - \
                   self.values_stats[max_value]['right']

    def greater(self, value):
        """
        Accepts an input value and check all greater values added in values list.
        :param value: value to evaluate.
        :return: greater values.
        """
        if value not in self.values_added:
            raise ValueError('The entered value has not been added before.')
        else:
            return self.values_stats[value]['right']
