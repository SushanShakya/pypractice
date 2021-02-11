# Write a Python function to insert a string in the middle of a string.
# Sample function and result :
# insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}

def insert_string_middle(main, value) -> str :
    s = list(main)
    middle = len(s) // 2
    s.insert(middle, value)
    return "".join(s)

print(insert_string_middle('[[]]', 'Python'))
print(insert_string_middle('{{}}', 'PHP'))

