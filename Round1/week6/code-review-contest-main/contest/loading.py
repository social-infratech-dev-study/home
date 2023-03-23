import time

print("How many seconds?")
print(">>> ", end="")
n = int(input())

print("loding starts\n")

elapsed = 0
while elapsed < n:
    elapsed += 1
    time.sleep(1)
    print("loading... " + str(elapsed))

print("\nloading ends")
