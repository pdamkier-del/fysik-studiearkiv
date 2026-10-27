# Plan for det samlede matematikkompendium

`00-matematik/main.tex` bygger den samlede udgave; `volumes/bind-1.tex` til `bind-6.tex` bygger seks emnebind fra præcis de samme kapitelkilder. Se [bindplanen](BINDPLAN.md) og [underemnerne](ALLE_BIND_UNDEREMNER.md). Hvert hovedemne har én kapitelkilde i `chapters/` og kan udbygges med underafsnit eller flere underkapitelkilder via `\input`, uden at der oprettes nye kursusmapper eller parallelle kompendier. Klikbar indholdsfortegnelse og PDF-bogmærker afspejler strukturen. Hovedemnernes rækkefølge er faglig, ikke kursus- eller datobaseret.

Differentialregning er det eksisterende pilotkapitel og bevares. Trigonometri udbygges med et første sammenhængende afsnit; integralregning er nu et udviklet kapitel; de resterende hovedemner er fortsat dispositioner. Hvert færdigt afsnit skal have introduktion, definitioner, symboler, centrale formler, egenskaber, gyldighedsbetingelser, begrebsforbindelser og relevante fysikanvendelser og figurer. Den oprindelige trigonometri-disposition er flyttet samlet til et selvstændigt hovedemne. Komplekse tal og kompleks analyse behandles sammen med tydelige underafsnit, så det eksisterende analysestof bevares.

Statistik indgår ikke i matematikkompendiet. Den tidligere, endnu ikke fagligt udfyldte statistikdisposition er fordelt på de eksisterende arbejdsområder i `02-fysikbibliotek/statistik/`; den indlæses ikke længere af matematikdokumentet. Ingen statistiske noter eller formler er slettet: den gamle kilde indeholdt kun overskrifter og dispositionsmarkører.

## 01-algebra · Algebra og funktioner

- Talområder, ligninger og uligheder
- Funktioner, inverse funktioner og sammensætning
- Eksponential- og logaritmefunktioner

## 02-trigonometri · Trigonometri

- Trigonometriske identiteter og hyperbolske funktioner
  - Radianer og enhedscirklen
  - Addition, dobbeltvinkler og produkter
  - Inverse funktioner og valg af gren
  - Hyperbolske funktioner
  - Faser og fysiske størrelser

## 03-komplekse-tal-og-analyse · Komplekse tal og kompleks analyse

- Komplekse tal, argument og grene
- Holomorfi og Cauchy–Riemann
- Analytiske og harmoniske funktioner
- Potensrækker og komplekse Taylorudviklinger
- Konturintegration og Cauchys sætning
- Laurentrækker, singulariteter og residuer
- Konforme afbildninger

## 04-differentialregning · Differentialregning

- Grænseværdier, kontinuitet og lokal adfærd
- Den afledte og differentialet
- Regneregler og sammensatte afhængigheder
- Standardafledte med definitionsområder
- Middelværdisætninger og globale konklusioner
- Højere afledte, monotoni og krumning
- Taylorudvikling og kontrollerede restled
- Grænseværdier og l'Hôpitals regel
- Fysisk fortolkning og følsomhed
- Numerisk differentiation og fejlbalance
- Metodeoverblik og kontrolpunkter

## 05-integralregning · Integralregning og standardintegraler

- Stamfunktioner og analysens hovedsætning
- Substitution, partiel integration og partialbrøker
- Standardintegraler med gyldighedsbetingelser
- Uegentlige integraler og parameterintegration
- Bestemte standardintegraler og specialfunktioner
- Numerisk integration og dokumenteret fejlkontrol
- Metodevalg, dimensioner og faglig kontrol

## 06-raekker · Rækker, konvergens og approksimationer

- Følger, punktvis og uniform konvergens
- Konvergenskriterier og potensrækker
- Taylor- og Fourierrækker
- Asymptotiske rækker og fejlkontrol

## 07-ode · Ordinære differentialligninger

- Eksistens, entydighed og begyndelsesbetingelser
- Førsteordensligninger og integrerende faktor
- Andenordensligninger, dæmpning og drivning
- Lineære systemer og fundamentalløsninger
- Stabilitet, faseportrætter og perturbation
- Randbetingelser og metodeoverblik

## 08-pde · Partielle differentialligninger

- Klassifikation og randbetingelser
- Separation af variable
- Varme-, bølge- og Laplaceligningen
- Karakteristikker og svage løsninger

## 09-lineaer-algebra · Lineær algebra

- Vektorrum, basis og lineære afbildninger
- Determinanter, rang og lineære ligninger
- Egenværdier og diagonalisering
- Indre produkter, spektralsætning og SVD

## 10-geometri · Analytisk geometri i 2D og 3D

- Linjer, planer og afstande
- Keglesnit og kvadrikker
- Parametriserede kurver, krumning og torsion
- Koordinatsystemer og orientering

