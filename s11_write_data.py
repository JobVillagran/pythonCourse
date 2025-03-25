# the W means write
# The test_write file is linked to this file

with open('test_write.txt', 'r') as reader:
    content = reader.readlines()
    with open('test_write.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
