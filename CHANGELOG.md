# Årshjul – endringslogg

Begge utgavene (enkel og team) bygges fra `src.html` med `python3 build.py`.

## Versjon 11 – 21. november 2026
**Ny logo: Lindbach Årshjul**
- Ny logo øverst i appen: hjulsymbolet, «Lindbach» i penselskrift og «ÅRSHJUL». Lys og mørk utgave følger nettleserens fargevalg.
- Nytt favicon i Lindbach-fargene: mørkegrå skive, blå, oransje og grønne felt og rød viser.
- Startside for GitHub Pages (`index.html`) med logo og valg mellom enkel og team.
- Ingen endringer i funksjoner eller lagring – oppgavene dine ligger der de lå.

## Versjon 10 – 21. november 2026
**Nytt i begge utgaver: kalenderfiler (.ics), gjøremål og hendelser, lisens**
- Hent fra kalender (Innstillinger → Hent fra kalender): leser .ics-filer fra Outlook, Google og Teams.
  - **Avtaler merket privat (CLASS:PRIVATE) eller konfidensiell (CLASS:CONFIDENTIAL) blir aldri hentet.** De forkastes med en gang filen leses; bare antallet vises, aldri tittel eller innhold.
  - Avlyste avtaler og endringer av enkeltmøter i en serie tas ikke med (antallet vises).
  - Forhåndsvisning: velg år, kategori («Kalender» lages automatisk med ledig farge), ring og hvilke avtaler som skal med.
  - Gjentakelser som støttes: hver uke / hver 2.–4. uke (også flere ukedager), daglig på hverdager, n-te ukedag i måneden (inkl. siste), hvert år. Slutt etter dato (UNTIL) eller antall ganger (COUNT) følges.
  - Det som ikke kan vises i årshjulet (f.eks. «den 15. hver måned», «hver 3. dag»), listes for seg med årsak.
  - Tider gjøres om til norsk tid – også for møter satt opp i andre tidssoner (Windows-navn som «W. Europe Standard Time» og «FLE Standard Time», IANA-navn og UTC).
  - Heldagsavtaler over flere uker fyller ukene; flere dager innen en uke (f.eks. konferanse tir–tor) får ukedagene.
  - Ingen dobbeltlagring: samme avtale (UID) oppdateres ved ny innhenting, og kategori, ring og avkrysninger beholdes. Uendrede avtaler er ikke krysset av.
  - Avtaler blir hendelser uten avkrysning som standard («Skal krysses av» kan slås på før innlegging).
- Last ned → Til kalenderen: årets oppgaver som .ics-fil. Oppgaver med ukedag og klokkeslett blir avtaler (Europe/Oslo), faste møter blir gjentakende avtaler, hele uker blir heldagshendelser merket som ledig tid. Egen UID per oppgave, så en eksport aldri overskriver det opprinnelige møtet i Outlook.
- Valgfri avkrysning: «Skal krysses av (gjøremål)» i skjemaet, på som standard. Uten hake blir oppgaven en hendelse: ingen avkrysningsrute, aldri blek i hjulet, telles ikke i fullført/gjenstår, og står som «Hendelse» i tabellen. Eksisterende oppgaver er gjøremål som før.
- Gjøremålsliste: «Alle | Gjøremål» øverst i panelet, både i måneds- og ukesvisningen. Valget huskes.
- Lisens: MIT, © 2026 A. Lindbach – i toppen av filen, i hjelpen og under hjulet. Lisensteksten ligger i LICENSE.
- Hjelpen har fått avsnitt om gjøremål og hendelser, kalenderfil og henting fra kalender.
- Liten rettelse: «Hele uka» i ukesvisningen brytes ikke lenger over to linjer.

## Versjon 9 – 20. november 2026
**Nytt i begge utgaver: gjentakelser, ukedager, klokkeslett og ukesoversikt**
- Gjentakelse i skjemaet (erstatter «Gjentas hvert år»): Ingen · Hver uke · Hver 2./3./4. uke · Hver måned · Hvert år.
- Ukedager (Man–Søn) kan velges; uten ukedag gjelder oppgaven hele uka som før. Med ukedag kan klokkeslett fra–til fylles inn.
- Hver måned = n-te ukedag i måneden (første/andre/tredje/fjerde/siste), f.eks. «første tirsdag i måneden».
- Forhåndsvisning under skjemaet: regelen i klartekst og antall ganger (f.eks. «Hver tirsdag kl. 09:00–10:00 · uke 1–53 · 52 ganger»).
- Ukentlige og månedlige serier lagres som én oppgave og vises som små merker i en smal stripe innenfor ukenumrene. Klikk på et merke åpner uka.
- Ukesoversikt: «Måned | Uke» øverst i panelet. Uka vises mandag–søndag med oppgavene under riktig dag, sortert etter klokkeslett; «Hele uka» for oppgaver uten ukedag. Bla med pilene. Valget huskes.
- Hvert møte i en serie krysses av for seg (i ukesoversikten). Månedsvisningen viser hvor mange av månedens møter som er gjennomført.
- Serier følger kalenderåret (f.eks. 52 tirsdager i 2026). Faste møter blir med når man henter faste oppgaver til neste år.
- Tabell/CSV: nye kolonner «Dag og tid» og «Gjentakelse»; serier viser «x av y gjennomført».
- Under hjulet: «Faste møter: x av y gjennomført».
- Hjelpen har fått avsnitt om gjentakelser og ukesoversikt.
- Eldre oppgaver med «Gjentas hvert år» blir automatisk «Hvert år».

