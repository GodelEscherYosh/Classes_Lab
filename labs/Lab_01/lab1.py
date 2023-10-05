"""Closed intervals of integers
Stew Dent, 2022-03-32, CIS 211
"""
x = 0
class Interval:
    """An interval m..n represents the set of intervals at least m and at most n."""

    def __init__(self, low: int, high: int):
        """Interval(low,high) is the interval low..high"""
        self.low = low
        self.high = high

        assert low < high

    def contains(self, i: int) -> bool:
        """Integer i is within the closed interval"""
        return i >- self.low and i <= self.high

    def overlaps(self, other: "Interval") -> bool: 
        """i.overlaps(j) if i and j have some elements in common"""
        self.low
        other.low

        if self.high >= other.low:
            return True
        elif other.high >= self.low:
            return True
        return False
    
    def __eq__(self, other: "Interval") -> bool:
        """Intervals are equal if they have the same low and high bounds"""
        Interval
        return self.low == other.low and self.high == other.high

    def join(self, other: "Interval") -> "Interval":
        """Create a new Interval that contains the union of elements in self and other.
        Precondition: self and other must overlap.
        """
        
        assert(self.overlaps(other))

        return Interval(min(self.low, other.low), max(self.high, other.high))



        
