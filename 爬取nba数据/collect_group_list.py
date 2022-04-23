import requests
import re
from bs4 import BeautifulSoup
import datetime
import xlwt


def get_data(url, head):
    """获取数据"""
    response = requests.get(url, head)
    text = response.text
    soup = BeautifulSoup(text, "html.parser")
    flag = soup.find_all("table", class_="players_table")
    soup_2 = BeautifulSoup(str(flag), "html.parser")
    tr = soup_2.find_all("tr")
    east_list = []
    level_east = 1  # 获取东部赛区的数据

    for east in tr[2:17]:
        tr_list = re.findall('<td>(.*?)</td>', str(east))

        soup_obj_1 = BeautifulSoup(str(east), "html.parser")
        east_name = soup_obj_1.find('a', target="_blank").string
        num = re.findall('<span class="rank_bg">(\d+)</span>', str(east))
        if len(num) != 0:
            level_east = int(num[0])
        else:
            level_east += 1

        east_win_num = tr_list[-12]
        east_fail_num = tr_list[-11]
        east_win_may = tr_list[-10]
        east_win_cha = tr_list[-9]
        zhuchang = tr_list[-8]
        kechang = tr_list[-7]
        location = tr_list[-6]
        east_part = tr_list[-5]
        win_goal = tr_list[-4]
        fail_goal = tr_list[-3]
        full_win = tr_list[-2]
        linked_win = tr_list[-1]
        east_data = [level_east, east_name, east_win_num, east_fail_num, east_win_may, east_win_cha, zhuchang,
                     kechang, location, east_part, win_goal, fail_goal, full_win, linked_win]
        east_list.append(east_data)

    west_list = []
    level_west = 0
    for west in tr[19:34]:  # 获取西部赛区的数据
        tr_list = re.findall('<td>(.*?)</td>', str(west))

        soup_obj_1 = BeautifulSoup(str(west), "html.parser")
        west_name = soup_obj_1.find('a', target="_blank").string

        num = re.findall('<span class="rank_bg">(\d+)</span>', str(west))
        if len(num) != 0:
            level_west = int(num[0])
        else:
            level_west += 1

        west_win_num = tr_list[-12]
        west_fail_num = tr_list[-11]
        west_win_may = tr_list[-10]
        west_win_cha = tr_list[-9]
        west_zhuchang = tr_list[-8]
        west_kechang = tr_list[-7]
        west_location = tr_list[-6]
        west_part = tr_list[-5]
        west_win_goal = tr_list[-4]
        west_fail_goal = tr_list[-3]
        west_full_win = tr_list[-2]
        west_linked_win = tr_list[-1]

        west_data = [level_west, west_name, west_win_num, west_fail_num, west_win_may, west_win_cha, west_zhuchang,
                     west_kechang, west_location, west_part, west_win_goal, west_fail_goal,
                     west_full_win, west_linked_win]
        west_list.append(west_data)

    return east_list, west_list


def save(east_list, west_list, time):
    """写入xls文件"""
    col = ["排名", "队名", "胜", "负", "胜率", "胜场差", "主场", "客场", "赛区", "东部", "得分", "失分", "净胜", "连胜/负"]
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("nba3")
    for i in range(14):  # 填写标题
        sheet.write(0, i, col[i])
    sheet.write(1, 6, "东部赛区")
    a = 1
    for j in range(15):  # 填写数据
        list = east_list[j]
        for x in range(14):
            sheet.write(a + 1, x, list[x])
        a += 1

    b = 18
    sheet.write(18, 6, "西部赛区")
    for i in range(15):
        list = west_list[i]
        for x in range(14):
            sheet.write(b + 1, x, list[x])

        b += 1

    workbook.save(f"{time}NBA球队排名.xls")


def main():
    url = 'https://nba.hupu.com/standings'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'}
    print("正在爬取NBA数据中~~~")
    east_list, west_list = get_data(url, headers)

    time = datetime.date.today()
    print("正在保存数据~~~")
    save(east_list, west_list, time)
    print("xls文件保存成功，保存在本文件路径下")
    input("按任意键退出~~")


if __name__ == '__main__':
    main()
