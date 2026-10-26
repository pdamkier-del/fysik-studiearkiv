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

## Pensum og fagskel
- Alle matematikkurser bidrager til `00-matematik/`; opret ikke separate kompendier for LinALys, Matematik F eller den uafklarede ugeplan.
- Bevar præcise inklusioner, undtagelser og delvise sidegrænser i `99-kilder-og-pensum/`. Skeln mellem brugeroplysninger, læste originalkilder og foreløbig emnemapping. Gæt ikke kapitelindhold uden indholdsfortegnelse eller tekst.
- `Kursusplan_Termodynamik_2026.pdf` er autoritativ for gennemgået termodynamikpensum, når den foreligger. Bevar sporbarhed til præcise kildesteder; organiser fagligt, ikke efter kalenderen.
- Statistisk fysik forbliver i `04-termodynamik-statistisk-fysik/`. Statistisk metode udvikles i `06-statistik/` med Roger Barlow som grundbog, selvstændig dansk tekst og verificeret notation/struktur, når den anvendte udgave er tilgængelig. Statistik må ikke indgå som kapitel eller særskilt PDF under `00-matematik/`; hele metodefaget ligger i `06-statistik/`.

- Matematik er ét samlet dokument med store matematiske hovedemner, underafsnit, klikbar indholdsfortegnelse og PDF-bogmærker. Opdater den eksisterende hovedemnestruktur og bevar indhold ved flytninger.

## Konsoliderede standarder og fortsættelse
- Læs `README.md`, `ROADMAP.md`, `PENSUM.md` og `STATUS.md` før videre arbejde. Status er faktisk evidens; roadmap er plan; pensumregisteret bevarer præcise kildegrænser. Opdater dem ved relevante ændringer.
- Matematiske forklaringer integreres i hvert fysikfag sammen med fysisk fortolkning, notation og antagelser. Henvis til den generelle matematikteori uden at erstatte den lokale forklaring eller kopiere hele kompendieafsnit.
- Bevar eksisterende AM-, EM- og matematikoriginaler uændret. En kendt Drive-linktitel eller et fil-id er ikke bevis for læst indhold, korrekt PDF-format eller godkendt publiceringsdestination.
- Følg A4/11-punkts Latin Modern, 26 mm margin, fælles blå/rød stil, læsbare formler/tabeller, sidetal, sidehoveder, klikbar indholdsfortegnelse, krydshenvisninger og PDF-bogmærker. Brug underafsnit under store matematiske hovedemner.
- Omfattende forklarende tekst og originale matematiske vektorfigurer er faglige leverancekrav; mapper, overskrifter og skabeloner tæller ikke som gennemarbejdede kapitler. Hold planlagt, implementeret, lokalt verificeret og eksternt verificeret adskilt.
- Udvikl fysikfagene efter dokumenteret pensum. Gæt ikke på fremtidige emner eller uoplyste lærebogspassager. Dokumenter uløste konflikter og bevar arbejdet.
- GitHub indeholder kilder og figurer; Drive er til færdige, godkendte PDF'er. Ingen automatisk overskrivning før mål, rettigheder og integration er konfigureret og testet. Test med fake API/offline-dry-run, ikke med produktionsfiler. Brug korte identitetsbaserede credentials og GitHub Secrets; aldrig nøgler i Git.
- Publicering må kun ske fra godkendte ændringer på beskyttet main med eksplicitte eksisterende fil-id'er; ingen dubletter. Bevar manuel udgivelse, backup og rollback. Et vellykket lokalt build beviser ikke en GitHub- eller Drive-kørsel.
