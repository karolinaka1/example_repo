def trojkat(bok_a, bok_b, bok_c, h_a):
    pole = bok_a * h_a / 2
    obwod = bok_a + bok_b + bok_c
    return pole, obwod


print(f'Pole i obwód trójkąta wynoszą: {trojkat(10, 15, 12, 8)}')

def prostokat(a_p, b_p ):
    pole_p =  a_p* b_p
    obwod_p = 2 * a_p + 2 * b_p
    return pole_p, obwod_p

print(f'Pole i obwod prostokata wynoszą:{prostokat(6,7)}')

def romb(a_r, h_r):
    pole_r = a_r * h_r
    obwod_r = 4 * a_r
    return pole_r, obwod_r

print(f'Pole i obwód romoba wynoszą:{romb(5,4)}')
