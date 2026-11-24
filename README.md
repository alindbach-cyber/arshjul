# Årshjul

Et årshjul for oppgaver som fungerer rett i nettleseren. Året vises som en sirkel med måneder, uker og aktivitetsringer.

**Bruk det her:** https://alindbach-cyber.github.io/arshjul/

- Oppgaver på uker, med kategorier og farger
- Gjentakelser (hver uke, hver måned på samme ukedag eller samme dato, hvert år), ukedag og klokkeslett
- Gjøremål som krysses av, og hendelser som bare vises
- Statistikk over fullførte og ikke-fullførte oppgaver
- Flytt oppgaver frem og tilbake
- Flere årshjul i faner
- Last ned bilde (PNG), tabell (Excel) og kalenderfil (.ics)
- Hent enkeltavtaler og møteinnkallinger (.ics). Private og konfidensielle avtaler blir aldri hentet

Alt lagres i brukerens egen nettleser. Ingenting sendes til en server.

## Bruk

Åpne nettsiden og trykk **Åpne årshjulet**. Samme app passer både for én person og for flere som deler et årshjul: sikkerhetskopi til fil, og innhenting som enten slår sammen endringer eller erstatter alt.

Fra versjon 12 er det én app (`arshjul.html`). Gamle lenker til `arshjul-enkel.html` og `arshjul-team.html` sender videre dit.

Vil du ha appen som én fil på maskinen din? Trykk **Last ned arshjul.html** på startsiden, eller hent filen under **Releases** – hver versjon har den ferdige filen vedlagt.

## Filer

| Fil | Hva |
| --- | --- |
| `src.html` | Kildefilen |
| `build.py` | Bygger `arshjul.html` fra `src.html` (og videresendingssider for de gamle filnavnene) |
| `index.html` | Startsiden |
| `favicon.svg` | Ikonet |
| `.github/workflows/pages.yml` | Bygger og publiserer nettsiden automatisk |

## Slik oppdateres nettsiden

Hver gang noe endres på `main`, bygger GitHub appen og publiserer nettsiden på nytt. Det tar et par minutter. Fremdriften ses under **Actions**.

Bygge selv:

```
python3 build.py
```

Det lager `dist/arshjul.html` og videresendingssidene `dist/arshjul-enkel.html` og `dist/arshjul-team.html`. Se `CHANGELOG.md` for hva som er nytt i hver versjon.

## Lisens

MIT © 2026 A. Lindbach – se [LICENSE](LICENSE).
