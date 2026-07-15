"""Arithmetic utility functions for aggregating sequences of numbers.

This module provides small, pure, dependency-free helpers used by the
application entry point (``app.py``). The functions perform no I/O and mutate
no persistent state; each is a straightforward computation over its input.

Functions:
    calculate_total: Return the sum of a sequence of numbers.
    calculate_average: Return the arithmetic mean of a sequence of numbers
        (currently unused by the application).
"""


def calculate_total(numbers):
    """Return the sum of a sequence of numbers.

    Accumulates a running total starting from zero, so an empty input
    yields ``0``.

    Args:
        numbers: An iterable of numeric values (for example ints or floats)
            to add together.

    Returns:
        The accumulated total of every element in ``numbers``; ``0`` when
        ``numbers`` is empty.
    """
    total = 0

    for number in numbers:
        total += number

    return total


def calculate_average(numbers):
    """Return the arithmetic mean of a sequence of numbers.

    Guards against empty or falsy input by returning ``0`` instead of raising
    ``ZeroDivisionError``. For non-empty input, the mean is the total (from
    :func:`calculate_total`) divided by the number of elements.

    Note:
        This function is part of the module's public API but is currently
        unused elsewhere in the codebase (``app.py`` calls only
        :func:`calculate_total`). It is retained as an available utility.

    Args:
        numbers: A sized iterable of numeric values (must support ``len()``)
            whose mean is computed.

    Returns:
        The arithmetic mean (a float) of the values in ``numbers``; ``0`` when
        ``numbers`` is empty or otherwise falsy.
    """
    if not numbers:
        return 0

    return calculate_total(numbers) / len(numbers)