## 11-flervariabel · Flervariabel analyse

- Differentiabilitet, Jacobimatrix og kæderegel
- Hessian og kritiske punkter
- Implicitte funktioner og Lagrangemultiplikatorer
- Integration i krumme koordinater og Jacobideterminant

## 12-vektoranalyse · Vektoranalyse

- Gradient, divergens og rotation
- Kurve- og fladeintegraler med orientering
- Gauss og Stokes med forudsætninger
- Ortogonal krum koordinatnotation

## 13-transformationer · Fourier- og Laplacetransformationer

- Konventioner, normalisering og enheder
- Fouriertransformation og inversion
- Laplace og konvergensområder
- Parseval, spektra og differentialoperatorer

## 14-green · Konvolution, deltafunktion og Greenfunktioner

- Testfunktioner og distributioner
- Deltafunktionen og koordinatskift
- Konvolution og fundamentalløsninger
- Greenfunktioner, randbetingelser og kausalitet

## 15-sturm-liouville · Sturm–Liouville-teori

- Selvadjungerede operatorer og vægtfunktion
- Randbetingelser og randled
- Ortogonalitet, spektrum og fuldstændighed
- Egenfunktionsudvikling og Greenkerner

## 16-specialfunktioner · Specialfunktioner

- Gamma- og betafunktionen
- Besselfunktioner og cylindrisk symmetri
- Legendre og sfæriske harmoniske
- Hermite, Laguerre og ortogonalitet

## 17-variation · Variationsregning

- Funktionaler og første variation
- Euler–Lagrange og randbetingelser
- Bivariable, bindinger og multiplikatorer
- Symmetrier og Noethers sætning

## 18-numerik · Numeriske metoder

- Afrunding, kondition og stabilitet
- Rodfinding og lineære systemer
- Interpolation, differentiation og kvadratur
- ODE-integration, konvergens og fejlestimation

## 19-tensorer · Tensorregning

- Multilineære afbildninger og dualrum
- Indekser og transformationslove
- Kontraktion, symmetri og tensorprodukter
- Metrik, indeksflytning og orientering

## 20-differentialgeometri · Differentialgeometri og matematik til GR

- Mangfoldigheder og koordinatkort
- Tangentrum og dualrum
- Tensorer og koordinattransformationer
- Metrikker og linjeelementer
- Kovariant differentiation og Christoffelsymboler
- Paralleltransport og holonomi
- Geodæter og affin parameter
- Riemanntensor og fortegnskonvention
- Riccitensor og skalarkrumning
- Geodætisk deviation
- Killingvektorer og Lie-afledte
- Differentialformer og Hodge-dualitet
- Bianchi-identiteterne
- Lorentzgeometri og introduktion til GR

## 21-grupper · Gruppeteori og symmetrier

- Grupper, homomorfier og repræsentationer
- Liegrupper, Liealgebraer og generatorer
- Rotationer, SO(3) og SU(2)
- Symmetrier og bevarelseslove

## Illustrationsplan for differentialgeometri

Udvikl særskilte, matematisk kontrollerede figurer til overlappende koordinatkort og overgangsafbildninger; tangent- og cotangentbaser; metrik og linjeelement; paralleltransport langs to kurver; geodæter og nærliggende geodæters deviation; sektionskrumning og holonomi; integralstrømme og Killingvektorer; orientering, former og Hodge-dualitet; lyskogler og kausale kurver. Angiv signatur, orientering, dimension og eventuelle skematiske forenklinger i hver figurtekst. Udled ikke Lorentzgeometri fra euklidiske skitser uden forbehold.

## Pensumkilder og integration

Præcise afgrænsninger opbevares i [pensumregisteret](../99-kilder-og-pensum/README.md). Emner integreres ét sted i ovenstående struktur. Kildekoblingen er ikke en påstand om, at hele et hovedemne er kursuspensum eller færdigskrevet.

| Kilde og emne | Destination og integrationsregel |
| --- | --- |
| LinALys: grundlæggende analyse | Algebra og funktioner; Differentialregning; Rækker, konvergens og approksimationer |
| LinALys: differentialregning og integration | Udbyg eksisterende differential- og integralkapitler; bevar pilotkapitlet |
| LinALys: differentialligninger | Ordinære differentialligninger |
| LinALys: flervariabel calculus | Flervariabel analyse |
| LinALys: vektorrum, matricer og lineære afbildninger | Lineær algebra; matricer som repræsentationer med eksplicit basisvalg |
| LinALys: egenværdier og spektralsætningen | Eksisterende spektralafsnit med forudsætninger; SVD er en bredere arkivplan, ikke dokumenteret LinALys-pensum |
| UG-01 og UG-02: Cauchy–Riemann, analytiske og harmoniske funktioner | Komplekse tal og kompleks analyse |
| UG-03: potens-, Taylor- og Laurentrækker | Generel konvergensteori under Rækker; kompleks repræsentation under Komplekse tal og kompleks analyse. Lokale Taylorrestled bevares under Differentialregning |
| UG-04 og UG-05: singulariteter, residuer og konturintegraler | Udbyg de eksisterende afsnit under Komplekse tal og kompleks analyse |
| UG-06: konforme afbildninger | Nyt planlagt underafsnit under Komplekse tal og kompleks analyse |
| UG-07: Laplace- og Fouriertransformationer | Eksisterende transformationskapitel; Fourier-rækker behandles under Rækker |
| Matematik F: FV og EMM | Afventer indholdsfortegnelser/tekst før emnemapping. Alle oplyste inklusioner, undtagelser og delvise sidegrænser bevares i registeret |

