# Plan: matematik i seks bind og én samlet udgave

**Status (27. oktober 2026):** Seks bindindgange og den samlede udgave genbruger de samme 21 kapitelkilder. Alle seks bind er nu kompileret og har bestået log-, navigations- og emnekontrol. Bind 1 har fået de første tre underemner gennemarbejdet og de berørte sider gennemgået visuelt. Det er **ikke** en faglig færdigmelding af bind 1 eller af de øvrige bind. Ingen Drive-filer er ændret. Aktuel evidens og næste emne står i [STATUS.md](../STATUS.md).

## Bind og eksisterende kapitelkilder

| Bind | Titel | Kapitelnumre |
|---|---|---|
| 1 | Algebra og lineær algebra | 01, 02, 09 |
| 2 | Calculus og analyse | 04, 05, 06, 11 |
| 3 | Differentialligninger | 07, 08, 14, 15 |
| 4 | Matematiske metoder | 03, 13, 16, 18 |
| 5 | Geometri og tensorer | 10, 12, 19, 20 |
| 6 | Variationsregning og symmetrier | 17, 21 |

Ovenstående dækker samtlige 21 kapitler præcis én gang. Rækkefølgen er en redaktionel læseinddeling og ændrer ikke den samlede bogs indholdsfortegnelse.

## Teknisk status og fortsat validering

- Bevar `00-matematik/chapters/*.tex` som **eneste kilde** for hvert kapitel.
- **Udført:** `volumes/bind-1.tex` til `bind-6.tex` inkluderer de eksisterende kapitelkilder uden kopier.
- Genbrug samme fælles typografi, makroer og hyperref-opsætning.
- **Kørt og lokalt kontrolleret:** `make bind-1` ... `make bind-6` og `make alle-bind`; `make pdf` bevares som samlet udgave.
- Opbevar hver PDF i et separat build-output, og valider bogmærker, indholdsfortegnelse, figurer, links og referencer.
- Revider tværbindsreferencer eksplicit. En reference til en udeladt label må ikke bare blive '??'; brug enten en kort tekstlig henvisning med bind og kapitel eller et verificeret eksternt PDF-link.
- Udgiv ikke bindene i Google Drive, før mål-id'er, godkendelse og særskilt publicering er verificeret.
- Statistik er fortsat et selvstændigt fag uden for matematikbindene.
- Matematik fra LinALys, MatF1, MatF2 og Algebra integreres efter emne, ikke som selvstændige kurser.

## Indholdsstatus

Et bind må ikke betegnes som færdiggjort blot fordi kapitlets fil er oprettet. Lineær algebra blev udbygget 27. oktober 2026 med definitioner og formelstof om baser, lineære afbildninger, rang, spektralteori og SVD. Den tidligere lineære algebraudvidelse er nu kompileret i bind 1 og den samlede udgave; den systematiske faglige og visuelle gennemgang af alle dens underemner afventer fortsat. Der må ikke påstås grøn build ud fra blot oprettede kildefiler.

## Bind 1 – første faglige udbygning 27. oktober 2026

- `chapters/01-algebra.tex` er udbygget fra overskrifter til forklarende referencekapitel om algebra, definitionsområder, ligninger, uligheder, funktioner, inverser, logaritmer, eksponentialfunktioner og fysiske skaleringslove.
- `figures/algebra-eksplog.tex` er en ny original PGFPlots-figur, indsat i kapitlet.
- `chapters/02-trigonometri.tex` har fået erstattet henvisninger, der pegede på afsnit uden for bind 1, med tekstlige krydsbindshenvisninger.
- `chapters/09-lineaer-algebra.tex` indeholder den tidligere udvidelse om vektorrum, baser, egenværdier, SVD mv.
- **Historisk kontrolstatus ved oprettelsen:** Kilderne blev først skrevet uden kompilering. Den senere kontrol nedenfor erstatter denne tekniske blokering; publicering er fortsat deaktiveret.

## Redaktionelt princip: én rød tråd gennem alle seks bind

De seks bind er **ét sammenhængende matematisk referenceværk**, ikke seks uafhængige kompendier. Referencer skal gøre det nemmere at forstå et senere emne ud fra tidligere begreber uden at gøre hvert kapitel afhængigt af konstant opslag.

- Forklar først et begreb klart i dets eget kapitel; henvis derefter kort til et tidligere fundament, hvor en forbindelse faktisk hjælper.
- Introducér avancerede begreber gennem velkendte specialtilfælde, men undgå at påstå, at to forskellige matematiske operationer er det samme.
- Brug en kort **Forbindelse til tidligere emner** eller **Videre anvendelse** kun hvor den har faglig værdi; ikke obligatorisk i hvert afsnit.
- Angiv bind og kapitel i selvstændige PDF'er; i den samlede bog kan verificerede LaTeX-krydsreferencer være klikbare. Ingen døde referencer.
- Prioritér kæderne algebra → lineær algebra → flervariabel analyse → tensorer → differentialgeometri; calculus → ODE/PDE → Fourier, Greenfunktioner og specialfunktioner; differentialregning/integration → variationsregning → Lagrange/Hamilton; egenværdier → koblede oscillatorer, randværdiproblemer og spektralteori.
- Bevar en læsevenlig forklaring af hvornår et værktøj anvendes og hvilke antagelser der gælder. Undgå at fremhæve enkeltstående eksempler som gennemgående tema, hvis de blot var illustrationer af ønsket om sammenhæng.

