# Eksisterende originaler på Google Drive

Links er oplyst af brugeren. Fil-id'erne er dokumentidentifikatorer, ikke adgangstokens. Indhold, faktisk filtype og version er endnu ikke verificeret: hentning fra Drive svarede HTTP 403 i miljøet. Linktitlernes »svg« bruges derfor ikke som bevis for filformatet.

| Original-id | Oplyst titel | Drive-fil-id | Faglig destination |
| --- | --- | --- | --- |
| ORIG-AM | Analytisk Mekanik – formelsamlingsvg | `1D0pjoV7JmySzJWmegeGOnvZoLxPrMQNA` | `01-universitetsfag/analytisk-mekanik/formelsamling/` |
| ORIG-MAT | Matematik – eksisterende kompendiumsvg | `1YjrsA63LHS96ShigE7u1i7_kU2zDjO4e` | Eksisterende hovedemner i `00-matematik/` |

- [Original AM-formelsamling](https://drive.google.com/file/d/1D0pjoV7JmySzJWmegeGOnvZoLxPrMQNA/view)
- [Originalt matematikkompendium](https://drive.google.com/file/d/1YjrsA63LHS96ShigE7u1i7_kU2zDjO4e/view)

Når indholdet er tilgængeligt, bevares en uændret original med kildehenvisning og checksum. Sammenhold afsnit, notation og eksisterende korrekt indhold før integration. Flyt ikke automatisk AM-stof ind i matematik eller omvendt. Opret ikke dubletter eller rekonstruktioner ud fra titlen.

Disse læsehenvisninger giver ikke i sig selv grundlag for automatisk versionsoverskrivning i Drive. Det skal særskilt afklares, om original-id'et også er den ønskede destination for fremtidige PDF-versioner, og om filtype og opdateringsrettigheder passer. Ingen Drive-filer er ændret.

## Migration til to hovedområder

Fil-id’erne ovenfor er bevaret uændret. AM- og EM-originaler tilhører universitetskursernes `originaler/` som uændrede referenceversioner, når de kan importeres. Matematikoriginalens konkrete indhold skal først læses for at afgøre, hvad der er kursusnoter, og hvad der er generelt referencestof. Ingen fil flyttes i Drive eller godkendes automatisk som bibliotekets publiceringsmål.

## Brugeropdatering: eksisterende destinationer

Brugeren har nu oplyst, at begge originaler er PDF’er og er flyttet til de ønskede mapper. Matematikfilen `1YjrsA63LHS96ShigE7u1i7_kU2zDjO4e` ligger efter brugerens oplysninger i `00 Matematik` (`1_mJgxHaXD8UcXcJ-pMCpi2mKHLjveXe-`). AM-filen `1D0pjoV7JmySzJWmegeGOnvZoLxPrMQNA` ligger i AM-mappen under universitetsområdet. De stabile id’er, indhold og links skal bevares. Destinationerne er registreret i [Drive-konfigurationen](../config/drive-targets.json), men hverken metadata, indhold eller rettigheder er kontrolleret via API her. EM-fil-id er fortsat uverificeret. Ingen Drive-fil er ændret af Codex.

## Bekræftet Drive-placering og identifikation, 27. oktober 2026

Brugeren præciserede, at de to dokumenter ovenfor er de AM-noter, som skal samles under **01 Universitetsfag / Analytisk Mekanik**. Metadata er nu læst fra de eksakte eksisterende Drive-fil-id'er, og den matematiske original er flyttet ved metadata-opdatering til samme AM-mappe uden at ændre indhold, navn eller id. Tidligere tekst i dette historiske register om en matematisk placering i `00 Matematik` er derfor overhalet af denne opdatering.

| Brugerbetegnelse | Eksisterende filnavn | Fil-id | Placering |
|---|---|---|---|
| AM_noter | Analytisk_mekanik_formelsamling.pdf | `1D0pjoV7JmySzJWmegeGOnvZoLxPrMQNA` | `01 Universitetsfag/Analytisk Mekanik` |
| AM_mat_noter | Matematik_notesark.pdf | `1YjrsA63LHS96ShigE7u1i7_kU2zDjO4e` | `01 Universitetsfag/Analytisk Mekanik` |

Matematik_notesark.pdf er en selvstændig historisk original med AM-relevant indhold. Den er **ikke** den generelle nye `00-matematik/main.tex`-bog og må ikke automatisk bruges som publiceringsmål for den nye matematik-PDF. PDF'erne er læst via vedhæftede originaler, men ingen redigerbar LaTeX-original er verificeret eller importeret. 
