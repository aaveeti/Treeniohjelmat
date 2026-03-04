# Treeniohjelmat

## Toiminnot
- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
- Käyttäjä pystyy lisäämään sovellukseen treeniohjelmia. Lisäksi käyttäjä pystyy muokkaamaan ja poistamaan lisäämiään treeniohjelmia.
- Käyttäjä näkee sovellukseen lisätyt treeniohjelmat. Käyttäjä näkee sekä itse lisäämänsä että muiden käyttäjien lisäämät treeniohjelmat.
- Käyttäjä pystyy etsimään treeniohjelmia hakusanalla tai muulla perusteella. Käyttäjä pystyy hakemaan sekä itse lisäämiään että muiden käyttäjien lisäämiä treeniohjelmia.
- Sovelluksessa on käyttäjäsivut, jotka näyttävät jokaisesta käyttäjästä tilastoja ja käyttäjän lisäämät treeniohjelmat.
- Käyttäjä pystyy valitsemaan treeniohjelmalle yhden tai useamman luokittelun (esim. kokemustaso, tavoite).
- Käyttäjä pystyy antaa treeniohjelmalle positiivisen tai negatiivisen arvion ja kommentin.
## Miten sovellusta voi testata
Asenna `flask` -kirjasto:
```bash
$ pip install flask
```

Luo tietokannan taulut ja lisää alkutiedot:
```bash
$sqlite3 database.db < schema.sql
$sqlite3 database.db < init.sql
```

Voit käynnistää sovelluksen näin:
```bash
$ flask run
```
