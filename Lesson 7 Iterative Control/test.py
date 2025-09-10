# # # while
# # i=1
# # while i<=10:
# #     print(f"2*{i}={2*i}")
# #     if (i==5):
# #         continue
# #     i=i+1 # terminate the loop at some point
# # print("Loop ka control khatam")

# i = 1
# while i <= 10:
#     if i == 6:
#         i += 1
#         continue
#     print(f"2*{i}={2*i}")
#     i += 1  # increment i to terminate the loop at some point
# print("Loop ka control khatam")

r=range(2,10,2)
print(r,type(r),sep="\n")
for num in r :
    print(num,end=',')