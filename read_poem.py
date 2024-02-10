# jabber = open('D:/Python/jabberwocky.txt', 'r')
#
#
# for line in jabber:
#     print(line.rstrip())
#     #print(line, end='')
#     #print(len(line))
#
# jabber.close()


# newstring = "       abcsssssabc    "
# print(newstring.lstrip(' abc'))


with open('D:/Python/jabberwocky.txt', 'r') as jabber:
    # for line in jabber:
    #     print(line.rstrip())
    lines = jabber.readlines()


print(lines)
print(lines[-1:])
for line in reversed(lines):
    print(line, end='--')
