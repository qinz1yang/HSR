import random
import configparser
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
config = configparser.ConfigParser()
config.read("config.ini")

def ener_defense(ener_lv):
    return 200+10*ener_lv

def defen(my_lv, ener_lv,jianfang):
    return (20 + my_lv) / ((20 + ener_lv) * (1 - jianfang) + 20 + my_lv)

def jianshang(js):
    tmp = 1
    while js:
        tmp *= (1-js[len(js)-1])
        js  = js[:(len(js)-1)]
    return tmp

def huineng(dangqian,jichu, huinengxiaolv, guding):
    return dangqian + jichu*(1 + huinengxiaolv) + guding

def yishang(ys, gj):
    return min((1 + ys + gj), 3.5)

def baoji(bjsh):
    return (1+ bjsh/100)

def xingdongzhi(sudu_jichu, sudu_tigao, sudu_jiangdi, sudu_jiacheng):
    sudu_buff = sudu_jichu*(1+sudu_tigao-sudu_jiangdi)+sudu_jiacheng
    return 10000/sudu_buff

def jiposhanghai(jipo_jishu, renxing_xishu, my_lv, ener_lv, jianfang):
    return jipo_jishu*renxing_xishu*defen(my_lv, ener_lv,jianfang)
     
def zongxingdongzhi(huiheshu):
    return (huiheshu-1)*100 + 150
#攻击力，技能倍率， 增伤， 暴击伤害， 韧性条减伤， 我的等级，对面等级， 抗性
def shanghai_baoji(gj, jinengbeilv, zs, bjsh, rx, my_lv, ener_lv, jianfang, kx):
    return int((gj * jinengbeilv * (1+zs/100) * baoji(bjsh) * rx * defen(my_lv, ener_lv, jianfang) * kx))
def shanghai_bubao(gj, jinengbeilv, zs, bjsh, rx, my_lv, ener_lv, jianfang, kx):
    return int((gj * jinengbeilv * (1+zs/100) * rx * defen(my_lv, ener_lv, jianfang) * kx))

def chixu_shanghai(gj, jinengbeilv, zs, bjsh, rx, my_lv, ener_lv, jianfang, kx, cengshu):
    return shanghai_bubao(gj, jinengbeilv, zs, bjsh, rx, my_lv, ener_lv, jianfang, kx)*cengshu

def kangxing(jiankang):
    return (1+jiankang/100)


gj = float(config.get("XIER", "juese_gongjili"))
jinengbeilv = float(config.get("XIER", "jinengbeilv"))/100
dazhaobeilv = float(config.get("XIER", "dazhaobeilv"))/100
zs = float(config.get("XIER", "changzhuzengshang"))
huiheshu=float(config.get("XIER", "huiheshu"))
xdz_zong = zongxingdongzhi(huiheshu)
sudu_jichu = float(config.get("XIER", "juese_jichusudu"))
sudu_jiacheng = float(config.get("XIER", "sudujiacheng"))
my_lv = float(config.get("XIER", "my_lv"))
ener_lv = float(config.get("XIER", "ener_lv"))
bjl = float(config.get("XIER", "baojilv"))
bjsh = float(config.get("XIER", "bjsh"))
jianfang = float(config.get("XIER", "jianfang"))/100
jiankang = float(config.get("XIER", "jiankang"))
kx = kangxing(jiankang)
huinengxiaolv = float(config.get("XIER", "huinengxiaolv"))/100



data_xier = []
data = []
i = 0
monicishu = 100


