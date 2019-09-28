# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 13:19:41 2019

@author: gurjaspal
"""

#https://realpython.com/python-csv/
import csv
import os

class Database:
    
    def __init__(self):
        self.db_path = "database.csv"
        
        try:
            os.remove(self.db_path)
        except OSError:
            print('error')
            pass
        self.file = open(self.db_path, "a+")
#        self.file_reader = open(self.db_path, "r")
        fieldnames = ['key', 'value', 'size']

        self.writer = csv.DictWriter(self.file, fieldnames=fieldnames)
        self.writer.writeheader()
        print("DB initialized")
#        self.reader = csv.DictReader(self.file)
            
    def set_value(self, key, value, size):
        self.writer.writerow({'key':key, 'value': value, 'size': size})
        
        
#    def get_value(self, key):
#        print(list(self.reader))
#        for row in reversed(list(self.reader)):
#            print("row", row)
#            if row['key'] == key:
#                return row['value']
            
#        return data[key]

if __name__ == "__main__":
    d = Database()
    d.set_value("height","100","1024")
    d.set_value("height","1003","1024")
    print(d.get_value("height"))
    d.file.close()
#    d.file_reader.close()