DELETE FROM Levels;
DELETE FROM WorkoutTypes;

INSERT INTO Levels (title) VALUES('Aloittelija');
INSERT INTO Levels (title) VALUES('Keskitaso');
INSERT INTO Levels (title) VALUES('Edistynyt');
INSERT INTO Levels (title) VALUES('Eliitti');

INSERT INTO WorkoutTypes (title) VALUES('Lihaskasvu');
INSERT INTO WorkoutTypes (title) VALUES('Voima');
INSERT INTO WorkoutTypes (title) VALUES('Kestävyys');
INSERT INTO WorkoutTypes (title) VALUES('Huolto ja liikkuvuus');