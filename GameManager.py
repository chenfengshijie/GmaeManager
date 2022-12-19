import time
import os
import json
from SendMail import Email
import datetime

class GameManager:
    def __init__(self,setting_files="setting.json"):
        setting_files = open(setting_files,"r")
        setting = json.load(setting_files)
        self.setting = setting
        self.email = Email(setting["Setting"]["EmailAddress"],setting["Setting"]["EmailPassword"],
        setting["Setting"]["EmailHost"])
        self.game = setting["Setting"]["Game"]
        self.time = setting['Setting']['Time']
        self.restricted_user = setting['Setting']['Time']
        # self.current_user = os.popen('echo "$USER"').read()
        self.current_user = "frozeworld"
        self.used_time = setting["User_info"][self.current_user]["Time"]
        self.password = setting["Setting"]["Password"]
        setting_files.close()

    def modify_setting(self,file_name):
        """Modify the settings file"""
        if not os.path.exists(file_name):
            raise Exception("File not found: %s" % file_name)
        if file_name.endswith(".json"):
            raise Exception("input a json file")
        
        setting = json.load(file_name)
        self.email = Email(setting["Setting"]["EmailAddress"],setting["Setting"]["EmailPassword"],
        setting["Setting"]["EmialHost"])
        self.game = setting["Setting"]["Game"]
        self.time = setting['Setting']['Time']
        self.restricted_user = setting['Setting']['Time']
        # TODO : modify_setting
        print("Setting modift successfully")

    # TODO:update time every 5 minutes
    def __update_time(self):
        """update time every 5 minutes
        """
        for game in self.game:
            cmd = "ps -ef | grep " + game # 该命令判断给定程序是否运行
            f = os.popen(cmd)
            if f.read() != "":
                self.used_time += 5 # 每隔五分钟更新
                break
        if self.used_time > self.time:
            self.__kill_game()
            # 发送邮件   
            info = "your child {} plays games for a long time, we close the game.".format(self.current_user)
            sender = self.email.email
            receiver = self.setting[self.current_user]["EmailAddress"]
            self.email.send_email(info,sender,receiver)
        
        # 禁止在晚上10点之后玩游戏
        now = datetime.datetime.now()
        flag = now.strftime("%H")
        if int(flag) > 22:
            self.__kill_game()
            # 发送邮件   
            info = "your child {} plays games after 22:00".format(self.current_user)
            sender = self.email.email
            receiver = self.setting[self.current_user]["EmailAddress"]
            self.email.send_email(info,sender,receiver)
            
            


    def __save_files(self):
        """save files
        """
        self.setting[self.current_user]["Time"] = self.used_time
        # 将游戏时间保存到文件中
        with open("setting.json","w") as f:
            json.dump(self.setting,fp=f)

    def __kill_game(self):
        """kill game after exceed time limit
        """
        # 通过命令行终止进程
        for game in self.game:
            cmd = "killall " + game
            os.system(cmd)


    def main_loop(self):
        self.modify_setting("setting.json")
        while True:
            self.__update_time()
            self.__save_files()
            time.sleep(300)

            
if __name__ == "__main__":
    test = GameManager()
    print("run GameManager")
    GameManager.main_loop()


