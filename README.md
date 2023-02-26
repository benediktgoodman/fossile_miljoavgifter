# Beregning av avgifter tilknyttet bruk av fossile energikilder

Opprettet av:
Benedikt Goodman <bgo@ssb.no>

---

## Om programmet og moduler som er skrevet for beregning av fossile avgifter
*Forfatter: Benedikt Goodman*

Dette programmet regner ut avgifter betalt basert på bruk av fossile energikilder.Programmet har tre hoveddeler og alle ligger i src/funksjoner folderen. Disse er som følger:
- **FolderSearcher** står for identifikasjon av data for import, samt tillagning av metadata
- **DataImporter** leser inn og transformerer data fra mange årganger til dataframes i en dictionary
- **main_program_functions** som inneholder funksjonene brukt til beregning

En sentral antakelse ved dette programmet er at brukeren er noe kjent med noe bruk av pandas og python som helhet. De komplekse bitene av programmet er dog gjemt på innsiden av objektene og funksjonene nevnt over. Det brukeren sitter igjen med er dermed et sett med funksjoner som er lette å bruke og som kan settes sammen til å gjenskape beregningsopplegget som eksisterer i SAS.

## Dataflyt
![Dataflyt](https://github.com/statisticsnorway/fossile_miljoavgifter/blob/main/dataflyt_program.png)

## Prosess for installasjon av pakken
- Klon repositoriet til jupyterhub i produksjonssonen i en passende filmappe
- Naviger til hovedmappen for prosjektet (der hvor pyproject.toml ligger)
- Åpne et terminalvindu (trykk plusstegnet og deretter terminal)
- Skriv følgende: ssb-project build 

## Hvor ligger ting?
- Byggeklosser (klasser og funksjoner) ligger i src/functions
- Det kjøres fra src/notebooks

## Om fremtidig kompatibilitet med DAPLA
Dataene dette programmet bruker eksisterer foreløpig kun på linux serverne til SSB, og prosessene som utføres er et mellomsteg i en større beregningsprosess. Programmet skriver derfor også data tilbake til linux serverne. DAPLA kompatilbitet er ikke skrevet inn i programmets import- og eksportfunksjoner, men kan lett legges til når hele løpet skal flyttes over på DAPLA.
