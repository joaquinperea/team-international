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
