# -- coding:utf-8 --
import hashlib
import requests
import json
_author = 'GJZ'


class Query_Course:

    def __init__(self, user_id, pwd):
        self.user_id = user_id
        self.pwd = pwd
        self.session = requests.Session()
        self.headers = {
            "User-Agent": "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15",
            "Origin": "https://uims.jlu.edu.cn",
            "Host": "uims.jlu.edu.cn",
        }
        self.post_data = {
        	"tag": "teachClassStud@schedule",
        	"branch": "default",
        	"params": {}
        }


    def Login(self):
        self.pwd = "UIMS" + self.user_id + self.pwd
        m = hashlib.md5()
        m.update(bytes(self.pwd, encoding="utf-8"))
        self.pwd = m.hexdigest()
        login_url = "https://uims.jlu.edu.cn/ntms/j_spring_security_check"
        self.headers["Referer"] = "https://uims.jlu.edu.cn/ntms/userLogin.jsp?reason=nologin"
        data = {
            "j_username": self.user_id,
            "j_password": self.pwd,
            "mousePath": "aGAABSCQAWRDgAfPGAAxOJABANNQBRNSABiMXAByMcQCDMhwCUMnQClMswC1MyADGM3gDWM9ADnYOADI",
        }
        self.session.header = self.headers
        res = self.session.post(url=login_url, data=data)

    def Get_Message(self, time):
        service_url = "https://uims.jlu.edu.cn/ntms/action/getCurrentUserInfo.do"
        self.headers["Content-Type"] = "Capplication/x-www-form-urlencoded"
        response = self.session.post(service_url, headers=self.headers)
        back_datas = json.loads(response.content.decode("utf-8"))
        self.post_data["params"]["studId"] = back_datas['userId']
        if time==0:self.post_data["params"]["termId"] = back_datas['defRes']['term_s']
        elif time==1:self.post_data["params"]["termId"] = int(back_datas['defRes']['term_s'])+1
        print("\n\n"+back_datas["nickName"]+'\n\n')
    
    
    def Get_Courses(self):
        service_url = "http://uims.jlu.edu.cn/ntms/service/res.do"
        self.headers["Content-Type"] = "application/json"
        response = self.session.post(url=service_url, data=json.dumps(self.post_data), headers=self.headers)
        data = json.loads(response.content.decode("utf-8"))
        data = data["value"]
        if data == []:
            print("教务处尚未排出课表!")
            return None
        for course in data:
            print("*"*50)
            print("\n"+course["teachClassMaster"]["lessonSegment"]["lesson"]["courseInfo"]["courName"])
            for i in course["teachClassMaster"]["lessonSchedules"]:
                print(i['classroom']['fullName'], i['timeBlock']['name'])
            print()
        
        
if __name__ == "__main__":
    user_id = input("请输入账号:")
    pwd = input("请输入密码:")
    program = Query_Course(user_id, pwd)
    program.Login()
    program.Get_Message(1)  # 0为当前学期课表，1为下学期课表
    program.Get_Courses()
    a = input()
