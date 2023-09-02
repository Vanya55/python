import numexpr as ne
b = "(-5+7*8)"
c = "((2+(2+7*2) * (2*4))"



def sum_form(a):
    try:
        return ne.evaluate(a)
    except:
        return "Incorrect degeneration"
