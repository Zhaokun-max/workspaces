import pytest
import requests

# 获取书籍ID

def writebookid(bookID):
    with open('bookID', 'w') as f:
        f.write(str(bookID))

#可以定义为fix函数
#如果不使用的话，把init和del中的getbookid删除，在format里面调用函数
@pytest.fixture()
def getbookid():
    with open('bookID','r') as f:
        return f.read()


#添加书籍
@pytest.mark.dependency()
def test_addbook(getToken):
    r=requests.post(
        url='http://127.0.0.1:5000/v1/api/books',
        json= {
            "author": "无涯",
            "done": False,
            "id": 2,
            "name": "Selenium3自动化测试实战"
        },
        headers={'Authorization':'JTW {0}'.format(getToken)}
    )
    writebookid(r.json()[0]['datas']['id'])
    print('添加书籍：\n', r.json())

#删除书籍
@pytest.mark.dependency(depends=['test_addbook'])
def test_delbook(getToken,getbookid):
    r=requests.delete(
        url='http://127.0.0.1:5000/v1/api/book/{0}'.format(getbookid),
        headers={'Authorization': 'JTW {0}'.format(getToken)})
    print('删除书籍：\n', r.json())

@pytest.mark.dependency(depends=['test_addbook'])
def test_get_book(getToken,getbookid):
    r=requests.get(
        url='http://127.0.0.1:5000/v1/api/book/{0}'.format(getbookid),
        headers={'Authorization': 'JTW {0}'.format(getToken)}
    )

    print('查看书籍：\n',r.json())




