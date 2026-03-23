create table if not exists mock_data1 (
	id int,
	lab text,
	ok text
	);
INSERT INTO mock_data1 (id, lab, ok) VALUES
(1, 'Alice', 'yes'),
(2, 'Bob', 'no'),
(3, 'Charlie', 'yes'),
(4, 'Diana', 'no'),
(5, 'Eve', 'yes');


create table if not exists mock_data2 (
	id int,
	lab text,
	ok text
	);