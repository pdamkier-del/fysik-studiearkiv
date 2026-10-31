# Fysik-studiearkiv

Et langsigtet dansk studiearkiv med tre selvstændige hovedområder. GitHub bevarer LaTeX, noter og figurer; Google Drive er læse- og publiceringssted for færdige, godkendte PDF'er. Repositoryet følger brugerens oplyste hovedopdeling i Drive uden at flytte eller overskrive filer dér.

```text
00-matematik/              # ét samlet kompendium med 21 hovedemner
  main.tex, chapters/, figures/, PLAN.md
01-universitetsfag/        # kun aktuelle kursusnoter
  analytisk-mekanik/
  elektromagnetisme/
02-fysikbibliotek/         # brede referencekompendier
  klassisk-mekanik/
  elektromagnetisme/
  termodynamik/
  statistisk-fysik/
  statistik/
  kvantemekanik/
  relativitet-og-gravitation/
  optik-og-boelger/
  atom-og-molekylefysik/
  kerne-og-partikelfysik/
  faststoffysik/
  numeriske-metoder/
90-faelles/
99-kilder-og-pensum/
config/, scripts/, tests/, docs/
```

[Matematik](00-matematik/README.md) er et selvstændigt hovedområde med ét generelt LaTeX-kompendium, omfattende forklaringer, formler, udledninger og originale figurer. MatF1, MatF2, LinALys og Algebra integreres efter matematiske emner, ikke som separate kursusmapper eller PDF'er. Præcise ukendte kursusreferencer gættes ikke.

[Universitetsfag](01-universitetsfag/README.md) indeholder kun AM og EM med separate formelsamlinger, udledningsnoter, opgavenoter og opgavesamlinger samt pladser til forelæsningsnoter, eksamensmateriale og uændrede originaler. Nye fag oprettes først efter dokumentation for faktisk kursusdeltagelse. Eksisterende AM-/EM-originaler importeres kun, når de kan læses, og bevares uændret som referencer.

[Fysikbiblioteket](02-fysikbibliotek/README.md) er bredt og uafhængigt af aktuelle kurser. Termodynamik ligger her med den tidligere kursusplan som dokumenteret, afgrænset kildegrundlag og mulighed for senere udvidelse. Statistik ligger også her, selvstændigt fra statistisk fysik og fra matematik, med Roger Barlow som hovedreference. De øvrige fysikområder udfyldes ikke automatisk. Kursusnoter og generelle referencer vedligeholdes separat; fælles komponenter kan genbruges uden at overskrive noter.

## Faste dokumenter

[AGENTS.md](AGENTS.md) fastlægger projektregler, og **[NOTESTANDARD.md](NOTESTANDARD.md) skal læses før enhver ændring af noter og PDF'er**; den fastlægger den obligatoriske LaTeX-, layout- og kvalitetskontrol. [ROADMAP.md](ROADMAP.md) indeholder planen. [PENSUM.md](PENSUM.md) peger på kilder og præcise afgrænsninger. [STATUS.md](STATUS.md) skelner mellem faktisk indhold, implementering, verificerede resultater og blokeringer. [Migrationsrapporten](docs/migration-tre-hovedomraader.md) dokumenterer den seneste strukturændring.

## Byg og kontroller

Kør fra repositoryets rod med LuaLaTeX, latexmk, dansk Babel-orddeling, Latin Modern og PGFPlots. Python-kontroller kræver `python3 -m pip install -r requirements-tools.txt`.

```sh
make check              # samlet matematik-PDF og navigations-/logkontrol
make statistik          # eksisterende statistikstruktur i fysikbiblioteket
make templates          # alle 20 oprindelige skabelonbuilds
make repository-check   # lokale links, LaTeX-imports og referencer
make publication-check  # begge PDF'er, sikkerhedstests og offline-dry-run
```

Output er `build/00-matematik/main.pdf` og `build/02-fysikbibliotek/statistik/main.pdf`. Skabelonoutput spejler kildeplaceringerne under `build/`. Alle 20 builds bevares: otte aktuelle kursusskabeloner, fire bevarede termodynamikskabeloner samt otte arkiverede kvante-/relativitetsskabeloner. Mapper og skabeloner er ikke færdige noter. PDF'er og buildfiler versionsstyres ikke; `make clean` fjerner kun `build/`.

## Drive og publiceringsstatus

[config/drive-targets.json](config/drive-targets.json) registrerer brugerens eksisterende mappe-id'er og stabile PDF-fil-id'er. Matematik ligger direkte i sin hovedmappe; AM og EM under universitetsområdet; øvrige fag under fysikbiblioteket. Ukendte fil-id'er står som `null` og udløser afvisning, hvis et sådant dokument forsøges godkendt til publicering. Oplyste mapper og flytninger er ikke selvstændigt API-verificeret.

Publicering er fortsat deaktiveret. Ingen eksisterende Drive-filer er ændret eller dubleret. Før aktivering kræves verificerede mapper, rettigheder, filidentiteter, OIDC, GitHub Secrets/review og backup-/rollback-test. Se [Drive-vejledningen](docs/google-drive.md) og [originalregisteret](docs/originaler.md). GitHub Actions-definitionen bygger og kontrollerer artifacts; en faktisk GitHub-hostet kørsel er ikke verificeret her.

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

Alle 21 hovedemner samles i én PDF med underafsnit, klikbar indholdsfortegnelse og PDF-bogmærker. Integralregning er udbygget til et gennemarbejdet kapitel, og arbejdet med ordinære differentialligninger fortsætter på den nye sti. Det allerede udviklede differential- og trigonometriske indhold bevares. Se [PLAN.md](00-matematik/PLAN.md) og [kilderegisteret](99-kilder-og-pensum/README.md). Kvalitet styrer omfanget; 200–400 sider er et langsigtet mål, ikke et fyldkrav.
