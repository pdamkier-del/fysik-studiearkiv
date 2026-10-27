# Sikker migration til universitetsfag og fysikbibliotek

Historisk rapport for den tidligere todeling. Den seneste brugerbeslutning og [migration til tre hovedområder](migration-tre-hovedomraader.md) har forrang.

Udgangspunkt: commit `3bfca2c5717da5fcb378261d8dd0f0c337df8161` på den eksisterende branch `feat/studiearkiv-fundament`. Arbejdsområdet var rent. Ingen worktree eller ny branch er oprettet.

## Flytninger med git mv

| Tidligere placering | Ny placering |
| --- | --- |
| `00-matematik` | `00-matematik` |
| `01-analytisk-mekanik` | `01-universitetsfag/analytisk-mekanik` |
| `02-elektromagnetisme` | `01-universitetsfag/elektromagnetisme` |
| `04-termodynamik-statistisk-fysik` | `02-fysikbibliotek/termodynamik` |
| `06-statistik` | `02-fysikbibliotek/statistik` |
| `03-kvantemekanik` | `02-fysikbibliotek/kvantemekanik/arkiverede-skabeloner` |
| `05-relativitet-og-gravitation` | `02-fysikbibliotek/relativitet-og-gravitation/arkiverede-skabeloner` |
| `99-kilder-og-pensum/eksisterende-originaler.md` | `docs/originaler.md` |
| `99-kilder-og-pensum` | `99-kilder-og-pensum` |
| `docs/kapitelplan.md` | `00-matematik/PLAN.md` |

Migrationen flyttede alle 86 eksisterende versionsstyrede filer til deres fortsatte placeringer eller bevarede dem på stedet. Før videre fagligt arbejde blev samtlige 54 eksisterende LaTeX-kilder sammenlignet med baseline efter udelukkende nødvendige stierstatninger. Tekst, notation og de fire oprindelige figurkilder var bevaret. De 20 oprindelige fysikskabeloner forbliver i et eksplicit buildmanifest, herunder de otte arkiverede skabeloner.

## Semantiske beslutninger

- Kun AM, EM, Termodynamik 2026 og Statistik optræder som konkrete kursusmapper. Matematik F-/LinALys-registeroplysninger bevares uden yderligere kursusmapper.
- Kvante-/relativitetsskabelonerne var tomme og uden dokumenteret kursusidentitet. De bevares i bibliotekets `arkiverede-skabeloner/`, ikke som KU-kurser eller færdige kompendier.
- Matematikkompendiet er ét bredt biblioteksdokument med 21 hovedemner. Kursusdokumenter og generelle referencer vedligeholdes separat. Statistik er kun universitetsfag, mens statistisk fysik også er et planlagt biblioteksområde.
- Universiteternes pensumregister er flyttet samlet, og matematikplanen har sin egen biblioteksplacering. Præcise pensumgrænser og originale Drive-id'er ændres ikke.
- Efter ren migration fortsættes matematikken i det eksisterende trigonometriemne. Dette er en selvstændig faglig udvidelse, ikke et påstået indhold fra en utilgængelig original.

## Tekniske følger

Alle builds køres fortsat fra repositoryets rod. Kildeimports, dokumentlinks, artifactstier, manifests, tests og workflow er migreret. Buildoutput spejler de to hovedområder. De oprindelige programmerings- og sikkerhedstests bevares og tilpasses det nye Drive-hierarki; ekstra tests afviser forkerte hovedområder og gammel flad målkonfiguration.

Drive-hierarkiet beskrives fremover med `areas` og `subjects`: arkivrod → hovedområde → fag → eksisterende PDF. Der foretages ingen automatisk flytning, oprettelse, upload eller autentificering mod Drive under migrationen. Alle produktionsposter forbliver `approved: false`, og stabile dokumentnøgler samt originale fil-id'er bevares. Eksisterende målkonfiguration skal senere verificeres manuelt før aktivering.

## Validering

De præcise resultater efter migration og matematikudvidelse registreres i [STATUS.md](../STATUS.md). Kontroller omfatter begge eksisterende PDF-dokumenter, alle 20 skabelonbuilds, PDF-navigation, LaTeX-imports/labels/referencer, lokale Markdown-links, sikkerhedstests, workflow-YAML og offline-dry-run. Ekstern CI og Drive-drift påstås ikke verificeret.
