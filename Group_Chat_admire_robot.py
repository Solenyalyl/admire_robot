# -*- coding: UTF-8 -*-
'''
Group Chat Robot
'''

import itchat, re
from itchat.content import *
import random
import json

'''
Corpus
'''
REPLY = {
    '工作': ['且不说你的工作多么认真，我并没有见过，但是从你的字里行间，我发现了乔布斯和小扎的影子！', '你拥有了这个年龄段近半数人无法拥有的理想职业，太优秀了！', '工作这件事，大家都习以为常，只有你让大家开始思考这个问题，说明你善于反思和质疑当前的制度，你的公司会因为你这样的人变得更好！'],
    '学习': ['这么多优秀的人相聚在这里，一定是场思想交流的盛宴', '看到群友们的发言，真是排山倒海，气宇轩昂之势！', '你这句话完美的表达了你想被夸的坚定信念，你一定是一个执着追求自己理想的人！'],
    '妈': ['老妈是世界上最棒的母亲', '老妈每天为家里忙里忙外幸苦了', '老妈每天照顾植物，真细心'],
    '爸': ['这么魁梧的身材，这么潇洒的外表！', '老爸每天在外工作幸苦了', '老爸每天脚踏实地，勤勤恳恳为家里做贡献', '老爸真是太牛逼了', '老爸是一个有责任、有担当的男人!'],
    '歌': ['老妹的歌声简直就是天籁之音'],
    '男朋友': ['你那么可爱肯定会有一个很好很好的人在等你！'],
    '妹': ['你就是我们的小天使', '你就是一个积极向上的正能量仙女', '瀑布一般的长发，淡雅的连衣裙，标准的瓜子脸，聪明的杏仁眼，那稳重端庄的气质，再调皮的人见了你都会小心翼翼','你从小就流露出这样才华横溢的天资', '你的美丽怎能用简单的漂亮二字来形容，你真的是沉鱼落雁 闭月羞花 倾国倾城', '这世间怎么会有这么好看的人']
    'default': ['太棒了', '你真聪明!','你很有想象力哦!','真不错', '一看你就是智慧与善良的化身', '你这么优秀，和你在一起的时候压力好大啊!','德才兼备说的就是你这样的社会主义接班人！', '太可爱了', '你真是太牛逼了','你就是闪闪发光啊','好开心', '你真是太优秀了', '搞得不错', '你太有洞察力了，睿智过人啊', '你真的太有魅力了', '一看你就是大富大贵的人', '老爸长得像吴彦祖，老妈长得像赵雅芝，老妹长得像迪丽热巴', '你如此聪明伶俐，精明能干', '在同龄人中，你的能力真是出类拔萃', '你真幽默，话从你口中说出来就是不一样', '你的思维太活跃了，我根本就跟不上', '今天又是进步的一天啊']
}
@itchat.msg_register([TEXT], isGroupChat=True)
def text_reply(msg):

    group_name = '一家人'
    if msg['User']['NickName'] == group_name:
        print('Message from: %s' %msg['User']['NickName'])
        
        username = msg['ActualNickName']#sender nick name
        print('Who sent it: %s' %username)
        
        match = re.search('妈', msg['Text'])
        if match:
            print('-+-+' * 5)
            print('Message content:%s' % msg['Content'])
            randomIdx = random.randint(0, len(REPLY['妈']) - 1)
            itchat.send('%s\n%s' % (username, REPLY['妈'][randomIdx]), msg['FromUserName'])
            print(REPLY['妈'][randomIdx])

         match = re.search('爸', msg['Text'])
        if match:
            print('-+-+' * 5)
            print('Message content:%s' % msg['Content'])
            randomIdx = random.randint(0, len(REPLY['爸']) - 1)
            itchat.send('%s\n%s' % (username, REPLY['爸'][randomIdx]), msg['FromUserName'])
            print(REPLY['爸'][randomIdx])


        match = re.search('歌', msg['Text'])
        if match:
            print('-+-+' * 5)
            print('Message content:%s' % msg['Content'])
            randomIdx = random.randint(0, len(REPLY['歌']) - 1)
            itchat.send('%s\n%s' % (username, REPLY['歌'][randomIdx]), msg['FromUserName'])
            print(REPLY['歌'][randomIdx])

        match = re.search('男朋友', msg['Text'])
        if match:
            print('-+-+' * 5)
            print('Message content:%s' % msg['Content'])
            randomIdx = random.randint(0, len(REPLY['男朋友']) - 1)
            itchat.send('%s\n%s' % (username, REPLY['男朋友'][randomIdx]), msg['FromUserName'])
            print(REPLY['男朋友'][randomIdx])

        match = re.search('妹', msg['Text'])
        if match:
            print('-+-+' * 5)
            print('Message content:%s' % msg['Content'])
            randomIdx = random.randint(0, len(REPLY['妹']) - 1)
            itchat.send('%s\n%s' % (username, REPLY['妹'][randomIdx]), msg['FromUserName'])
            print(REPLY['妹'][randomIdx])

        match = re.search('工作', msg['Text']) or re.search('加班', msg['Text'])
        if match:
            print('-+-+' * 5)
            print('Message content:%s' % msg['Content'])
            print('工作、加班 is: %s' % (match is not None))
            randomIdx = random.randint(0, len(REPLY['工作']) - 1)
            itchat.send('%s\n%s' % (username, REPLY['工作'][randomIdx]), msg['FromUserName'])
            print(REPLY['工作'][randomIdx])

        match = re.search('学习', msg['Text']) or re.search('考试', msg['Text'])
        if match:
            print('-+-+' * 5)
            print('Message content:%s' % msg['Content'])
            print('学习、考试 is: %s' % (match is not None))
            randomIdx = random.randint(0, len(REPLY['学习']) - 1)
            itchat.send('%s\n%s' % (username, REPLY['学习'][randomIdx]), msg['FromUserName'])
        else:
            randomIdx = random.randint(0, len(REPLY['default']) - 1)
            itchat.send('%s\n%s' % (username, REPLY['default'][randomIdx]), msg['FromUserName'])
            print('-+-+'*5)

itchat.auto_login(enableCmdQR=2, hotReload=True)#login
itchat.run()#run and stay online

