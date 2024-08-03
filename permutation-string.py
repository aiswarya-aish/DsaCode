
# Enter the input string
input_string_ = 'caat'

def permutation(s):

    if len(s) == 0:
        return []
    if len(s) == 1:
        return [s]
    output=[]
    for i in range(len(s)):
        current_char = s[i]
        remaing_char = s[:i] + s[i+1:]

        for i in permutation(remaing_char):
            output.append(current_char + i)
    return output

permuation_list = list(set(permutation(input_string_)))
print(permuation_list)
