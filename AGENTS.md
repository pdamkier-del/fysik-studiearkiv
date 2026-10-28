# Faste regler for fysik-studiearkiv

## Indhold og redaktion
1. Opdater eksisterende dokumenter frem for at oprette dubletter. Find det relevante fag, dokument og kapitel først.
2. Bevar korrekt eksisterende indhold; integrer udvidelser under fagligt relevante afsnit.
3. Brug LaTeX til matematik og fysik og dansk forklarende tekst som standard.
4. Bevar konsekvent notation inden for hvert dokument; definer symboler før brug og vedligehold notationsoversigten.
5. Prioritér matematisk korrekthed. Kontrollér antagelser, definitionsmængder, gyldighedsbetingelser, dimensioner og fortegnskonventioner.
6. Indsæt forklarende tekst mellem formler. Skeln mellem definitioner, sætninger, tilnærmelser og fysiske fortolkninger.
7. Brug originale fagligt relevante figurer med akser, enheder eller tydelig angivelse af dimensionsløse størrelser og forklarende billedtekster. Foretræk TikZ/PGFPlots eller vektor-PDF fra Python.
8. Ingen gennemregnede opgaveeksempler i matematikkompendiet. Generelle identiteter, beviser, metodebeskrivelser og illustrative grafer er tilladt.
9. Hold formelsamlinger, udledningsnoter, opgavenoter og opgavesamlinger adskilt, medmindre brugeren specifikt ønsker andet.
10. Bevar kilder og originale filer. Opfind aldrig pensum, kildeindhold eller henvisninger. Markér ufærdige kapitler ærligt.
11. AM- og EM-noter må først integreres, når originalerne er tilgængelige. Genskab dem ikke fra hukommelsen.

## Teknik og kontrol
- Genbrug `90-faelles/latex/studiearkiv.sty`; ét kapitel pr. kildefil, særskilte figurfiler. Udvid den eksisterende fælles stil i stedet for at kopiere design.
- Kør `make pdf` og `make check`. Se også `docs/udvikling.md`. Kontrollér alle nye sider visuelt: sideskift, tabeller, figurer, navigation og læsbarhed.
- Genererede PDF'er og hjælpefiler ligger normalt i `build/`; CI offentliggør artifacts. Efter brugerens udtrykkelige leveringskrav er netop `00-matematik/udgivelser/bind-1.pdf` en versionsstyret undtagelse, ledsaget af kildecommit og SHA-256. Redigér aldrig PDF'en separat fra LaTeX-kilden.
- Gem aldrig tokens eller hemmeligheder i repositoryet. Drive-opdatering er blokeret, indtil fil-id'er og adgangsrettigheder er fastlagt; brug eksisterende fil-id frem for at oprette dubletter.
- Brug det eksisterende checkout i cloudopgaver; opret kun worktrees efter udtrykkeligt ønske.
- Udfør ændringer i overskuelige commits. Rapportér præcist ændrede filer og kapitler samt udførte og ikke udførte kontroller.
- Spørg ikke om gentagen godkendelse af allerede aftalte tekniske standarder.

