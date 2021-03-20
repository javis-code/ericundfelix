import time

start_time = round(time.time())

i = 0

print("Starting addition benchmark...")

while i < 25000:
    print("Iteration {}".format(i))
    i += 1

add_bm_time_one = round(time.time())

i = 0

while i < 25000:
    print("Iteration {}".format(i))
    i += 1

add_bm_time_two = round(time.time())

score = round(((add_bm_time_one - start_time) +
               (add_bm_time_two - add_bm_time_one)) / 2)

print(score)