while i < monicishu:
    jineng_jiasu = 0
    xingdongcishu = 0
    zongshang = 0
    nengliang = 0
    xdz_zong = zongxingdongzhi(huiheshu)
    while xdz_zong > 0:
        if (jineng_jiasu >= 2):
            jineng_jiasu = 2
        xdz_jichu = xingdongzhi(sudu_jichu, jineng_jiasu*0.25, 0, sudu_jiacheng)

        if (xingdongcishu <= 1):
            if (random.randint(0,100) <= bjl):
                zongshang += shanghai_baoji(gj, jinengbeilv, zs, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)
                print("1本轮暴击伤害:" + str(shanghai_baoji(gj, jinengbeilv, zs, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)))
            else:
                zongshang += shanghai_bubao(gj, jinengbeilv, zs, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)
                print("1本轮普通伤害:" + str(shanghai_bubao(gj, jinengbeilv, zs, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)))
        else:
            if (random.randint(0,100) <= bjl):
                zongshang += shanghai_baoji(gj, jinengbeilv, zs + 148, bjsh, 0.9, my_lv, ener_lv, jianfang, kangxing(20))
                print("2本轮暴击伤害:" + str(shanghai_baoji(gj, jinengbeilv, zs, bjsh, 0.9, my_lv, ener_lv, jianfang, kangxing(20))))
            else:
                zongshang += shanghai_bubao(gj, jinengbeilv, zs + 148, bjsh, 0.9, my_lv, ener_lv, jianfang, kangxing(20))
                print("2本轮普通伤害:" + str(shanghai_bubao(gj, jinengbeilv, zs, bjsh, 0.9, my_lv, ener_lv, jianfang, kangxing(20))))

        jineng_jiasu += 1

        if (xingdongcishu >= 2):
            if (random.randint(0,100) <= bjl):
                zongshang += int(0.15*shanghai_baoji(gj, jinengbeilv, zs, bjsh, 0.9, my_lv, ener_lv, jianfang, kangxing(20)))
                print("印记暴击伤害:" + str(int(0.15*shanghai_baoji(gj, dazhaobeilv, zs + 148, bjsh + 120, 0.9, my_lv, ener_lv, jianfang, kangxing(20)))))
            else:
                zongshang += int(0.15*shanghai_bubao(gj, jinengbeilv, zs, bjsh, 0.9, my_lv, ener_lv, jianfang, kangxing(20)))
                print("印记普通伤害:" + str(int(0.15*shanghai_bubao(gj, dazhaobeilv, zs + 148, bjsh + 120, 0.9, my_lv, ener_lv, jianfang, kangxing(20)))))
        #计算希儿六命印记伤害

        nengliang = huineng(nengliang, 30, huinengxiaolv, 0)

        if (xingdongcishu <= 1): 
            #专武增伤计算
            if (nengliang >=  120):
                if (random.randint(0,100) <= bjl):
                    zongshang += shanghai_baoji(gj, jinengbeilv, zs + 40 + 15, bjsh + 80, 0.9, my_lv, ener_lv, jianfang, kx)
                    print("1大招暴击伤害:" + str(shanghai_baoji(gj, dazhaobeilv, zs, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)))
                else:
                    zongshang += shanghai_bubao(gj, jinengbeilv, zs + 40 + 15, bjsh + 80, 0.9, my_lv, ener_lv, jianfang, kx)
                    print("1大招普通伤害:" + str(shanghai_bubao(gj, dazhaobeilv, zs, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)))
                nengliang = 0
                huineng(nengliang, 5, huinengxiaolv, 0)
        else:
            if (nengliang >=  120):
                if (random.randint(0,100) <= bjl):
                    zongshang += shanghai_baoji(gj, jinengbeilv, zs + 88 + 15, bjsh + 120, 0.9, my_lv, ener_lv, jianfang, kangxing(20))
                    print("2大招暴击伤害:" + str(shanghai_baoji(gj, dazhaobeilv, zs, bjsh, 0.9, my_lv, ener_lv, jianfang, kangxing(20))))    
                else:
                    zongshang += shanghai_bubao(gj, jinengbeilv, zs + 88 + 15, bjsh + 120, 0.9, my_lv, ener_lv, jianfang, kangxing(20))
                    print("2大招普通伤害:" + str(shanghai_bubao(gj, dazhaobeilv, zs, bjsh, 0.9, my_lv, ener_lv, jianfang, kangxing(20))))
                nengliang = 0
                huineng(nengliang, 5, huinengxiaolv, 0)
        
        xdz_buff = xdz_jichu
        xdz_zong -= xdz_buff
        xingdongcishu+=1
    data_xier.append(zongshang)
    i+=1

mean_normal_xier = np.mean(data_xier)
std_normal_xier = np.std(data_xier)    

i = 0

gj = float(config.get("SHUXING", "juese_gongjili"))
jinengbeilv = float(config.get("SHUXING", "jinengbeilv"))/100
dazhaobeilv = float(config.get("SHUXING", "dazhaobeilv"))/100
zs = float(config.get("SHUXING", "changzhuzengshang"))
huiheshu=float(config.get("SHUXING", "huiheshu"))
xdz_zong = zongxingdongzhi(huiheshu)
sudu_jichu = float(config.get("SHUXING", "juese_jichusudu"))
sudu_jiacheng = float(config.get("SHUXING", "sudujiacheng"))
my_lv = float(config.get("SHUXING", "my_lv"))
ener_lv = float(config.get("SHUXING", "ener_lv"))
bjl = float(config.get("SHUXING", "baojilv"))
bjsh = float(config.get("SHUXING", "bjsh"))
jianfang = float(config.get("SHUXING", "jianfang"))/100
jiankang = float(config.get("SHUXING", "jiankang"))
kx = kangxing(jiankang)
huinengxiaolv = float(config.get("SHUXING", "huinengxiaolv"))/100