## Versjon 8 – 20. november 2026
**Nytt i begge utgaver: flere årshjul**
- Årshjulene vises som faner øverst. «+ Nytt årshjul» lager et nytt (navn skrives rett i fanen, Enter lagrer). Klikk for å bytte, dobbeltklikk for nytt navn. Maks 20 årshjul, og to kan ikke ha samme navn.
- Hvert årshjul har egne oppgaver, kategorier og ringer.
- Slette: Innstillinger → Dette årshjulet → Slett dette årshjulet (bekreftes med ekstra klikk; minst ett hjul må være igjen).
- Sist åpne årshjul huskes.
- Claude-versjonen får også flere hjul. Hjulet fra tidligere versjoner blir første fane og ligger der det lå (ingen data flyttes); nye hjul lagres under egne stier i databasen.
- Sikkerhetskopi: velg «Dette årshjulet» eller «Alle årshjul». Ny filversjon 3 for flere hjul; filer fra tidligere versjoner kan fortsatt hentes inn.
- Innhenting: hvert årshjul i filen havner i fanen med samme ID. Finnes det ikke, blir det en ny fane – eller tar over det tomme startfanen hvis det er det eneste hjulet. Forhåndsvisningen viser hva som skjer med hvert hjul.
- Hjelpen har fått et avsnitt om flere årshjul.

**Enkel**
- Hjul som finnes fra før, erstattes ved innhenting.

**Team**
- Hjul som finnes fra før, slås sammen eller erstattes (valg). Sperren mot «feil hjul» og «Åpne årshjul fra fil» er erstattet av fanene: en fil fra et annet hjul blir sin egen fane.

## Versjon 7 – 20. november 2026
**Nytt i begge utgaver**
- Andre år enn inneværende år (fremover og bakover) starter med uke 1 øverst, og uke 1 er valgt. «Nå»-viseren vises bare i inneværende år. «I dag» tar deg tilbake til dagens uke.
- Dager i starten/slutten av året som hører til naboårets uke (f.eks. 1.–3. januar 2027 = uke 53 i 2026) vises som grå felt, så uke-ringen ikke har hull.
- Favicon: et lite årshjul i nettleserfanen, lagt inn i filen (ingen eksterne kall).
- Velge sted ved lagring: i Chrome og Edge (filen åpnet direkte) åpner sikkerhetskopi, bilde og tabell et «Lagre som»-vindu som husker sist brukte mappe per filtype. Andre nettlesere og Claude-versjonen: vanlig nedlasting som før.
- Hjelpeteksten forklarer årsbytte, de grå feltene og hvor sikkerhetskopien havner.
- Nedlasting av bilde for andre år bruker samme rotasjon som hjulet (uke 1 øverst).

## Versjon 6 – 20. november 2026
**Nytt i begge utgaver**
- Last ned bilde av hjulet (PNG, 2400 px bred) med tittel og fargeforklaring – til PowerPoint, Word og rapporter. Valg: januar øverst, vis dagens dato, med/uten tittel. Bildet har alltid lyse farger.
- Oppgaver i tabell: forhåndsvisning, nedlasting som Excel-fil (CSV som åpnes direkte i norsk Excel med æ, ø og å) og «Kopier tabell» til Word/PowerPoint/e-post. Valg: med/uten fullførte.
- Hjelp på klart språk (knappen «? Hjelp»). Vises automatisk første gang for nye brukere.
- Ryddigere topplinje: «I dag», «Last ned», «Innstillinger», «Hjelp». Kategorier, ringer, navn og sikkerhetskopi ligger under Innstillinger.
- Ingen eksterne tilkoblinger: systemskrifter i stedet for Google Fonts.
- Versjonsnummer vises under hjulet og i hjelpen.

**Enkel**
- Sikkerhetskopi i stedet for eksport/import: «Hent inn fra fil» erstatter hele årshjulet med filen (gjenoppretting).
- Ingen hjul-liste og ingen sammenslåing.

**Team**
- Som før: flere hjul med navn og ID, sammenslåing ved import, sperre mot feil hjul.

**Rettet**
- Feilmelding ved import av feil hjul viser nå riktig vei (Innstillinger → Årshjul).

## Versjon 5 – 19. november 2026
- Navn og ID per årshjul; flere hjul på samme maskin; sperre mot import av feil hjul.
- Kategori-menyen står ikke lenger fast på «+ Ny kategori» etter import i et tomt hjul.

## Versjon 4 – 19. november 2026
- Eksport/import med sammenslåing (nyeste endring vinner, slettinger følger med).

## Versjon 3 – 19. november 2026
- Egne kategorier (maks 10) med unike farger; klikk på tom uke avslutter redigering.

## Versjon 2 – 19. november 2026
- Ukering, oppgaver på uker fra–til, 1–4 aktivitetsringer, nå kl. 12, redigering, faste årlige oppgaver.

## Versjon 1 – 19. november 2026
- Første prototype.
