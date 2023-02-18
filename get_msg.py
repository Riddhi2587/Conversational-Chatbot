def msg(chat_file):
    with open(chat_file, "r", encoding="utf-8") as msg_file:
        content = msg_file.read()

    split_msg = tuple(content.split("\n"))
    return split_msg