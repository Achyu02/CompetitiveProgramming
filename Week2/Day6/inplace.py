import random
def shuffle(the_list):

    # Shuffle the input in place
    n=len(the_list)
    for i in range(n-1,0,-1):
        j = random.randint(0,i)
        the_list[i],the_list[j] = the_list[j],the_list[i]
    return the_list


sample_list = [1, 2, 3, 4, 5]
print('Sample list:', sample_list)

print('Shuffling sample list...')
shuffle(sample_list)
print(sample_list)