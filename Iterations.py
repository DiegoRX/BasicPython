# counter = 0

# while counter < 10:
#     print(counter)
#     counter += 1

## Clock Like Counter
external_counter = 0
internal_counter = 0

while external_counter < 12:
    while internal_counter < 60:
        print(external_counter, internal_counter)
        internal_counter += 1

        if internal_counter >= 30:
            break
    external_counter += 1
    internal_counter = 0   

