# Plan: matematik i seks bind og én samlet udgave

**Status (27. oktober 2026):** Seks separate LaTeX-indgange er oprettet under `volumes/`, og `Makefile` har mål for bind 1–6. Kildekapitler og den samlede PDF-indgang er bevaret. Bind-builds er **ikke endnu kørt eller godkendt**, og tværbindshenvisninger kræver kontrol. Ingen Drive-filer er ændret.

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

## Teknisk status og manglende validering

- Bevar `00-matematik/chapters/*.tex` som **eneste kilde** for hvert kapitel.
- **Udført:** `volumes/bind-1.tex` til `bind-6.tex` inkluderer de eksisterende kapitelkilder uden kopier.
- Genbrug samme fælles typografi, makroer og hyperref-opsætning.
- **Udført i Makefile, endnu ikke kørt:** `make bind-1` ... `make bind-6` og `make alle-bind`; `make pdf` bevares som samlet udgave.
- Opbevar hver PDF i et separat build-output, og valider bogmærker, indholdsfortegnelse, figurer, links og referencer.
- Revider tværbindsreferencer eksplicit. En reference til en udeladt label må ikke bare blive '??'; brug enten en kort tekstlig henvisning med bind og kapitel eller et verificeret eksternt PDF-link.
- Udgiv ikke bindene i Google Drive, før mål-id'er, godkendelse og særskilt publicering er verificeret.
- Statistik er fortsat et selvstændigt fag uden for matematikbindene.
- Matematik fra LinALys, MatF1, MatF2 og Algebra integreres efter emne, ikke som selvstændige kurser.

## Indholdsstatus

Et bind må ikke betegnes som færdiggjort blot fordi kapitlets fil er oprettet. Lineær algebra blev udbygget 27. oktober 2026 med definitioner og formelstof om baser, lineære afbildninger, rang, spektralteori og SVD. Kapitlet og bindene afventer kompilering, visuel kontrol og illustrationer. Der må ikke påstås grøn build ud fra blot oprettede kildefiler.

## Bind 1 – første faglige udbygning 27. oktober 2026

- `chapters/01-algebra.tex` er udbygget fra overskrifter til forklarende referencekapitel om algebra, definitionsområder, ligninger, uligheder, funktioner, inverser, logaritmer, eksponentialfunktioner og fysiske skaleringslove.
- `figures/algebra-eksplog.tex` er en ny original PGFPlots-figur, indsat i kapitlet.
- `chapters/02-trigonometri.tex` har fået erstattet henvisninger, der pegede på afsnit uden for bind 1, med tekstlige krydsbindshenvisninger.
- `chapters/09-lineaer-algebra.tex` indeholder den tidligere udvidelse om vektorrum, baser, egenværdier, SVD mv.
- **Kontrol mangler:** De nye kilder er skrevet til GitHub, men det nye bind er ikke kompilations- eller layoutgodkendt i denne omgang. Krydsreferencer og figurer skal kontrolleres ved `make bind-1` og `make pdf` før publicering.
