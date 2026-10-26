# Fysik-studiearkiv

Et dansk, langsigtet LaTeX-arkiv til universitetsfysik. Første leverance er et fælles dokumentdesign, en intern struktur med 21 matematiske hovedemner og et udviklet pilotkapitel om differentialregning. De øvrige matematikkapitler er udtrykkeligt markeret som planlagte. Originale AM-/EM-noter er endnu ikke integreret. Oplyste pensumafgrænsninger og officielle kildehenvisninger er registreret særskilt med tydelig kontrolstatus i `99-kilder-og-pensum/`.

## Projektets faste dokumenter

- [AGENTS.md](AGENTS.md): permanente regler og designstandarder.
- [ROADMAP.md](ROADMAP.md): fag, dokumenttyper og videre udvikling.
- [PENSUM.md](PENSUM.md): dokumenterede kilder og afgrænsninger.
- [STATUS.md](STATUS.md): implementeret, verificeret, manglende og blokeret arbejde.

Repositoryet bevarer kildekode og figurer. Drive er læsested for de færdige PDF'er. Matematiske forklaringer integreres i hvert fysikfag, mens den generelle matematik samles i ét kompendium.

## Byg PDF

Kør fra repositoryets rod. Kræver TeX Live med LuaLaTeX, latexmk, luaotfload, Latin Modern, Babel med dansk orddeling, PGFPlots og de almindelige LaTeX-ekstrapakker. På Debian: `texlive-luatex texlive-latex-extra texlive-lang-european texlive-fonts-recommended latexmk`. PDF-kontrollen kræver Python 3 og PyMuPDF (`python3 -m pip install -r requirements-tools.txt`).

```sh
make pdf
make check
make templates
make statistik
```

Kompendiet ligger i `build/matematik/main.pdf`. `make check` kontrollerer den faktiske PDF for sider, bogmærker, links og forventet tekst og afviser logfiler med overfyldte bokse, manglende tegn eller uafklarede referencer. Visuel kontrol er stadig nødvendig. `make templates` kompilerer alle 20 faglige dokumentskabeloner. `make clean` fjerner kun `build/`.

## Struktur

- `00-matematik/`: kompendium, et kapitel pr. fil, egne vektorfigurer.
- `01-analytisk-mekanik/` og `02-elektromagnetisme/`: separate tomme skabeloner til formelsamling, udledningsnoter, opgavenoter og opgavesamling.
- `03-kvantemekanik/`, `04-termodynamik-statistisk-fysik/`, `05-relativitet-og-gravitation/`: samme udvidelige struktur.
- `06-statistik/`: selvstændig foreløbig kompendiestruktur med Barlow som grundbog; præcist pensum afventer.
- `90-faelles/`: fælles LaTeX-design, skabelon, notation og fælles figurer.
- `99-kilder-og-pensum/`: pensumregister for Matematik F, LinALys, en uafklaret matematik-ugeplan, termodynamik og statistik. Originale sidegrænser bevares uden gæt.
- `docs/`: redaktionel udviklingsvejledning, kapitelplan, Drive-procedure og kontrolrapport.

GitHub Actions bygger og kontrollerer PDF ved push og pull request og gemmer den som et artifact. Genererede filer og PDF'er versionsstyres ikke. Download PDF'en fra workflowets artifacts for læsning eller manuel Drive-opdatering.

Læs `AGENTS.md` før ændringer og `docs/udvikling.md` før nye kapitler. Langsigtet mål er 200–400 sider, men korrekthed og brugbarhed styrer omfanget. Drive-integrationen er under forberedelse og er ikke aktiveret; eksisterende filer må ikke overskrives under testen.

Alle matematikkurser integreres i ét dokument via `00-matematik/main.tex`; der oprettes ingen kursusspecifikke matematikkompendier. Statistik indgår ikke i matematikdokumentet. Statistisk metode ligger i `06-statistik/`, mens statistisk fysik forbliver under termodynamik.

## Matematikkompendiets hovedemner

1. Algebra og funktioner
2. Trigonometri
3. Komplekse tal og kompleks analyse
4. Differentialregning
5. Integralregning og standardintegraler
6. Rækker, konvergens og approksimationer
7. Ordinære differentialligninger
8. Partielle differentialligninger
9. Lineær algebra
10. Analytisk geometri i 2D og 3D
11. Flervariabel analyse
12. Vektoranalyse
13. Fourier- og Laplacetransformationer
14. Konvolution, deltafunktion og Greenfunktioner
15. Sturm–Liouville-teori
16. Specialfunktioner
17. Variationsregning
18. Numeriske metoder
19. Tensorregning
20. Differentialgeometri og matematik til GR
21. Gruppeteori og symmetrier

Hvert hovedemne har sin egen kildefil i `00-matematik/chapters/` og matematiske underafsnit. Én samlet PDF har klikbar indholdsfortegnelse og PDF-bogmærker. Se [den interne plan](docs/kapitelplan.md) og [pensumregisteret](99-kilder-og-pensum/README.md) for emnefordeling og præcise kildeafgrænsninger.
