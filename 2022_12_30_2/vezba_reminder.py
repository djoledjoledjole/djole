import time

message = input("Enter message: ")
enter_time = int(input("Enter time: "))

# for i in range(enter_time, 0, -1):
#     print("Time remaining: ", i)            # sa for petljom
#     time.sleep(1)

while enter_time > 0:
    print("Time remaining: ", enter_time)
    enter_time -= 1                           # sa while peljom
    time.sleep(1)

for x in range(10):
    print(message)