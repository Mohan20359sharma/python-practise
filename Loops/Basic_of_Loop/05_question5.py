start = int(input("Enter a start number: "))
end = int(input("Enter a end number: "))
print(f"Even number between {start} and {end}")
for i in range(start, end + 1):
    if i % 2 == 0 :
        print(i)