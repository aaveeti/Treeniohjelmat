# Treeniohjelmat

## Toiminnot
- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
- Käyttäjä pystyy lisäämään sovellukseen treeniohjelmia. Lisäksi käyttäjä pystyy muokkaamaan ja poistamaan lisäämiään treeniohjelmia.
- Käyttäjä näkee sovellukseen lisätyt treeniohjelmat. Käyttäjä näkee sekä itse lisäämänsä että muiden käyttäjien lisäämät treeniohjelmat.
- Käyttäjä pystyy etsimään treeniohjelmia hakusanalla. Käyttäjä pystyy hakemaan sekä itse lisäämiään että muiden käyttäjien lisäämiä treeniohjelmia.
- Sovelluksessa on käyttäjäsivut, jotka näyttävät jokaisesta käyttäjästä tilastoja ja käyttäjän lisäämät treeniohjelmat.
- Käyttäjä pystyy valitsemaan treeniohjelmalle kaksi luokittelua (kokemustaso, tavoite).
- Käyttäjä pystyy antamaan treeniohjelmalle numeroarvion (1-5) ja kommentin. Käyttäjä pystyy myös poistamaan antamansa kommentin.
## Miten sovellusta voi testata
Asenna `flask` -kirjasto:
```bash
$ pip install flask
```

Luo tietokannan taulut ja lisää alkutiedot:
```bash
$ sqlite3 database.db < schema.sql
$ sqlite3 database.db < init.sql
```

Voit käynnistää sovelluksen näin:
```bash
$ flask run
```
## Suuren tietomäärän testaaminen
Testasin sovellusta suurella tietomäärällä. Ensiksi loin tietokantaan seed.py skriptillä:
- 1000 käyttäjää
- 100 000 treeniohjelmaa
- 1 000 000 arviota
Olin luonut sivutuksen jo ohjelman etusivulle, joten testidata ei vaikuttanut etusivun toimintaan huomattavasti.

Hakusivulla en ollut vielä tehnyt sivutusta, jonka vuoksi hakusanalla "program" (joka hakee kaikki 100 000 treeniohjelmaa) haku kesti noin 2-3 sekunttia.

Lisäsin indeksit:
```
CREATE INDEX idx_programs_user_id ON programs(user_id);
CREATE INDEX idx_programs_level_id ON programs(level_id);
CREATE INDEX idx_programs_type_id ON programs(type_id);
CREATE INDEX idx_reviews_program_id ON reviews(program_id);
CREATE INDEX idx_reviews_user_id ON reviews(user_id);
```
Indeksien lisäys ei vaikuttanut 100 000 treeniohjelman hakuun huomattavasti, mutta rajatummat haut, kuten hakusanat "program9" ja "program11" kestävät alle sekunnin, joka on minusta hyväksyttävä tulos.

Lisäsin sivutuksen hakusivulle, jonka jälkeen haku kesti kaikilla hakusanoilla alle sekunnin.

Suuri tietomäärä ei vaikuttanut kirjautumiseen ja rekisteröitymiseen millään tavalla. Käyttäjäsivut toimivat jo valmiiksi tehokkaasti, mutta lisäsin vielä niille sivutuksen, koska se näyttää siistimmältä suurella tietomäärällä.