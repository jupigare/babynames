1. Run MAMP and MySQL Workbench

2. In Workbench, create a database (schema) and table

  CREATE DATABASE  IF NOT EXISTS `babynames` /*!40100 DEFAULT CHARACTER SET latin1 */;
  USE `babynames`;

  CREATE TABLE `frequency` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `gender` char(1) DEFAULT NULL,
    `count` int(11) DEFAULT NULL,
    `year` int(4) DEFAULT NULL,
    `state` char(2) DEFAULT NULL,
    `name` varchar(45) DEFAULT NULL,
    PRIMARY KEY (`id`)
  )

3. Still in Workbench, run this query, changing the URL to wherever your file is (and change the table name, columns, etc.)
LOAD DATA LOCAL INFILE 'D:/Documents/Coding Dojo/CodingDojo_Python/python_project/data_namesbystate/XX.txt'
	INTO TABLE frequency
  FIELDS TERMINATED BY ','
	LINES TERMINATED BY '\r\n'
	(state,gender,year,name,count)
  set id=null;

4. DO a Data Export (making a dumpfile.sql), send to everyone else on your team

5. EVERYONE on the team needs their settings.py file to have this:

  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'babynames',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
  }

6. EVERYONE in their Terminal run these commands:
  > python manage.py inspectdb
  > python manage.py inspectdb > apps/APPNAMEHERE/models.py