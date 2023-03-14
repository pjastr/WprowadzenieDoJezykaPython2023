zm1 = 442
zm2 = -567
zm3 = 3
print("zm1")
s1 = "wyr1_{:d}".format(zm1)
print(s1)
s2 = "wyr2_{: d}".format(zm1)
print(s2)
s3 = "wyr3_{:2d}".format(zm1)
print(s3)
s4 = "wyr4_{:7d}".format(zm1)
print(s4)
# s5= "wyr5_{:7.2d}".format(zm1) # nie działa dla int
s6 = "wyr6_{:07d}".format(zm1)
print(s6)
# s7= "wyr7_{:07.2d}".format(zm1) # nie działa dla int
s8 = "wyr8_{:<8d}".format(zm1)  ## tu trzeba usunąć minus a wstawić <
print(s8)
print("zm2")
s11 = "wyr1_{:d}".format(zm2)
print(s11)
s12 = "wyr2_{: d}".format(zm2)
print(s12)
s13 = "wyr3_{:2d}".format(zm2)
print(s13)
s14 = "wyr4_{:7d}".format(zm2)
print(s14)
# pominiete
s16 = "wyr6_{:07d}".format(zm2)
print(s16)
# pominiete
s18 = "wyr8_{:<8d}".format(zm2)  ## tu trzeba usunąć minus a wstawić <
print(s18)
print("zm3")
s21 = "wyr1_{:d}".format(zm3)
print(s21)
s22 = "wyr2_{: d}".format(zm3)
print(s22)
s23 = "wyr3_{:2d}".format(zm3)
print(s23)
s24 = "wyr4_{:7d}".format(zm3)
print(s24)
# pominiete
s26 = "wyr6_{:07d}".format(zm3)
print(s26)
# pominiete
s28 = "wyr8_{:<8d}".format(zm3)  ## tu trzeba usunąć minus a wstawić <
print(s28)
print("wyr8-%-8d" % zm3)