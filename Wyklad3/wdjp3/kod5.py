zm1 = 3.45
zm2 = 87
zm3 = "R"
zm4 = 0.000000023
zm5 = 213456355231
zm6 = "abc"
# %a jako napis
print("wyr1 %a" % zm1)
# %c jako znak
print("wyr2 %c" % zm2)
print("wyr3 %c" % zm3)
# %d oraz %i dotyczą liczb całkowitych w systemie dziesiętnym
print("wyr4 %d" % zm2)
print("wyr5 %i" % zm2)
# %e oraz %E to notacja wykładnicza dla float
print("wyr6 %e" % zm1)
print("wyr7 %E" % zm1)
# %f notacja dla float z wyrównanie domyślnie do 6 miejsc po przecinku
print("wyr8 %f" % zm1)
# %g oraz %G - format łączący %e i %f w zależności od zmiennej
print("wyr9 %g" % zm1)
print("wyr10 %g" % zm4)
print("wyr11 %g" % zm5)
# %o (mała litera o) liczba całkowista w systeme ósemkowym
print("wyr12 %o" % zm2)
# %s do napisów
print("wyr13 %s" % zm6)
# %0x oraz %0X to liczba całkowita w systemie szestnastkowym (procent zero x)
print("wyr14 %x" % zm2)
print("wyr15 %X" % zm2)