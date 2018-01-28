
def yield_test(para):
    num = 0
    while num < para:
        a = yield num
        num += 1


for i in yield_test(5):
    yield_test(5).send('哈哈')
    print('打印为=：%s' % i)


def gen():
    i = 0
    while i < 5:
        temp = yield i
        print(temp)
        i += 1

