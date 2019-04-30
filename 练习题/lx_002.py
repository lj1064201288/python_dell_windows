import random, string
import pymysql

forselect = string.ascii_letters + '1234567890'

def generate(count, lenght):
    '''
    :param count: 激活码的个数
    :param lenght: 激活码的长度
    :return: 激活码
    '''
    for i in range(count):
        code = ''
        for j in range(lenght):
            code += random.choice(forselect)
        yield code

def Mysql(codes):
    db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='codes')
    cursor = db.cursor()
    try:
        for code in codes:
            print(code)
            sql = 'insert into code (code) values (%s)'
            cursor.execute(sql, (code))
            db.commit()
            print("插入成功")
    except Exception as e:
        db.rollback()
        print('插入失败', e.args)
    finally:
        db.close()

if __name__ == '__main__':
    code = generate(200, 20)
    Mysql(code)
