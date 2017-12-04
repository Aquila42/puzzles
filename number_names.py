# Limit 9 million

number_names = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
        100: "hundred",
        1000: "thousand",
        1000000: "million"
    }


def under_100(num):
    if num == 0:
        return ""
    copy = num
    place = 1
    ans = ""
    digits = 0
    if 9 < copy % 100 < 20:
        ans = number_names[copy % 100]
        copy = copy // 100
        place = 1
        digits = 2
    while copy != 0:
        lookup = copy % 10 * place #
        place = place * 10
        copy = copy // 10
        digits = digits + 1
        if lookup in number_names:
            ans = number_names[lookup] + " " + ans
    return ans.strip()


def lexical_order_names(n):
    """
    :type n: int
    :rtype: List[int]
    """
    copy = n
    place = 1
    digits = 1
    thou_flag = 0
    and_flag = 0
    ans = ""
    lookup = 0
    while copy != 0:  # 1000
        if place < 100:
            lookup = copy % 10 * place + lookup # 3 * 100 + 21 = 321
        else:
            if place == 100:
                ans = under_100(lookup) + ans
                place = 1
            lookup = copy % 10 * place
            print(lookup, place, digits, copy)
            if digits == 3:
                if len(ans) > 0:
                    ans = "and " + ans
                if lookup in number_names:
                    ans = number_names[lookup] + " hundred " + ans
            # print("over 1000 lookup: " + str(lookup))
            elif digits > 3 and lookup in number_names:
                if thou_flag == 0:
                    thousand = "thousand "
                    thou_flag = 1
                else:
                    thousand = ""
                ans = number_names[lookup] + " " + thousand + ans
                if digits == 6:
                    place = 1
            elif digits == 7:
                ans = number_names[lookup] + " " + "million "
        digits = digits + 1
        place = place * 10
        copy = copy // 10
    if ans == "" and lookup > 0:
        ans = under_100(lookup)
    return ans


assert (under_100(1) == "one")
assert (under_100(10) == "ten")
assert(under_100(11) == "eleven")
assert(under_100(99) == "ninety nine")


# print(lexical_order_names(1))
# print(lexical_order_names(11))
# print(lexical_order_names(21))
# print(lexical_order_names(99))
# print(lexical_order_names(100))
print(lexical_order_names(119))
# print(lexical_order_names(131))
print(lexical_order_names(1000))
# print(lexical_order_names(1001))
# print(lexical_order_names(1021))
# print(lexical_order_names(4321))
# print(lexical_order_names(10000))
# print(lexical_order_names(10040))
# print(lexical_order_names(54321))
# print(lexical_order_names(654321))
# print(lexical_order_names(7654321))
