# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 13:19:41 2019

@author: gurjaspal
"""

#https://realpython.com/python-csv/
import csv
#import os

class Database:
    
    def __init__(self):
        self.db_path = "database.csv"
        
        with open(self.db_path, "w+"):
            pass
        
        self.file = open(self.db_path, "a+")
        self.file_reader = open(self.db_path, "r")
        fieldnames = ['key', 'value', 'size']

        self.writer = csv.DictWriter(self.file, fieldnames=fieldnames)
        self.writer.writeheader()
        print("DB initialized")
        self.reader = csv.DictReader(self.file)
            
    def set_value(self, key, value, size=1024):
        print("set.value", key, value)
        self.writer.writerow({'key':key, 'value': value, 'size': size})
        self.file.flush()
        
        
    def get_value(self, key):
        for row in reversed(list(self.reader)):
            if row['key'] == key:
                return row['value'] + "\r\n"

if __name__ == "__main__":
    d = Database()
    d.set_value("height","100","1024")
    d.set_value("height","1003","1024")
#    print(d.get_value("height"))
    d.file.close()
#    d.file_reader.close()