Dette princip gælder også for senere fysiknoter. Kursusnoterne i AM og EM forbliver selvstændige originaler.

## Bind 1 – fastlagt fuld faglig disposition (27. oktober 2026)

**Arbejdsrækkefølge:** Fastlæg samtlige relevante emner først; udbyg derefter kapitlerne i rækkefølge. De nuværende forklarende tekster bevares. Disposition er **ikke** ensbetydende med, at emnet er færdigskrevet.

### Del I: Algebra og funktioner
1. Talområder, mængder, intervalnotation, absolutværdi, uligheder og definitionsmængder.
2. Potenser, rødder, brøker, eksponentregler, rationelle eksponenter og dimensionskontrol.
3. Polynomier, faktorisering, kvadratsætninger, kubiksætninger, binomialformlen og polynomiumsdivision.
4. Lineære, kvadratiske og højeregradsligninger; diskriminant; kvadratkomplettering; rational- og rodsligninger; parameterafhængighed.
5. Partialbrøksopdeling: forskellige og gentagne lineære faktorer, irreducible andengradsfaktorer.
6. Funktioner: domæne/værdimængde, invers, sammensætning, graftransformationer og stykvist definerede funktioner.
7. Eksponential- og logaritmefunktioner; logaritmeregler, eksponentielle modeller, skalering og dimensionsløse kombinationer.
8. Komplekse tal som basal algebra: polarform, konjugation og modulus; dybere kompleks analyse henvises til bind 4.

### Del II: Trigonometri og hyperbolske funktioner
9. Vinkler, radianer, enhedscirkel, symmetrier og fortegn.
10. Sinus, cosinus, tangens, perioder, frekvenser og faser; sammenhængen med rotationer.
11. Additions-, dobbelt-, halv- og produkt-til-sum-formler; identitetsoversigt.
12. Trigonometriske ligninger, inverse funktioner, grenvalg og atan2.
13. Harmonske svingninger og omskrivning mellem sinus/cosinus; amplituder og faseforskydning.
14. Hyperbolske funktioner, identiteter, inverser og geometrisk fortolkning.

### Del III: Lineær algebra
15. Vektorer, vektorrum, underrum, spænd, basis, dimension og lineær uafhængighed.
16. Lineære afbildninger, koordinater, repræsentation i baser og basisskift.
17. Matrixregning: sum, produkt, transponering, adjungering, identitet, inverse og blokmatricer.
18. Lineære systemer, Gauss- og Gauss–Jordan-elimination, rang, kerne, billede og frihedsgrader.
19. Determinant, udviklingsregler, orientering, volumenfaktor og invertibilitet.
20. Spor, egenværdier, egenvektorer, algebraisk/geometrisk multiplicitet, diagonalisering og begrænsninger.
21. Indre produkter, normer, ortogonalitet, Gram–Schmidt og ortonormale baser.
22. Symmetriske, hermiteske, unitære og ortogonale operatorer; spektralsætning.
23. Kvadratiske former, positiv definithed, Hessian og stabilitet.
24. Ortogonal projektion, mindste kvadrater, QR, singularværdier, SVD, pseudoinvers og konditionstal.
25. Matrixeksponential, lineære systemer og små koblede svingninger/normalmoder.

### Referenceapparat i hvert kapitel
- **Lær:** begreb, geometrisk intuition, fuld forklaring og forudsætninger.
- **Slå op:** kompakte regnetabeller, definitioner, identiteter og standardprocedurer.
- **Anvend:** typiske opgavemønstre, metodevalg, dimensionskontrol og faldgruber.
- **Forbind:** korte henvisninger til begreber tidligere i værket og relevante senere bind.
- **Visualisér:** originale figurer, når de giver faglig forståelse, frem for pynt.

**Afgrænsning:** Egentlig differential- og integralregning ligger i bind 2; ODE/PDE i bind 3; kompleks analyse, Fourier, specialfunktioner i bind 4; tensorer og geometri i bind 5; variationsregning og symmetrier i bind 6. Gentag kun det, der er nødvendigt for et selvstændigt opslag.

## Systematisk indholdsarbejde: første tre underemner

På `feat/matematik-bind1-fagindhold` fra `e4e4d1b` er de første tre underemner udbygget i den eksisterende algebrafil: tal og mængder; potenser/rødder/brøker; polynomier/binomialformel. De har intuition, definitioner og betingelser, udledninger, formelopslag, metodevalg, fysikforbindelser og lokale eller tekstlige krydsbindshenvisninger. To originale figurer viser intervalendepunkter og rodmultiplicitet. De oprindelige efterfølgende afsnit er bevaret.

Bind 1 har underafsnit i både indholdsfortegnelsen og bogmærkerne. PDF-kontrollen skelner nu mellem indholdet af hvert bind og hele værket; den samme kontrol af overfyldte bokse, tegn og uløste referencer gælder stadig.

**Næste indhold:** Ligninger og kvadratkomplettering, derefter uligheder/absolutværdi og partialbrøker, før resten af algebraen. En vellykket kompilering gør ikke disse eksisterende korte afsnit færdigskrevne. Der er ikke gået videre med nyt indhold i bind 2–6.
