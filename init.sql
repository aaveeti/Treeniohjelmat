DELETE FROM levels;
DELETE FROM workout_types;

INSERT INTO levels (title) VALUES('Aloittelija');
INSERT INTO levels (title) VALUES('Keskitaso');
INSERT INTO levels (title) VALUES('Edistynyt');
INSERT INTO levels (title) VALUES('Eliitti');

INSERT INTO workout_types (title) VALUES('Lihaskasvu');
INSERT INTO workout_types (title) VALUES('Voima');
INSERT INTO workout_types (title) VALUES('Kestävyys');
INSERT INTO workout_types (title) VALUES('Huolto ja liikkuvuus');