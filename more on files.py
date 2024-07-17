with open("simran.txt")as f:
    a=f.read(8)
    print(a)


f=open("simran.txt")
# # print(f.tell())
print(f.readline())
# # print(f.tell())
# f.seek(0)
# print(f.readline())
# # print(f.tell())
f.close()