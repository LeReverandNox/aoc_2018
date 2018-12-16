# INPUT = 51589
# INPUT = 59414
# INPUT = 92510
# INPUT = "01245"
INPUT = 165061


def find_seq_in_deque(seq, len_seq, d, len_d):
    curr_s = d[-len_seq:]
    if curr_s == seq:
        return True


def loop():
    d = [3, 7]
    n1 = 0
    n2 = 1
    input_str = [int(i) for i in str(INPUT)]
    len_input = len(input_str)

    j = 2
    while True:
        n1 = (n1 + d[n1] + 1) % j
        n2 = (n2 + d[n2] + 1) % j
        new_recipe = str(d[n1] + d[n2])

        for i in new_recipe:
            j += 1
            d.append(int(i))

            if j > len_input:
                res = find_seq_in_deque(input_str, len_input, d, j)
                if res:
                    return j - len_input


print(loop())
