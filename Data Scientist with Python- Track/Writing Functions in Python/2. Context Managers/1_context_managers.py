# The number of cats
# Open "alice.txt" and assign the file to "file"
with open('alice.txt') as file:
    text = file.read()

n = 0
for word in text.split():
    if word.lower() in ['cat', 'cats']:
        n += 1

print('Lewis Carroll uses the word "cat" {} times'.format(n))

# The speed of cats
image = get_image_from_instagram()

# Time how long process_with_numpy(image) takes to run
with timer():
    print('Numpy version')
    process_with_numpy(image)

# Time how long process_with_pytorch(image) takes to run
with timer():
    print('Pytorch version')
    process_with_pytorch(image)
