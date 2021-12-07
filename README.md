# clien_rss

A brief introduction:
    RSS build code for the Korean community site 'Clien'


Environment:
    python 3.6.2
    MariaDB10 on synology dsm 6.1.3,
    
Additional python module:    
    MySQL Connector for Python 2.1.6,
    RyRSS2Gen,
    BeautifulSoup from BS4

[web-site](https://slowlifecoding.blogspot.com/2017/08/build-clien-rss-by-python3.html)  


### mysql install  
```shell
sudo apt-get update
sudo apt-get install mysql-server
```
  
### mysql setting  
```shell
sudo ufw allow mysql
sudo systemctl start mysql
sudo systemctl enable mysql
```

### mysql make DB and Tables  
exampe) TEST_DB
```shell
sudo /usr/bin/mysql -u root -p

mysql> SELECT User, Host, authentication_string FROM mysql.user;

mysql> CREATE DATABASE TEST_DB;
mysql> SHOW DATABASES;

mysql> CREATE USER testuser@localhost IDENTIFIED BY 'password';
mysql> FLUSH PRIVILEGES;
mysql> SELECT User, Host, authentication_string FROM mysql.user;

mysql> GRANT ALL PRIVILEGES ON TEST_DB.* to testuser@localhost;
mysql> FLUSH PRIVILEGES;
mysql> SHOW GRANTS FOR testuser@localhost;

mysql> SET PASSWORD FOR testuser@localhost = PASSWORD('password');

mysql> use TEST_DB;
```
mysql> [CREATE TABLE rss](MySQL_CREATE_TABLE.sql)