## Tre hovedområder (seneste brugerbeslutning)
- `00-matematik/` er matematik som selvstændigt hovedområde, ikke en undermappe af fysikbiblioteket. Bevar ét sammenhængende referenceværk med 21 hovedemner, én samlet udgave (`main.tex`) og seks bindindgange (`volumes/bind-1.tex` til `bind-6.tex`). Hvert kapitel har kun én autoritativ kilde, delt af bind og samlet udgave. Bevar forklaringer, notation, figurer, klikbar indholdsfortegnelse og PDF-bogmærker. MatF1, MatF2, LinALys og Algebra integreres efter emner, ikke som selvstændige kursusmapper eller kompendier. Gæt ikke præcise kursusidentiteter eller referenceækvivalenser.
- `01-universitetsfag/` indeholder aktuelt kun Analytisk Mekanik og Elektromagnetisme. Bevar adskilte formelsamlinger, udledningsnoter, opgavenoter og opgavesamlinger samt originale referenceversioner, forelæsningsnoter og eksamensmateriale. Tilføj kun senere kursusmapper, når faktisk kursusdeltagelse er dokumenteret.
- `02-fysikbibliotek/` indeholder brede generelle referencekompendier. Termodynamik og Statistik ligger her, ikke under universitetsfag. Statistik bruger Roger Barlow som hovedreference med selvstændig dansk tekst og verificeret notation/struktur, når bogen foreligger. Hold statistisk metode, statistisk fysik og matematik fagligt adskilt.
- Den tidligere termodynamikplan er kildegrundlag, ikke bibliotekets endelige afgrænsning. `Kursusplan_Termodynamik_2026.pdf` er autoritativ for det historiske gennemgåede stof, når filen kan læses. Udvidelser ud over denne afgrænsning markeres som generelt bibliotek, ikke som gennemgået pensum.
- Fælles kilde- og pensumregister ligger i `99-kilder-og-pensum/`; matematikkens egen kapitelplan i `00-matematik/PLAN.md`. Bevar præcise inkluderede/udeladte passager og delvise sidegrænser. Skeln mellem brugeroplysninger, læste originaler og emnemapping. Bibliotekets omfang begrænses ikke automatisk af en kursuskilde.
- Kursusnoter og generelle referenceværker er forskellige dokumenter. Overskriv aldrig kursusnoter med generelt stof. Genbrug fælles LaTeX-komponenter og fagligt egnede figurer med kildehenvisning. De øvrige fysikområder udfyldes ikke automatisk.
- Alle tidligere skabeloner og builds bevares, også termodynamikkens fire dokumenttyper og de otte arkiverede kvante-/relativitetsskabeloner. De er ikke dokumentation for nye aktuelle KU-kurser eller færdige kompendier.

## Konsoliderede standarder og fortsættelse
- Læs `README.md`, `ROADMAP.md`, `PENSUM.md` og `STATUS.md` før videre arbejde. Status er faktisk evidens; roadmap er plan; pensumregisteret bevarer præcise kildegrænser. Opdater dem ved relevante ændringer.
- Matematiske forklaringer integreres i hvert fysikfag sammen med fysisk fortolkning, notation og antagelser. Henvis til den generelle matematikteori uden at erstatte den lokale forklaring eller kopiere hele kompendieafsnit.
- Bevar eksisterende AM-, EM- og matematikoriginaler uændret. En kendt Drive-linktitel eller et fil-id er ikke bevis for læst indhold, korrekt PDF-format eller godkendt publiceringsdestination.
- Følg A4/11-punkts Latin Modern, 26 mm margin, fælles blå/rød stil, læsbare formler/tabeller, sidetal, sidehoveder, klikbar indholdsfortegnelse, krydshenvisninger og PDF-bogmærker. Brug underafsnit under store matematiske hovedemner.
- Omfattende forklarende tekst og originale matematiske vektorfigurer er faglige leverancekrav; mapper, overskrifter og skabeloner tæller ikke som gennemarbejdede kapitler. Hold planlagt, implementeret, lokalt verificeret og eksternt verificeret adskilt.
- Udvikl universitetsfagene efter dokumenteret pensum; bibliotekets generelle fysik må udvikles bredere med egne faglige planer. Gæt aldrig kursusdækning, bogindhold eller kildehenvisninger. Dokumenter uløste konflikter og bevar arbejdet.
- GitHub indeholder kilder og figurer; Drive er til færdige, godkendte PDF'er. Ingen automatisk overskrivning før mål, rettigheder og integration er konfigureret og testet. Test med fake API/offline-dry-run, ikke med produktionsfiler. Brug korte identitetsbaserede credentials og GitHub Secrets; aldrig nøgler i Git.
- Publicering må kun ske fra godkendte ændringer på beskyttet main med eksplicitte eksisterende fil-id'er; ingen dubletter. Bevar manuel udgivelse, backup og rollback. Et vellykket lokalt build beviser ikke en GitHub- eller Drive-kørsel.

