# Faktisk projektstatus

Status er evidensbaseret, ikke en liste over ambitioner. Genereret PDF, kildefiler, lokal validering, GitHub-hostet CI og Drive-publicering er forskellige resultater. Se [ROADMAP.md](ROADMAP.md) for planen og [PENSUM.md](PENSUM.md) for kilder.

## Implementeret

- Ét matematikdokument med 21 hovedemner og egne underafsnit, herunder særskilt trigonometri og bevaret kompleks analyse. Statistik er fjernet fra matematikindgangen; det tidligere statistikindhold var kun dispositioner, hvis emner nu bevares i det selvstændige fag.
- Pilotkapitel om differentialregning med definitioner, antagelser, formeltabeller, restled, numerisk fejlanalyse og fire originale PGFPlots-figurer. Øvrige matematikemner er dispositioner, ikke færdige kapitler. Filflytninger bevarer pilotkapitlet; interne kapitelhenvisninger bruger labels.
- Fælles LaTeX-design med klikbar navigation og PDF-bogmærker. 20 tomme fysikskabeloner fordelt på fem fag og fire dokumenttyper. Ingen færdige AM-/EM-noter er integreret.
- Statistikstruktur med seks redaktionelle arbejdsområder; ingen færdige statistikkapitler eller verificeret Barlow-kapitelmapping.
- Fagligt organiseret termodynamikplan og kilderegister for FV/EMM, LinALys, den uafklarede ugeplan, termodynamik, Barlow og Drive-originaler.
- Lokale byggekommandoer, PDF-kontrol og GitHub Actions-builddefinition. PDF'er og hjælpefiler er ignoreret i Git.

## Verificeret før denne konsolidering

- Lokal matematisk PDF-build og `make check`: 38 sider, 123 bogmærker og 125 links efter hovedemneomlægningen; ingen overfyldte bokse, manglende tegn eller uafklarede referencer.
- Selvstændig statistikstruktur kompilerer til 9 sider. Dette validerer teknisk struktur, ikke et færdigt statistikfag.
- Alle 20 fysikskabeloner kompilerede under den oprindelige fundamentkontrol. Fællesstilen og disse skabeloner er ikke ændret ved denne konsolidering.
- Den tidligere pilot-PDF blev visuelt gennemgået. Den nyligt omordnede PDF skal også gennemgås visuelt før endelig levering af de igangværende ændringer.
- Tidligere Git-push fungerede. PR-oprettelse via GitHub-API var blokeret med `Forbidden`; ingen oprettet PR er verificeret.

## Igangværende opgave, endnu ikke afsluttet

Drive-publicering forberedes efter brugerens seneste instruktion. Et uploaderudkast, manifest med alle dokumenter sat til `approved: false` og fake-HTTP-tests findes i arbejdsområdet. Uploaderens testresultater, den endelige workflowkobling og rollback skal verificeres, før de beskrives som implementerede og lokalt testede. Der er ikke foretaget Drive-skrivning. Ingen produktionsintegration eller rigtig OAuth/Drive-opdatering er verificeret.

## Blokeringer og manglende input

- Autoritativ termodynamik-PDF mangler lokalt. FV/EMM-tekster og indholdsfortegnelser, Barlow-udgave og præcist statistikpensum mangler.
- KU-kursusbeskrivelsen og Drive-downloads svarede HTTP 403. Den uafklarede ugeplans fulde reference mangler. Disse dokumenter er ikke læst.
- AM- og matematik-id'er er kendt som originalhenvisninger; filtype, indhold, destinationsrolle, ejer, mappehierarki og opdateringsrettigheder er ikke verificeret. EM-fil-id og original mangler.
- GCP-projekt, Drive API, Workload Identity Federation, dedikeret servicekonto, GitHub Secrets/environment, beskyttet main og godkendelsesprocedure er endnu ikke konfigureret/verificeret.
- GitHub-hostet CI og snapshotrestaurering i en helt ny cloudopgave er ikke verificeret. Ingen miljøpublicering påstås.

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

Der er ingen uløst konflikt, som kræver sletning af eksisterende arbejde. Uafklarede kilder og adgangsforhold bevares som åbne punkter frem for gæt.

## Fortsættelse

Afslut den allerede igangværende PDF-/Drive-forberedelse med lokale sikkerhedstests og visuel PDF-kontrol. Opdater denne status med faktiske resultater, commit og push på den eksisterende featurebranch. Publicer ikke ufærdige kompendier eller eksisterende Drive-originaler. Start derefter med kildeafklaring og den prioriterede faglige udvikling i ROADMAP; genstart ikke projektet.

`docs/kontrolrapport.md` beskriver den første leverance og er historisk. Dens tidligere sidenumre og bogmærketal er ikke den aktuelle status efter strukturændringer.
