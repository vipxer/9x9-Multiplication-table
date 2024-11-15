def print_multiplication_table():
    for i in range(1, 10):
        for j in range(1, i + 1):
            product = i * j
            print(f"{j} × {i} = {product:<2}", end="  ")
        print()

if __name__ == "__main__":
    print("9x9 Multiplication table:")
    print("-" * 50)
    print_multiplication_table()
