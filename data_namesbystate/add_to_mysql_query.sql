LOAD DATA LOCAL INFILE 'D:/Documents/Coding Dojo/CodingDojo_Python/python_project/data_namesbystate/XX.txt'
	INTO TABLE frequency
    FIELDS TERMINATED BY ','
	LINES TERMINATED BY '\r\n'
	(state,gender,year,name,count)
    set id=null;