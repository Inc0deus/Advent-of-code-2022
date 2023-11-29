# Advent of Code 2022 - Day 3

# ================ part I ================
"""
96 = ord('a')-1
38 = ord('A')-27
"""

t,s,a,b=open('i.txt').readlines(),0,96,38
for l in t:
 l=l.strip();n=len(l)//2
 for c in l[:n]:
  if c in l[n:]:s+=ord(c)-(a if c.islower()else b);break

print(f"part I: {s}")

# ================ part II ================
"""
"""

t,s,a,b=open('i.txt').readlines(),0,96,38
for i in range(0,len(t),3):
 for c in t[i]:
  if c in t[i+1] and c in t[i+2]:s+=ord(c)-(a if c.islower()else b);break

print(f"part II: {s}")
