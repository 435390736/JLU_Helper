# -- coding:utf-8 --
import hashlib
import requests
import json


class Query_Scores:

    def __init__(self, user_id, pwd):
        self.user_id = user_id
        self.pwd = pwd
        self.session = requests.Session()
        self.headers = {
            "User-Agent": "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15",
            "Origin": "https://uims.jlu.edu.cn",
            "Host": "cjcx.jlu.edu.cn",
        }

    def Login(self):
        self.pwd = "UIMS" + self.user_id + self.pwd
        m = hashlib.md5()
        m.update(bytes(self.pwd, encoding="utf-8"))
        self.pwd = m.hexdigest()
        login_url = "https://cjcx.jlu.edu.cn/score/action/security_check.php"
        self.headers["Referer"] = "https://cjcx.jlu.edu.cn/score/userLogin.php"
        data = {
            "j_username": self.user_id,
            "j_password": self.pwd,
        }
        self.session.post(url=login_url, data=data, headers=self.headers)

    def Get_Scores(self):
        service_url = 'https://cjcx.jlu.edu.cn/score/action/service_res.php'
        post_data = {
            'tag': 'lessonSelectResult@oldStudScore',
            'params': {
                'xh': self.user_id
            }
        }
        self.headers['Content-Type'] = 'application/json'
        self.headers['Referer'] = 'https://cjcx.jlu.edu.cn/score/action/index.php'
        res = self.session.post(url=service_url, data=json.dumps(post_data), headers=self.headers)
        data = res.content.decode('utf-8')
        data = json.loads(data)
        items = data['items']
        items.sort(key=lambda time: time['termId'], reverse=True)
        print('\n' + items[0]['studName'], items[0]['xh'] + '\n\n')
        print('课程名称\t课程绩点\t成绩\t对应绩点')
        for item in items:
            print(item['kcmc'], '\t', item['credit'], '\t', item['cj'], '\t', item['gpoint'])


def main():
    user_id = input('请输入学号:')
    pwd = input('请输入密码:')
    program = Query_Scores(user_id, pwd)
    program.Login()
    program.Get_Scores()
    input()

if __name__ == '__main__':
    main()
