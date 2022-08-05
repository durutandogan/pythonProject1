# # ### değişken tanımlama
# # i = 5
# # print(i)
# # print(type(i))
# #
# # i = 8
# # print(i)
# #
# # m = "abcdefg"
# # print(i)
# # print(type(i))
# #
# # i = float(i)
# # print(i)
# # print(type(i))
# #
# # i = str(i)
# # print(i)
# # print(type(i))
# #
# #
# # ### değişken değiştirme
# # a = 4
# # b = 5
# # a,b = b,a
# # print("a =", a)
# # print("b =", b)
# #
# # ### değişken değeri arttırma
# # a = 5
# # a = a + 1
# # print("a =", a)
# #
# # a += 1
# # print("a =", a)
# #
# # ### string oluşturma
# # x = "abcdefg"
# # print(type(x))
# #
# # ### string indexleme
# # x = "abcdefg"
# # print( x[0] )
# # print( x[1] )
# # print( x[3] )
# # print( x[-1] )
# #
# # ###  string parçalama
# # x = "abcdefg"
# # print( x[2:5] )
# # print( x[5:1:-1] )
# # print( x[1:6:2] )
# # print( x[::2] )
# # print( x[::-1] )
# #
# # ### string özellikleri
# # x = "abcdefg"
# # print( len(x) )
# #
# # a = "Duru"
# # a = a + "Tandoğan"
# # print(a) # nasıl yazdıracak?
# # a = a + "" + "Tandoğan"
# # print(a) # nasıl yazdıracak
# #
# # print(a*3)
# #
# # ###Listeler
# # liste = []
# # print(type(liste))
# # x = "abcdefg"
# # liste_2 = list(x)
# # print(liste_2)
# # print(type(liste_2))
# #
# # ### liste indexleme ve parçalama
# # liste = [1,2,3,4,5,6,7,8]
# # print(liste[0])
# # print(liste[-1])
# # print(liste[2:5:2])
# # print(liste[:4:-1])
# #
# # ##liste toplama
# # liste = [1,2,3]
# # liste_2 = [4,5,6]
# # liste_3 = liste + liste_2
# # print(liste_3)
# #
# # print(liste * 3) #listem değişti mi?
# # print(liste)
# # liste = liste * 3
# # print(liste)
# #
# # print(liste_2)
# # liste_2[1] = 10
# # print(liste_2)
# #
# # liste_d = [1,2, [4,5,6]]
# # print(liste_d[2][1])
#
# ###liste methodları
liste = [6, 3, 5, 7]
liste.append(4)
print(liste)
liste.pop()
print(liste)
liste.pop(liste[1])
print(liste)

print(liste.sort())

# # ###Tuple
# #
# # Tuple = (1, 2, 3, 3, 4, 5)
# # print(type(Tuple))
# #
# # print(Tuple[1])
# # print(Tuple[1:4])
# #
# # # Tuple[1] = 7
# # # print(Tuple)
# #
# # print(Tuple.count(3))
# #
# # ### setler
# # list = [1,2,3,4,5]
# # set = set(list)
# # print(set)
# #
# # set_A = {0,1,2,3,4}
# # set_B = {2,3,4,5,6,7}
# #
# # print("Union: ", set_A.union(set_B))
# # print("Intersect: ", set_A.intersection(set_B))
# #
# # print(set_A[3])
# # set_A[3] = 7
# # print(set_A)
#
# # ###dictionary
# # dict = {"key_1" : 3, "key_2": 4 ,"key_3": 5, "key_4" : 6}
# #
# # print(dict["key_1"])
# # dict["key_5"] = 7
# # print(dict)
# #
# # dict["key_3"] = 19
# # print(dict)
# #
# # dict_2 = {"key_1" : 1, "key_2": [1,2,3] ,"key_3": 2, "key_4" : 3}
# # print(dict_2["key_2"][1])
#
# ### IF/ELSE/ELIF
# if 3 > 4:
#     print("3 daha büyük")
# print("3 daha küçük")
#
#
# a = 10
# b = 20
# c = 20
# if a > b and b > c:
#     print("a b'den büyük VE b c'den büyük")
# elif a < b and b < c:
#     print("a b'den küçük VE b c'den küçük")
# else:
#     print("Koşullar sağlanmadı")
#
# ### in operatörü
# # içinde olup olmadığına bakar.
# print(5 in [1,2,3,4])
# print(2 in [1,2,3,4])


### for döngüsü
# liste = [1,2,3,4,5]
# for eleman in liste:
#     print(eleman)

# i = 0
# while i<5:
#      print(i)
###sonsuza kadar devam eder
   ### i += 1


### Range fonksiyonu
# print(range(0,20))
# print(*range(0,20))
# print(*range(0,20,2))
#
# for i in range(1,6):
#     print("1" * i)


###fonksiyonlar
table1 = [['Sam', 36, 85.95],
 ['Carol', 75, 53.65],
 ['Sam', 90, 95.37],
 ['Doug', 61, 19.8],
 ['Sam', 41, 45.22],
 ['Doug', 29, 42.98],
 ['Oliver', 61, 95.74],
 ['Carol', 32, 17.12],
 ['Tari', 27, 68.83],
 ['Tari', 81, 62.47]]

name_counter = {}
for row in table1:
    name = row[0]
    if name in name_counter.keys():
        name_counter[name] += 1
    else:
        name_counter[name] = 1
print(name_counter)   ###elime yeni tablo gelirse ne yapacağım??


def count_names_in_tables(table_to_count):
    name_counter = {}
    for row in table_to_count:
        name = row[0]
        if name in name_counter.keys():
            name_counter[name] += 1
        else:
            name_counter[name] = 1
    return name_counter

print(count_names_in_tables(table1))

table2 = [['Oliver', 12, 49.95],
 ['Tari', 76, 30.71],
 ['Carol', 98, 25.07],
 ['Carol', 24, 11.85],
 ['Carol', 34, 13.36],
 ['Kelly', 14, 34.31],
 ['Tari', 6, 86.11],
 ['Tari', 90, 29.08],
 ['Carol', 55, 45.61],
 ['Sam', 88, 97.47]]

print(count_names_in_tables(table2))