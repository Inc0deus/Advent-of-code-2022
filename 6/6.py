# Advent of Code 2022 - Day 6

# ================ part I ================
"""
"""

t,r=open('i.txt').readlines()[0],4
while r<len(t):
 l,v=t[r-4:r],0
 for i in range(3): v|=l[i]in l[i+1:]
 r+=v
 if not v:break

print(f"part I: {r}")

# ================ part II ================
"""
"""

t,r=open('i.txt').readlines()[0],14
while r<len(t):
 l,v=t[r-14:r],0
 for i in range(13): v|=l[i]in l[i+1:]
 r+=v
 if not v:break

print(f"part II: {r}")

