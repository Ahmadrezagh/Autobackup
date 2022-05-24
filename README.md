# Autobackup
1-download repository <br> 
2-create `\BackUpApp` folder <br> 
3-copy `projects.py` and `sql.py` file in `\BackUpApp` foder <br> 
4-create `\BackUpApp\sql` folder <br> 
5-create `\BackUpApp\projects` folder <br> 
6-projects must be in `\domains` folder <br> 
7-edit `db` and `ftp` details in `projects.py` and `sql.py` <br> 
8-install cron job <br> 
9-`crontab -e` <br> 
10-add `* 1 * * * /usr/bin/python3 /BackUpApp/main.py > /BackUpApp/log.txt` <br> 
11-add `* 1 * * * /usr/bin/python3 /BackUpApp/projects.py > /BackUpApp/log_projects.txt` <br> 
12-`systemctl restart cron` <br> 

