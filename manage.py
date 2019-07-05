from crawler import crawler
import jieba
import itchat
import argparse

WARNING_REPLY = """
该消息涉嫌严重剧透，现已屏蔽！
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
远离剧透，世界和平
"""

WARNING_KEYWORDS = []

def check_msg(msg):
    keyword_list = jieba.cut(msg)

    for word in keyword_list:
        if word in WARNING_KEYWORDS:
            return True
    return False


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    from_friend = itchat.search_friends(userName=msg["FromUserName"])["NickName"]
    print(from_friend)
    if check_msg(msg["Text"]):
        print(f"WARNING! 这条消息涉嫌剧透,现已自动屏蔽 FROM：{from_friend}")
        return WARNING_REPLY

def detect(name):
    print('运行了？')
    spider = crawler.DouBan(name)
    keys = jieba.cut(spider.fetch())
    return keys

def main():
    __usage__ = '防剧透机器人'
    parser = argparse.ArgumentParser(description=__usage__)
    parser.add_argument('name')
    args = parser.parse_args()

    WARNING_KEYWORDS.append(args.name)
    keys = detect(args.name)
    WARNING_KEYWORDS.extend(keys)

    print(WARNING_KEYWORDS)

    itchat.auto_login(hotReload=True)
    itchat.run()



if __name__ == "__main__":
    main()



