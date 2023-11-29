# Advent of Code 2022 - Day 2

# ord('A') = 65
# ord('X') = 88


# ================ part I ================
"""
variable 's' to store the score,
for each instruction there are 2 computations to do:
    1) add the score of the shape 
    2) add the score of the outcome

for 1), just add the score by checking for equalities ('X'=rock -> +1, 'Y'=paper -> +2, 'Z'=scissors -> +3):
    (x=='X') + 2*(x=='Y') + 3*(x=='Z')
where x is the input value

for 2) I noticed that we can get the outcome score by using the arithmetic expression:
    (a-x+1)%3 * 3
where a and x are in {0:rock,1:paper,2:scissors} (this can be obtained by substracting ord('A') or ord('X') from the ord of the input)
which gives in code : (ord(l[2])-88 - ord(l[0])+65 + 1)%3 * 3
or simplified       : (ord(l[2])-ord(l[0])-22)%3*3
"""

t,s=open('i.txt').readlines(),0
for l in t:n=l[2];s+=(n=='X')+2*(n=='Y')+3*(n=='Z')+(ord(n)-ord(l[0])-22)%3*3

print(f"part I: {s}")

# ================ part II ================
"""
similarly,

for 2) I noticed that we can get the score of the shape by using the arithmetic expression:
    (a+x-1)%3 + 1
where a and x are in {0:rock,1:paper,2:scissors}
which gives in code : (ord(l[0])-65 + ord(l[2])-88 - 1)%3 + 1
or simplified       : (ord(l[0])+ord(l[2])-154)%3+1

for 2) the value of the letter can be used to retrieve the score:
    3*x
where x is in {0:loose,1:draw,2:win}
"""

t,s=open('i.txt').readlines(),0
for l in t:m,n=ord(l[0]),ord(l[2]);s+=(m+n-154)%3+1+3*(n-88)

print(f"part II: {s}")

