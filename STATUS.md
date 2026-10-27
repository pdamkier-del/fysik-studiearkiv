# Faktisk projektstatus

Opdateret 27. oktober 2026. Migrationen tager udgangspunkt i `3bfca2c` på den eksisterende branch `feat/studiearkiv-fundament`. Ingen ny branch eller worktree er oprettet. Se [ROADMAP.md](ROADMAP.md) for planen og [PENSUM.md](PENSUM.md) for universiteternes kilder.

## Implementeret arkitektur

- `01-universitetsfag/`: kun de fire dokumenterede kurser Analytisk Mekanik, Elektromagnetisme, Termodynamik 2026 og Statistik. Kursernes faktiske pensum og noter vedligeholdes separat fra det generelle bibliotek. Der er ikke oprettet kursusmapper for mulige fremtidige fag.
- `02-fysikbibliotek/`: 12 planlagte referenceområder med eget fagligt omfang uafhængigt af kursusgrænser. Kun matematik har et generelt LaTeX-kompendium under udvikling; de øvrige generelle fysikkompendier er ikke skrevet.
- Matematik er fortsat ét dokument med 21 hovedemner. Differentialregningspiloten og de fire oprindelige figurer er bevaret. Trigonometri er nu udbygget med radianer, enhedscirkel, identiteter, inverse grene, hyperbolske funktioner og fasefortolkning samt en ny original TikZ-figur. Øvrige hovedemner er fortsat dispositioner.
- Statistik er alene et selvstændigt universitetsfag med Barlow som hovedreference og seks redaktionelle arbejdsområder. Der er intet statistikbibliotek og intet statistikkapitel i matematikdokumentet. Statistikstrukturen er ikke et færdigt fag eller en verificeret gengivelse af bogens struktur.
- Universiteternes kilderegister er flyttet til `01-universitetsfag/pensum/`. Matematikbibliotekets egen kapitelplan ligger i `02-fysikbibliotek/matematik/PLAN.md`. Kildekobling mellem dem betyder ikke, at et kursuskompendium og et generelt referenceværk er samme dokument.
- Der er bevaret 12 kursusskabeloner og otte tidligere kvante-/relativitetsskabeloner. De otte er arkiveret i de relevante biblioteksområder, ikke klassificeret som KU-kurser eller færdige generelle kompendier. Alle 20 indgår i `config/latex-templates.json`.
- Kurserne har særskilte pladser til forelæsningsnoter, eksamensmateriale og uændrede referenceoriginaler. Mapperne indeholder ikke importerede originaler eller færdige nye noter.
- Imports, byggekommandoer, manifests, teststier, Actions-artifactstier og lokale dokumentlinks er migreret. Fælles LaTeX-design, notation og tests er bevaret. Se [migrationsrapporten](docs/migration-2026-10-27.md).

## Verificeret efter migration

| Kontrol | Faktisk resultat |
| --- | --- |
| Bevaring før videre fagligt arbejde | Alle 86 eksisterende versionsstyrede filer bevaret på nye eller uændrede stier. Alle 54 oprindelige LaTeX-kilder sammenlignet med baseline efter kun stirettelser |
| Ren migrationsbuild, før trigonometriudvidelsen | Matematik bevarede 38 sider, 123 bogmærker og 125 links; statistik 9 sider, 19 bogmærker og 19 links |
| Matematik efter videreudvikling | 41 sider, 21 hovedemner, 123 bogmærker og 128 links; ingen overfyldte bokse, manglende tegn eller uafklarede referencer |
| Statistik | 9 sider med 19 bogmærker og 19 links; selvstændigt kursusdokument |
| `make templates` | Alle 20 oprindelige skabeloner kompilerer på nye stier. PDF'ernes faktiske skabelontekst og navigation er kontrolleret |
| Link-/referencekontrol | Alle 55 aktuelle LaTeX-kilder/imports og referencer samt alle lokale Markdown-links kontrolleret offline. Ingen manglende imports, labels eller interne dokumentmål |
| Sikkerhedstests | Alle 11 oprindelige tests bevaret og bestået; to nye tests af hovedområdehierarki og gammel flad målkonfiguration består. I alt 13 tests |
| Publiceringskontrol | Begge PDF'er valideres; offline-dry-run med syntetiske mål-id'er består uden credentials eller netværksrequests og uden ændringer af produktionsmanifestet |
| Deaktivering under migration | `check_repository.py --require-drive-disabled` består. Alle produktionsposter er `approved: false`; normal uploaderkørsel foretager ingen Drive-requests |
| Workflow | YAML er syntakskontrolleret; build/main/featureflag/environment-krav er bevaret. GitHub-hostet eksekvering er ikke verificeret |
| Visuel kontrol | Matematikdokumentets sider er renderet i oversigt; nye trigonometrisider, figur, tabeller og navigation er gennemgået ved læsbar opløsning |

Migration og videreudvikling er forskellige ændringer: den rene migration bevarede den oprindelige tekst, mens trigonometri derefter fik selvstændigt skrevet nyt biblioteksindhold. Ingen kursuspensumafgrænsninger er udvidet som følge af dette.

## Drive-forberedelse og sikkerhed

Workflow og uploader er implementeret og lokalt testet, men ikke aktiveret eller live-verificeret. Fremtidig logisk struktur er arkivrod → hovedområde → fag → eksisterende PDF. `areas` beskriver hovedområderne, og `subjects` bruger fulde fagstier. Gammel flad konfiguration kræver manuel verifikation; mapper og filer flyttes ikke automatisk.

