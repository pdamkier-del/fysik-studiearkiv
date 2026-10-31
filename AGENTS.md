# Faste regler for fysik-studiearkiv

## Obligatorisk før enhver note- eller PDF-ændring
**Læs og følg [NOTESTANDARD.md](NOTESTANDARD.md) fra ende til anden før arbejdet.** Den fastlægger både didaktik, visuel stil og den tekniske proces. Redigér autoritative LaTeX-kilder og genkompilér hele dokumentet; PDF-overlay, indsatte løse tillægssider og små overlejrede tekstfelter er ikke acceptable som integrerede ændringer. Kontrollér alle sider visuelt samt indholdsfortegnelse, sidetal og links før publicering. Hvis kildekoden mangler, rapportér blokeringen og genskab en redigerbar kilde før større redigeringer. Bevar én aktiv Drive-version og arkivér gamle versioner.

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
- Genererede PDF'er og hjælpefiler skal ligge i `build/`, aldrig i Git-historikken. CI offentliggør PDF som artifact.
- Gem aldrig tokens eller hemmeligheder i repositoryet. Drive-opdatering er blokeret, indtil fil-id'er og adgangsrettigheder er fastlagt; brug eksisterende fil-id frem for at oprette dubletter.
- Brug det eksisterende checkout i cloudopgaver; opret kun worktrees efter udtrykkeligt ønske.
- Udfør ændringer i overskuelige commits. Rapportér præcist ændrede filer og kapitler samt udførte og ikke udførte kontroller.
- Spørg ikke om gentagen godkendelse af allerede aftalte tekniske standarder.

## Tre hovedområder (seneste brugerbeslutning)
- `00-matematik/` er matematik som selvstændigt hovedområde, ikke en undermappe af fysikbiblioteket. Bevar ét LaTeX-dokument med de eksisterende 21 hovedemner, forklaringer, notation, figurer, klikbar indholdsfortegnelse og PDF-bogmærker. MatF1, MatF2, LinALys og Algebra integreres efter emner, ikke som selvstændige kursusmapper eller kompendier. Gæt ikke præcise kursusidentiteter eller referenceækvivalenser.
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
