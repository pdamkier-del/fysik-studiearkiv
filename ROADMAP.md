# Faglig udviklingsplan

Dette dokument samler projektets mål og næste trin. Faktiske resultater står i [STATUS.md](STATUS.md), og dokumenterede afgrænsninger i [PENSUM.md](PENSUM.md). Mapper og skabeloner er fundament, ikke færdige fag.

## Fag og dokumenter

| Område | Dokumenter | Udviklingsretning |
| --- | --- | --- |
| `00-matematik/` | Ét samlet kompendium med 21 matematiske hovedemner og underafsnit | Udbyg ét sammenhængende emne ad gangen; ingen separate kursuskompendier |
| `01-analytisk-mekanik/` | Formelsamling, udledningsnoter, opgavenoter og opgavesamling | Læs og bevar den eksisterende AM-original før integration; præcist pensum afventer |
| `02-elektromagnetisme/` | Samme fire adskilte dokumenttyper | Modtag og bevar originalerne; intet rekonstrueret pensum |
| `03-kvantemekanik/` | Samme fire dokumenttyper | Kun fundament indtil dokumenteret pensum foreligger |
| `04-termodynamik-statistisk-fysik/` | Samme fire dokumenttyper; faglig plan i fagets README | Integrer kapitel 1–6 og præcise emner/sider fra original kursusplan, når den kan læses |
| `05-relativitet-og-gravitation/` | Samme fire dokumenttyper | Kun fundament indtil dokumenteret pensum foreligger |
| `06-statistik/` | Selvstændigt statistikkompendium | Barlow som hovedreference; afstem struktur/notation med faktisk udgave; afgræns pensum senere |
| `90-faelles/` | Design, LaTeX-skabelon, notation og fælles figurer | Vedligehold fælles standard uden kopierede stilfiler |
| `99-kilder-og-pensum/` | Kilderegister, originale afgrænsninger og adgangsstatus | Bevar sporbarhed, originaler og forskellen mellem oplyst og verificeret |

Matematiske forklaringer skal indgå i hvert fysikfag: definer de nødvendige matematiske begreber, antagelser og notation dér, hvor de bruges, og forbind dem med den fysiske fortolkning. Henvis til matematikkompendiet for den generelle teori, uden at erstatte den lokale forklaring med et link eller kopiere hele kapitler.

## Matematik

Følg [hovedemneplanen](docs/kapitelplan.md). Den omfatter algebra og funktioner, trigonometri, komplekse tal/kompleks analyse, differential- og integralregning, rækker, ODE/PDE, lineær algebra, geometri, flervariabel analyse, vektoranalyse, transformationer, Greenfunktioner, Sturm–Liouville, specialfunktioner, variationsregning, numerik, tensorer, differentialgeometri/GR og gruppeteori.

Bevar pilotkapitlet om differentialregning. Læs det eksisterende matematikkompendium før egentlig indholdsintegration, og udbyg eksisterende afsnit frem for at skabe dubletter. Langsigtet mål er 200–400 sider; matematisk kvalitet bestemmer omfanget. Ingen gennemregnede opgaveeksempler i kompendiet. Avancerede emner, især Greenfunktioner, Sturm–Liouville, konvergens/asymptotik, krumme koordinater og differentialgeometri, kræver grundigere introduktioner. GR-planens geometriske illustrationsprogram bevares.

## Statistik og termodynamik

Statistisk metode, sandsynlighedsfordelinger, estimatorer, likelihood, hypotesetest, regression og usikkerhedsanalyse hører alene under `06-statistik/`. Ensembler, partitionfunktioner, Boltzmann- og Maxwellfordeling hører under statistisk fysik i termodynamikfaget. En organisatorisk placering er ikke dokumentation for, at et emne indgår i kursets pensum.

Barlows bog skrives ikke af: forklar selvstændigt på dansk og bevar faglig opbygning og notation, hvor den faktisk er verificeret og egnet. Termodynamik organiseres efter faglige sammenhænge, mens registeret bevarer præcise henvisninger til kursusplanen.

## Leverancer i rækkefølge

1. Vedligehold konsoliderede regler, kildeafgrænsninger og faktisk status; bevar nuværende arbejde.
2. Afslut og test PDF-build samt den allerede igangværende, deaktiverede Drive-forberedelse. Aktiver ingen ekstern skrivning under test.
3. Afklar adgang til original AM, matematik og EM samt kursusplanen for termodynamik. Læs først, map derefter, integrer til sidst.
4. Verificer LinALys-beskrivelsen, FV/EMM-indholdsfortegnelser og Barlow-udgave. Udfyld ingen ukendte afsnit ud fra gæt.
5. Udbyg ét fagligt sammenhængende kapitel/dokument ad gangen med forklaringer, LaTeX og originale faglige figurer; byg og gennemse PDF før levering.
6. Aktiver Drive-publicering først efter verificerede mål, rettigheder, autentificering, beskyttet hovedbranch og godkendelsesprocedure. Bevar manuel publicering og backupbaseret rollback.

GitHub er kildearkiv; Drive er læse- og publiceringssted. Genererede PDF'er leveres som build-artifacts, ikke i kildehistorikken.
