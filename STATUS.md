# Aktuel projektstatus

## Seneste arbejde: systematisk bind 1, 27. oktober 2026

**Arbejdsbranch:** `feat/matematik-bind1-fagindhold`, oprettet fra `feat/studiearkiv-fundament` ved `e4e4d1b`. Det tidligere arbejde er hentet ved fast-forward og bevaret. Indholdet er gemt i `8cbaae5`; den nødvendige bindkontrol i `a6c10a3`. De ældre statusafsnit nedenfor er historik; dette afsnit har forrang ved modstridende antal sider og dokumentindgange.

### Implementeret fagligt indhold

De første tre underemner er gennemarbejdet i den fælles kilde `00-matematik/chapters/01-algebra.tex`:

1. **Tal og mængder:** talområder og konventioner, lukkethed og fuldstændighed, mængder og kvantorer, logiske betingelser, operationer og De Morgan, intervaller, produktmængder, definitionsmængder og reversible omskrivninger. Fysikbro til energitilladte positioner og diskrete besættelsestal.
2. **Potenser, rødder og brøker:** heltallige/rationale/reelle eksponenter med betingelser, rodgrene og absolutværdi, forkortning/fællesnævner, rationalisering, metodevalg, dimensionskontrol og fysiske skaleringer.
3. **Polynomier og binomialformlen:** grad og koefficienter, standardidentiteter med udledninger, endelige geometriske summer, binomialkoefficienter, polynomiumsdivision og entydighed, restsætning/faktorsætning, multiplicitet og konjugerede rødder. Fundamentalsætningen er udtrykkeligt anført uden bevis. Fysikbro til potentialsymmetri og karakteristiske polynomier.

Alle tre har forklaringer, definitioner, formelopslag, udledninger, metodevalg og forbindelser til resten af værket. To nye originale TikZ/PGFPlots-figurer viser intervalendepunkter og fortegn ved rodmultiplicitet. Den visuelle kontrol opdagede og rettede en farveindstillingsfejl, der først gjorde åbne intervalpunkter fyldte. Eksisterende fagligt indhold er bevaret; der er ingen gennemregnede opgaveeksempler, SymPy-afsnit eller programmeringsvejledninger.

### Lokalt verificeret

- Alle seks bind kompilerer og består emne-, log-, bogmærke- og linkkontrol (`make alle-bind`). De senere bind indeholder fortsat mange dispositioner: build er ikke faglig godkendelse.
- Bind 1: 29 sider, 60 bogmærker og 65 links. Underafsnit er klikbare i indholdsfortegnelse og bogmærker. Titelbladets sammenløbne bundtekst er rettet. De ændrede algebrasider, figurer, titelblad og indholdsfortegnelse er renderet og visuelt gennemgået.
- Samlet udgave: 79 sider, 136 bogmærker og 151 links. Ingen overfyldte bokse, manglende tegn eller uafklarede referencer i de kontrollerede PDF-logs. Sideantallet er en observation, ikke et kvalitetsmål.
- PDF-kontrollen havde tidligere kun krav for hele værket, som fejlagtigt afviste bindene. `--bind N` vælger nu relevante emner og minimumskrav til navigation. Den oprindelige kontrol af den samlede udgave er bevaret. Negative kontroller afviser forkert bind, indsat overfull-advarsel og fjernede bogmærker.
- De nye udledninger er matematisk gennemlæst med kontrol af nul, fortegn, nævnere, eksponentkonventioner, multiplicitet og enheder. Eksakte supplerende stikprøver består: 512 tripler af delmængder, 1.944 binomial-/potensforskelidentiteter og brøkregning med positive/negative tællere og ikke-nul nævnere. Stikprøver er ikke et formelt generelt bevis.
- `make publication-check` består: samlet matematik, statistikstrukturen på 9 sider, kilde-/reference- og linkkontrol, alle 15 eksisterende sikkerhedstests samt syntetisk offline-publiceringsplan. `check_repository.py --require-drive-disabled` bekræfter deaktiveret godkendelse. Ingen Google API-kald eller Drive-ændringer er foretaget.
- Fælles typografipakke og fysikkilder er uændrede. De 20 fysikskabelonbuilds er ikke genkørt i denne indholdsopgave; tidligere kontrol står nedenfor. GitHub-hostet CI er ikke verificeret her.

