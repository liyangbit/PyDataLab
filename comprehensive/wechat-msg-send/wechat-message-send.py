#coding=utf8
import itchat, time
import pandas as pd
 
itchat.auto_login(True)
 
friendList = itchat.get_friends(update=True)[1:]

# --------------------------start------------------------------
# step 1： 获取所有的微信好友列表，在获取完毕后，需要注释掉这段代码
# 从获得的好友列表里筛选你想发送消息的好友，同时可以将好友按照不同的分组进行设置
# 获取所有微信好友列表，这里我获取的是好友的备注名称
count_02 = 0
friends_remark = []
for friend in friendList:
    friends_remark.append(friend['RemarkName'])
    count_02 = count_02 + 1

# df_friends = pd.Series(friends_remark)
# df_friends.to_csv('friends.csv', encoding='utf_8_sig') # utf-8
print(friends_remark)
print("Total {} friends".format(count_02))
# -------------------------end---------------------------------



# --------------------------start------------------------------
# step 2: 给指定好友按不同分组发送不同的消息
# 在运行 step 1 的代码时，这里的代码需要注释

# 定义要发送的好友的范围，防止自动乱发消息
# 好友列表里，我用的是 备注名称
friend_msg_list_01 = ["lemon-zs", "lemon-zs-01"]  # 根据自己的实际情况设置好友分组
friend_msg_list_02 = ["lemon-zs-02", "lemon-zs-02" ] # 根据自己的实际情况设置好友分组


#设置不同好友分组需要发送的内容
SINCERE_WISH = u'test, 祝%s新年快乐！'  # 根据自己的实际情况设置祝福内容
msg_01 = 'test01, 祝新年快乐！！！'     # 根据自己的实际情况设置祝福内容
msg_02 = 'test02, 祝新年快乐！！！'     # 根据自己的实际情况设置祝福内容


count = 0
for friend in friendList:
    # 通过 if 条件设置，可以只针对 指定的好友发送消息
    # 也可以设置为几个分组，不同分组发送不同的消息
    # 由于我的好友一般都设置了备注名称， 即 "RemarkName"，所以我是用 备注名称来作为条件判断的
    # 主要是为了防止别错发给一些不能随便发送信息的老板或领导或其他人士
    if friend['RemarkName'] in friend_msg_list_01:
        # itchat.send( SINCERE_WISH % (friend['DisplayName'] or friend['NickName']), friend['UserName'])
        itchat.send( SINCERE_WISH % (friend['DisplayName'] or friend['NickName']), friend['UserName'])
        time.sleep(5)
        count = count + 1
    elif friend['RemarkName'] in friend_msg_list_02:
        itchat.send( msg_01, friend['UserName'])
        time.sleep(5)
        count = count + 1


print("Total {} messages have been sent.".format(count))
print("----end----")
# -------------------------end---------------------------------