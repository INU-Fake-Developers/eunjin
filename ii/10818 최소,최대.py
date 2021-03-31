n=int(input())
n_list=list(map(int, input().split()))

small=n_list[0]
big=n_list[0]

for i in n_list:
            if i<small:
                small=i
            if i>big:
                big=i

print(small,big)