### Planlagt og næste trin

Bind 1 er **ikke færdigt**. Næste underemne er ligninger og kvadratkomplettering, efterfulgt af uligheder/absolutværdi, partialbrøker, funktioner/inverser og eksponential-/logaritmefunktioner. Bevar og udbyg de eksisterende afsnit frem for dubletter. Derefter følger trigonometri og den systematiske gennemgang af lineær algebra. Bind 2–6 skal først udbygges videre efter faglig og teknisk gennemarbejdning af bind 1.

Den seneste beslutning er seks bind og én samlet udgave fra samme 21 kapitelkilder. Ældre udsagn om kun én dokumentindgang er erstattet i regler og planer; separate kursuskompendier oprettes stadig ikke. Pensumafgrænsninger og kildestatus er ikke ændret af den generelle algebraudvidelse. Drive-publicering er fortsat deaktiveret.

---

# Historisk status før bindarbejdet

Opdateret 27. oktober 2026. Arbejdet fortsætter på `feat/studiearkiv-fundament`; integralregning blev leveret i `0ce2b53` efter `07a092a`. Seneste brugerbeslutning om tre hovedområder erstatter den tidligere todeling. [ROADMAP.md](ROADMAP.md) er plan; [PENSUM.md](PENSUM.md) og [kilderegisteret](99-kilder-og-pensum/README.md) angiver dokumentationsstatus.

## Aktuel struktur og faktisk indhold

- `00-matematik/`: ét samlet kompendium med 21 hovedemner. Differentialregningspiloten og trigonometri er bevaret. Integralregning er udbygget fra disposition til 11 gennemarbejdede sider med metodeforklaringer, konvergenskrav, 49 stamfunktionsidentiteter og 11 bestemte integralfamilier samt fire originale figurer. ODE er efter strukturcommit udbygget til et udviklet første kapitel på 8 sider. PDE og øvrige ufyldte hovedemner forbliver dispositioner.
- MatF1, MatF2, LinALys og Algebra integreres efter matematiske emner i det samme kompendium. Nye ukendte kursusreferencer eller ækvivalenser med Matematik F 2026 gættes ikke.
- `01-universitetsfag/`: aktuelt kun AM og EM. Separate formelsamlinger, udledningsnoter, opgavenoter og opgavesamlinger samt pladser til forelæsningsnoter, eksamensmateriale og uændrede originaler bevares. Der er ikke importeret originalnoter.
- `02-fysikbibliotek/`: brede referenceområder, herunder Termodynamik og Statistik. Statistik bygger fortsat på Roger Barlow og holdes adskilt fra statistisk fysik og matematik. Den eksisterende statistikstruktur er ikke et færdigt kompendium eller en verificeret Barlow-kapitelrækkefølge.
- Termodynamikkens fire skabeloner og dokumentpladser er bevaret. Den tidligere faglige kursusplan er bevaret som `KURSUSGRUNDLAG.md`, mens den generelle README ikke blev overskrevet. Det historiske kursusgrundlag begrænser ikke fremtidig bredde, men bredere stof må ikke markeres som gennemgået kursuspensum.
- De øvrige fysikkompendier udfyldes ikke automatisk. Otte arkiverede kvante-/relativitetsskabeloner bevares. Samtlige 20 oprindelige skabelonbuilds findes stadig i manifestet: otte AM-/EM-skabeloner, fire termodynamikskabeloner og otte arkiverede skabeloner.
- Kilde-/pensumregisteret ligger igen samlet i `99-kilder-og-pensum/`. Matematikken har egen `PLAN.md`. Kursusnoter, historiske kildeplaner og brede referenceværker holdes adskilt.

