# Faglig udviklingsplan

Projektet har tre selvstændige hovedområder. Faktisk status står i [STATUS.md](STATUS.md); universiteternes dokumenterede kilder og afgrænsninger i [PENSUM.md](PENSUM.md). Mapper, planer og skabeloner tæller ikke som færdige fag.

## Tre selvstændige hovedområder

1. `00-matematik/`: ét sammenhængende matematisk referenceværk med 21 hovedemner, seks bind og én samlet udgave fra fælles kapitelkilder. MatF1, MatF2, LinALys og Algebra integreres efter emner; ingen separate kursuskompendier eller mapper. Præcise ukendte kursusreferencer afventer dokumentation.
2. `01-universitetsfag/`: kun aktuelle AM- og EM-kursusnoter med separate dokumenttyper. Nye kurser tilføjes først ved faktisk deltagelse og dokumentation. Originale formelsamlinger bevares uændret før integration.
3. `02-fysikbibliotek/`: brede referencekompendier i klassisk mekanik, EM, termodynamik, statistisk fysik, statistik, kvantemekanik, relativitet/gravitation og de øvrige allerede planlagte fysikområder. Matematik ligger ikke her. Øvrige kompendier udfyldes ikke automatisk.

Statistik bygger fortsat på Roger Barlow og behandler statistisk metode, ikke statistisk fysik. Termodynamik kan udvikles fra det bevarede historiske kursusgrundlag og senere udvides bredere. Omfang ud over den gamle kursusplan skal markeres som generelt stof, ikke som gennemgået pensum. De eksisterende 20 skabelonbuilds og alle kilder bevares.

Det fælles kilderegister ligger i `99-kilder-og-pensum/`. Aktuelle kursusnoter og brede referenceværker er forskellige dokumenter; fælles komponenter genbruges uden at overskrive noter. Matematiske forklaringer, symboler, antagelser og fysisk fortolkning indgår lokalt i fysikfremstillinger.

## Matematikkompendiet

Følg [bibliotekets egen hovedemneplan](00-matematik/PLAN.md). Bevar det eksisterende pilotkapitel om differentialregning. Trigonometri har nu et sammenhængende første afsnit og en faglig figur og kan udbygges videre; de øvrige hovedemner udvikles ét ad gangen. Korrekthed, forståelse og anvendelighed bestemmer omfanget; tidligere sidetalsmål er ikke et acceptkriterium. Ingen gennemregnede opgaveeksempler.

Greenfunktioner, Sturm–Liouville, konvergens/asymptotik, krumme koordinater, tensorer og differentialgeometri kræver særligt grundige introduktioner. Bevar GR-planens geometriske illustrationsprogram. Et eventuelt senere numerisk fysikkompendium fokuserer på fysiske modeller og beregninger med henvisning til den generelle numeriske matematik uden dubletter.

Det eksisterende matematikmateriale på Drive skal læses og bevares før import. Afklar om originalens afsnit er kursusnoter eller generelt stof før placering; en migration må ikke omklassificere ukendt indhold ud fra filnavnet.

## Leverancer og publicering

1. Fuldfør sikker migration med bevaret indhold og alle oprindelige builds/tests; opdater faktisk status.
2. Fortsæt kun den igangværende matematikudvikling, ikke alle generelle fysikkompendier.
3. Afklar adgang til AM-, EM- og matematikoriginaler, termodynamik-PDF, FV/EMM-indholdsfortegnelser, KU-beskrivelse og Barlow-udgave. Læs først, map derefter, integrer til sidst.
4. Udvikl kursernes noter inden for dokumenteret pensum; udvikl biblioteket efter egne faglige planer uden at overskrive kursusdokumenter.
5. Bevar GitHub som kildearkiv og Drive som læsested. De brugeroplyste eksisterende Drive-mapper registreres: Matematik-PDF direkte i sit hovedområde; øvrige fag under det relevante hovedområde. Fil-id’er bevares, og ingen Drive-filer flyttes automatisk.
6. Aktiver først publicering efter verificerede mål/rettigheder, OIDC, beskyttet main, godkendelsesprocedure og sikker integrationstest. Bevar manuel publicering og backupbaseret rollback. Indtil da er alle manifestposter deaktiverede.

## Seneste prioritet

Udbyg matematikbindene systematisk fra bind 1 på en separat arbejdsbranch. Følg [underemnerne](00-matematik/ALLE_BIND_UNDEREMNER.md) og den uddybende [bindplan](00-matematik/BINDPLAN.md). De første tre algebraemner er udbygget; fortsæt med ligninger, uligheder og partialbrøker før de øvrige emner. Bevar tidligere integral-, differential- og ODE-indhold. Gå først videre til næste bind, når bind 1 er fagligt og teknisk gennemarbejdet. Sidetal er ikke et leverancekriterium. Ingen Drive-publicering aktiveres.
