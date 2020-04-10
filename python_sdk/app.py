# coding: utf8
import datetime
import random 
import string 
import time 
from pymongo import MongoClient

def main():
  #client = MongoClient('mongodb://siteRootAdmin:password@192.168.0.102', 27017)
  client = MongoClient('mongodb://192.168.0.102', 27017, retryWrites=False)
  db = client.db_sharding
  collection = db.users
  post = {"name": ''.join(random.sample(string.ascii_letters + string.digits, 8)),
           "age": random.randint(1,120),
           "create_at" : time.time()}
  # 增加
  post_id = collection.insert_one(post).inserted_id
  print(post_id)

  # 删除 
  myquery = { "age" : { "$lt" : 88.0 }}
  result = collection.delete_many(myquery)
  print("del count:%d", result.deleted_count)

  # 查询
  posts = collection.find();
  for post in posts:
    print(post)
if __name__ == '__main__':
  main()
