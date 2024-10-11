def sum_of_series(n):
    total = 0.0
    for i in range(1, n+1):
        if i % 2 == 0:
            total -= 1 / i
        else:
            total += 1 / i
    return total
n =  int(input("Enter a number of terms:"))
print(f"Sum of the series: {sum_of_series(n):.5f}")