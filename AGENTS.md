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
