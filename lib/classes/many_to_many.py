class NationalPark:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise Exception("Invalid name")
        self._name = name
        self._trips = []

    @property
    def name(self):
        return self._name

    def trips(self):
        return self._trips

    def visitors(self):
        return list({trip.visitor for trip in self._trips})

    def total_visits(self):
        return len(self._trips)

    def best_visitor(self):
        if not self._trips:
            return None
        from collections import Counter
        visitor_counts = Counter(trip.visitor for trip in self._trips)
        return visitor_counts.most_common(1)[0][0]


class Visitor:
    def __init__(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise Exception("Invalid name")
        self._name = name
        self._trips = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 15):
            raise Exception("Invalid name")
        self._name = value

    def trips(self):
        return self._trips

    def national_parks(self):
        return list({trip.national_park for trip in self._trips})

    def total_visits_at_park(self, park):
        return sum(1 for trip in self._trips if trip.national_park == park)


class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        if not isinstance(start_date, str) or len(start_date) < 7:
            raise Exception("Invalid start_date")
        if not isinstance(end_date, str) or len(end_date) < 7:
            raise Exception("Invalid end_date")

        self._visitor = visitor
        self._national_park = national_park
        self._start_date = start_date
        self._end_date = end_date

        national_park.trips().append(self)
        visitor.trips().append(self)

        Trip.all.append(self)

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        if not isinstance(value, str) or len(value) < 7:
            raise Exception("Invalid start_date")
        self._start_date = value

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        if not isinstance(value, str) or len(value) < 7:
            raise Exception("Invalid end_date")
        self._end_date = value

    @property
    def visitor(self):
        return self._visitor

    @property
    def national_park(self):
        return self._national_park
