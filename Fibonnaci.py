try:
	n = int(input("Enter number of terms: "))
except ValueError:
	print("Please enter a valid integer.")
else:
	if n <= 0:
		print("Please enter a positive integer.")
	else:
		a, b = 0, 1
		print(f"Fibonacci sequence up to {n} terms:")
		first = True
		for _ in range(n):
			if not first:
				print(' ', end='')
			print(a, end='')
			first = False
			a, b = b, a + b
		print()
