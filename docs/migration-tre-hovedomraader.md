# Migration til tre hovedområder

Seneste brugerbeslutning har forrang: Matematik er et selvstændigt hovedområde; universitetsfag omfatter kun AM og EM; Termodynamik og Statistik ligger i fysikbiblioteket. Dette erstatter den tidligere godkendte todeling, som fortsat findes som historisk rapport.

Flytningen fortsætter fra `0ce2b53e05164d831cd435257d0753824a416575` på samme branch og bevarer også den endnu igangværende ODE-tekst og tre nye figurer. Alle 131 registrerede eksisterende filer og alle 62 LaTeX-kilder blev kontrolleret for bevaring efter nødvendige stierettelser.

| Tidligere sti | Ny sti |
| --- | --- |
| `02-fysikbibliotek/matematik` | `00-matematik` |
| `01-universitetsfag/statistik` | `02-fysikbibliotek/statistik` |
| `01-universitetsfag/termodynamik-2026/README.md` | `02-fysikbibliotek/termodynamik/KURSUSGRUNDLAG.md` |
| `01-universitetsfag/termodynamik-2026` | `02-fysikbibliotek/termodynamik` |
| `01-universitetsfag/pensum` | `99-kilder-og-pensum` |
| `config/drive-targets.example.json` | `config/drive-targets.json` |

Der er brugt `git mv`, hvor det er relevant. Den eksisterende generelle termodynamik-README blev ikke overskrevet: den tidligere kursusplan-README er bevaret som `KURSUSGRUNDLAG.md`. Alle fire termodynamikskabeloner og øvrige dokumentpladser er bevaret. De 20 oprindelige skabelonbuilds findes fortsat i manifestet. ODE-arbejdet fortsætter efter migrationen, uden at integralregningen eller de tidligere kapitler mistes.

De brugeroplyste Drive-mappe-id'er er registreret i `config/drive-targets.json`; matematik og AM har deres eksisterende stabile PDF-id'er. Manglende fil-id'er er `null`. Ingen mapper eller filer oprettes, flyttes, overskrives eller slettes i Drive. Oplysningerne er ikke uafhængigt API-verificeret, og publicering er ikke aktiveret.

Builds, workflows, imports, teststier og dokumentlinks er opdateret. Matematik-PDF'en ligger nu under `build/00-matematik/`, statistik-PDF'en under `build/02-fysikbibliotek/statistik/`. Aktuelle resultater og fortsatte kilde-/adgangsblokeringer står i [STATUS.md](../STATUS.md).
