# Google Drive-publicering: forberedt, ikke aktiveret

GitHub bevarer LaTeX og figurer; Drive er læsested for færdige, godkendte PDF'er. Ingen Drive-fil er oprettet, flyttet eller overskrevet under udvikling/test. AM-, EM- og matematikoriginaler bevares. [Originalregisteret](originaler.md) indeholder kendte læsehenvisninger, ikke automatisk godkendte publiceringsmål.

## Implementeret forløb

`.github/workflows/pdf.yml` bygger og kontrollerer matematik og statistik på push og PR, tester uploaderens sikkerhedsgrænser med fake HTTP og kompilerer de 20 fysikskabeloner. PDF'er og aktuelle kompilationslogs gemmes i `validated-pdfs`-artifact. Et separat Drive-job afhænger af en vellykket build og validerer de downloadede PDF'er igen.

Drive-jobbet kræver `refs/heads/main`, et event som ikke er PR, repositoryvariablen `DRIVE_PUBLICATION_ENABLED=true` og GitHub environment `drive-production`. Det giver ikke i sig selv beskyttelse af main eller krav om review: disse indstillinger skal konfigureres i GitHub før aktivering. Alle dokumenter i `config/pdf-publication.json` er foreløbigt `approved: false`, fordi strukturudkast og pilotversioner ikke er godkendte færdige kompendier.

Uploaderen opdaterer kun eksisterende fil-id'er med Drive `files.update` (HTTP PATCH med media upload). Der findes ingen create-/delete-/move-kald. Manglende mapping, dubleret fil-id, forkert MIME-type, forkert mappe, manglende editoradgang eller manglende versions-/ETag-oplysninger stopper skrivningen. Den kontrollerer hovedområdets placering under arkivroden, fagmappens placering under hovedområdet og PDF'ens placering under fagmappen. Den flytter ikke originaler automatisk til en ny mappe.

Før hver opdatering downloades den eksisterende PDF og gemmes med fil-id, versionsnummer og SHA-256. En ændring under backup eller et mislykket `If-Match` stopper overskrivningen. Efter upload kontrolleres de hentede bytes mod den lokale PDF's checksum. Backup bevares også, når upload fejler. Flere dokumenter er ikke én atomisk transaktion: en senere fejl kan efterlade tidligere dokumenter opdateret, med backup til manuel rollback.

## Konfiguration, der mangler før aktivering

1. **Google Cloud og identitet.** Opret/vælg et GCP-projekt, aktivér Google Drive API og IAM Service Account Credentials API, og opret en dedikeret servicekonto. Konfigurér Workload Identity Federation for GitHubs OIDC-udsteder `https://token.actions.githubusercontent.com`. Begræns providerens attributbetingelser til repositoryet `pdamkier-del/fysik-studiearkiv`, ref `refs/heads/main` og environment `drive-production`. Bind kun den konkrete identitet til `roles/iam.workloadIdentityUser` på servicekontoen. Brug ingen downloadet JSON-privatnøgle og ingen domæneomfattende delegation.
2. **Drive-adgang.** Del kun den relevante arkivrod/fagmapper og de eksisterende PDF'er med servicekontoen med editorrettighed. Verificer reel skriveadgang til de enkelte filer; Google Cloud IAM giver ikke i sig selv adgang til Drive. Uploaderen bruger OAuth-scopet `https://www.googleapis.com/auth/drive`, da allerede eksisterende brugerfiler ikke nødvendigvis er tilgængelige med `drive.file`. Begræns rækkevidden gennem den dedikerede kontos konkrete Drive-delinger. Godkend scope/politik i organisationen, hvis nødvendigt.
3. **Mappehierarki.** Verificer én arkivrod, de to hovedområder `01-universitetsfag` og `02-fysikbibliotek`, og fagmapper under det relevante hovedområde, fx `analytisk-mekanik` og `matematik`. Første oprettelse/placering sker manuelt og separat; uploaderen opretter ikke mapper. Ændr ikke originals placering eller destination uden afklaring.
4. **Eksisterende fil-id'er.** Bekræft for hvert færdigt dokument id, faktisk PDF-format, titel, ejer, fagmappe og opdateringsrettigheder. AM-/matematiklinkene er endnu kun originalhenvisninger; EM-id mangler. For et helt nyt dokument skal dets første Drive-fil oprettes én gang separat og id'et derefter registreres. Gæt aldrig id'er, og opret ikke en ny fil ved hver kørsel.
5. **GitHub Secrets i environment `drive-production`.** Opret `GCP_WORKLOAD_IDENTITY_PROVIDER` (fuldt provider-resource-navn), `GCP_DRIVE_SERVICE_ACCOUNT` (servicekonto-email) og `DRIVE_TARGETS_JSON` (målmapping efter `config/drive-targets.example.json`, uden placeholderværdier). Disse værdier er primært konfiguration; de gemmes i Secrets for at undgå logning og holde mål adskilt fra kilderne. OIDC giver kortlivede tokens ved runtime; ingen adgangsnøgle skal gemmes i Git eller chat.
6. **Godkendelse.** Beskyt main med påkrævet PR-review og grøn buildkontrol. Konfigurer environment `drive-production` med required reviewers, prevention of self-review hvor tilgængeligt og deployment branch policy kun main. Beskyt også workflow, manifest og scripts med review. Uden disse faktiske GitHub-indstillinger er »kun godkendte ændringer« ikke verificeret.
7. **Læsende integrationstest.** Når konfigurationen er på plads, aktiver kun de konkret godkendte mål i manifestet via review. Kør den manuelle workflowtilstand `validate`: den validerer lokalt og foretager kun metadata-GET mod Drive. Kontrollér id'er, MIME-type, mapper og rettigheder. Den reelle Google-authentificering, ETag-understøttelse og upload/rollback er endnu ikke live-testet. Afprøv om nødvendigt media-opdatering og rollback på en særskilt disponibel test-PDF med et særskilt manifest; aldrig på originalerne. Produktionsaktivering kræver denne test og udtrykkelig godkendelse.
8. **Aktivering.** Sæt repositoryvariablen `DRIVE_PUBLICATION_ENABLED=true`, når ovenstående er konfigureret og godkendt. Push til main udgiver da kun manifestposter med `approved: true`, efter grøn build og environment-godkendelse. De nuværende ufærdige PDF'er må ikke godkendes blot for at få flowet til at køre. Sæt variablen til false igen for at deaktivere jobben.

