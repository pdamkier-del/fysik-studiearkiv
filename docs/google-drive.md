# Sikker publicering til Google Drive

Drive er læsested for færdige PDF'er; Git er kilden til LaTeX og figurer. Der er ikke aktiveret Drive-adgang, automatisering eller overskrivning.

## Første registrering

Fastlæg for hvert dokument det eksisterende Drive-fil-id, dokumenttitel, ejer og destinationsmappe. Verificer med læseadgang, at id'et peger på den rigtige PDF, og at den tiltænkte konto har opdateringsrettigheder. Opbevar en ikke-hemmelig dokument-til-fil-id-tabel i en lokal konfigurationsfil uden for Git, når de faktiske id'er foreligger. Ingen id'er gættes.

## Manuel procedure nu

1. Byg med `make check`, og kontroller PDF'en visuelt.
2. Åbn den eksisterende PDF i Drive, verificer titel og fil-id, og brug **Administrer versioner → Upload ny version**. Opret ikke en ny fil.
3. Kontroller, at det oprindelige link stadig virker, at sidetallet passer, og at den nye PDF kan læses. Bevar den tidligere version til tilbagerulning.

## Mulig API-integration senere

En særskilt opgave kan implementere en eksplicit dokument-til-fil-id-mapping og Drive API `files.update(fileId=..., media_body=...)`, aldrig `files.create` ved opdatering. Hent først filmetadata og rettigheder; afbryd ved manglende id, forkert MIME-type, identitetskonflikt eller manglende adgang. Brug mindst mulige OAuth-rettigheder, sikker hemmelighedslagring og eksplicit valg af opdatering. Tokens må ikke stå i Git, scripts eller logs. Kontrollér checksum/version efter upload, og bevar mulighed for gendannelse. Automatisk skrivning kræver først fastlagte id'er og rettigheder.
