import pymysql
pymysql.install_as_MySQLdb()
import sqlite3 as MySQLdb
import xlrd


conn = MySQLdb.connect('project.db')


cursor = conn.cursor()


stall_details_table = ("CREATE TABLE IF NOT EXISTS stall_details_table (Group_leader varchar(40) ,Phone_number int NOT NULL,member_count int, Food_Item varchar(255),Power_Points int,Stall_ID int);")


cursor.execute(stall_details_table)


#read excel_sheet


excel_sheet = xlrd.open_workbook('Food Fest project.xls')
excel_sheet
# In[7]




sheet_name = excel_sheet.sheet_names()
sheet_name


# In[9]:


for sh in range(0,len(sheet_name)):
   sheet= excel_sheet.sheet_by_index(sh)
  
   for r in range(1,sheet.nrows):
       Group_leader = sheet.cell(r,1).value


       Phone_number = sheet.cell(r,2).value


       member_count = sheet.cell(r,3).value
   
       Food_Item = sheet.cell(r,4).value
    
       Power_Points = sheet.cell(r,5).value
      
       Stall_ID = sheet.cell(r,7).value
       stall_details_value = (Group_leader,Phone_number,member_count,Food_Item,Power_Points,Stall_ID)
      
       insert_query = "INSERT INTO stall_details_table (Group_leader,Phone_number,member_count,Food_Item,Power_Points,Stall_ID) VALUES ('{}',{},{},'{}',{},{})".format(Group_leader,Phone_number,member_count,Food_Item,Power_Points,Stall_ID)
       cursor.execute(insert_query)
       conn.commit()
cursor.close()
conn.close()
