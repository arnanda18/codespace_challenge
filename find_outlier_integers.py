def find_outlier(integers):
    odds = [n for n in integers if n%2!=0]
    evens = [n for n in integers if n%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]

print(find_outlier([2,4,6,8,10,3]))