Feltet `files` i målkonfigurationen bruger stabile dokumentnøgler, mens `areas` bruger hovedområderne, og `subjects` bruger fulde logiske stier som `02-fysikbibliotek/matematik` og `01-universitetsfag/statistik`. Tilføj først AM-/EM-PDF'er i buildmanifestet og workflowets artifactliste, når deres kilder og byggekommandoer foreligger og er testet. De tomme skabeloner er ikke publiceringsmål.

## Manuel publicering

GitHub Actions → **Build PDFs and prepare Drive publication** → **Run workflow**, vælg **main** og mode **validate** eller **publish**. Samme buildkrav, manifestgodkendelse, featureflag og environment-review gælder. En featurebranch kan ikke bruges til Drive-jobbet.

Uden aktiveret API-integration kan en godkendt PDF fortsat versionsopdateres manuelt i Drive: verificer det eksisterende fil-id, brug **Administrer versioner → Upload ny version**, og kontrollér at linket og den nye PDF virker. Opret ikke en ny fil, og brug ikke denne procedure til at omgå en uafklaret destination.

## Tilbagerulning

Ved opdatering gemmer workflowet artifactet `drive-backup` med de tidligere PDF-bytes og deres metadata. Standardretention er 90 dage, begrænset yderligere af repositoryets indstillinger. Det er ikke en permanent backup: download og bevar godkendte backups sikkert uden for Git, hvis længere retention kræves. Artifactadgang følger repositoryets adgang; et offentligt repository er ikke egnet til private originaler uden særskilt adgangsafklaring.

Manuel workflowkørsel på main med mode **rollback** og **backup_run_id** henter `drive-backup` fra den angivne tidligere kørsel i samme repository. Scriptet afviser ændrede checksums og id'er, der ikke svarer til de aktuelt godkendte mål. Det tager en ny backup af den nuværende version før gendannelse. Delvise backups gendannes ikke automatisk som et fuldt sæt; vælg og kontroller de berørte dokumenter separat. Workflowet kræver fortsat environment-review. Alternativt kan den verificerede backup uploades som ny version til samme id via Drives versionshåndtering.

## Lokale kontroller uden Drive-adgang

```sh
make check statistik
python scripts/check_repository.py
python scripts/validate_publication.py
python -m unittest discover -s tests -v
python scripts/check_publication_plan.py
python scripts/publish_drive.py
```

Sidste kommando er offline som standard. Med det nuværende manifest er der ingen godkendte dokumenter og ingen Drive-requests. `--check-remote` tilføjer læsende kontrol; kun et eksplicit `--apply` kan skrive. Lokale fake-HTTP-tests beviser sikkerhedsmekanismerne i koden, ikke Google API-kompatibilitet eller produktionsrettigheder.

## Arkitekturmigration 27. oktober 2026

Det fremtidige hierarki er arkivrod → hovedområde → fag → eksisterende PDF. Eksempelkonfigurationen har nu `areas` med de to hovedområders mappe-id'er og `subjects` med fulde fagstier. Gammel flad målkonfiguration afvises for godkendte dokumenter; der foretages ingen automatisk remapping eller flytning af eksisterende Drive-filer. En eksisterende PDF i en anden mappe skal afklares manuelt før aktivering, og dens stabile fil-id skal bevares.

Dokumentnøglerne `matematik` og `statistik` er bevaret, så backup/rollback og `files`-mapping fortsat identificerer samme dokumenter. De to kendte original-id'er står uændret i [originalregisteret](originaler.md). Ingen af dem er automatisk blevet et godkendt publiceringsmål. Produktionsmanifestet forbliver helt deaktiveret, og ingen autentificeret Drive-operation indgår i migrationstesten.

CI og `make publication-check` bruger nu `check_publication_plan.py` med midlertidigt godkendte kopier og udelukkende syntetiske id’er. Det kontrollerer hele build-/målplanen uden adgang til GitHub Secrets eller Drive, også når en senere produktionsversion får reelle godkendelser. Produktionsmanifestet ændres ikke. Migreringskontrollen kan desuden køres med `check_repository.py --require-drive-disabled`; dette er en eksplicit migrationskontrol og ikke en permanent blokering for senere, korrekt godkendt publicering.
