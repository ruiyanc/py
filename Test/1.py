from redis import *
import pymysql

person = {
    'id': '20120001',
    'user': 'bob',
    'age': 20
}
if __name__ == '__main__':
    try:
        # 创建Connection连接
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='xu1998', database='test')
        # 获得游标cursor对象
        cursor = conn.cursor()
        # 执行select语句
        count = cursor.execute('select * from students')
        print("查询到%d数据" % count)
        for i in range(count):
            result = cursor.fetchone()
            print(result)
        cursor.close()
        conn.close()
        sr = StrictRedis()
        # s = sr.set('str', 'to')
        # print(s)
        print(sr.keys())
        print(sr.get('name'))
        print(sr.lrange('a1', 0, -1))
    except Exception as e:
        print(e)

