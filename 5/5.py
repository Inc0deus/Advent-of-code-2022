# Advent of Code 2022 - Day 5

# ================ part I ================
"""
"""

t,n=open('i.txt').readlines(),0
while t[n][1]!='1':n+=1
k=int(t[n][-3]);s=[[] for _ in range(k+1)]
for l in t[:n]:
 i=-1
 while i:
  i=l.find('[',i+1)+1
  if i:s[i//4+1]=[l[i]]+s[i//4+1]
for l in t[n+2:]:
 l=l.strip().split()
 for _ in range(int(l[1])):s[int(l[5])].append(s[int(l[3])].pop())
r="".join([a[-1] for a in s[1:]])
    
print(f"part I: {r}")

# ================ part II ================
"""
"""

t,n=open('i.txt').readlines(),0
while t[n][1]!='1':n+=1
k=int(t[n][-3]);s=[[] for _ in range(k+1)]
for l in t[:n]:
 i=-1
 while i:
  i=l.find('[',i+1)+1
  if i:s[i//4+1]=[l[i]]+s[i//4+1]
for l in t[n+2:]:
 l=l.strip().split();m,n=int(l[1]),int(l[3])
 s[int(l[5])]+=s[n][-m:];s[n]=s[n][:-m]
r="".join([a[-1] for a in s[1:]])

print(f"part II: {r}")

