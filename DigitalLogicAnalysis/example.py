from Inputs.max_terms import MaxTerms

a = MaxTerms(2)
print(a)
a.set_terms([0, 2])
print(a)
# a.set_decimal_positions([0, '2'])
# a.set_decimal_positions([0, 2, 6, 7])
a.set_terms([0, 0, 0, 0, 0])
print(a)