while i < monicishu:
    zongshang = 0
    nengliang = 0
    xdz_zong = zongxingdongzhi(huiheshu)
    if(config.get("JUESE", "xuanze") == "yinlang"):
        while xdz_zong > 0:
            xdz_jichu = xingdongzhi(sudu_jichu, 0, 0, sudu_jiacheng)
            if (random.randint(0,100) <= bjl):
                zongshang += shanghai_baoji(gj, jinengbeilv, zs, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)
                print("本轮暴击伤害:" + str(shanghai_baoji(gj, jinengbeilv, zs, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)))
            else:
                zongshang += shanghai_bubao(gj, jinengbeilv, zs, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)
                print("本轮普通伤害:" + str(shanghai_bubao(gj, jinengbeilv, zs, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)))
            xdz_buff = xdz_jichu
            xdz_zong -= xdz_buff

    elif(config.get("JUESE", "xuanze") == "kafuka"):
        zongshang = 0
        chudian = 0
        yousi = 0
        xingdongcishu = 0
        while xdz_zong > 0:
            if (xingdongcishu >= 3):
                xingdongcishu = 3
            xdz_jichu = xingdongzhi(sudu_jichu, 0.08*xingdongcishu, 0, sudu_jiacheng)
            if (chudian == 0):
                if (random.randint(0,100) <= bjl):
                    zongshang += shanghai_baoji(gj, jinengbeilv, zs, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)
                    print("1本轮暴击伤害:" + str(shanghai_baoji(gj, jinengbeilv, zs, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)))
                    if (yousi):
                        zongshang += 0.78 * shanghai_bubao(gj, 0.6, zs + 156, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)
                    yousi = 1
                else:
                    zongshang += shanghai_bubao(gj, jinengbeilv, zs, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)
                    print("1本轮普通伤害:" + str(shanghai_bubao(gj, jinengbeilv, zs, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)))
                    if (yousi):
                        zongshang += 0.78 * shanghai_bubao(gj, 0.6, zs + 156, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)
                    yousi = 1
            else:
                if (random.randint(0,100) <= bjl):
                    zongshang += shanghai_baoji(gj, jinengbeilv, zs + 156, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)
                    print("2本轮暴击伤害:" + str(shanghai_baoji(gj, jinengbeilv, zs + 156, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)))
                    zongshang += 0.78 * shanghai_bubao(gj, 3.1828, zs + 156, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)
                    print("本轮触发触电:" + str(0.78 * shanghai_bubao(gj, 3.1828, zs + 156, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)))
                    if (yousi):
                        zongshang += 0.78 * shanghai_bubao(gj, 0.6, zs + 156, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)
                    yousi = 1
                else:
                    zongshang += shanghai_bubao(gj, jinengbeilv, zs + 156, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)
                    print("2本轮普通伤害:" + str(shanghai_bubao(gj, 3.1828, zs + 156, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)))
                    zongshang += 0.78 * shanghai_bubao(gj, 3.1828, zs + 156 + 25, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)
                    print("本轮触发触电:" + str(0.78 * shanghai_bubao(gj, 3.1828, zs + 156 + 25, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)))
                    if (yousi):
                        zongshang += 0.78 * shanghai_bubao(gj, 0.6, zs + 156, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)
                    yousi = 1
            xingdongcishu += 1
            nengliang = huineng(nengliang, 30, huinengxiaolv, 0)

            if (chudian == 0): 
                #dot区分
                if (nengliang >=  120):
                    if (random.randint(0,100) <= bjl):
                        zongshang += shanghai_baoji(gj, jinengbeilv, zs, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)
                        print("1大招暴击伤害:" + str(shanghai_baoji(gj, dazhaobeilv, zs, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)))
                        if (yousi):
                            zongshang += 0.78 * shanghai_bubao(gj, 0.6, zs + 156, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)
                    else:
                        zongshang += shanghai_bubao(gj, jinengbeilv, zs, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)
                        print("1大招普通伤害:" + str(shanghai_bubao(gj, dazhaobeilv, zs, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)))
                        if (yousi):
                            zongshang += 0.78 * shanghai_bubao(gj, 0.6, zs + 156, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)
                    nengliang = 0
                    huineng(nengliang, 5, huinengxiaolv, 0)
                    chudian = 1
            else:
                if (nengliang >=  120):
                    if (random.randint(0,100) <= bjl):
                        zongshang += shanghai_baoji(gj, jinengbeilv, zs + 156, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)
                        print("2大招暴击伤害:" + str(shanghai_baoji(gj, dazhaobeilv, zs + 156, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)))
                        zongshang += 1.04 * shanghai_bubao(gj, 3.1828, zs + 156, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)
                        print("大招触发触电:" + str(1.04 * shanghai_bubao(gj, 3.1828, zs + 156 + 25, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)))
                        if (yousi):
                            zongshang += 0.78 * shanghai_bubao(gj, 0.6, zs + 156, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)    
                    else:
                        zongshang += shanghai_bubao(gj, jinengbeilv, zs + 156, bjsh + 120, 0.9, my_lv, ener_lv, jianfang, kx)
                        print("2大招普通伤害:" + str(shanghai_bubao(gj, dazhaobeilv, zs + 156, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)))
                        zongshang += 1.04 * shanghai_bubao(gj, 3.1828, zs + 156 + 25, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)
                        print("大招触发触电:" + str(1.04 * shanghai_bubao(gj, 3.1828, zs + 156 + 25, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)))
                        if (yousi):
                            zongshang += 0.78 * shanghai_bubao(gj, 0.6, zs + 156, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)
                    nengliang = 0
                    huineng(nengliang, 5, huinengxiaolv, 0)
                    chudian = 1
            xdz_buff = xdz_jichu
            xdz_zong -= xdz_buff
            nengliang = huineng(nengliang, 0, huinengxiaolv, 2)
        zongshang += huiheshu * shanghai_bubao(gj, 3.1828, zs + 25, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)
    i += 1
    print(zongshang)
    data.append(zongshang)
    