## Verificeret indhold og migration

- Integralregningskapitlet blev kompileret og gennemgået visuelt på alle 11 sider. 49 stamfunktionsidentiteter er kontrolleret ved symbolsk differentiation; negative ydre rodgrene er kontrolleret særskilt. 11 bestemte integralfamilier er stikprøvekontrolleret ved uafhængig højpræcisionskvadratur. Det er ikke en udtømmende formel bevisverifikation.
- Før ODE-udvidelsen var matematik-PDF'en 51 sider med 126 bogmærker og 135 links uden overfyldte bokse, manglende tegn eller uafklarede referencer.
- Den nye migration bevarer 131 registrerede eksisterende filer, inklusive den aktive ODE-tekst og tre figurkilder i arbejdsområdet. Alle 62 aktuelle LaTeX-kilder er kontrolleret for bevaring efter nødvendige stirettelser. Se [migrationsrapporten](docs/migration-tre-hovedomraader.md).
- Imports, buildkommandoer, artifactstier, workflow, teststier og dokumentlinks er migreret. Der er ikke oprettet en ny branch eller worktree. Fælles design og tidligere matematiske kapitler bevares.
- Alle 20 skabelonbuilds er kørt efter flytningen og består. Statistikstrukturen kompilerer fortsat til 9 sider. Mapper og skabeloner dokumenterer ikke færdige fag.
- Alle 13 tidligere sikkerhedstests er bevaret og består; to nye tests for direkte matematikdestination og afvisning af en ekstra matematisk undermappe består. I alt 15 sikkerhedstests, udelukkende med fake HTTP.
- Lokale Markdown-links samt LaTeX-imports og labels/referencer kontrolleres offline. Produktionsmanifestet forbliver deaktiveret; offline-planen bruger syntetiske id'er og ændrer ingen godkendelser.
- GitHub Actions-definitionen er migreret, men en faktisk GitHub-hostet kørsel er ikke verificeret. Ændringerne er ikke merged til main; tidligere PR-oprettelse via GitHub-API var blokeret med `Forbidden`.

## Afsluttet ODE-udvidelse og aktuel PDF

- Strukturændringen er gemt i `fc4e326`; integralregning i `0ce2b53`. ODE afsluttes i et separat indholdscommit på samme branch.
- Matematik-PDF'en er nu 58 sider med de samme 21 hovedemner, 128 bogmærker og 141 links. Integralregning fylder 11 sider; ODE 8 sider. Der er ingen overfyldte bokse, manglende tegn eller uafklarede referencer. Alle nye integral- og ODE-sider er renderet og gennemgået visuelt.
- ODE omfatter eksistens/entydighed, følsomhed, førsteordensmetoder, andenordensligninger, oscillatorrespons, lineære systemer, variation af konstanter, stabilitet, energi, perturbation og randbetingelsesforbehold. Tre originale figurer er tilføjet. Ingen gennemregnede opgaveeksempler er indsat.
- Symbolsk residualkontrol består for alle tre oscillatorregimer og responskernernes normalisering, resonansbetingelsen, Riccati-transformationen, variationsformlen ved konstante og variable koefficienter samt alle tre faseportrætmatricer og deres Liouville-determinanter. Dette supplerer matematisk gennemlæsning, men er ikke en udtømmende formel bevisverifikation.
- `make publication-check` består med begge PDF'er, 15 sikkerhedstests, kilde-/referencekontrol og offline-dry-run med syntetiske id'er. Statistikstrukturen er fortsat 9 sider. Alle 20 skabelonbuilds er desuden kørt efter migrationen og består. Aktuelt 62 LaTeX-kilder/imports og referencer er kontrolleret sammen med alle lokale Markdown-links.
- Fælles design, de tidligere kapitlers faglige indhold og alle oprindelige figurer bevares. Det generelle fysikbiblioteks øvrige kompendier er ikke udfyldt automatisk. Drive er urørt og publicering er deaktiveret.

