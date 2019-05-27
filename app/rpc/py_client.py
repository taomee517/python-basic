# -*- coding:utf-8 -*-
from generated.PersonService import Client
from generated.ttypes import *

__author__ = 'taomee'

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol

try:
    tSocket = TSocket.TSocket("localhost", 8899)
    tSocket.setTimeout(900)

    transport = TTransport.TFramedTransport(tSocket)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    client = Client(protocol)

    transport.open()

    person = client.getPersonByUsername("张三")

    print(person.username)
    print(person.age)
    print(person.married)

    print('---------------------')

    newPerson = Person()
    newPerson.username = "李四"
    newPerson.age = 30
    newPerson.married = True

    client.savePerson(newPerson)

    transport.close()

except Thrift.TException as tx:
    print('%s' % tx.message)
