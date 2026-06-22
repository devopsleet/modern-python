# open the file with a read mode
jabber = open('jabberwocky.txt', 'r')

for line in jabber:

    line.strip()
    print(line.rstrip())
    #print(len(line))

jabber.close()
