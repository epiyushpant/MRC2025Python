def print_pattern(rows):
    print("\n=== PATTERN 1: Right-Angled Triangle ===")
    for i in range(1, rows + 1):
        print("* " * i)

    print("\n=== PATTERN 2: Pyramid ===")
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        print("* " * i)

    print("\n=== PATTERN 3: Inverted Pyramid ===")
    for i in range(rows, 0, -1):
        print(" " * (rows - i), end="")
        print("* " * i)

    print("\n=== PATTERN 4: Diamond ===")
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        print("* " * i)
    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i), end="")
        print("* " * i)

    print("\n=== PATTERN 5: Number Pyramid ===")
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

if __name__ == "__main__":
    rows = int(input("Enter number of rows (3-9 recommended): "))
    print_pattern(rows)