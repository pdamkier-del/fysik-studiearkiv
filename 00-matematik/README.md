# Matematik · selvstændigt hovedområde

`main.tex` bygger ét samlet dokument med 21 matematiske hovedemner, matematiske underafsnit, omfattende forklaringer, generelle formler og faglige vektorfigurer. Samme kapitelkilder indlæses af de [seks bind](BINDPLAN.md), så der ikke opstår parallelle bøger. Se [PLAN.md](PLAN.md) og [underemneplanen](ALLE_BIND_UNDEREMNER.md). Statistik indgår ikke og vedligeholdes separat i fysikbiblioteket.

Kompendiet er et bredt referenceværk og er ikke begrænset af Matematik F, LinALys eller andre kursers pensum. [Universiteternes kilderegister](../99-kilder-og-pensum/README.md) kan pege på relevante emner her, men udgør ikke dette dokuments kapitelgrænse og må ikke bruges som bevis for, at hele bibliotekskapitler er gennemgået pensum.

Kør `make check` fra repositoryets rod. PDF: `build/00-matematik/main.pdf`. Korrekt eksisterende tekst, notation og figurer bevares under udvidelser. Pilotkapitlet om differentialregning bevares; trigonometri indgår nu som et gennemarbejdet kapitel i den samlede bind-1-levering. Der er ingen gennemregnede opgaveeksempler.

Integralregning er udbygget til et sammenhængende kapitel med standardintegraler, metoder, konvergens, parameterintegration og fire originale figurer. Ordinære differentialligninger er efterfølgende udbygget med metoder, eksistens/stabilitet og tre originale figurer.

Matematik er flyttet ud af fysikbiblioteket som eget hovedområde. MatF1, MatF2, LinALys og Algebra skal integreres efter matematiske emner; der oprettes ikke separate kompendier. De præcise referencer og forholdet mellem kursusbetegnelserne skal verificeres fra kilder, før nye pensumpåstande tilføjes.

Byg bind 1 med `make bind-1` og alle seks med `make alle-bind`. Bind-PDF'er ligger under `build/00-matematik/bind-N/bind-N.pdf`. Udviklingen følger nu underemnerne i bind 1 fra begyndelsen. Hele bind 1 er nu genopbygget med den aftalte emnedækning, 18 minimalistiske figurer og et samlet klikbart formelregister. Se [aktuel status](../STATUS.md).

## Leveret bind 1

[Download den kvalitetskontrollerede PDF](udgivelser/bind-1.pdf). Den er gemt i Git efter brugerens udtrykkelige leveringskrav; alle øvrige genererede PDF'er bliver i `build/`. [Metadata](udgivelser/bind-1.json) registrerer kildecommit og checksum, og [kontrolrapporten](../docs/kontrol-bind-1.md) beskriver dækning, tests og afgrænsninger. Bind 2–6 er uændrede. Drive er ikke opdateret.
