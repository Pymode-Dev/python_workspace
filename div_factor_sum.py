def div_factor(last_number):
    div = []
    for i in range(1, last_number):
        if i % 3 == 0 or i % 5 == 0:
            div += [i]

    adding = 0
    for i in div:
        adding += i
    print(adding)


div_factor(100)
