import time

# initial = time.time()
# print(initial)
#
# k = 0
# while(k<45):
#  print ("we are just testing")
#  k+=1
# print(f"while loop ran in {time.time()-initial} seconds")
#
# initial2 = time.time()
# for i in range(45):
#     print("we are just testing")
# print(f"for loop ran in {time.time()-initial2} seconds")

localtime=time.asctime(time.localtime(time.time()))
print(localtime)
