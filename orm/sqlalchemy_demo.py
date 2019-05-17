# 导入:
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()


# 定义User对象:
class User(Base):
    # 表的名称
    __tablename__='tb_user'

    '表的结构'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))


# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/db_demo')
DBSession = sessionmaker(bind=engine)


session = DBSession()
count = session.query(User).count()
result = session.query(User).filter(User.id == 12)
# 三元表达式
user = None if result is not None else result.one()
print(count)
if user is not None:
    print(user.__dict__)
session.close()
