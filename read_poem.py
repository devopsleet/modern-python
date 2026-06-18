jabber = open('jabberwocky.txt', 'r')


for line in jabber:
    print(line.strip(), end='')
    # print(len(line))


jabber.close()
