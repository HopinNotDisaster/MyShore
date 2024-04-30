# import requests
# import re
# import pymysql

# url = "https://pic.netbian.com/new/"
# res = requests.get(url)
# res = res.content.decode("GBK")
# # print(res)
#
# categorys = re.findall(r'<a href="/.*?/" title="(.*?)图片">.*?</a>', res, re.S)
# # print(categorys)
# categorys = categorys[:12]
# print(categorys)
#
# con = pymysql.connect(host="192.168.11.16",port=3308,user="zh",password="123456",database="shore_db")
# cur = con.cursor()
#
#
# cur.execute("delete from main_category")
# con.commit()
#
# cur.executemany("insert into main_category (title) values (%s)", categorys)
#
# con.commit()
# cur.close()
# con.close()
#


