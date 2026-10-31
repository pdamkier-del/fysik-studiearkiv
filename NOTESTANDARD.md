# NOTESTANDARD – obligatorisk redaktionel og teknisk standard

**Gælder alle nye og ændrede studiearkivnoter**, især AM-/EM-formelsamlinger, udledningsnoter, opgavenoter og matematikbind. Læs denne fil og `AGENTS.md` før nogen dokumentændring. Det er en kvalitetskontrakt, ikke forslag.

## 1. Formål og notetyper
- **Formelsamling:** hurtigt eksamensopslag med definitioner, komponentformler, gyldighedsbetingelser, regneregler og korte metoder.
- **Udledningsnoter:** sammenhængende, kontrollerede teoretiske udledninger.
- **Opgavenoter:** genbrugelige løsningsopskrifter, metodevalg, faldgruber og standardkontroller.
- **Eksamensløsninger:** original opgavetekst (inkl. figurer) direkte efterfulgt af metode, udregning, svar og kontrol, organiseret efter fagligt emne.
- **Matematikbind:** præcise grundbegreber, klare regler og relevante figurer; undgå omstændelige essays.
Hold notetyperne adskilte, medmindre brugeren eksplicit ændrer afgrænsningen.

## 2. Pædagogik og indhold
1. **Definition → brugbar formel → betydning → metode → eventuel henvisning.** Skriv normalt 2–5 linjers forklaring til et begreb, længere kun ved reelt behov.
2. Angiv **alle nødvendige definitioner og komponentudtryk**, så en eksamensopgave kan løses uden at gætte: fx `L = r × p` samt `L_x = yp_z - zp_y`, `L_y = zp_x - xp_z`, `L_z = xp_y - yp_x`.
3. Gør grundregler operationelle: fx `p_phi = ∂L/∂phi_dot` under cyklisk vinkel; `mr² phi_dot` er et særligt tilfælde, ikke en universel definition.
4. Vis hvor relevant **hvordan man kommer fra opgavetekst til resultat**: variable, metodevalg, opstilling, mellemtrin, kontrol. Hold standardmetoder tydeligt adskilt fra særlige eksempler.
5. Angiv præcise antagelser, notation, konventioner, begrænsninger, enheder, fortegn og eventuelle specialtilfælde. Påstå ikke, at manglende oplysninger kan beregnes.
6. Fremhæv praktiske identiteter samme sted som teori, fx `{F,q_i} = -∂F/∂p_i`, `{F,p_i} = ∂F/∂q_i`, og test af kanonisk transformation ved et eller flere par.
7. Saml symmetri, tilhørende cyklisk koordinat, generaliseret impuls og bevarelseslov i læsbare skemaer, uden fejlagtig generalisering.
8. Skriv kort og akademisk på dansk, med matematiske symboler i korrekt LaTeX og konsistent notation. Ingen personlige eksempler eller unødvendige anekdoter.
9. Gentag ikke samme teori mange steder; brug klikbare krydshenvisninger mellem emner og dokumenter, når muligt.

## 3. Layout – minimalistisk og visuelt
- Hvid baggrund, mørk tekst, højst én afdæmpet accentfarve, professionel matematiktypografi.
- God luft og passende marginer; læselig grundskrift, ikke miniaturetekst. Tydelige konsekvente kapitel- og underoverskrifter.
- Formler skal stå samlet med de forklaringer, de hører til. Brug diskrete fremhævninger, ikke tunge grafiske bokse.
- Mange **relevante, enkle og originale** TikZ-/PGFPlots-figurer, hvor en geometrisk fortolkning hjælper: fx transformationsmatrix ved siden af rotation; determinant ved siden af arealskalering. Få rene linjer, enkel 2D-grafik, ingen dekorative 3D-effekter, gradienter eller tætte gitre.
- Figurer skal være matematisk korrekte med labels, akser og relevante enheder.
- Ingen unødvendig forside: titel og klikbar indholdsfortegnelse er normalt nok. Ingen tomme sider eller løse appendiksark, der burde være integreret i kapitlerne.
- Opgave og fuld løsning skal stå direkte ved hinanden, aldrig som separat facitsektion forrest, hvis brugeren ønsker eksamensopslag.

