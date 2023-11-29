# Advent of Code 2022 - Day 1

# ================ part I ================
"""
counter 'c' to store the number of calories,
if there is a separation between lines (ie. l='\n'), the maximum between the previous maximum and the counter is stored
"""

t,m,c=open('i.txt').readlines(),0,0
for l in t:
 if l=='\n':m,c=max(c,m),0
 else:c+=int(l.strip())
m=max(c,m)

print(f"part I: {m}")

# ================ part II ================
"""
counter 'c' to store the number of calories,
if there is a separation between lines (ie l='\n'), the function 'f' is called,
the function 'f' return the three maxima of {c,m,n,o} in order, assuming that m>=n>=o (ie. they are the previous maxima)
"""

t,m,n,o,c=open('i.txt').readlines(),0,0,0,0
def f(c,m,n,o):o=max(o,c);n,o=max(n,o),min(n,o);return max(m,n),min(m,n),o
for l in t:
 if l=='\n':c,m,n,o=0,*f(c,m,n,o)
 else:c+=int(l.strip())
m,n,o=f(c,m,n,o);m+=o+n

print(f"part II: {m}")
