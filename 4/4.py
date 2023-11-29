# Advent of Code 2022 - Day 4

# ================ part I ================
"""
"""

t,c=open('i.txt').readlines(),0
for l in t:l=l.replace(',','-').strip().split('-');m,n,o,p=int(l[0]),int(l[1]),int(l[2]),int(l[3]);c+=(m<=o and p<=n)or(o<=m and n<=p)

print(f"part I: {c}")

# ================ part II ================
"""
"""

t,c=open('i.txt').readlines(),0
for l in t:l=l.replace(',','-').strip().split('-');m,n,o,p=int(l[0]),int(l[1]),int(l[2]),int(l[3]);c+=m<=o<=n or m<=p<=n or o<=m<=p or o<=n<=p

print(f"part II: {c}")

