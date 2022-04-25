import collect_group_list
import collect_nba_player_goals
import collect_today_match


print("——————————欢迎来到nba数据爬取工具————————")
print("作者github主页：https://github.com/ojcsdream/")
while True:
    choice = input("输入1：爬取nba排名数据\n输入2：爬取nba球员得分排名\n输入3: 爬取nba当天比赛数据\n输入-1：退出程序:")
    if choice in ["1", "2", "-1"]:
        if choice == "1":
            collect_group_list.main()
            break
        elif choice == "2":
            collect_nba_player_goals.main()
            break
        elif choice == "3":
            collect_today_match.main()
        elif choice == "-1":
            break
    else:
        print("输入错误，请输入1或2")

print("欢迎下次使用，其他功能还未完善，敬请期待")