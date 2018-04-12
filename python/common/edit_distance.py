# coding: utf-8
__author__ = 'lapis-hong'
__date__ = '2017/8/18'

s1 = 'today is sunday'
s2 = 'today is saturday'


def normal_leven(str1, str2):
    len_str1 = len(str1) + 1
    len_str2 = len(str2) + 1
    # create matrix
    matrix = [0 for n in range(len_str1 * len_str2)]
    # init x axis
    for i in range(len_str1):
        matrix[i] = i
    # init y axis
    for j in range(0, len(matrix), len_str1):
        if j % len_str1 == 0:
            matrix[j] = j // len_str1

    for i in range(1, len_str1):
        for j in range(1, len_str2):
            if str1[i - 1] == str2[j - 1]:
                cost = 0
            else:
                cost = 1
            matrix[j * len_str1 + i] = min(matrix[(j - 1) * len_str1 + i] + 1,
                                           matrix[j * len_str1 + (i - 1)] + 1,
                                           matrix[(j - 1) * len_str1 + (i - 1)] + cost)

    return matrix[-1]


if __name__ == '__main__':
    dis = normal_leven(s1, s2)
    print(dis)
