class Point:
    _points = 5

    @classmethod
    def add_extra_points(cls):
        cls._points += 1
        print("You earned 1 point for 2 extra words")

    @classmethod
    def add_points(cls):
        cls._points += 2
        print("You earned 2 points for every valid word")

    @classmethod
    def get_points(cls):
        return cls._points
