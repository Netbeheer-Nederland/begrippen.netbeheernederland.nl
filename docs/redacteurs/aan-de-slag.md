---
title: Aan de slag
parent: Redacteurs
nav_order: 1
---

# Aan de slag

## Installatie

Om begrippen vast te leggen in Turtle heb je enkel [VS Code](https://code.visualstudio.com/) nodig met de [Mentor](https://mentor-vscode.dev/) extensie (optioneel, voor snel inzicht in verwijzingen met Nano-ID's). De installatie vereist geen beheerrechten.

## Repository openen

De gemakkelijkste manier is om de repository remote te openen:

1. Klik op `Connect to...`
2. Kies `Open Remote Repository...`
3. Voer de URL in: `https://github.com/Netbeheer-Nederland/begrippen.netbeheernederland.nl`

## Begrippen maken en bewerken

Begrippen liggen vast in TTL-bestanden conform [NL-SBB](https://docs.geostandaarden.nl/nl-sbb/nl-sbb/). Om overzicht te bewaren, is het begrippenkader opgesplitst in meerdere bestanden:

- één bestand voor het kader (`00-kader.ttl`)
- één bestand voor bronnen (`01-bronnen.ttl`)
- één bestand per domein (bijvoorbeeld `C1-klant.ttl`)

Een begrip wordt vastgelegd als `skos:Concept`.

{: .text-delta }
Voorbeeld

```turtle
:bpm8z a skos:Concept ;
    dct:source :2i83j ;
    skos:definition "verplaatsing van energie via een energienet"@nl ;
    skos:inScheme <> ;
    skos:prefLabel "energietransport"@nl ;
    skos:topConceptOf <> ;
    adms:status status:valid .
```

De inhoud en formulering van de definitie volgen de richtlijnen op de pagina [Definities](definities.html).

Om je wijzigingen op te slaan, klik je links op `Source Control` om deze te 'committen'. Als je ze daarna 'synct', staan je wijzigingen binnen een paar minuten online.