LinALys-URL'en er officiel, men dens ordlyd kunne ikke hentes i miljøet (HTTP 403). Emnemappingen bygger derfor foreløbigt på brugerens oplysninger. Den uafklarede ugeplans kursusnavn og bogreference må ikke udfyldes ud fra lighed med andre kurser. Ingen bogkapiteltitler i FV eller EMM er gættet.

## Afgrænsning mod andre fag og eksisterende originaler

Statistisk metode udvikles udelukkende under `02-fysikbibliotek/statistik/` med Barlow som grundbog; statistisk fysik forbliver under `02-fysikbibliotek/termodynamik/`. Termodynamikkens præcise pensum afventer den autoritative kursusplan-PDF.

Det eksisterende matematikkompendium på Drive er registreret som original i [originalregisteret](../docs/originaler.md). Indholdet er endnu ikke læst pga. HTTP 403. Ved adgang skal dets kursus-/bibliotekstilhørsforhold først afklares. Generelt referenceindhold sammenholdes med bibliotekets eksisterende kapitler, mens egentlige kursusnoter bevares separat; der må ikke oprettes en konkurrerende matematiksamling eller overskrives en Drive-fil.

## Uafhængig biblioteksplan

Dette er en generel matematisk kapitelplan, ikke et KU-kursuskompendium eller en afgrænsning af eksamenspensum. Bredden kan udvides ud over kursernes dokumenterede pensum. Kursusnoter og originaler vedligeholdes separat; kildekoblingerne ovenfor er sporbarhed, ikke dokumentidentitet. Det første afgrænsede videreudviklingstrin om trigonometri med radianer, enhedscirkel, identiteter, inverse grene og hyperbolske funktioner er nu leveret; yderligere stof kan tilføjes trinvist.

## Leveret første trigonometriudvidelse

Hovedemne 2 har nu et udviklet første afsnit med generelle identiteter, definitionsområder, inverse grene, hyperbolske funktioner og fasefortolkning. Den originale enhedscirkelfigur forbinder projektioner med symboldefinitionerne. Det er selvstændigt biblioteksstof, ikke en import af ukendt kursusmateriale. Resten af kapitlet kan udbygges; de øvrige planlagte hovedemner er ikke automatisk færdige.

## Integralregning leveret i denne indholdsopgave

Kapitel 5 er udbygget med 60 standardintegralidentiteter/-familier, integrationsmetoder, reduktion, konvergens, parameterintegration og numeriske fejlgrænser. Fire originale figurer ledsager den forklarende tekst. Kapitlet er et udviklet første referencekapitel, ikke en erklæring om udtømmende dækning. Ordinære differentialligninger er efterfølgende udbygget som beskrevet nedenfor.

## Ordinære differentialligninger: udviklet første kapitel

Kapitel 7 er udbygget med lokale eksistens-/entydighedsbetingelser, maksimal fortsættelse, residualestimater, separation og tabte ligevægte, lineære førsteordensmetoder, Bernoulli/exakte former/Riccati, andenordensligninger, dæmpning og resonans, fundamentalmatrix/variation af konstanter samt stabilitet og perturbationsforbehold. Tre originale figurer viser retningsfelt, dæmpningsregimer og faseportrætter. Centrale identiteter og de viste lineære systemer er kontrolleret symbolsk. Kapitlet er et udviklet første referencekapitel; PDE-kapitlet og en udtømmende perturbations-/randværditeori er ikke færdigskrevet.

## Aktuel arbejdsrækkefølge: bind 1

Den seneste opgave prioriterer en systematisk gennemgang af bindene frem for nye infrastrukturlag. De første tre underemner i algebra er udbygget: tal og mængder; potenser, rødder og brøker; polynomier og binomialformlen. De efterfølgende eksisterende afsnit bevares, men er ikke dermed gennemarbejdet efter alle syv faglige krav. Næste trin er ligninger og kvadratkomplettering, derefter uligheder/absolutværdi og partialbrøker i underemneplanens rækkefølge. Den uddybende bindplan samler visse grundbegreber tidligere; den kræver ikke en ny parallel behandling af dem.
