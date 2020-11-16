BEGIN TRANSACTION;
CREATE TABLE users(id INTEGER PRIMARY KEY, username TEXT, email TEXT, regdate TEXT);
INSERT INTO "users" VALUES(1,'joy','danny5336@naver.com','2020년 10월 25일 20시 15분 10초');
INSERT INTO "users" VALUES(2,'amamov','danny5336@naver.com','2020년 10월 25일 20시 15분 10초');
INSERT INTO "users" VALUES(3,'yoon','ysangsuk78@gmail.com','2020년 10월 25일 20시 15분 10초');
INSERT INTO "users" VALUES(4,'sang','ysangsuk78@gmail.com','2020년 10월 25일 20시 15분 10초');
INSERT INTO "users" VALUES(5,'wow','danny5336@gmail.com','2020년 10월 25일 20시 15분 10초');
COMMIT;
