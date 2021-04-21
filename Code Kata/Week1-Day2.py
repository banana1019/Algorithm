# def reverse(number):
#     x = str(number)[-1::-1]
#     if '-' in x:
#         x = -int(x[:-1])
#     return int(x)

def reverse(number):
    x = str(number)[::-1]
    if number < 0:
        x = "-" + x[:-1]
    return int(x)
