# def get_len_of_str(s):
#     a = ''
#     b = []
#     c = 0
#     for i in s:
#         if i in a:
#             a = ''
#         a = a + i
#         b.append(a)
#     for i in b:
#         if len(i) > c:
#             c = len(i)
#     return c

   def get_len_of_str(s):
        count = 0
    ls = []
    for x in s:
        if x not in ls:
            ls.append(x)
        else:
            count = max(count, len(ls))
            ls = [x]
    return max(count, len(ls))
