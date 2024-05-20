def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    print("Enter a number to find its factorial:")
    num = int(input())
    result = factorial(num)
    print("Factorial of", num, "is", result)

if __name__ == "__main__":
    main()
