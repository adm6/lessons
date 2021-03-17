def upper_lower_count(txt):
    uppers = 0
    lowers = 0
    for i in txt:
        if i.isupper():
            uppers += 1
        else:
            lowers += 1
    print(f'{uppers=}')
    print(f'{lowers=}')


upper_lower_count('Bu ArAlAsh TeXts SomethING')