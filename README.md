# Fysik-studiearkiv

Et dansk, langsigtet LaTeX-arkiv til universitetsfysik. Første leverance er et fælles dokumentdesign, en disposition for 21 matematikkapitler og et udviklet pilotkapitel om differentialregning. De øvrige matematikkapitler er udtrykkeligt markeret som planlagte. Der er endnu ikke integreret originale AM-/EM-noter eller konkret KU-pensum.

## Byg PDF

Kør fra repositoryets rod. Kræver TeX Live med LuaLaTeX, latexmk, luaotfload, Latin Modern, Babel med dansk orddeling, PGFPlots og de almindelige LaTeX-ekstrapakker. På Debian: `texlive-luatex texlive-latex-extra texlive-lang-european texlive-fonts-recommended latexmk`. PDF-kontrollen kræver Python 3 og PyMuPDF (`python3 -m pip install -r requirements-tools.txt`).

```sh
make pdf
make check
make templates
```

Kompendiet ligger i `build/matematik/main.pdf`. `make check` kontrollerer den faktiske PDF for sider, bogmærker, links og forventet tekst og afviser logfiler med overfyldte bokse, manglende tegn eller uafklarede referencer. Visuel kontrol er stadig nødvendig. `make templates` kompilerer alle 20 faglige dokumentskabeloner. `make clean` fjerner kun `build/`.

## Struktur

- `00-matematik/`: kompendium, et kapitel pr. fil, egne vektorfigurer.
- `01-analytisk-mekanik/` og `02-elektromagnetisme/`: separate tomme skabeloner til formelsamling, udledningsnoter, opgavenoter og opgavesamling.
- `03-kvantemekanik/`, `04-termodynamik-statistisk-fysik/`, `05-relativitet-og-gravitation/`: samme udvidelige struktur.
- `90-faelles/`: fælles LaTeX-design, skabelon, notation og fælles figurer.
- `99-kilder-og-pensum/`: kildepolitik; originalmateriale registreres, når det foreligger.
- `docs/`: redaktionel udviklingsvejledning, kapitelplan, Drive-procedure og kontrolrapport.

GitHub Actions bygger og kontrollerer PDF ved push og pull request og gemmer den som et artifact. Genererede filer og PDF'er versionsstyres ikke. Download PDF'en fra workflowets artifacts for læsning eller manuel Drive-opdatering.

Læs `AGENTS.md` før ændringer og `docs/udvikling.md` før nye kapitler. Langsigtet mål er 200–400 sider, men korrekthed og brugbarhed styrer omfanget. Ingen automatisk Drive-skrivning er implementeret.
