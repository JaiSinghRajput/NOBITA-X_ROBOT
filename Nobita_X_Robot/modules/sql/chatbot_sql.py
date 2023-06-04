import threading

from sqlalchemy import Column, String

from Nobita_X_Robot.modules.sql import BASE, SESSION


class nobiChats(BASE):
    __tablename__ = "nobi_chats"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


nobiChats.__table__.create(checkfirst=True)
INSERTION_LOCK = threading.RLock()


def is_nobi(chat_id):
    try:
        chat = SESSION.query(nobiChats).get(str(chat_id))
        return bool(chat)
    finally:
        SESSION.close()


def set_nobi(chat_id):
    with INSERTION_LOCK:
        nobichat = SESSION.query(nobiChats).get(str(chat_id))
        if not nobichat:
            nobichat = nobiChats(str(chat_id))
        SESSION.add(nobichat)
        SESSION.commit()


def rem_nobi(chat_id):
    with INSERTION_LOCK:
        nobichat = SESSION.query(nobiChats).get(str(chat_id))
        if nobichat:
            SESSION.delete(nobichat)
        SESSION.commit()
