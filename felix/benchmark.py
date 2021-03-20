import time

start_time = round(time.time())

i = 0

print("Starting addition benchmark...")

while i < 10000:
    print("Iteration {}".format(i))
    i += 1

add_bm_time_one = round(time.time())

i = 0

while i < 10000:
    print("Iteration {}".format(i))
    i += 1

add_bm_time_two = round(time.time())

i = 0

# TB => Time Benchmark // IT => Iteration

while i < 10000:
    print("TB {} -- IT {}".format(time.time(), i))
    i += 1

add_bm_time_three = round(time.time())

i = 0

while i < 10000:
    print("TB {} -- IT {}".format(time.time(), i))
    i += 1

add_bm_time_four = round(time.time())

score = round(((add_bm_time_one - start_time) +
               (add_bm_time_two - add_bm_time_one) +
               (add_bm_time_three - add_bm_time_two) +
               (add_bm_time_four - add_bm_time_three)) / 4)

print("Final Score: {}".format(score))