## 4. Ufravigelig redigeringsprocedure
1. **Læs først** `AGENTS.md`, denne `NOTESTANDARD.md`, fagets eksisterende LaTeX-kilder, dokumentets indholdsfortegnelse og de relevante originalfiler. Beskriv kort planen.
2. **Find den autoritative, redigerbare kilde**. Ret kildeteksten i det **eksisterende faglige afsnit**, omstrukturér om nødvendigt hele kapitlet for at bevare rækkefølge og læsbarhed.
3. **Aldrig klæbe nye sider, tekstbokse eller overlays på en gammel PDF** som erstatning for at redigere LaTeX; heller ikke 'ekstra metodeguide' forrest, når den hører til et eksisterende kapitel.
4. Hvis kun en PDF findes og kilden mangler: hent/identificér den autoritative original og **genskab en konsistent LaTeX-kilde** før større ændringer. **Stop og rapportér blokeringen** frem for at lade som om en PDF-lapning er en fuldt integreret redigering. Bevar originalen.
5. Kompilér **hele dokumentet** fra samme LaTeX-kildetræ. Beregn indholdsfortegnelse, sidetal, interne links og bogmærker på ny. Gennemkør LaTeX flere gange, hvis referencer kræver det.
6. Kontrollér **alle sider visuelt** og dokumentér især ændrede sider, sideskift, matematiske symboler, overfyldte bokse, overlap, margen, fontstørrelse, figurer, sidetal, links og bookmarknavigation.
7. Kør automatiske builds/tests hvor tilgængelige, men de **erstatter ikke visuel kontrol**. Korrigér problemerne før publicering.
8. Udskift den **ene aktive** fil i den rigtige Google Drive-mappe og arkivér tidligere udgaver uden datatab. Verificér filnavn, placering og link via Drive. Hvis upload ikke lykkes, sig det klart.
9. Rapportér nøjagtigt hvilke kapitler/afsnit der er ændret, hvad der er valideret, og hvad der eventuelt ikke er gennemført. Skriv aldrig 'færdig og kontrolleret' uden reel kontrol.

## 5. Særlig tjekliste: AM-formelsamling
- Hamilton: fra `L` til `p_i`, `H`, Hamiltons EOM, eventuel eliminering af impuls.
- Kanoniske transformationer: fundamental PB-test; Kroneckers delta; én frihedsgrad (`{Q,P}=1`); flere frihedsgrader (`{Q_i,Q_j}=0`, `{P_i,P_j}=0`, `{Q_i,P_j}=δ_ij`), alle parenteser i gamle kanoniske variable.
- Genererende funktioner `F_1`–`F_4`: deres variable, fortegn og tidsled; ny Hamiltonfunktion `K(Q,P,t) = H(q(Q,P,t),p(Q,P,t),t) + ∂F/∂t` hvor den relevante type F og dens uafhængige variable skal angives.
- Impulsmoment: vektordefinition, alle tre kartesiske komponenter, forskel på mekanisk og kanonisk impuls hvor relevant; rotationssymmetri og bevarelse.
- Poissonparenteser: definition, basisidentiteter, genvejsregler og tydelige indekskonventioner.
- Metodevejviseren må være kort, men de detaljerede metoder **skal ligge under deres faglige kapitler**, ikke kun forrest.

## 6. Konsekvens
Enhver fremtidig Codex-/assistentopgave, som ændrer studiearkivnoter, **skal læse og følge denne fil før arbejdet**. Hvis den eksisterende filstruktur gør et krav umuligt, rapportér det ærligt og ret den underliggende struktur frem for at skjule problemet.
