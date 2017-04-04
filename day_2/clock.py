class Clock(object):
		"""Display a clock depending on the parameters given"""
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
        self.calculation()  # saves me from having to repeat
        # calculation(self) in __eq__

    def calculation(self):
        # the arguments are not hours, minutes - because they are in __init__?
        # this calculation can be optimized with floor division.
        # We don't need all the ifs.
        if self.minutes < 0:
            self.hours += (self.minutes - (self.minutes % 60)) / 60
            self.minutes -= (self.minutes - (self.minutes % 60))

        if self.minutes >= 60:
            self.hours += (self.minutes - (self.minutes % 60)) / 60
            self.minutes -= (self.minutes - (self.minutes % 60))

        if self.hours < 0:
            self.hours -= (self.hours - (self.hours % 24))

        if self.hours >= 24:
            self.hours -= (self.hours - (self.hours % 24))

        self.minutes = int(self.minutes)
        self.hours = int(self.hours)

    def __str__(self):  # can also be __repr__
        # we need Clock to be displayed in this format 15:16
        return '%0*d' % (2, self.hours)+':'+'%0*d' % (2, self.minutes)

    def add(self, extra):
        return Clock(self.hours, self.minutes + extra)
        # this method returns minutes with whatever is passed in as extra added to it.

    def __eq__(self, other):
        return self.minutes == other.minutes and self.hours == other.hours

    # def __ne__(self, other):
    #     return self.minutes != other.minutes and self.hours != other.hours
    # I'm guessing this is not needed since __eq__ returns true or false
    # for its conditon.


watch = Clock(1, 1)


print watch.add(3)