## Drive: registreret, ikke aktiveret eller API-verificeret

[config/drive-targets.json](config/drive-targets.json) indeholder alle 15 mappe-/fil-id'er fra brugerens seneste opdatering. Matematik-PDF'en ligger efter brugerens oplysninger direkte i `00 Matematik`; AM-PDF'en i AM-mappen under universitetsfag. Begge stabile fil-id'er, deres indhold og links skal bevares. EM-fil-id og statistikfil-id er stadig ukendte og står som `null`.

Oplysningerne om eksisterende mapper og gennemførte flytninger kommer fra brugeren. Metadata, ejer, rettigheder og faktisk PDF-indhold er ikke verificeret via API her. Ingen Drive-autentificering, upload, flytning, overskrivning, sletning eller dubletoprettelse er foretaget som led i migrationen.

Alle publiceringsposter er `approved: false`. Produktionsworkflow kræver fortsat grøn build, main, featureflag og environment-review. Faktisk branchbeskyttelse, GCP/OIDC, Google-rettigheder, Secrets og backup-/rollbackadfærd skal verificeres før aktivering. De ikke-hemmelige destinations-id'er i Git er ikke adgangsnøgler. Se [Drive-vejledningen](docs/google-drive.md) og [originalregisteret](docs/originaler.md).

## Manglende materiale og eksterne blokeringer

- Originale AM-, EM- og matematikfiler er ikke læst/importeret. Tidligere hentning fra Drive gav HTTP 403. Brugerens seneste oplysning om filtype og placering er registreret, men er ikke en læsning af deres indhold.
- `Kursusplan_Termodynamik_2026.pdf` findes endnu ikke lokalt. Præcise sider og emnefordeling samt bogreference afventer originalen; den er fortsat autoritativ for historisk gennemgået stof.
- FV/EMM-indholdsfortegnelser/tekster, Barlow-udgave og den uafklarede ugeplans fulde reference mangler. KU-kursusbeskrivelsen gav tidligere HTTP 403. Eksisterende præcise FV-/EMM-afgrænsninger er bevaret uændret.
- MatF1, MatF2 og Algebra har ikke nye verificerede kursuskoder/sideafgrænsninger. De må ikke automatisk identificeres med Matematik F 2026 eller få egne kompendier.
- Rigtig Google API-adfærd, ETag, live-upload/rollback, GitHub-hostet CI og en ny cloudopgaves snapshotrestaurering er ikke verificeret. Der påstås ingen miljøpublicering.

## Beslutningshistorik og fortsættelse

1. Den oprindelige flade struktur blev konsolideret; statistik blev taget ud af matematikken.
2. `07a092a` indførte en todeling med matematik i referencebiblioteket og fire kurser under universitetsfag. Den historiske rapport bevares i [den tidligere migrationsrapport](docs/migration-2026-10-27.md).
3. Integralregning blev leveret i separat indholdscommit `0ce2b53`.
4. Den seneste brugeropdatering flytter matematik til eget hovedområde og Termodynamik/Statistik til fysikbiblioteket. Kun AM og EM forbliver aktuelle universitetsfag. Dette har forrang frem for tidligere mappe- og fagbeslutninger; intet eksisterende kildearbejde slettes.
5. Efter strukturcommit er den igangværende ODE-udvidelse afsluttet med kompilering, visuel gennemgang og referencekontrol til et separat indholdscommit. Fortsæt derefter matematikken trinvist; begynd ikke automatisk at skrive øvrige fysikkompendier.

Ingen gennemregnede opgaveeksempler tilføjes. Ingen Drive-publicering aktiveres. `docs/kontrolrapport.md` og den tidligere todelingsrapport er historiske; dette dokument angiver aktuel status.
