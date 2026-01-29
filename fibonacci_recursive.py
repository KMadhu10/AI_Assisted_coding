"""
Recursive Fibonacci Implementation

This module demonstrates a recursive approach to calculating Fibonacci numbers.
While elegant and intuitive, pure recursion is inefficient for large n due to
redundant calculations. This file includes examples of basic recursion and
optimized recursion with memoization.

Time Complexity (basic): O(2^n) - exponential, very slow!
Time Complexity (memoized): O(n)
Space Complexity (basic): O(n) - call stack depth
Space Complexity (memoized): O(n) - memo cache + call stack
"""

from typing import List, Dict


def fibonacci_recursive_basic(n: int) -> int:
    """
    Calculate the nth Fibonacci number using basic recursion.
    
    WARNING: This is VERY inefficient for n > 35!
    Use memoization or iteration for larger values.
    
    Args:
        n: Index of Fibonacci number (0-indexed).
        
    Returns:
        The nth Fibonacci number.
        
    Raises:
        ValueError: If n is negative.
        
    Time Complexity: O(2^n) - exponential, VERY SLOW
    Space Complexity: O(n) - call stack depth
    
    Example:
        >>> fibonacci_recursive_basic(5)
        5
        >>> fibonacci_recursive_basic(10)
        55
        
    WARNING: Do NOT use for n > 35 - it will be extremely slow!
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Recursive case: fib(n) = fib(n-1) + fib(n-2)
    return fibonacci_recursive_basic(n - 1) + fibonacci_recursive_basic(n - 2)


def fibonacci_recursive_memoized(n: int, memo: Dict[int, int] = None) -> int:
    """
    Calculate the nth Fibonacci number using recursion with memoization.
    
    Memoization caches results to avoid redundant calculations.
    Much more efficient than basic recursion!
    
    Args:
        n: Index of Fibonacci number (0-indexed).
        memo: Dictionary to cache results (internal use).
        
    Returns:
        The nth Fibonacci number.
        
    Raises:
        ValueError: If n is negative.
        
    Time Complexity: O(n) - each unique subproblem calculated once
    Space Complexity: O(n) - memo cache + call stack
    
    Example:
        >>> fibonacci_recursive_memoized(5)
        5
        >>> fibonacci_recursive_memoized(50)
        12586269025
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    
    # Initialize memo dictionary on first call
    if memo is None:
        memo = {}
    
    # Check if result already computed
    if n in memo:
        return memo[n]
    
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Recursive case with memoization
    memo[n] = fibonacci_recursive_memoized(n - 1, memo) + fibonacci_recursive_memoized(n - 2, memo)
    return memo[n]


def fibonacci_sequence_recursive(n: int) -> List[int]:
    """
    Generate Fibonacci sequence using recursion with memoization.
    
    Args:
        n: Number of terms to generate.
        
    Returns:
        List of n Fibonacci numbers.
        
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    
    result = []
    for i in range(n):
        result.append(fibonacci_recursive_memoized(i))
    return result


# Execution Flow Demonstration
def demonstrate_recursive_basic():
    """Demonstrate basic recursive execution flow (tree structure)."""
    print("=" * 60)
    print("BASIC RECURSIVE FIBONACCI - EXECUTION FLOW TREE")
    print("=" * 60)
    
    n = 5
    print(f"\nCalculating fibonacci_recursive_basic({n}):")
    print("Function call tree:\n")
    
    def print_tree(n, depth=0):
        """Print recursive call tree."""
        indent = "  " * depth
        if n == 0:
            print(f"{indent}fib({n}) = 0 [BASE CASE]")
            return
        if n == 1:
            print(f"{indent}fib({n}) = 1 [BASE CASE]")
            return
        
        print(f"{indent}fib({n})")
        print(f"{indent}├─ fib({n-1})")
        print(f"{indent}└─ fib({n-2})")
        if depth < 3:  # Limit depth for readability
            print_tree(n - 1, depth + 1)
            print_tree(n - 2, depth + 1)
    
    print_tree(n)
    print(f"\n⚠️  Notice the REDUNDANT CALCULATIONS!")
    print(f"   Example: fib(3) is calculated multiple times")
    
    print(f"\nTotal function calls: ~2^{n} = {2**n}")
    print(f"Result: {fibonacci_recursive_basic(n)}")


def demonstrate_recursive_memoized():
    """Demonstrate memoized recursive execution flow."""
    print("\n" + "=" * 60)
    print("MEMOIZED RECURSIVE FIBONACCI - EXECUTION FLOW")
    print("=" * 60)
    
    n = 6
    memo = {}
    
    print(f"\nCalculating fibonacci_recursive_memoized({n}) with memoization:\n")
    print("Each subproblem calculated exactly once:")
    print("┌─────────────────────────────────────┐")
    
    for i in range(n + 1):
        result = fibonacci_recursive_memoized(i, memo)
        print(f"│ fib({i:2d}) = {result:4d} [stored in memo]")
    
    print("└─────────────────────────────────────┘")
    print(f"\nMemo cache contents: {memo}")
    print(f"Total unique calculations: {n + 1} (much better than 2^{n} = {2**n}!)")


# Performance Comparison
def performance_comparison():
    """Compare performance of different approaches."""
    print("\n" + "=" * 60)
    print("PERFORMANCE COMPARISON")
    print("=" * 60)
    
    print("\nEstimated function calls for fib(n):\n")
    print("n  | Basic Recursion | Memoized Recursion | Iterative")
    print("---|-----------------|--------------------|-----------")
    
    for n in [5, 10, 15, 20, 25, 30]:
        basic_calls = 2 ** n
        memo_calls = n
        iter_calls = n
        
        print(f"{n:2d} | {basic_calls:>15,} | {memo_calls:>18,} | {iter_calls:>9,}")
    
    print("\n⚠️  Basic recursion grows EXPONENTIALLY!")
    print("✓ Memoization and iteration grow LINEARLY")


if __name__ == "__main__":
    # Test basic recursion (small values only!)
    print("Testing fibonacci_recursive_basic() (small values only):")
    for i in range(7):
        print(f"  fibonacci_recursive_basic({i}) = {fibonacci_recursive_basic(i)}")
    
    print("\nTesting fibonacci_recursive_memoized():")
    for i in range(12):
        print(f"  fibonacci_recursive_memoized({i}) = {fibonacci_recursive_memoized(i)}")
    
    print("\nTesting fibonacci_sequence_recursive():")
    result = fibonacci_sequence_recursive(8)
    print(f"  First 8 Fibonacci numbers: {result}")
    
    # Demonstrate execution flows
    demonstrate_recursive_basic()
    demonstrate_recursive_memoized()
    
    # Performance comparison
    performance_comparison()
    
    # Interactive usage
    print("\n" + "=" * 60)
    print("INTERACTIVE MODE")
    print("=" * 60)
    try:
        n = int(input("\nEnter Fibonacci index (recursive): "))
        if n < 0:
            print("Please enter a non-negative integer.")
        elif n > 35:
            print("⚠️  For n > 35, using memoization to avoid slowness...")
            result = fibonacci_recursive_memoized(n)
            print(f"fibonacci_recursive_memoized({n}) = {result}")
        else:
            result_basic = fibonacci_recursive_basic(n)
            result_memo = fibonacci_recursive_memoized(n)
            print(f"fibonacci_recursive_basic({n}) = {result_basic}")
            print(f"fibonacci_recursive_memoized({n}) = {result_memo}")
    except ValueError:
        print("Please enter a valid integer.")
