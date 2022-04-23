import nba_01
import collect_nba_player_goals


print("——————————欢迎来到nba数据爬取工具————————")
print("作者github主页：https://github.com/ojcsdream/")
while True:
    choice = input("输入1：爬取nba排名数据\n输入2：爬取nba球员得分排名")
    if choice in ["1", "2"]:
        if choice == "1":
            nba_01.main()
            break
        else:
            collect_nba_player_goals.main()
            break

    else:
        print("输入错误，请输入1或2")

print("欢迎下次使用，其他功能还为完善，敬请期待")