# Leveret PDF – bind 1

[Bind 1 – Algebra og lineær algebra](bind-1.pdf) er den kompilerede levering af hele bind 1, gennemgået 28. oktober 2026. PDF'en er egnet til manuel overførsel til Drive; ingen Drive-filer er ændret.

[Buildmetadata](bind-1.json) registrerer kildecommit, SHA-256, buildkommando og PDF'ens faktiske omfang. LaTeX-kapitlerne er autoritative; PDF'en må ikke redigeres separat. De samme kapitler indgår i den samlede udgave.

For at gentage bygningen: checkout det registrerede kildecommit, aktivér projektets LaTeX/Python-miljø, og kør `make bind-1` fra repositoryets rod. Output er `build/00-matematik/bind-1/bind-1.pdf`. TeX-metadata kan medføre et andet bytehash ved en ny bygning; den leverede fils hash dokumenterer netop denne levering.

Efter ændringer skal samtlige berørte sider gennemgås, og `make bind-1` skal bestå inklusive formelregisterets sidetalskontrol, før leveringsfil og metadata opdateres samlet. Der findes ikke en separat redaktionel version her.

Kun denne ene PDF er undtaget fra projektets almindelige regel om genererede filer i `build/`. Bind 2–6 er ikke udgivet eller ændret ved denne levering. Ingen upload aktiveres af en PDF i denne mappe.
