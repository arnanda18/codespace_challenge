def solution(s):
    if not s:  
        return ""
    parts = []
    current_part = s[0]
    
    for char in s[1:]:
        if char.isupper() != current_part[-1:].isupper():
            parts.append(current_part)
            current_part = char
        else:
            current_part += char
    
    parts.append(current_part)
    return ' '.join(parts)


print(solution("camelCAseTurbo"))