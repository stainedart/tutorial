from random import randint


def generaterandomlist(length):
    print 'generating list of length: %d' % length
    sample = []
    i = 0
    while i < length:
        sample.append(randint(1, 100))
        i = i + 1
    return sample


print '1'
a = generaterandomlist(randint(1, 100))
print 'list a'
a.sort()
print a
b = generaterandomlist(randint(1, 100))
print 'list b'
b.sort()
print b
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common = []
for itemA in a:
    if itemA in b and itemA not in common:
        common.append(itemA)
print 'common items'
print common
