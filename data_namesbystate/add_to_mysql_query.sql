CREATE DATABASE  IF NOT EXISTS `babynames` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `babynames`;

CREATE TABLE `frequency` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `state` char(2) DEFAULT NULL,
  `gender` char(1) DEFAULT NULL,
  `year` int(4) DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  `count` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
)

LOAD DATA LOCAL INFILE 'D:/Documents/Coding Dojo/CodingDojo_Python/python_project/data_namesbystate/XX.txt'
	INTO TABLE frequency
    FIELDS TERMINATED BY ','
	LINES TERMINATED BY '\r\n'
	(state,gender,year,name,count)
    set id=null;