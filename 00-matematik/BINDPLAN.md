# Plan: matematik i seks bind og én samlet udgave

**Status:** Arkitekturplan, ikke aktiveret build. Den eksisterende `main.tex` og dens samlede PDF bevares. Ingen Drive-filer ændres.

## Bind og eksisterende kapitelkilder

| Bind | Titel | Kapitelnumre |
|---|---|---|
| 1 | Algebra og lineær algebra | 01, 02, 09 |
| 2 | Calculus og analyse | 04, 05, 06, 11 |
| 3 | Differentialligninger | 07, 08, 14, 15 |
| 4 | Matematiske metoder | 03, 13, 16, 18 |
| 5 | Geometri og tensorer | 10, 12, 19, 20 |
| 6 | Variationsregning og symmetrier | 17, 21 |

Ovenstående dækker samtlige 21 kapitler præcis én gang. Rækkefølgen er en redaktionel læseinddeling og ændrer ikke den samlede bogs indholdsfortegnelse.

## Implementering ved fremtidig teknisk opdeling

- Bevar `00-matematik/chapters/*.tex` som **eneste kilde** for hvert kapitel.
- Opret separat `volumes/bind-1.tex` til `bind-6.tex`, der inkluderer de eksisterende kapitelkilder; undgå kopierede kapitler.
- Genbrug samme fælles typografi, makroer og hyperref-opsætning.
- Tilføj `make bind-1` ... `make bind-6` og `make alle-bind`; bevar `make pdf` som samlet bind.
- Opbevar hver PDF i et separat build-output, og valider bogmærker, indholdsfortegnelse, figurer, links og referencer.
- Revider tværbindsreferencer eksplicit. En reference til en udeladt label må ikke bare blive '??'; brug enten en kort tekstlig henvisning med bind og kapitel eller et verificeret eksternt PDF-link.
- Udgiv ikke bindene i Google Drive, før mål-id'er, godkendelse og særskilt publicering er verificeret.
- Statistik er fortsat et selvstændigt fag uden for matematikbindene.
- Matematik fra LinALys, MatF1, MatF2 og Algebra integreres efter emne, ikke som selvstændige kurser.

## Indholdsstatus

Et bind må ikke betegnes som færdiggjort blot fordi kapitlets fil er oprettet. Udbygning af lineær algebra begyndte 27. oktober 2026 med en samlet indføring i baser, lineære afbildninger, rang, spektralteori og SVD. Kapitlet afventer kompilering, visuel kontrol og illustrationer.
