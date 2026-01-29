"""
Iterative Fibonacci Implementation

This module demonstrates an efficient iterative approach to generating
Fibonacci sequences. The iterative method uses a loop instead of recursion,
making it suitable for large values of n.

Time Complexity: O(n)
Space Complexity: O(1) for computation, O(n) for result list
"""

from typing import List


def fibonacci_iterative(n: int) -> List[int]:
    """
    Generate Fibonacci sequence iteratively up to n terms.
    
    Args:
        n: Number of Fibonacci terms to generate. Must be >= 0.
        
    Returns:
        List of n Fibonacci numbers.
        
    Raises:
        ValueError: If n is negative.
        
    Time Complexity: O(n) - single loop, n iterations
    Space Complexity: O(n) - output list storage
    
    Example:
        >>> fibonacci_iterative(5)
        [0, 1, 1, 2, 3]
        >>> fibonacci_iterative(0)
        []
        >>> fibonacci_iterative(1)
        [0]
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    
    if n == 0:
        return []
    
    # Initialize result list with first Fibonacci number
    result: List[int] = [0]
    
    if n == 1:
        return result
    
    # Start with first two Fibonacci numbers
    a, b = 0, 1
    
    # Generate remaining Fibonacci numbers
    for _ in range(1, n):
        result.append(b)
        a, b = b, a + b  # Update: b becomes a, and a+b becomes new b
    
    return result


def get_nth_fibonacci_iterative(n: int) -> int:
    """
    Get the nth Fibonacci number (0-indexed) using iteration.
    
    Args:
        n: Index of Fibonacci number to retrieve (0-indexed).
        
    Returns:
        The nth Fibonacci number.
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Example:
        >>> get_nth_fibonacci_iterative(0)
        0
        >>> get_nth_fibonacci_iterative(5)
        5
        >>> get_nth_fibonacci_iterative(10)
        55
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b


# Execution Flow Demonstration
def demonstrate_iterative():
    """Demonstrate iterative Fibonacci execution flow."""
    print("=" * 60)
    print("ITERATIVE FIBONACCI - EXECUTION FLOW")
    print("=" * 60)
    
    n = 6
    print(f"\nGenerating first {n} Fibonacci numbers iteratively:\n")
    
    result = [0]
    a, b = 0, 1
    
    print(f"Initial: result = [0], a = {a}, b = {b}")
    print("\nIteration steps:")
    
    for i in range(1, n):
        result.append(b)
        print(f"  Iteration {i}: append({b}) → result = {result}, a = {b}, b = {a + b}")
        a, b = b, a + b
    
    print(f"\nFinal Result: {result}")
    print(f"Time taken: O(n) = O({n})")
    print(f"Memory used: O(1) for computation + O(n) for result")


if __name__ == "__main__":
    # Test basic functionality
    print("Testing fibonacci_iterative():")
    for i in range(8):
        print(f"  fibonacci_iterative({i}) = {fibonacci_iterative(i)}")
    
    print("\nTesting get_nth_fibonacci_iterative():")
    for i in range(8):
        print(f"  get_nth_fibonacci_iterative({i}) = {get_nth_fibonacci_iterative(i)}")
    
    # Demonstrate execution flow
    demonstrate_iterative()
    
    # Interactive usage
    print("\n" + "=" * 60)
    print("INTERACTIVE MODE")
    print("=" * 60)
    try:
        n = int(input("\nEnter number of Fibonacci terms (iterative): "))
        if n < 0:
            print("Please enter a non-negative integer.")
        else:
            result = fibonacci_iterative(n)
            print(f"Fibonacci sequence: {result}")
    except ValueError:
        print("Please enter a valid integer.")
