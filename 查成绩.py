# -- coding:utf-8 --
import hashlib
import requests
import json
_author = 'GJZ'

class Query_Scores:

    def __init__(self, user_id, pwd):
        self.user_id = user_id
        self.pwd = pwd
        self.session = requests.Session()
        self.headers = {
            "User-Agent": "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15",
            "Origin": "https://uims.jlu.edu.cn",
            "Host": "uims.jlu.edu.cn",
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

    def Show_scores(self):
        service_url = "http://uims.jlu.edu.cn/ntms/service/res.do"
        post_data = {
 			"tag": "archiveScore@queryCourseScore",
 			"branch": "latest",
 			"params": {},
			 "rowLimit": "100"
		}

        self.headers["Content-Type"]="application/json"
        response = self.session.post(service_url, headers=self.headers, data=json.dumps(post_data))
        back_datas = json.loads(response.content.decode("utf-8"))
        print("\n\n"+back_datas["value"][0]["student"]["name"]+"\n\n")
        for value in back_datas["value"]:
            print(value["teachingTerm"]["termName"]+"\t\t", value["score"]+"\t\t", value["credit"]+"\t\t", value["gpoint"]+"\t\t",value["course"]["courName"])
        


if __name__ == "__main__":
    user_id = input("请输入账号:")
    pwd = input("请输入密码:")
    program = Query_Scores(user_id, pwd)
    program.Login()
    program.Show_scores()
    a = input()
