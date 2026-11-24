# Årshjul

Et årshjul for oppgaver som fungerer rett i nettleseren. Året vises som en sirkel med måneder, uker og aktivitetsringer.

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

## Filer

| Fil | Hva |
| --- | --- |
| `index.html` | Startsiden med valg av utgave |
| `arshjul.html` | Den ferdige appen (bygges fra `src.html`) |
| `src.html` | Kildefilen |
| `build.py` | Bygger `arshjul.html` (og videresendingssider for de gamle filnavnene) |
| `favicon.svg` | Ikonet |

## Bygge

```
python3 build.py
```

Det lager `dist/arshjul.html` og videresendingssidene `dist/arshjul-enkel.html` og `dist/arshjul-team.html`. På GitHub gjør arbeidsflyten dette automatisk ved hver endring. Se `CHANGELOG.md` for hva som er nytt i hver versjon.

## Lisens

MIT © 2026 A. Lindbach – se [LICENSE](LICENSE).
