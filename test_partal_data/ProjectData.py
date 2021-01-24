from test_partal_data.ProjectName import Project_Name
import json
#from test_Portal.test_portai_api import ApiTest
# 申请参数

class Publish_Data():
    # 发布建筑物
    def building_001(self):
        Name = Project_Name().str_Name()
        #Name = Name.str_Name()
        data = {'address': "",
                'assetsInfo': '[{"massifName":"家住无","area":"100.00","price":"100000.00","certificateNo":"","originalContractor":"","address":"000","serialNumber":"00000000","bidStructure":"000000000","originalPurpose":"用提","attachmentRemark":"撒大声地"}]',
                'bondRatio': '10',
                'circulationType': "",
                'circulationTypeCode': "",
                'city': "2203",
                'commonOwnershipDesc': "",
                'county': "220322",
                'creditCode': "",
                'deliveryPeriod': "10",
                'endTime': "2021-01-29",
                'everyYearSumPrice': "100000.00",
                'forestOwner': "",
                'forestUser': "",
                'installmentDesc': "",
                'isSublet': False,
                'landCategory': "",
                'leaseDeposit': "10",
                'managementSubject': "",
                'managementSubjectCode': "1",
                'payDay': "100",
                'payType': "1",
                'projectName': "四平市梨树县蔡家镇蔡家村{}".format(Name),
                'projectNameInit': "嗷嗷啊所多",
                'projectSubType': "1",
                'projectType': "6",
                'province': "22",
                'startTime': "2021-01-18",
                'sumArea': "100.00",
                'sumMargin': 100000,
                'township': "220322106",
                'tradeType': "1",
                'transferType': "1",
                'transfereeIdCard': "",
                'transfereeName': "",
                'transfereePhoneNo': "",
                'transfereeType': "1",
                'village': "220322106201"}
        return data

    def read_01(self):
        with open('ID', 'r') as f:
            return f.read()
    #第二步
    def building_002(self):

        json = {'assignmentCondition': '啊撒大声地',
                'bidType': '1',
                'increaseAmount': '1000',
                'increaseTime': '60',
                'projectId': '{}'.format(self.read_01()),
                'qualificationRestriction': '1',
                'unBidSel': '1'}
        return json
    #第三步
    def building_003(self):
        data={'bizType': '', 'width': '1024', 'height': '768', 'Content-Disposition': 'form-data'}
        return data
    #获取图片地址
    def read_photo(self):
        with open('../test_Portal/photo', 'r', encoding='utf-8') as f:
            return f.readlines()


class bu():
    def building_004(self):
        ID = Publish_Data().read_01()
        L= Publish_Data().read_photo()
       # List1=json.(L)
        List=L
        json = {"projectId": ID,
                "files": [{"imgEnumType": 1, "urls": ["{}".format(List[1])]},
                          {"imgEnumType": 12, "urls": ["{}".format(List[2])]},
                          {"imgEnumType": 3, "urls": ["{}".format(List[3])]},
                          {"imgEnumType": 4, "urls": ["{}".format(List[4])]},
                          {"imgEnumType": 13, "urls": ["{}".format(List[5])]},
                          {"imgEnumType": 15, "urls": ["{}".format(List[6])]},
                          {"imgEnumType": 16, "urls": ["{}".format(List[7])]},
                          {"imgEnumType": 17, "urls": ["{}".format(List[8])]},
                          {"imgEnumType": 10, "urls": ["{}".format(List[9])]}]}
        return json
    # 确认承诺函
    def building_005(self):
        ID=Publish_Data().read_01()
        data={'projectId': "{}".format(ID), 'promiseHit': "", 'promiseHitOther': "萨达萨达萨达是"}
        return data
