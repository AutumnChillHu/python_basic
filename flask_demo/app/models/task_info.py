# coding: utf-8
from sqlalchemy import CHAR, Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TaskInfo(Base):
    __tablename__ = 'task_info'

    id = Column(Integer, primary_key=True)
    name = Column(CHAR(1), nullable=False)
    state = Column(Integer, nullable=False, comment='0-新建；1-进行中；2-已结束；3-已删除')
