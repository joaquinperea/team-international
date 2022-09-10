from stats import Stats


class DataCapture:
    def __init__(self):
        """
        Initialize a DataCapture object declaring both structures.
        """
        self.values_added = []
        self.values_stats = {}

    def add(self, value):
        """
        Function that adds new elements to the "values_added" list.
        :param value: input value to add.
        """
        try:
            if isinstance(value, int) and 0 <= value < 1000:
                self.values_added.append(value)
            else:
                print('Value inserted is not an integer, is not positive or higher than 1000.')
        except Exception as e:
            print(f'Exception found on add method: {e}')

    def build_stats(self):
        """
        Function that generates the necessary statistics structure to be consumed
        through the "stats" object.
        :return: Stats object.
        """
        try:
            self.values_added.sort()
            for i, elem in enumerate(self.values_added):
                if elem not in self.values_stats:
                    self.values_stats[elem] = {
                        'left': i,
                        'right': len(self.values_added) - i - 1,
                        'count': 1
                    }
                else:
                    self.values_stats[elem]['right'] = len(self.values_added) - i - 1
                    self.values_stats[elem]['count'] += 1
            return Stats(self.values_added, self.values_stats)
        except Exception as e:
            print(f'Exception found on build_stats method: {e}')
