V tomto projektu vytvářím textový analyzátor

Program si vyžádá od uživatele:

    •   přihlašovací jméno a heslo,
    •   zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů,
    •   pokud je registrovaný, pozdraví jej a umožní mu analyzovat texty,
    •   pokud není registrovaný, upozorní jej a ukončí program.

Mám předem definované uživatele:

    +------+-------------+
    | user |   password  |
    +------+-------------+
    | bob  |     123     |
    | ann  |   pass123   |
    | mike | password123 |
    | liz  |   pass123   |
    +------+-------------+

Dále je program schopný ze třech (předpřipravených) textů (1 - 3) zjistit o každém z nich různé informace:

    •   počet slov,
    •   počet slov začínajících velkým písmenem,
    •   počet slov psaných velkými písmeny,
    •   počet slov psaných malými písmeny,
    •   počet čísel (ne cifer),
    •   sumu všech čísel (ne cifer) v textu.

Dále také ve sloupcovém grafu zobrazí četnost různých délek slov ve vybraném textu.
Pokud uživatel vybere takové číslo textu, které není v zadání, program jej upozorní a skončí.
Pokud uživatel zadá jiný vstup než číslo, program jej rovněž upozorní a skončí.

