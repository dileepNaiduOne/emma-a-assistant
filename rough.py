collection_size = int(input().strip())
collection = list(map(int, input().strip().split()))
pair_size = int(input().strip())
groups = []

for each in range(pair_size):
    a = list(map(int, input().strip().split()))
    # print(a)
    for sub_group in range(len(groups)):
        if (a[0] in groups[sub_group]):
            groups[sub_group].append(a[1])
            break
        elif a[1] in groups[sub_group]:
            groups[sub_group].append(a[0])
            break
    else:
        groups.append([a[0], a[1]])

group_collection = []
maxi = -1

not_done = list(map(str, list(range(collection_size))))
for each in groups:
    final_groups = list(set(each))

    summ = 0
    for i in final_groups:
        summ += collection[i-1]
        not_done.remove(str(i-1))

    group_collection.append(summ)
    if summ > maxi:
        maxi = summ


for i in not_done:
    if collection[int(i)] > maxi:
        maxi = collection[int(i)]

print(maxi, end="\n")


