-- create students table to work with

create type emp_gender as enum ('male', 'female');

CREATE TABLE Students (
    id INT PRIMARY KEY,
    name VARCHAR(30),
    salary money,
    logintime timestamp,
    absent boolean,
    gender emp_gender,
    born_date DATE,
    subject VARCHAR(30),
    score INT,
    max_score INT,
    track_name VARCHAR(30)
);

-- optional
ALTER Students ADD CONSTRAINT LastName varchar(30);

-- 7. insert new data to all tables

INSERT INTO Students (id, name, salary, logintime, absent, gender, born_date, subject, score, max_score, track_name) VALUES
(1, 'John Doe', 10000, '2023-07-29 12:00:00', false, 'male', '1970-01-01', 'Math', 90, 100, 'Data Science'),
(2, 'Jane Doe', 20000, now() , true, 'female', '1985-01-01', 'English', 80, 100, 'Business'),
(3, 'Peter Smith', 30000, now(), false, 'male', '2000-01-01', 'Science', 70, 100, 'Engineering'),
(4, 'Mary Jones', 40000, '2023-07-29 15:00:00', true, 'female', '1995-01-01', 'History', 60, 100, 'Arts'),
(5, 'David Brown', 50000, now(), false, 'male', '1990-01-01', 'Computer Science', 50, 100, 'Computer Science');


-- 8. Display all students’ information.

SELECT * FROM Students;

-- 9. Display male students only.

SELECT * FROM Students WHERE gender = 'male';

-- 10. Display the number of female students.

SELECT COUNT(*) FROM Students WHERE gender = 'female';

-- 11. Display the students who are born before 1992-10-01.

SELECT * FROM Students WHERE born_date < '1992-10-01';

-- 12. Display male students who are born before 1991-10-01.

SELECT * FROM Students WHERE gender = 'male' AND born_date < '1991-10-01';

-- 13. Display subjects and their max score sorted by max score.

SELECT subject, max_score FROM Students ORDER BY max_score DESC;

-- 14. Display the subject with highest max score

SELECT subject, max_score FROM Students ORDER BY max_score DESC LIMIT 1;

-- 15. Display students’ names that begin with A.

SELECT * FROM Students WHERE name LIKE 'A%';

-- 16. Display the number of students’ their name is “Mohammed”

SELECT COUNT(*) FROM Students WHERE name = 'Mohammed';

-- 17. Display the number of males and females.

SELECT gender, COUNT(*) AS count FROM Students GROUP BY gender;

-- 18. Display the repeated first names and their counts if higher than 2.

SELECT name, COUNT(*) AS count FROM Students GROUP BY name HAVING COUNT(*) > 2;

-- 19. Display the all Students and track name that belong to it.

SELECT name, track_name FROM Students;

--- 20. (Bouns) Display students’ names, their score and subject name.

SELECT name, score, subject FROM Students;