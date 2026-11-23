# Lindbach Årshjul

Et årshjul for oppgaver som fungerer rett i nettleseren. Året vises som en sirkel med måneder, uker og aktivitetsringer.

**Bruk det her:** https://alindbach-cyber.github.io/arshjul/

- Oppgaver på uker, med kategorier og farger
- Gjentakelser (hver uke, hver måned, hvert år), ukedag og klokkeslett
- Statistikk over fullførte og ikke-fullførte oppgaver
- Flytt oppgaver frem og tilbake
- Flere årshjul i faner
- Last ned bilde (PNG), tabell (Excel) og kalenderfil (.ics)
- Hent avtaler fra Outlook og Google (.ics). Private avtaler blir aldri hentet

Alt lagres i brukerens egen nettleser. Ingenting sendes til en server.

## Utgaver

- **Årshjul enkel** – for én person, med sikkerhetskopi til fil
- **Årshjul team** – for flere, med eksport og import som slår sammen endringer

Vil du ha appen som én fil på maskinen din? Åpne den på nettsiden og velg *Lagre side som* i nettleseren.

## Filer

| Fil | Hva |
| --- | --- |
| `src.html` | Felles kildefil for begge utgavene |
| `build.py` | Bygger `arshjul-enkel.html` og `arshjul-team.html` fra `src.html` |
| `logo.json` | Lindbach-logoen (lys og mørk) som bygges inn i appen |
| `index.html` | Startsiden med logo og valg av utgave |
| `favicon.svg`, `bilder/` | Ikon og logo til startsiden |
| `.github/workflows/pages.yml` | Bygger og publiserer nettsiden automatisk |

## Slik oppdateres nettsiden

Hver gang noe endres på `main`, bygger GitHub begge utgavene og publiserer nettsiden på nytt. Det tar et par minutter. Fremdriften ses under **Actions**.

Bygge selv:

```
python3 build.py
```

Det lager `dist/arshjul-enkel.html` og `dist/arshjul-team.html`. Se `CHANGELOG.md` for hva som er nytt i hver versjon.

## Lisens

MIT © 2026 A. Lindbach – se [LICENSE](LICENSE).
