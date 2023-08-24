# Jason Sy
# CSS 340: Applied Algorithmics
# 5/11/2022
# Using recursion to calculate a Catalan number

import sys

# catalan function
def cat(n):
    if n <= 1:
        return 1
    result = 0
    for i in range(n):
        result += cat(i) * cat(n - i - 1)

    return result

# Main function
def main():
    if len(sys.argv) >= 2:
        n = int(sys.argv[1])
    else:
        n = int(input("Please input argument: "))
    print(cat(n))



main()