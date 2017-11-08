"""
回复“功能”时的处理，查询订阅号功能参数
"""
def replyFunction(to_user, receiveData):
    # 下面两行用于初始化，请保留
    yield None
    msg_content, is_replay = yield None  # 获得用户的消息内容

    msg = "本订阅号功能参数为：\n" \
          "回复以下数字进入相应的对话模式:\n" \
          "【0】 查看详细功能参数；\n" \
          "【1】 未来5天天气预报查询；\n" \
          "【2】 区域站雨量信息查询，仅支持湖北地区\n" \
          "【3】 与机器人（ZM助手）聊天模式；\n" \
          "【9】 处于某会话模式时，用于退出当前模式；\n\n" \
          "备注：\n(1)继续支持“地区+天气”以及“县/区+年月日时+雨量”进行天气和雨量查询;\n"\
          "(2)可回复人物图片，智能识别人物性别与年龄（仅供娱乐）;\n" \
          "(3)处于机器人聊天模式时可直接发送语音进行聊天！\n\n"\
          "功能持续开发中...."
    return ('TextMsg', msg)  # 如果没有后续会话就return，return格式(<MsgType>, <内容>)
