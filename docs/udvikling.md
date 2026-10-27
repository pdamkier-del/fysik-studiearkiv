# Udvikling af nye kapitler

1. Find det eksisterende kapitel og læs dispositionen i [bibliotekets kapitelplan](../00-matematik/PLAN.md). Udvid filen; opret ikke en konkurrerende version. Fjern først planlagt-markeringen, når kapitlet faktisk er udviklet og kontrolleret.
2. Afgræns emnet og skriv antagelser, symboler, definitioner og forbindelser til andre kapitler før formeltabeller. Forklar forskellen på nødvendige og tilstrækkelige betingelser. Angiv definitionsområder, enheder og fortegn.
3. Grundlæggende stof samles i fyldige tabeller med forklaringer. Avancerede emner skal have en længere begrebsmæssig introduktion, beviser eller begrundelser og præcise anvendelsesbetingelser. Ingen gennemregnede opgaveeksempler i matematikkompendiet.
4. Tilføj originale, relevante figurer som separate TikZ/PGFPlots-filer i `00-matematik/figures/`. Angiv, om data er analytiske, numeriske eller skematiske. Kontroller kurver og særlige punkter algebraisk. Brug radianer matematisk; PGFPlots' trigonometriske udtryk kræver eksplicit `deg(x)` ved radianinput.
5. Brug fælles makroer fra `90-faelles/latex/studiearkiv.sty`. Tilføj stabile labels og krydshenvisninger. Hvis en figur eller formel deles, lægges den i den fælles mappe.
6. Registrer reelt anvendte kilder med udgave og relevante afsnit. Opfind ikke sidetal eller KU-pensum. Bevar originale kilder og brugerens noter uændret.
7. Kør `make check`, og gennemse alle ændrede PDF-sider ved læsbar opløsning. Kontroller figurtekster, akser, specialtegn, tabellers sideskift, sidehoveder, indholdsfortegnelse, bogmærker og interne links. En grøn teknisk kontrol beviser ikke matematisk korrekthed.
8. Ved stilændringer køres også `make templates`. Hold buildfiler ude af Git. Lav overskuelige commits og rapporter præcist ændrede kapitler og kontrolresultater.

## Designkontrakt

A4, 11-punkts Latin Modern, 26 mm margin, rolig blå/rød farvepalette, klikbar indholdsfortegnelse og bogmærker. Farver suppleres med linjemønstre i grafer. Figurer er vektorbaserede og har forklarende billedtekster. Sætningen i en formel må ikke stå uden tekstlig kontekst. Fysiske fags fire dokumenttyper holdes adskilt.

## Faglig videreudvikling

Pilotkapitlet er en første håndbogsversion, ikke en garanti for udtømmende dækning. Videreudvikling kan omfatte flere kontrollerede identiteter, udvidet fejlanalyse og forbindelser til flervariabel calculus. Byg ét sammenhængende kapitel ad gangen; ingen fyldtekst for at ramme et sideantal.

## Kursusnoter og referenceværker

Vælg dokumenttype før redigering. AM-/EM-kursusnoter under `01-universitetsfag/` følger dokumenteret pensum; matematikkens hovedområde `00-matematik/` og fysikbiblioteket `02-fysikbibliotek/` har egne brede faglige planer. Kilderegisteret ligger i `99-kilder-og-pensum/`. Genbrug fælles komponenter, men overskriv ikke et kursusdokument med biblioteksstof. Nye kursusmapper kræver dokumenteret kursusidentitet.
