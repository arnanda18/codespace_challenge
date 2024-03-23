def likes(names):
    if len(names) == 1:
        return ' and '.join(names) + ' likes this'
    if len(names) == 2:
        return ' and '.join(names) + ' like this'
    if len(names) == 3:
        return ', '.join(names[:2]) + f' and {names[2]} like this'
    if len(names) > 2:
        return ', '.join(names[:2]) + f' and {len(names) - 2} others like this'
    else:
        return "no one likes this"
    
# ALTERNATIF SOLUTION
    # n = len(names)
    # return {
    #     0: 'no one likes this',
    #     1: '{} likes this', 
    #     2: '{} and {} like this', 
    #     3: '{}, {} and {} like this', 
    #     4: '{}, {} and {others} others like this'
    # }[min(4, n)].format(*names[:3], others=n-2)
       
            
print(likes(['Jacob']))
print(likes(['Jacob', 'Alex']))
print(likes(['Jacob', 'Alex', 'Maven']))
print(likes(['Jacob', 'Alex', 'Rendra', 'Rafael']))