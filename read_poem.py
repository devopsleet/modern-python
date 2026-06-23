# # open the file with a read mode
# jabber = open('jabberwocky.txt', 'r')
#
# for line in jabber:
#
#     line.strip()
#     print(line.rstrip())
#     #print(len(line))
# #
# # jabber.close()
#
# with open('jabberwocky.txt', 'r') as jabber:
#
#     lines = jabber.readlines()
# #
# # print(lines)
# # print(lines[-1:])
# for line in reversed(lines):
#     print(line)
#     # for line in jabber:
#     #     print(line.strip())

with open('Jabberwocky.txt') as jabber:
    text = jabber.read()

print(text)
