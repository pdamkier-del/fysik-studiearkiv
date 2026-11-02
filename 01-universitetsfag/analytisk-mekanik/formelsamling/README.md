# Analytisk Mekanik — formelsamling (LaTeX)

Den samlede formelsamling har én redigerbar kilde: `main.tex` og `chapters/01.tex` til `chapters/08.tex`. Grafikken er skrevet i TikZ/PGFPlots og kan redigeres. Den tidligere skabelon er bevaret som `template-original.tex`.

## Byg

Kør `make pdf` i denne mappe. Det kræver `latexmk`, LuaLaTeX og de TeX-pakker, der benyttes i `main.tex`. Resultatet er `build/main.pdf`. Kør `make check` til logkontrol. Gennemgå desuden hele den renderede PDF visuelt før publicering.

## Redaktionelt

Læs repositoryets `NOTESTANDARD.md` og `AGENTS.md` før dokumentændringer. Ret under det eksisterende emne; aldrig PDF-overlays eller indsatte tillægssider. Den hidtidige 28-siders aktive PDF i Drive er reference til tidligere indhold og figurer og må først erstattes efter en indholdsmæssig kontrol af rekonstruktionen. Kilden rummer samlet metode for centralkraft, Legendretransformation, genererende funktioner og Hamilton–Jacobi.
