# Pylint-raportti

Pylint antaa seuraavan raportin sovelluksesta:

```
************* Module app
app.py:287:0: C0304: Final newline missing (missing-final-newline)
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:4:0: E0401: Unable to import 'markupsafe' (import-error)
app.py:6:0: E0401: Unable to import 'flask' (import-error)
app.py:7:0: E0401: Unable to import 'flask' (import-error)
app.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:21:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:28:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:35:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:51:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:72:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:83:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:91:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:111:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:138:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:154:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:170:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:197:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:197:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:220:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:242:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:246:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:264:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:284:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module config
config.py:1:0: C0304: Final newline missing (missing-final-newline)
config.py:1:0: C0114: Missing module docstring (missing-module-docstring)
config.py:1:0: C0103: Constant name "secret_key" doesn't conform to UPPER_CASE naming style (invalid-name)
************* Module db
db.py:36:0: C0304: Final newline missing (missing-final-newline)
db.py:1:0: C0114: Missing module docstring (missing-module-docstring)
db.py:2:0: E0401: Unable to import 'flask' (import-error)
db.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:10:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:10:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:20:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:20:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:26:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:32:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module programs
programs.py:138:0: C0304: Final newline missing (missing-final-newline)
programs.py:1:0: C0114: Missing module docstring (missing-module-docstring)
programs.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
programs.py:8:0: C0116: Missing function or method docstring (missing-function-docstring)
programs.py:8:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
programs.py:16:0: C0116: Missing function or method docstring (missing-function-docstring)
programs.py:24:0: C0116: Missing function or method docstring (missing-function-docstring)
programs.py:41:0: C0116: Missing function or method docstring (missing-function-docstring)
programs.py:59:0: C0116: Missing function or method docstring (missing-function-docstring)
programs.py:64:0: C0116: Missing function or method docstring (missing-function-docstring)
programs.py:68:0: C0116: Missing function or method docstring (missing-function-docstring)
programs.py:74:0: C0116: Missing function or method docstring (missing-function-docstring)
programs.py:93:0: C0116: Missing function or method docstring (missing-function-docstring)
programs.py:102:0: C0116: Missing function or method docstring (missing-function-docstring)
programs.py:102:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
programs.py:110:0: C0116: Missing function or method docstring (missing-function-docstring)
programs.py:118:0: C0116: Missing function or method docstring (missing-function-docstring)
programs.py:133:0: C0116: Missing function or method docstring (missing-function-docstring)
programs.py:133:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
************* Module seed
seed.py:38:0: C0304: Final newline missing (missing-final-newline)
seed.py:1:0: C0114: Missing module docstring (missing-module-docstring)
seed.py:13:0: C0103: Constant name "user_count" doesn't conform to UPPER_CASE naming style (invalid-name)
seed.py:14:0: C0103: Constant name "program_count" doesn't conform to UPPER_CASE naming style (invalid-name)
seed.py:15:0: C0103: Constant name "review_count" doesn't conform to UPPER_CASE naming style (invalid-name)
************* Module users
users.py:51:0: C0304: Final newline missing (missing-final-newline)
users.py:1:0: C0114: Missing module docstring (missing-module-docstring)
users.py:1:0: E0401: Unable to import 'werkzeug.security' (import-error)
users.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:9:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:23:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:30:0: C0116: Missing function or method docstring (missing-function-docstring)

------------------------------------------------------------------
Your code has been rated at 7.42/10 (previous run: 7.42/10, +0.00)
```

Käydään seuraavaksi läpi tarkemmin raportin sisältö ja perustellaan, miksi kyseisiä asioita ei ole korjattu sovelluksessa.

## Docstring-ilmoitukset

Suurin osa Pylintin ilmoituksia ovat:

```
users.py:23:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:30:0: C0116: Missing function or method docstring (missing-function-docstring)
```

Nämä ilmoitukset tarkoittavat, että moduuleissa ja funktioissa ei ole docstring-kommentteja. Kurssin ohjeistuksen ja esimerkkien mukaan niitä ei tarvitse tehdä, joten ne on jätetty tekemättä.

## Import-ilmoitukset

Raportissa on seuraavat ilmoitukset liittyen `import`-komentoihin:

```
app.py:4:0: E0401: Unable to import 'markupsafe' (import-error)
app.py:6:0: E0401: Unable to import 'flask' (import-error)
app.py:7:0: E0401: Unable to import 'flask' (import-error)
db.py:2:0: E0401: Unable to import 'flask' (import-error)
users.py:1:0: E0401: Unable to import 'werkzeug.security' (import-error)
```

