from collections import defaultdict, Counter

arr1 = [[8, 13], [8, 14], [8, 15], [8, 16], [8, 17], [9, 11], [9, 12], [9, 13], [9, 14], [9, 15], [9, 16], [9, 17], [9, 18], [10, 10], [10, 11], [10, 12], [10, 13], [10, 17], [10, 18], [11, 9], [11, 10], [11, 11], [11, 17], [11, 18], [12, 8], [12, 9], [12, 10], [
    12, 16], [12, 17], [13, 7], [13, 8], [13, 9], [13, 16], [14, 7], [14, 8], [14, 15], [15, 7], [15, 8], [15, 13], [15, 14], [16, 8], [16, 9], [16, 10], [16, 11], [16, 12], [16, 13], [16, 14], [16, 15], [17, 14], [17, 15], [17, 16], [18, 15], [18, 16], [19, 15], [19, 16]]


def grp_values(arr):
    d_dict = defaultdict(list)
    for k, v in arr:
        d_dict[k].append(v)
    return d_dict


print(grp_values(arr1))

arr2 = ['1 2 50', '1 7 70', '1 3 20', '2 2 17']


def user2(arr):
    l_users = [x.split()[:2] for x in arr]
    keys = Counter()

    for users in l_users:
        if users[0] != users[1]:
            matches = Counter(user for user in users)
        else:
            matches = Counter(users[0])
        keys += matches

    return [k for k, v in keys.items() if v >= 2]


print(user2(arr2))


def count_user(arr):
    l_users = [x.split()[:2] for x in arr]
    matches = []
    result = defaultdict(int)
    for users in l_users:
        if users[0] != users[1]:
            for user in users:
                matches.append(user)
        else:
            matches.append(users[0])
    for i in matches:
        result[i] += 1

    return [k for k, v in result.items() if v >= 2]


print(count_user(arr2))
