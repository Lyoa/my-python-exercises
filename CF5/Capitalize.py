def capitalize(s):
    # Initialize a list to store the capitalized characters
    capitalized = []
    # Capitalize the first character in the string
    capitalized.append(s[0].upper())
    
    # Iterate through the rest of the characters in the string
    for i in range(1, len(s)):
        # If the current character is a space and the character before it is not a space,
        # capitalize the current character
        if s[i-1] != ' ' and s[i] == 'i':
            capitalized.append('I')
        # If the current character is a period, exclamation point, or question mark,
        # capitalize the next non-space character
        elif s[i] in ['.', '!', '?']:
            j = i + 1
            while j < len(s) and s[j] == ' ':
                j += 1
            if j < len(s):
                capitalized.append(s[j].upper())
            else:
                capitalized.append(s[i])
        # Otherwise, just add the character to the list as is
        else:
            capitalized.append(s[i])
    
    # Join the capitalized characters and return the capitalized string
    return ''.join(capitalized)