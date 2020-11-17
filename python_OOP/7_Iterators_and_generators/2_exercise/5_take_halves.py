def solution():
    def integers():
        num = 1
        while True:
            yield num
            num += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        my_list = []
        for num in seq:
            if len(my_list) == n:
                return my_list
            my_list.append(num)

    return take, halves, integers