# print("xingdongcishu:" + str(xingdongcishu))

# print("技能暴击伤害:" + str(shanghai_baoji(gj, jinengbeilv, zs, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)))
# print("技能普通伤害:" + str(shanghai_bubao(gj, jinengbeilv, zs, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)))
# print("大招暴击伤害:" + str(shanghai_baoji(gj, dazhaobeilv, zs, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)))
# print("大招普通伤害:" + str(shanghai_bubao(gj, dazhaobeilv, zs, bjsh, 0.9, my_lv, ener_lv, jianfang, kx)))

fig1= plt.figure(figsize=(15,12))
mean_normal = np.mean(data)
std_normal = np.std(data)
print("mu = " + str(mean_normal))
print("sigma = " + str(std_normal))

space_xier = np.linspace(mean_normal_xier - 3*std_normal_xier, mean_normal_xier + 3*std_normal_xier, 100)
plt.plot(space_xier, stats.norm.pdf(space_xier, mean_normal_xier, std_normal_xier), label='xier', color = 'purple')

space = np.linspace(mean_normal - 3*std_normal, mean_normal + 3*std_normal, 100)
plt.plot(space, stats.norm.pdf(space, mean_normal, std_normal), label=config.get("JUESE", "xuanze"))

plt.text(mean_normal_xier, 0, r'xier: mu = ' +  str(mean_normal_xier))
plt.axvline(mean_normal_xier, color="red")

plt.text(mean_normal, 0, r'mu = ' +  str(mean_normal))
plt.axvline(mean_normal, color="red")
plt.title("1mubiao\n" + config.get("JUESE", "xuanze") + ":gongjili=" + config.get("SHUXING", "juese_gongjili") + " jinengbeilv=" + config.get("SHUXING", "jinengbeilv") +" dazhaobeilv=" + config.get("SHUXING", "dazhaobeilv") + "\n changzhuzengshang=" + config.get("SHUXING", "changzhuzengshang") +" huiheshu="+ config.get("SHUXING", "huiheshu") + " baojilv=" + config.get("SHUXING", "baojilv") + " baojishanghai=" + config.get("SHUXING", "bjsh") + "\n my_lv=" + config.get("SHUXING", "my_lv") + " ener_lv=" + config.get("SHUXING", "ener_lv") + "\n sudu_jichu=" + config.get("SHUXING", "juese_jichusudu") + " sudu_jiacheng=" + config.get("SHUXING", "sudujiacheng") + "\n jianfang=" + config.get("SHUXING", "jianfang") + " jiankang=" + config.get("SHUXING", "jiankang") + " huinengxiaolv=" + config.get("SHUXING", "huinengxiaolv"))

# plt.hist(data)
plt.legend()
plt.savefig(fname = 'res.png')
plt.show()