Pylint antaa jostain syystä nämä ilmoitukset, vaikka Flask-kirjasto on asennettu kehitysympäristössä. Nämä voi jättää huomiotta, koska ne toimivat itse sovelluksessa.

## Puuttuva palautusarvo

Raportissa on seuraavat ilmoitukset liittyen funktion palautusarvoon:

```
app.py:197:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
programs.py:8:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
programs.py:102:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
programs.py:133:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
```

Nämä ilmoitukset liittyvät tilanteeseen, jossa funktio käsittelee metodit `GET` ja `POST`, mutta ei muita metodeja. Esimerkiksi ensimmäinen ilmoitus koskee seuraavaa funktiota:

```
@app.route("/delete_program/<int:program_id>", methods=["GET", "POST"])
def delete_program(program_id):
    require_login()
    program = programs.get_program(program_id)

    if not program:
        abort(404)

    if program["user_id"] != session["user_id"]:
        abort(403)

    if request.method == "GET":
        return render_template("delete_program.html", program=program)

    if request.method == "POST":
        check_csrf()
        if "remove" in request.form:
            programs.delete_program(program_id)
            return redirect("/")

        return redirect("/program/" + str(program_id))
```

Tämä funktio poistaa treeniohjelman. Funktio palauttaa arvon, kun `request.method` on `GET` tai `POST`, mutta periaatteessa voisi tulla tilanne, jossa `request.method` on jotain muuta eikä koodi palauttaisi arvoa. Käytännössä tällainen tilanne ei ole kuitenkaan mahdollinen, koska funktion dekoraattorissa on vaatimus, että metodin tulee olla joko `GET` tai `POST`. Eli tässä tapauksessa ei ole riskiä, että funktio ei palauttaisi arvoa.

## Vakion nimi

Raportissa on seuraava ilmoitus liittyen vakion nimeen:

```
config.py:1:0: C0103: Constant name "secret_key" doesn't conform to UPPER_CASE naming style (invalid-name)
seed.py:13:0: C0103: Constant name "user_count" doesn't conform to UPPER_CASE naming style (invalid-name)
seed.py:14:0: C0103: Constant name "program_count" doesn't conform to UPPER_CASE naming style (invalid-name)
seed.py:15:0: C0103: Constant name "review_count" doesn't conform to UPPER_CASE naming style (invalid-name)
```

Pylint tulkitsee nämä muuttujat vakioiksi, joiden nimet tulisi olla kirjoitettu suurilla kirjaimilla. Kuitenkin sovelluksen kehittäjän näkökulmasta näyttää paremmalta, kun kaikki muuttujan nimet ovat kirjoitettu yhtenäisesti pienillä kirjaimilla. Muuttujia käytetään koodissa näin:

```
app.secret_key = config.secret_key
user_count = 1000
program_count = 10**5
review_count = 10**6
```

## Vaarallinen oletusarvo

Raportissa on seuraavat ilmoitukset:

```
db.py:10:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:20:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
```

Ensimmäinen ilmoitus koskee funktiota:

```
def execute(sql, params=[]):
    con = get_connection()
    result = con.execute(sql, params)
    con.commit()
    g.last_insert_id = result.lastrowid
    con.close()
```

Tässä parametrin oletusarvo on tyhjä lista. Tässä ongelmaksi voisi tulla, että sama oletusarvona oleva tyhjä listaolio on jaettu kaikkien funktion kutsujen kesken ja jos jossain kutsussa listan sisältöä muutettaisiin, tämä muutos näkyisi myös muihin kutsuihin. Funktio ei muuta listaoliota, joten tämä ei haittaa.

## Puuttuva \n tiedoston lopussa

Raportissa on seuraavat ilmoitukset:

```
app.py:287:0: C0304: Final newline missing (missing-final-newline)
config.py:1:0: C0304: Final newline missing (missing-final-newline)
db.py:36:0: C0304: Final newline missing (missing-final-newline)
programs.py:138:0: C0304: Final newline missing (missing-final-newline)
seed.py:38:0: C0304: Final newline missing (missing-final-newline)
users.py:51:0: C0304: Final newline missing (missing-final-newline)
```

Nämä johtuvat siitä, että sovelluksen tiedostojen lopussa ei ole tyhjää riviä. Voi olla, että tämä johtuu käyttämästäni tekstieditorista. Sovellukseni toimii ilman tyhjiä rivejä, joten nämä ilmoitukset eivät haittaa.