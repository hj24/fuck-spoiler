from crawler import crawler
from utils import rules
import jieba
import jieba.analyse
import itchat
import argparse

WARNING_REPLY = """
该消息涉嫌严重剧透，现已屏蔽！
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
远离剧透，世界和平
"""

WARNING_KEYWORDS = []

def check_msg(msg, warning):
    keyword_list = jieba.cut(msg)

    final_key = set(keyword_list) - rules.symbols
    warning_set = set(warning)

    for word in final_key:
        if word in warning_set:
            return True
    return False


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):

    from_friend = itchat.search_friends(userName=msg["FromUserName"])["NickName"]

    # print(WARNING_KEYWORDS)

    if check_msg(msg["Text"], WARNING_KEYWORDS):
        print("WARNING! 这条消息涉嫌剧透,现已自动屏蔽 FROM: %s" % from_friend)
        return WARNING_REPLY

def detect(name):
    spider = crawler.DouBan(name)
    content = spider.fetch()

    core_keys = jieba.analyse.extract_tags(content, topK=20, withWeight=False, allowPOS=('n',))

    return core_keys

def _main():
    __usage__ = '防剧透机器人'

    parser = argparse.ArgumentParser(description=__usage__)
    parser.add_argument('name')
    args = parser.parse_args()

    WARNING_KEYWORDS.append(args.name)
    keys = detect(args.name)
    WARNING_KEYWORDS.extend(keys)

    itchat.auto_login(hotReload=True)
    itchat.run()