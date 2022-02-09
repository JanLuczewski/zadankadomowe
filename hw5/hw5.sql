--HW5
--Stworzyć bazę danych i tabele: uzytkownik, zamówienie i produkt. Zapisać SQLową komendę (CREATE DATABASE ... + CREATE TABLE)
--Tabela zamówienia powinna mieć relację do użytkownika i do produktu (FOREIGN KEY)
--Napisać komendy do dodania kilku przykładowych zamówień, użytkowników i produktów
CREATE DATABASE fakturki;
CREATE TABLE zamowienie (
    id int NOT NULL AUTO_INCREMENT,
    uzytkownik_id int,
    produkt_id int,
    ile int,
    PRIMARY KEY (id),
    FOREIGN KEY (uzytkownik_id) REFERENCES uzytkownik(id),
    FOREIGN KEY (produkt_id) REFERENCES produkt(id)
);
INSERT INTO zamowienie
VALUES (1, 1, 9);

CREATE TABLE uzytkownik (
    id int NOT NULL AUTO_INCREMENT,
    imie varchar(255),
    nazwisko varchar(255),
    PRIMARY KEY (id)
);
INSERT INTO uzytkownik
VALUES ('Karol','Mularski');

CREATE TABLE produkt (
    id int NOT NULL AUTO_INCREMENT,
    nazwa varchar(255),
    kategoria varchar(255),
    PRIMARY KEY (id)
);
INSERT INTO produkt
VALUES ('czekoladki','slodycze');
