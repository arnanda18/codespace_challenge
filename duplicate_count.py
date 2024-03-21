def duplicate_count(text):

##Solution 1  
    # char_count = {}
    # duplicate = 0

    # for char in text.lower():
    #     if char in char_count:
    #         char_count[char] += 1
    #     else:
    #         char_count[char] = 1

    # for count in char_count.values():
    #     if count > 1:
    #         duplicate +=1
    # return duplicate

##Solution 2
    return len([char for char in set(text.lower()) if text.lower().count(char)>1])

print(duplicate_count("aasd dddabccccjl"))