- Ved migration bruges `git mv`; bevar matematik, figurer, originaler og tests. Opdater imports, builds, manifests, teststier, dokumentlinks og fremtidige Drive-destinationer. Kør alle PDF-builds, sikkerhedstests og link-/referencekontroller. Bevar stabile Drive-fil-id’er, publiceringsnøgler og deaktiveret publicering; foretag ingen automatiske Drive-flytninger.

- Drive-mapper og PDF-id’er registreret i `config/drive-targets.json` er brugeroplyste og ikke API-verificerede. Matematik-PDF’en ligger direkte under `00 Matematik`; øvrige mål følger hovedområde/fag. Aktivér ikke publicering, og overskriv, slet eller flyt ingen eksisterende Drive-filer under denne opgave. Bevar fil-id’er og links; ingen dubletter.

## Systematisk faglig udfyldning af matematikbindene
- Seneste beslutning om seks bind har forrang for ældre krav om kun én PDF-indgang; der oprettes ingen parallelle kapitelkilder eller kursusbøger.
- Følg `00-matematik/ALLE_BIND_UNDEREMNER.md` og den uddybende `BINDPLAN.md`. Arbejd kronologisk fra bind 1. Gå først til næste bind, når det foregående er fagligt og teknisk gennemarbejdet.
- Hvert underemne skal have intuition, præcis definition med betingelser, udledning af centrale formler, formelopslag, metodevalg, fysisk anvendelse og naturlige forbindelser i værket. Bevar eksisterende gennemarbejdet indhold.
- Brug original TikZ/PGFPlots, hvor det forklarer matematikken. Tilføj ikke SymPy-afsnit, programmeringsvejledninger eller gennemregnede opgaveeksempler.
- Arbejd på en særskilt branch fra `feat/studiearkiv-fundament` med konkrete indholdscommits. Kompilér det berørte bind og den samlede udgave; kontrollér nye sider visuelt. Skeln mellem gennemarbejdede underemner og blot eksisterende overskrifter.

## Bind 1: kortfattet lærebog og samlet formelregister
- Seneste opgave tillader fagligt begrundet omskrivning og omstrukturering af eksisterende bind-1-tekst. Bevar begreber og korrekt matematik; ingen parallelle versioner eller løsrevne tillæg.
- Prioritér korte forklaringer, præcise definitioner og betingelser, enkle relevante figurer samt korte metode-/fysikforbindelser. Længere udledninger bruges, når de bærer forståelsen. Ingen programmeringsvejledninger.
- Bind 1 bruger `bindet`-optionen i fællespakken: hvid baggrund, mørk tekst, én afdæmpet blå accent og tynde linjer. Bind 2–6 bruger fortsat standarddesignet; deres kilder og figurer ændres ikke som led i bind-1-opgaven.
- Centrale regler registreres med `\formel` ved deres faglige primærsted. Formelregisteret genereres fra dem; `make bind-1` skal kontrollere både linkdestination og registerets trykte sidetal, også ved sideskift.
- En udgivelses-PDF og dens metadata opdateres samlet efter build og visuel kontrol. De eksisterende Drive-id'er bevares; ingen upload uden verificeret destination, adgang og godkendelse.

## Visuel opslagsværdi i bind 1
- Prioritér mange relevante geometriske forklaringer frem for mere løbende tekst. Ved matrixoperationer vises så vidt muligt både matrix, geometrisk virkning og deres relation; brug fælles målestok, hvor længder/vinkler sammenlignes.
- Bevar enkle 2D-grafer, tynde streger, én blå accent, korte figurtekster og tydelige formelbokse. Ingen dekorative illustrationer, personlige eksempler eller 3D for 3D's skyld.
- Den visuelle udbygning foretages på en separat branch fra den aktuelle leveringsbranch. Bevar bind 2–6 og deres allerede eksisterende pilotindhold; »skeletter« er ikke en tilladelse til at slette tidligere arbejde.
