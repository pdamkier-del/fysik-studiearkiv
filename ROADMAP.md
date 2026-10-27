# Faglig udviklingsplan

Projektet har to selvstændige hovedområder. Faktisk status står i [STATUS.md](STATUS.md); universiteternes dokumenterede kilder og afgrænsninger i [PENSUM.md](PENSUM.md). Mapper, planer og skabeloner tæller ikke som færdige fag.

## Universitetsfag

Kun dokumenterede kursusidentiteter får egne mapper under `01-universitetsfag/`:

| Kursus | Dokumenter og næste faglige trin |
| --- | --- |
| Analytisk Mekanik | Bevarede fire dokumentskabeloner; forelæsningsnoter og eksamensmateriale har egne pladser. Læs AM-originalen før integration; bevar en uændret referenceversion |
| Elektromagnetisme | Samme adskilte dokumenttyper. Modtag og bevar EM-originalen og dokumenter det konkrete pensum |
| Termodynamik 2026 | Bevar den faglige kursusplan og fire dokumentskabeloner. Læs kapitel 1–6, præcise sider og emner fra den autoritative original-PDF, når den foreligger |
| Statistik | Selvstændigt kursuskompendium med Barlow som hovedreference; udgave, indholdsfortegnelse og præcis pensumafgrænsning afventer |

Kursusnoter bruges til undervisning og eksamen og skal være pensumtro. Matematiske forklaringer, symboldefinitioner, antagelser og fysisk fortolkning integreres lokalt. Generel teori kan henvises til biblioteket uden at erstatte den lokale forklaring eller kopiere hele kapitler.

[Universiteternes pensumregister](01-universitetsfag/pensum/README.md) bevarer også Matematik F-, LinALys- og ugeplansdokumentationen. Der er ikke oprettet ekstra kursusmapper som led i migrationen.

## Generelt matematik- og fysikbibliotek

Bibliotekets referencekompendier i `02-fysikbibliotek/` er selvstændige værker med formler, forklaringer, udledninger, matematiske sammenhænge og originale figurer. Deres indhold kan udbygges ud over konkrete kursers pensum.

1. Matematik: ét eksisterende LaTeX-dokument med 21 hovedemner; den eneste aktive generelle kompendieudvikling i denne leverance.
2. Klassisk mekanik.
3. Elektromagnetisme.
4. Termodynamik.
5. Statistisk fysik.
6. Kvantemekanik.
7. Relativitet og gravitation.
8. Optik og bølger.
9. Atom- og molekylefysik.
10. Kerne- og partikelfysik.
11. Faststoffysik.
12. Numeriske metoder.

Område 2–12 er planer, ikke færdige kompendier. Eksisterende tomme kvante-/relativitetsskabeloner bevares som arkiverede skabeloner med fortsat buildkontrol, ikke som påståede KU-kurser. Der oprettes intet generelt statistikbibliotek. Statistikmetode og statistisk fysik må ikke forveksles.

## Matematikkompendiet

Følg [bibliotekets egen hovedemneplan](02-fysikbibliotek/matematik/PLAN.md). Bevar det eksisterende pilotkapitel om differentialregning. Trigonometri har nu et sammenhængende første afsnit og en faglig figur og kan udbygges videre; de øvrige hovedemner udvikles ét ad gangen. Langsigtet mål er 200–400 sider, men korrekthed og læsbarhed bestemmer omfanget. Ingen gennemregnede opgaveeksempler.

Greenfunktioner, Sturm–Liouville, konvergens/asymptotik, krumme koordinater, tensorer og differentialgeometri kræver særligt grundige introduktioner. Bevar GR-planens geometriske illustrationsprogram. Et eventuelt senere numerisk fysikkompendium fokuserer på fysiske modeller og beregninger med henvisning til den generelle numeriske matematik uden dubletter.

Det eksisterende matematikmateriale på Drive skal læses og bevares før import. Afklar om originalens afsnit er kursusnoter eller generelt stof før placering; en migration må ikke omklassificere ukendt indhold ud fra filnavnet.

## Leverancer og publicering

1. Fuldfør sikker migration med bevaret indhold og alle oprindelige builds/tests; opdater faktisk status.
2. Fortsæt kun den igangværende matematikudvikling, ikke alle generelle fysikkompendier.
3. Afklar adgang til AM-, EM- og matematikoriginaler, termodynamik-PDF, FV/EMM-indholdsfortegnelser, KU-beskrivelse og Barlow-udgave. Læs først, map derefter, integrer til sidst.
4. Udvikl kursernes noter inden for dokumenteret pensum; udvikl biblioteket efter egne faglige planer uden at overskrive kursusdokumenter.
5. Bevar GitHub som kildearkiv og Drive som læsested. Fremtidig destination er arkivrod → hovedområde → fag → PDF, men eksisterende fil-id'er bevares, og ingen Drive-filer flyttes automatisk.
6. Aktiver først publicering efter verificerede mål/rettigheder, OIDC, beskyttet main, godkendelsesprocedure og sikker integrationstest. Bevar manuel publicering og backupbaseret rollback. Indtil da er alle manifestposter deaktiverede.
