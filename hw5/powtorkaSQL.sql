--Zadanie:
--tabela użytkownik (imie,nazwisko, data urodzenia, telefon)
--tabela produkt (nazwa, kategoria)
--tabela zamówienie (Foreign Key do użytkownika i produktu, ilość)



--ZAMIAST "id int NOT NULL AUTO_INCREMENT," JAK NORMALNIE JEST "id SERIAL" ,TAK WYMGA BAZA POSTGRES
CREATE TABLE produkt (
    id SERIAL,
    nazwa_produktu varchar(255),
    kategoria_produktu varchar(255),
    PRIMARY KEY (id)
);
CREATE TABLE uzytkownik (
    id SERIAL,
    imie_uzytkownika varchar(255),
    nazwisko_uzytkownika varchar(255),
    data_urodzenia date,
    numer_tel int,
    PRIMARY KEY (id)
);
CREATE TABLE zamowienie (
    id SERIAL,
    produkt_id int,
    uzytkownik_id int,
    ile_produktu int,
    PRIMARY KEY (id),
    FOREIGN KEY (uzytkownik_id) REFERENCES uzytkownik(id),
    FOREIGN KEY (produkt_id) REFERENCES produkt(id)


