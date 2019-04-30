import string, random

forselect = string.ascii_letters + "1234567890"
print(forselect)


def generate(count, lenght):
    '''
    :param count: 激活码的个数
    :param lenght: 激活码的长度
    :return:
    '''
    for x in range(count):
        RE = ""
        for i in range(lenght):
            RE += random.choice(forselect)
        print(RE)

if __name__ == '__main__':
    generate(200,20)



