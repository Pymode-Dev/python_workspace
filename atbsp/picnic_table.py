def picnic(stuff, lef, r):

    print('PICNIC ITEMS'.center(lef + r, '-'))
    for k, v in stuff.items():
        print(k.ljust(lef, '.') + str(v).rjust(r))


picnic_items = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
picnic(picnic_items, 12, 5)
