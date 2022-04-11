a=[[1,3,5,7], [8, 10, 2], [2,3,4,1]]

for i in range(len(a)):
    arr = []
    for j in a[i]:
        if j % 2 != 0:
            arr.append(j)
    if arr == a[i]:
        a[i] = a[-1]
        a[-1] = arr

print(a)