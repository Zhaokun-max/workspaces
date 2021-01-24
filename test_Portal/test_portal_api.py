import requests
import json
import unittest
import warnings
from test_partal_data.ProjectData import Publish_Data
from test_partal_data.getHeaders import Get_headers
from test_partal_data.ProjectData import bu
import os
headers = Get_headers().getheaders
data = Publish_Data().building_001()

url='http://test.portal.jlncjy.cacfintech.com/api/v1.0/chanquan/project/save'

class Requests:
    def request(self,url, method='get', **kwargs):
        if method=='get':
            return requests.request(url=url, method=method, **kwargs)
        elif method=='post':
            return requests.request(url=url, method=method, **kwargs)

    def get(self, url, **kwargs):
        return self.request(url=url, method='get', **kwargs)

    def post(self, url, **kwargs):
        return self.request(url=url, method='post', **kwargs)


#获取id
class ApiTest(unittest.TestCase):
    def setUp(self):
        self.obj=Requests()
        warnings.simplefilter('ignore', ResourceWarning)
    #@pytest.fixture()
    def get(self,ID):
        with open('ID', "w") as f:
            f.write(str(ID))
    #获取id
    @property
    def read(self):
        with open('ID', 'r') as f:
            return f.read()
    #发布编辑项目信息
    def test_publish_001(self):
        r=self.obj.post(url=url,
                        json=data,
                        headers=headers)
        print(r.json())
        if r.json()['code']==None or r.json()['data']==None or r.json()['data']==999:
            self.assertEqual(r.json()['code'],str(0))
        else:
            self.get(r.json()['data'])


    #发布编辑受让信息
    def test_publish_002(self):
        data_02 = Publish_Data().building_002()
        r = self.obj.post(
            url='http://test.portal.jlncjy.cacfintech.com/api/v1.0/chanquan/project/saveAssignmentConditionsInfo',
            json=data_02,
            headers=headers)
        self.assertEqual(r.json()['code'],str(0))
        self.assertEqual(r.json()['data'],int(self.read))
    # 上传图片
    def test_publish_003(self):
        cookies=Get_headers().getheaders_002()
        data = Publish_Data().building_003()
        headers = cookies
        url='http://test.portal.jlncjy.cacfintech.com/api/v1.0/chanquan/fast/uploadFile'
        files = {"file": ("123.jpg", open(r'C:\Users\Administrator\Desktop\123.jpg', 'rb'), "image/jpeg")}
        for i in range(10):
            r = self.obj.post(url=url, files=files, headers=headers,json=data)
            if r.json()['code']==None or r.json()['data']==None or r.json()['data']==999:
                self.assertEqual(r.json()['code'], str(0))
            else:
                self.save_photo(r.json()['data']['fullPath'])
    #保存图片地址
    #@property
    def save_photo(self,photo):
        with open('photo', 'a') as f:
            f.write(str(photo)+'\n')
    # 发布上传附件信息
    def test_publish_004(self):
        L=bu().building_004()
        json=L
        url = 'http://test.portal.jlncjy.cacfintech.com/api/v1.0/chanquan/project/uploadFile'
        r = self.obj.post(url=url,json=json,headers=headers)
        if r.json()['code'] == None or r.json()['data'] == None or r.json()['data'] == 999:
            self.assertEqual(r.json()['code'], str(0))
#确认承诺函
    def test_publish_005(self):
        data=bu().building_005()
        r=self.obj.post(
            url='http://test.portal.jlncjy.cacfintech.com/api/v1.0/chanquan/project/savePromiseHit',
            json=data,
            headers=headers
        )
        self.assertEqual(r.json()['code'], str(0))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromModule('test_portal_api.py')
    unittest.TextTestRunner(verbosity=2).run(suite)