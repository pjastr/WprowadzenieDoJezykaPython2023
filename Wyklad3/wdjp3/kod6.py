zm1 = 3.45
zm2 = 87
zm3 = "R"
zm4 = 0.000000023
zm5 = 213456355231
zm6 = "abc"

s1 = "wyr1 {}".format(zm1)
print(s1)
# s1= "wyr1b {:s}".format(zm1) - :s nie używamy do floatów
s1b = "wyr1b {!s}".format(zm1)  # przy obiektowości __str__
print(s1b)
s1c = "wyr1c {!r}".format(zm1)  # przy obiektowości __repr__
print(s1c)
s2 = "wyr2 {:c}".format(zm2)
print(s2)
s3 = "wyr2 {}".format(zm3)  # :c do str nie zadziała
print(s3)
s4 = "wyr4 {:d}".format(zm2)
print(s4)
# s5="wyr5 {:i}".format(zm2) # :i nie działa
s6 = "wyr6 {:e}".format(zm1)
print(s6)
s7 = "wyr7 {:E}".format(zm1)
print(s7)
s8 = "wyr8 {:f}".format(zm1)
print(s8)
s9 = "wyr9 {:g}".format(zm1)
print(s9)
s10 = "wyr10 {:g}".format(zm4)
print(s10)
s11 = "wyr11 {:g}".format(zm5)
print(s11)
s12 = "wyr12 {:o}".format(zm2)
print(s12)
s13 = "wyr13 {}".format(zm6)  # :s nie ma
print(s13)
s14 = "wyr14 {:x}".format(zm2)
print(s14)
s15 = "wyr15 {:X}".format(zm2)
print(s15)