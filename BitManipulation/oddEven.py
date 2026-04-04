def check_odd_even(n):
    return n & 1


if __name__ == "__main__":
    for n in range(11):
        x = check_odd_even(n)
        o = "Even" if x == 0 else "Odd"
        print(f"{n = } {o}")
