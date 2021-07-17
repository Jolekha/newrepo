# split in half

def split_in_half(text):
    length = len(text)
    split = length // 2
    add = 0
    if length % 2:
        add =1
        st = text[:split+ add]
        nd = text[split+ add:]
        return nd +st
print('orginal string = bbbbbcaaaaa')
print(split_in_half('bbbbbcaaaaa'))