def reverse_char(word):
    tmp_str = ''
    copy_str = ''
    num = []   # 3, 2, 9, 5
    num_index = []   # 8, 7, 6, 3
    for letter in range(len(word)-1, -1, -1):
        if word[letter].isalpha():
            tmp_str += word[letter]
        else:
            num.append(word[letter])
            num_index.append(letter)

    for i in range(len(num_index)-1, -1, -1):
        copy_str = tmp_str[:num_index[i]]
        tmp_str = tmp_str[num_index[i]:]
        copy_str += str(num[i])
        copy_str += tmp_str
        tmp_str = copy_str

    return copy_str


print(reverse_char('ab89c'))

# ab89c ---> cb89a   ===>> cba
# jkl5mn923o ---> onm5lk923j  ===>> onmlkj
# 123a45 ---> 123a45
