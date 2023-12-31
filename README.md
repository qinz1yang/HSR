[list][*]更新日志
[*]简介
[*]应用
[*]已知不足
[*]下载链接
[/list]
===更新日志===
v1.00 目前仅支持6+5希儿和6+5卡夫卡

===简介===
我对小程序里笼统的期望伤害一直感到不太满意，因为这个数值并不能反映角色的强度。所以我自制了这样一个程序，通过对于数据进行模拟和统计学分析的方法，直观的反映出来角色的强度。默认情况下会进行一千次模拟，然后对数据进行正态分布拟合，当sigma越小说明该角色发挥越稳定，当mu越大说明这个角色平均下来能造成的伤害越高。一次模拟会包含10回合(10000行动值)。在config.ini中保存了角色的数据，它长这个样子：
[XIER]
juese_gongjili = 3627
jinengbeilv = 242
dazhaobeilv = 459
changzhuzengshang = 48.8
huiheshu = 10
juese_jichusudu = 115
sudujiacheng = 2
my_lv = 80
ener_lv = 72
baojilv = 96.4
bjsh = 150.4
jianfang = 20
jiankang = 0
huinengxiaolv = 100


[JUESE]
xuanze = kafuka

[SHUXING]
juese_gongjili = 4000
jinengbeilv = 176
dazhaobeilv = 86.4
changzhuzengshang = 88.8
huiheshu = 10
juese_jichusudu = 100
sudujiacheng = 2
my_lv = 80
ener_lv = 72
baojilv = 50
bjsh = 80
jianfang = 0
jiankang = 0
huinengxiaolv = 120

目前角色只能选择希儿或者卡夫卡，如果想选择希儿就把kafuka替换成xier就行。
其中SHUXINg中的内容可以进行修改，在这里我选取了攻击力4000，战技倍率176%(12级战技)，大招倍率86.4%(12级大招)，常驻增伤是48.8%雷衣和40%五精专武增伤，模拟回合数为10回合，基础速度为100，速度加成和我的希儿对齐，等级为80，暴击率为50%， 暴击伤害为80%， 能量回复速率为120的卡夫卡对战无限血的72级怪物。其中这些属性可以根据角色进行更改，这样能获得对强度的直观认知。
模拟完成后，该程序会输出一张统计图表，其中mu是可以直观参考的伤害中位数。
[img]./mon_202307/09/mqQ2s-croyK1rT3cSsg-mr.jpg[/img]
输出的图片大概长这样。

===应用===
我同时对我自己的6+5希儿和想象中的6+5卡夫卡进行了模拟，并将模拟结果整合到了一张图上。
单目标：
[img]./mon_202307/09/mqQ2s-eb3iK1tT3cSsg-mr.jpg[/img]
三目标：
[img]./mon_202307/09/mqQ2s-7rfnK26T3cSsg-mr.jpg[/img]
对于这个结果我不做评论，数据全是从某网站找的。因为这是角色单人素质检验，所以卡夫卡的天赋并没有被计算在内。还有，卡夫卡的套装效果因为我不知道也全都没有计算在内。当然，希儿的击杀再动，四命回能效果，和6命印记别人打额外伤害也无法触发。

===已知不足===
1. 仅支持希儿和卡夫卡
2. 仅支持单角色模拟，无法触发有关击杀和队友联动的技能/天赋。
3. 在用我自己的希儿进行模拟计算时，这个程序模拟的数值和实际值总有一些误差，具体这个误差并没有超过两位数，所以我认为在进行长回合、多次模拟之后，这些误差的影响应该会可以忽略。
当然我还是很希望能得到一个尽可能精确的值，如果有大佬知道误差的来源请指导我一下。
这里计算时将所有角色当成主C来处理，只要能动随便甩战技，希望反应角色的上限，跟实际结果会有略微出入。
