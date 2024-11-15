# def f(s, lowercase=0, uppercase=0):
#     if not s:
#         return lowercase, uppercase

#     first_char = s[0]

#     if first_char.islower():
#         lowercase += 1
#     elif first_char.isupper():
#         uppercase += 1

#     return f(s[1:], lowercase, uppercase)

# input_str = input("請輸入一個字串：")
# lowercase_count, uppercase_count = f(input_str)
# print(f"小寫字母總數：{lowercase_count}")
# print(f"大寫字母總數：{uppercase_count}")

i = "1010101"
for j in range(len(i) - 2, -1, -1):
    print(j)
