def solve(n, m, a):
    seen = set()
    seen.add(0)
    s = 0
    for i in range(n):
        s += a[i]
        temp = s - m
        while temp >= 0:
            if temp in seen:
                return "Yes"
            temp -= m
        seen.add(s)
    return "No"

if __name__ == "__main__":
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        sys.exit(0)
    n = int(data[0])
    m = int(data[1])
    a = list(map(int, data[2:2+n]))
    print(solve(n, m, a))
