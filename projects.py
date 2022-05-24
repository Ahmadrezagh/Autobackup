import mysql.connector
import os
from ftplib import FTP
from os import path, system

def checkIfSqlDirectoryExistOrCreate():
  if not path.exists('projects'):
    os.system('mkdir projects')

def uploadSqlOnFtp(ftp_host,ftp_user,ftp_pass,current_directory):
  ftp = FTP(ftp_host)
  ftp.login(user=ftp_user, passwd=ftp_pass)


  for directory in os.listdir('/domains'):
    full_fname = os.path.join('/domains', directory)
    zip_name = current_directory+'/projects/'+directory+'.zip'
    os.system('zip -r '+zip_name+' '+full_fname)
    ftp.cwd('/backup/projects')
    ftp.storbinary('STOR ' + directory+'.zip', open(zip_name, 'rb'))

ftp_host = '185.4.28.27'
ftp_user = 'sultimat'
ftp_pass = 'P[4Xi.Wl212Jif'


current_directory = (os.path.dirname(os.path.abspath(__file__)))
checkIfSqlDirectoryExistOrCreate()
uploadSqlOnFtp(ftp_host,ftp_user,ftp_pass,current_directory)

print("Projects BackUp Done!!!")
