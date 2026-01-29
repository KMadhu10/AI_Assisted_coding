"""
Function-based Fibonacci generator

This file contains a simple `generate_fibonacci(n)` function that returns
the Fibonacci sequence up to `n` terms. The implementation is iterative
for O(n) time and uses minimal extra space. Comments were written with
AI assistance to make the code clearer for learners.

Copilot prompt used (example):

"""

from typing import List


def generate_fibonacci(n: int) -> List[int]:
    """Return a list with the first `n` Fibonacci numbers.

    Args:
        n: Number of terms to generate. If n <= 0, returns an empty list.

    Returns:
        A list of integers containing the Fibonacci sequence up to n terms.

    Complexity:
        Time: O(n) — a single loop producing n values.
        Space: O(n) for the output list (the result). Uses O(1) extra space.
    """
    if n <= 0:
        return []

    seq: List[int] = [0]
    if n == 1:
        return seq

    a, b = 0, 1
    for _ in range(1, n):
        seq.append(b)
        a, b = b, a + b

    return seq


if __name__ == "__main__":
    # Interactive usage: accept a single integer from the user and print
    # the Fibonacci sequence on one line separated by spaces.
    try:
        n = int(input("Enter number of terms: "))
    except ValueError:
        print("Please enter a valid integer.")
    else:
        seq = generate_fibonacci(n)
        if not seq:
            print("Please enter a positive integer.")
        else:
            print("Fibonacci sequence up to {} terms:".format(n))
            print(' '.join(map(str, seq)))


def _run_sample_tests() -> None:
    """Simple sample tests printing input and output for verification."""
    samples = [7, 1, 0]
    for s in samples:
        out = generate_fibonacci(s)
        print(f"n={s} -> {' '.join(map(str, out)) if out else '(empty)'}")


# When run as a script with argument `--test`, run the sample tests.
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        _run_sample_tests()