Dokumentnøglerne `matematik` og `statistik` er bevaret, og de to kendte originale Drive-fil-id'er står uændret i [originalregisteret](docs/originaler.md). AM-/matematiklinks er stadig originalhenvisninger, ikke automatisk godkendte publiceringsmål. Der er ikke foretaget nogen autentificering, upload, oprettelse, flytning eller overskrivning mod Drive under migrationen. Testene bruger fake HTTP og offline-dry-run.

Uploaderen bevarer metadata-/mapperettighedskontrol, backup før skrivning, versionskontrol via ETag/If-Match, efterfølgende checksum og manuel rollback. Produktionsjob kræver fortsat grøn build, main, featureflag og environment; faktisk branchbeskyttelse og reviewerkrav skal konfigureres i GitHub. En ny offentliggørelse kræver review og godkendelse af dokumentets faktiske indhold, ikke blot et grønt skabelonbuild. Se [Drive-vejledningen](docs/google-drive.md).

## Udtrykkeligt ikke verificeret eller endnu manglende

- Originale AM-, EM- og matematikfiler er ikke importeret. Tidligere Drive-downloads gav HTTP 403. AM-/matematik-id'er er kendt; EM-original og -id mangler. Filformat, ejerskab, placering, destinationsrolle og opdateringsrettigheder er ikke verificeret.
- `Kursusplan_Termodynamik_2026.pdf` findes ikke lokalt. Præcise sideintervaller og emnefordeling afventer læsning. FV/EMM-indholdsfortegnelser/tekster, Barlow-udgave og præcist statistikpensum mangler. Den uafklarede ugeplans fulde reference er ikke verificeret.
- KU-kursusbeskrivelsen gav tidligere HTTP 403 og er ikke læst her. Registeret skelner mellem officielle kildehenvisninger og brugeroplyst emneindhold.
- Faktisk GCP/OIDC/Drive-adgang, GitHub Secrets, målmapper, beskyttet main og environment-review er ikke konfigureret/verificeret i denne opgave. En tidligere tilstedeværende ADC-variabel kunne ikke indlæses af google-auth; den dokumenterer ikke brugbar Drive-adgang. Ingen nøgle er lagt i Git.
- Rigtig Google API-adfærd, herunder ETag og live-upload/rollback, er ikke testet. Der er ikke offentliggjort en PDF eller flyttet en original.
- GitHub-hostet CI, en ny cloudopgaves snapshotrestaurering og miljøpublicering er ikke verificeret. Ændringerne er ikke merged til main. Tidligere PR-oprettelse var blokeret af GitHub-API'et med `Forbidden`; ingen oprettet PR påstås.
- De generelle fysikkompendier ud over matematik er planer. Kursusskabeloner, dokumentpladser og kilderegister er ikke gennemarbejdede kursusnoter.

## Beslutningshistorik og konflikter

| Tidligere instruktion/tilstand | Afklaring og behandling |
| --- | --- |
| Den oprindelige matematikplan havde statistik som kapitel | Den senere udtrykkelige beslutning fjerner statistik helt fra matematik. Dispositionsemnerne flyttes til statistikfaget; ingen faglige noter slettes |
| Første matematikstruktur samlede algebra og trigonometri | Seneste hovedemneplan giver trigonometri eget hovedemne i samme dokument; eksisterende trigonometrisk disposition flyttes med |
| »Komplekse tal« i hovedemnelisten og tidligere kompleksanalysepensum | Begge bevares i ét hovedemne med underafsnit. Der er ikke grundlag for at slette kompleks analyse |
| Barlows struktur ønskes bevaret, men udgave/indholdsfortegnelse mangler | Foreløbig redaktionel struktur markeres tydeligt; ingen bogkapitelrækkefølge eller notation gættes |
| Først ingen Drive-id'er, senere to links | De to original-id'er registreres; de bliver ikke automatisk publiceringsmål. EM-id er stadig ukendt |
| Automatisk Drive-publicering ønskes, men originalsikring og test kræves først | Forbered deaktiveret integration med godkendelseskrav; ingen eksterne writes under testen |
| Arkivet planlægger flere fag end dokumenteret pensum | Mapper er kun fundament. Fagligt indhold udvikles efter dokumentation; ingen fremtidige kurser markeres som gennemgået |
| Seneste arkitekturændring: flade fagmapper og bredt matematikkompendium | Konkrete kurser flyttes til universitetsområdet; generelle referencer til biblioteket. Kursusnoter og biblioteksstof er selvstændige dokumenter, også når emnet er det samme |
| Tidligere kvante-/relativitetsmapper uden dokumenteret kursus | Alle skabeloner bevares som arkiverede biblioteksskabeloner med fortsat buildkontrol; der opfindes ingen KU-kursusidentitet |

Den seneste brugerbeslutning om to hovedområder har forrang frem for den tidligere flade organisering. Ingen uløst konflikt kræver sletning af eksisterende arbejde. Ukendt originalindhold og kildetilhørsforhold afklares ved læsning, ikke ved gæt.

## Fortsættelse

Fortsæt matematikbiblioteket ét fagligt afsnit ad gangen, bevar differentialregningspiloten og det nye trigonometriindhold, og brug bibliotekets PLAN. Begynd ikke at skrive alle generelle fysikkompendier. Afklar og importer først universiteternes originalkilder, før kursusnoter udbygges pensumtro. Aktiver ikke Drive uden særskilt verificeret konfiguration og sikker integrationstest.

`docs/kontrolrapport.md` er historisk dokumentation for første leverance. Dens gamle sidetal og bogmærketal er ikke den aktuelle status. De fem roddokumenter er indgangen for fremtidige opgaver; ingen afhængighed af samtalehistorikken er nødvendig.
