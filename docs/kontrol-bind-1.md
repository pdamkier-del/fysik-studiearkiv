# Bind 1 – kvalitetskontrol og levering

Gennemgået 28. oktober 2026 på `feat/bind1-visuel-opslagsbog`, udgået fra den foregående levering `74136b1`. Den tidligere indholdsbranch er flettet ind med bevaret historik. Fagkilder og figurer er autoritative; [leverings-PDF](../00-matematik/udgivelser/bind-1.pdf) og [metadata](../00-matematik/udgivelser/bind-1.json) er afledte produkter.

## Faglig dækning

| Planlagte områder | Primær placering i bindet |
| --- | --- |
| Talområder, mængder, intervaller, logik og domæner | Kapitel 1, Tal, mængder og intervaller |
| Absolutværdi, afstand, fejlgrænser og uligheder | Kapitel 1, Absolutværdi og uligheder |
| Potenser, rødder, brøker, rationalisering og dimensioner | Kapitel 1, Potenser, rødder og brøker |
| Summer/produkter, geometriske summer, polynomier, binomial, division og rødder | Kapitel 1, Summer, produkter og polynomier |
| Ligninger, parametergrænser, kvadratkomplettering og partialbrøker | Kapitel 1, Ligninger og kvadratkomplettering; Partialbrøker |
| Domæne/codomæne/billede, injektivitet/surjektivitet/bijektivitet, invers og sammensætning | Kapitel 1, Funktioner og grafer |
| Paritet, monotoni, periodicitet, stykvise funktioner, graftransformationer og asymptoter | Kapitel 1, Funktioner og grafer |
| Eksponential/logaritmer, skalaer, vækst/henfald og følsomhed | Kapitel 1, Eksponential- og logaritmefunktioner |
| Konjugation, modulus, polarform, fase og komplekse rødder | Kapitel 1, Basal kompleks algebra |
| Radianer, cirkel, sinus/cosinus/tangens og standardværdier | Kapitel 2, Vinkler, enhedscirkel og standardfunktioner |
| Addition, dobbelt/halvvinkel, produkt/sum, grene, atan2 og alle løsninger | Kapitel 2, Identiteter; Inverse funktioner og trigonometriske ligninger |
| Amplitude/fase, harmoniske svingninger og hyperbolske funktioner | Kapitel 2, Amplitude, fase og harmoniske svingninger; Hyperbolske funktioner |
| Vektorrum, underrum, spænd, basis, dimension, afbildninger og basisskift | Kapitel 3, de første to hovedafsnit |
| Matrixoperationer, inverse, blokke, Gauss/Gauss–Jordan, rang, kerne, billede og LU | Kapitel 3, Matrixregning og inverse; Lineære ligningssystemer og elimination |
| Determinant, spor, egenværdier, multipliciteter, diagonalisering og matrixfunktioner | Kapitel 3, Determinant og spor; Egenværdier og diagonalisering |
| Indre produkt, ortogonalitet, projektion, Gram–Schmidt og spektralsætning | Kapitel 3, Indre produkter; Adjungering og spektralsætningen |
| Definithed, kvadratiske former, mindste kvadrater, QR, SVD, pseudoinvers og kondition | Kapitel 3, Kvadratiske former; Mindste kvadrater, QR og SVD |
| Matrixeksponential, generaliserede egenværdier, normalmoder og stabilitet | Kapitel 3, de sidste faglige hovedafsnit |

Alle planlagte underemner i bind 1 har nu fagtekst frem for dispositionsmarkører. Hovedresultater er ledsaget af gyldighedsbetingelser, metodevalg og centrale begrundelser. Nogle større sætninger anføres uden fuldt bevis, især algebraens fundamentalsætning og Sylvesters kriterium. Det er angivet eller afgrænset i teksten. Avanceret kompleks analyse, fuld Jordan-teori, numeriske algoritmer og uendeligdimensionale operatorers domæneteori hører fortsat til senere stof; de er ikke skjult som gennemarbejdede emner her. Ingen gennemregnede opgaveeksempler eller programmeringsvejledninger er indsat.

## Visuel kontrol

Samtlige 40 PDF-sider er renderet og visuelt gennemgået, herunder titelblad, læsevejledning/notation, tre siders indholdsfortegnelse, alle tre kapitler, 34 figurer og begge registersider. Endeligt rettede registersider er renderet og gennemgået igen.

Der er kontrolleret plads omkring formler, sideskift, tabeller, labels, åbne/lukkede intervalpunkter, radianer, grenvalg, orientering, geometriske proportioner og figurers relevans. Figurer, der delte løbende sætninger, er flyttet til eksplicitte afsnitsgrænser. Et for langt atan2-udtryk er sat på særskilt linje. Et PGFPlots-markørproblem er afhjulpet ved eksplicitte TikZ-punkter uden at deaktivere kontrol af manglende tegn. Den nye stil har hvid baggrund, mørk tekst og én afdæmpet blå accent. Den aktiveres kun med `bindet` i bind 1.

