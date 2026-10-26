# Kontrolrapport · 26. oktober 2026

## Leverance og afgrænsning

Repositoryet var tomt og uden commits eller fjernbrancher. Første leverance etablerer 21 matematikkapitler, et selvstændigt pilotkapitel om differentialregning, fire originale PGFPlots-figurer, fælles dokumentdesign, permanente agentregler og 20 tomme faglige dokumentskabeloner. Detaljeret kapitelplan og en illustrationsplan til differentialgeometri findes i `kapitelplan.md`. Øvrige kapitler er dispositioner, ikke færdige noter.

## Udført kontrol

- `make check`: PDF på 38 sider, 124 bogmærker og 125 links. Pilotkapitlet fylder 10 sider (trykte sider 2–11).
- Logkontrol: ingen overfyldte bokse, manglende tegn eller uafklarede referencer. Dansk orddeling er indlæst fra `loadhyph-da.tex`.
- Alle sider er renderet og gennemgået i oversigt. Pilotkapitlets tekst, formeltabeller, fire figurer, billedtekster og sideskift er desuden gennemgået ved læsbar opløsning. Indholdsfortegnelsens nummerbredde og pilotkapitlets afsluttende kontrolafsnit er justeret efter gennemgangen.
- Figurernes sekant- og tangenthældninger, stationære punkter, Taylorrest og fejlmodellens minimum er kontrolleret mod de angivne udtryk. Ingen gennemregnede opgaveeksempler er tilføjet.
- Faglige skabeloner kontrolleres med `make templates`; genererede filer ligger i `build/` og er ignoreret af Git.

## Miljø

Cloudmaskinen havde LuaLaTeX og latexmk, men manglede luaotfload og dansk orddeling. Debians signatur- og checksumkontrollerede pakker er hentet med APT og udpakket lokalt uden systemændringer. Et lokalt Python-miljø bruger den fastlagte PyMuPDF-version. Miljøets gemte installations- og opstartsvejledning beskriver aktivering; ingen serverproces er nødvendig.

## Begrænsninger

GitHub Actions-filen er etableret, men en faktisk GitHub-hostet CI-kørsel er endnu ikke verificeret. Layoutkontrol og matematisk gennemlæsning er udført af samme forfatter; ingen uafhængig fagfællebedømmelse er påstået. Bibliografien er en liste over relevante kontrolværker, ikke verificerede henvisninger til brugerens pensum. Ingen originale AM-/EM-noter, Drive-fil-id'er eller Drive-rettigheder er modtaget. Drive-opdatering er kun beskrevet og udfører ingen netværksskrivning.
