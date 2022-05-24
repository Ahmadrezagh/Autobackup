import mysql.connector
import os
from ftplib import FTP
from os import path, system

def checkIfSqlDirectoryExistOrCreate():
  if not path.exists('sql'):
    os.system('mkdir sql')


def ExportSqlToSql(db_host,db_user,db_pass,current_directory):

  mydb = mysql.connector.connect(
      host=db_host,
      user=db_user,
      password=db_pass,
  )

  mycursor = mydb.cursor()

  mycursor.execute("show databases")

  myresult = mycursor.fetchall()

  for object in myresult:
      db = object[0]
      os.system('mysqldump -u root -p'+db_pass+' '+str(db) +
                ' > '+(current_directory)+'/sql/'+db+'.sql')

def uploadSqlOnFtp(ftp_host,ftp_user,ftp_pass,current_directory):
  ftp = FTP(ftp_host)
  ftp.login(user=ftp_user, passwd=ftp_pass)


  for root, dirs, files in os.walk(current_directory+'/sql'):
      for fname in files:
          full_fname = os.path.join(root, fname)
          ftp.cwd('/backup/sql')
          ftp.storbinary('STOR ' + fname, open(full_fname, 'rb'))


current_directory = (os.path.dirname(os.path.abspath(__file__)))
db_host = "127.0.0.1"
db_user = "root"
db_pass = ""

ftp_host = '185.4.28.27'
ftp_user = 'sultimat'
ftp_pass = 'P[4Xi.Wl212Jif'

checkIfSqlDirectoryExistOrCreate()
ExportSqlToSql(db_host,db_user,db_pass,current_directory)
uploadSqlOnFtp(ftp_host,ftp_user,ftp_pass,current_directory)

print("Sql BackUp Done!!!")