## Teknisk kontrol

- `make bind-1`: 40 sider, 73 bogmærker, 136 links og 60 nummererede formelregisterposter.
- Alle 60 registerlinks er kontrolleret mod både formelnummer, faktisk destinationsside og trykt sidetal. En fundet sideskiftsfejl i registerets sidetal er rettet; kontrollen er nu en del af `scripts/check_pdf.py --bind 1`. En negativ regression med manipuleret sidetal afvises.
- `make publication-check`: samlet udgave på 85 sider og statistikstruktur på 9 sider; kilde-/link-/referencekontrol; alle 15 eksisterende sikkerhedstests; syntetisk offline-publiceringsplan. Ingen Google API-kald i testene.
- `make alle-bind`: alle seks bind består deres egne log-/emne-/navigationskontroller. Dette er ikke en faglig færdigmelding af bind 2–6.
- `make templates`: alle 20 bevarede fysikskabeloner består efter ændringen af den fælles pakke.
- Ingen overfyldte bokse, manglende tegn eller uafklarede referencer i de kontrollerede builds. Bind 1's tidligere dobbelte sideanker ved titelbladet er også rettet.
- Samtlige kapitler, figurer og bindindgange indlæst af bind 2–6 er bytevis uændrede i forhold til `74136b1` (henholdsvis 13, 8, 5, 5 og 3 LaTeX-kilder). Standarddesignet i pakken er bevaret; det nye design er opt-in.

## Matematisk kontrol

Fremstillingerne er gennemlæst med vægt på nulværdier, fortegn, nævnere, domæner, konjugation, basisvalg og dimensioner. Supplerende, uafhængige beregningsstikprøver består for 200 trigonometriske/hyperbolske/fasevalg samt 50 komplekse matrixsæt med basisskift, adjungering i ikke-ortogonal basis, rangdefekt SVD/pseudoinvers, pivotkonvention for LU og generaliserede normalmoder. Eksakte rationale partialbrøksidentiteter, diagrammets to-massesystem og en Jordan-eksponential er desuden kontrolleret. De tidligere eksakte algebraiske stikprøver bevares som historisk kontrol. Beregningskontrol er støtte til de skrevne udledninger, ikke et generelt formelt bevis.

## Afgrænsning af leveringen

Der er ingen kendte udestående build-, navigations- eller layoutfejl i den leverede bind-1-PDF. Præcise manglende kursusoriginaler og kildeafgrænsninger ændres ikke af det generelle lærebogsarbejde; se [PENSUM.md](../PENSUM.md). Der påstås ingen ekstern fagfællebedømmelse eller verificeret GitHub-hostet CI.

Drive-publicering er deaktiveret. Der er hverken uploadet, overskrevet eller flyttet filer i Drive. Bind-1-destinationens fil-id og skriveadgang er ikke verificeret, så den versionsstyrede PDF leveres til manuel overførsel. Eksisterende stabile fil-id'er og alle godkendelsesflag er bevaret.

## Visuel udvidelse i denne levering

16 nye figurer er føjet direkte til de eksisterende kapitler, uden parallelle versioner. Funktionernes atlas indeholder fire paneler; inverse bruger en geometrisk korrekt spejling med samme akseskala; asymptoter vises med adskilte grafgrene. I trigonometri kobles cirkel, tangens, grafer og drejede komponenter. Komplekse rødder er jævnt fordelt. Lineær algebra kobler matrix og geometri ved basisskift, rotation, projektion, spejling og determinantens arealskalering. Kvadratiske niveaukurver skelner positiv definithed fra indefinithed. Alle 60 centrale opslag har tynde blå formelbokse, kun aktiveret i bind 1.

Samtlige 40 sider er gennemgået visuelt; de to sider omkring den efterfølgende justering af rodfiguren er desuden renderet og gennemgået igen. De nye koordinater er kontrolleret mod rotationsortogonalitet/determinant, additionsformler, komplekse rødder, arealfaktor 3, det viste basisskift, ellipse-/hyperbelniveaer samt projektion/spejlingsmatricer. Den eksisterende matematiske emnedækning og 60-posters register er bevaret.

Den afsluttende detailkontrol har desuden flyttet etiketterne for $\cos\beta$ og den nye basisvektor, så de ikke overlapper vinkelbuer og hjælpelinjer. De to berørte sider er renderet og gennemgået igen; sidenummereringen er uændret.
