from itertools import accumulate

def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    for i, j in enumerate(accumulate(sequence), 1):
        yield round(j / i, 2)
