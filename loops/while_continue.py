# Example of a while loop with continue

i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        # Skip even numbers
        continue
    print(i)  # Print only odd numbers
