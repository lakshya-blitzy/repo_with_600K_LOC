"""Console entry point for the numeric-aggregation demo application.

This module orchestrates a small, deterministic workflow: it builds a fixed
list of integers, delegates summation to :func:`service.calculate_total`, and
prints the total, each individual value, and a completion message to standard
output.

The module depends on the local ``service`` module via an unqualified import
(``from service import calculate_total``); ``service.py`` must therefore be
co-located on the Python import path (typically the same directory), otherwise
``ModuleNotFoundError: No module named 'service'`` is raised at startup.

Run directly with::

    python3 app.py
"""

from service import calculate_total


def main():
    """Run the aggregation workflow and print results to standard output.

    Builds the fixed input list ``[10, 20, 30, 40]``, computes its sum with
    :func:`service.calculate_total`, and writes the following to standard
    output in order: ``Total: 100``, each value on its own line (``10``,
    ``20``, ``30``, ``40``), and finally ``Application completed``.

    This function executes only when the module is run as a script (under the
    ``if __name__ == "__main__":`` guard); importing the module does not run
    it.

    Returns:
        None. All results are produced as side effects on standard output.
    """
    # Fixed demonstration input; the utility takes no external configuration,
    # command-line arguments, or environment variables.
    numbers = [10, 20, 30, 40]

    # Delegate summation to the service module (returns 100 for this input).
    total = calculate_total(numbers)

    # Emit the aggregate total.
    print(f"Total: {total}")

    # Echo each input value on its own line, preserving list order.
    for number in numbers:
        print(number)

    # Signal successful completion.
    print("Application completed")


if __name__ == "__main__":
    main()
