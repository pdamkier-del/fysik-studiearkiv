# Fysik-studiearkiv

Et langsigtet dansk studiearkiv med to selvstændige hovedområder: konkrete universitetskurser og et bredt matematik-/fysikbibliotek. GitHub bevarer LaTeX-kilder og figurer; Google Drive er læse- og publiceringssted for færdige, godkendte PDF'er.

## Struktur

```text
01-universitetsfag/
  analytisk-mekanik/
  elektromagnetisme/
  termodynamik-2026/
  statistik/
  pensum/
02-fysikbibliotek/
  matematik/                     # ét LaTeX-dokument, 21 hovedemner
  klassisk-mekanik/
  elektromagnetisme/
  termodynamik/
  statistisk-fysik/
  kvantemekanik/                  # bevarer tidligere skabeloner
  relativitet-og-gravitation/     # bevarer tidligere skabeloner
  optik-og-boelger/
  atom-og-molekylefysik/
  kerne-og-partikelfysik/
  faststoffysik/
  numeriske-metoder/
90-faelles/                       # LaTeX-design, notation og fælles figurer
config/                          # buildmanifest og deaktiveret publicering
scripts/, tests/, docs/
```

[Universitetsfag](01-universitetsfag/README.md) indeholder kun dokumenterede kurser og deres faktiske pensum, forelæsningsnoter, formelsamlinger, udledningsnoter, opgavenoter, opgavesamlinger og eksamensmateriale. Originale AM-/EM-formelsamlinger importeres først, når de kan læses, og bevares uændret som referenceversioner.

[Fysikbiblioteket](02-fysikbibliotek/README.md) er uafhængige, brede referenceværker. Et generelt mekanikkompendium er ikke AM-kursusnoterne; tilsvarende adskillelse gælder EM og termodynamik. Matematiske forklaringer indgår lokalt i fysikdokumenter, mens generel teori kan henvises til biblioteket. Fælles komponenter genbruges uden at overskrive kursusnoter.

Statistik er fortsat et selvstændigt universitetsfag med Roger Barlow som hovedreference. Der oprettes intet statistikbibliotek. Bibliotekets statistiske fysik er et andet fagområde.

## Faste dokumenter

- [AGENTS.md](AGENTS.md): permanente regler og designstandarder.
- [ROADMAP.md](ROADMAP.md): fag, dokumenter og prioriteret udvikling.
- [PENSUM.md](PENSUM.md): indgang til universiteternes præcise kilderegister.
- [STATUS.md](STATUS.md): faktisk implementering, kontrolresultater og blokeringer.
- [Migration](docs/migration-2026-10-27.md): flytninger, bevaring og konsekvenser.

## Byg og kontroller

Kør fra repositoryets rod. Kræver LuaLaTeX, latexmk, luaotfload, dansk Babel-orddeling, Latin Modern, PGFPlots og LaTeX-ekstrapakker. På Debian: `texlive-luatex texlive-latex-extra texlive-lang-european texlive-fonts-recommended latexmk`. Python-værktøjer installeres med `python3 -m pip install -r requirements-tools.txt`; Drive-afhængigheder kræves kun til den ikke-aktiverede integration.

```sh
make pdf                # bibliotekets samlede matematikkompendium
make check              # PDF, bogmærker, links og kompilationslog
make statistik          # universitetsfagets eksisterende statistikstruktur
make templates          # samtlige 20 bevarede fysikskabeloner
make repository-check   # lokale dokumentlinks, LaTeX-imports og referencer
make publication-check  # PDF'er, arkitekturkontrol, Drive-tests og offline-dry-run
```

PDF'er ligger i `build/02-fysikbibliotek/matematik/main.pdf` og `build/01-universitetsfag/statistik/main.pdf`. De 20 skabelonbuilds spejler deres kildemapper under `build/`. Manifestet `config/latex-templates.json` bevarer 12 kursusskabeloner og otte arkiverede biblioteksskabeloner. Skabeloner og mapper er ikke færdige fag. `make clean` fjerner kun genererede filer i `build/`.

GitHub Actions-definitionen bygger og validerer de samme dokumenter og gemmer deres PDF'er som artifacts. Faktisk GitHub-hostet kørsel er ikke verificeret her. Drive-publicering forbliver deaktiveret; originale fil-id'er er uændrede. Det fremtidige hierarki er arkivrod → hovedområde → fag → eksisterende PDF. Ingen Drive-mapper eller filer flyttes af migrationen. Se [Drive-vejledningen](docs/google-drive.md) og [originalregisteret](docs/originaler.md).

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

Hovedemnerne samles i én PDF med underafsnit, klikbar indholdsfortegnelse og PDF-bogmærker. [Bibliotekets kapitelplan](02-fysikbibliotek/matematik/PLAN.md) er uafhængig af kursusgrænserne i [pensumregisteret](01-universitetsfag/pensum/README.md). Det langsigtede mål er 200–400 sider; kvaliteten styrer omfanget. Differentialregningspiloten bevares, og trigonometri udbygges afgrænset. De øvrige generelle fysikkompendier skrives ikke i denne leverance.
