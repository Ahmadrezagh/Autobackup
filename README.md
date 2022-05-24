# Autobackup
1-download repository \n
2-create `\BackUpApp` folder
3-copy `projects.py` and `sql.py` file in `\BackUpApp` foder
4-create `\BackUpApp\sql` folder
5-create `\BackUpApp\projects` folder
6-projects must be in `\domains` folder
7-edit `db` and `ftp` details in `projects.py` and `sql.py`
8-install cron job
9-`crontab -e`
10-add `* 1 * * * /usr/bin/python3 /BackUpApp/main.py > /BackUpApp/log.txt`
11-add `* 1 * * * /usr/bin/python3 /BackUpApp/projects.py > /BackUpApp/log_projects.txt`
12-`systemctl restart cron`

