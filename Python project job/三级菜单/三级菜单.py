#-*- coding:utf-8 -*-
'''
--------------------
三级菜单
可依次选择进入各子菜单
# b 返回上一层
# q 退出
--------------------
'''
#编写者：项思凯
#英文名：kevin Xiang
China = {
    "北京":{
        "昌平":["沙河","生命科学园"],
        "海淀":["上地","西二旗"],
        "朝阳":["北京站","建国门"]
    },
    "辽宁":{
        "沈阳":["沈阳站","沈阳北"],
        "丹东":["凤凰城","通远堡"]
    },
    "黑龙江":{
        "大庆":["黑江","黑河"],
        "哈尔滨":["哈尔滨站","哈尔滨北"],
    },
}
def xsk():
    """函数解释：输出“输入错误”"""
    print("\033[31;1m输入错误\033[0m\n")

exit_flag = False
print("".rjust(30,"-"),"\n三级菜单\n按“b”返回上一级\n按“q”退出\n".ljust(53,"-"))
while not exit_flag:
    for i in China:
        print(i)

    xuanze = input("选择进入1>>：")
    if xuanze in China or xuanze == "b" or xuanze == "q":
        if xuanze == "b":
            break
        if  xuanze == "q":
            exit_flag = True
        while not exit_flag:
            for i2 in China[xuanze]:
                print("\t",i2)
            xuanze2 = input("选择进入2>>：")
            if xuanze2 in China[xuanze] or xuanze2 == "b" or xuanze2 == "q":
                if xuanze2 == "b":
                    break
                if xuanze2 == "q":
                    exit_flag = True
                while not exit_flag:
                    for i3 in China[xuanze][xuanze2]:
                        print("\t\t",i3)
                    xuanze3 = input("选择进入3>>：")
                    if xuanze3 in China[xuanze][xuanze2] or xuanze3 == "b" or xuanze3 == "q":
                        if xuanze3 == "b":
                            break
                        if xuanze3 == "q":
                            exit_flag = True
                        for i4 in "结束":
                            print("\t\t\t",i4)
                        xuanze4 = input("输入任意键返回上一层>>:")
                        if xuanze4 == "b" or xuanze4 == "q":
                            if xuanze4 == "b":
                                break
                            if xuanze4 == "q":
                                exit_flag = True
                    else:
                        xsk()
            else:
                xsk()
    else:
        xsk()