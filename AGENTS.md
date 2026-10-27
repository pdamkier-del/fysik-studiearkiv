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
- Genererede PDF'er og hjælpefiler skal ligge i `build/`, aldrig i Git-historikken. CI offentliggør PDF som artifact.
- Gem aldrig tokens eller hemmeligheder i repositoryet. Drive-opdatering er blokeret, indtil fil-id'er og adgangsrettigheder er fastlagt; brug eksisterende fil-id frem for at oprette dubletter.
- Brug det eksisterende checkout i cloudopgaver; opret kun worktrees efter udtrykkeligt ønske.
- Udfør ændringer i overskuelige commits. Rapportér præcist ændrede filer og kapitler samt udførte og ikke udførte kontroller.
- Spørg ikke om gentagen godkendelse af allerede aftalte tekniske standarder.

## To adskilte hovedområder
- `01-universitetsfag/` indeholder konkrete dokumenterede KU-kurser. Begynd med Analytisk Mekanik, Elektromagnetisme, Termodynamik 2026 og Statistik. Opret kun nye kursusmapper, når kursusidentiteten er dokumenteret. Mapper med skabeloner dokumenterer ikke kursuspensum.
- Kursusdokumenter er pensumtro undervisnings-/eksamensmateriale med separate forelæsningsnoter, formelsamlinger, udledningsnoter, opgavenoter, opgavesamlinger, eksamensmateriale og uændrede referenceoriginaler.
- `02-fysikbibliotek/` indeholder selvstændige generelle referenceværker, hvis faglige omfang ikke begrænses af universiteternes pensum. Bibliotekets kompender og kursusnoter må aldrig sammenblandes eller overskrive hinanden. Genbrug gerne fælles komponenter og fagligt egnede figurer med kildehenvisning.
- Matematik er ét samlet biblioteksdokument i `02-fysikbibliotek/matematik/main.tex` med 21 hovedemner og underafsnit, omfattende forklaringer, formler, vektorfigurer og klikbar navigation. Der oprettes ikke separate matematiske kursuskompendier uden særskilt instruktion; universiteternes kilder kan kortlægges til biblioteksstoffet uden at gøre dem til samme dokument.
- Pensumregisteret er knyttet til universitetsfagene i `01-universitetsfag/pensum/`; bibliotekets egen kapitelplan er `02-fysikbibliotek/matematik/PLAN.md`. Bevar præcise inkluderede/udeladte passager, delvise sider, kildeidentitet og kontrolstatus. Gæt ikke indhold uden indholdsfortegnelse eller tekst.
- `Kursusplan_Termodynamik_2026.pdf` er autoritativ for det konkrete gennemgåede termodynamikpensum, når originalen foreligger. Registrer sporbarhed til kildesteder; organiser kursusstoffet fagligt, ikke efter kalenderen. Bibliotekets termodynamik og statistiske fysik udvikles uafhængigt.
- Statistisk metode er alene universitetsfaget `01-universitetsfag/statistik/`, baseret på Roger Barlow med selvstændig dansk tekst og verificeret notation/struktur. Der oprettes ikke et statistikbibliotek. Statistisk fysik er et særskilt generelt referenceområde og kan samtidig indgå pensumtro i termodynamikkurset.
- De tidligere kvante-/relativitetsskabeloner er bevaret som `arkiverede-skabeloner/` i biblioteket. De er hverken færdige generelle kompendier eller dokumenterede KU-kurser. Bevar deres builds.

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
