def gcd(m,n):
    if m < n:
        (m, n) = (n, m)
        
    if (m%n) == 0:
        return (n)
    else:
        diff = m - n
        return (gcd(max(diff, n), min(diff, n)))
    
print(gcd(12,14))