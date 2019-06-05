shangpin = [("book",1000),("pen",500),("huawei",2000)]
gongzi = input("输入工资：")
if gongzi.isdigit():
    gongzi = int(gongzi)
gouwuche = []
while True:
    for index,i in enumerate(shangpin):
        print(index,i)
    bianhao = input("输入产品编号:")
    if bianhao.isdigit():
        bianhao = int(bianhao)
        if bianhao < len(shangpin) and bianhao >=0:
            shangpinhao = shangpin[bianhao]
            if shangpinhao[1] <= gongzi:
                gouwuche.append(shangpinhao)
                gongzi -= shangpinhao[1]
                print("您购买的 %s 已经购买完成您还剩%s块钱" %(shangpinhao[0],gongzi))
            else:
                print("\033[41;1m您的余额只剩%s啦，还买你妈逼啊\033[0m"%(gongzi))
        else:
            print("您输入的商品号码不存在")
    elif bianhao == 'q':
        print("-------------购物表------------")
        for p in gouwuche:
            print(p[0])
        print("感谢您的购物您的余额为：",gongzi)
        exit()
    else:
        print("输入错误")