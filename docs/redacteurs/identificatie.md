---
title: Identificatie
parent: Redacteurs
---

# Identificatie

Ieder begrip krijgt een betekenisloze, stabiele [NanoID](https://github.com/ai/nanoid) met karakterlengte `5` en alfabet `2346789abcdefghijkmnpqrstwxyz`. Het alfabet bevat geen hoofdletters om problemen met bestandsnamen op Windows te voorkomen. Daarnaast vermijden we look-alikes (`1l0ouv5s`). Dit patroon geeft meer dan 20 miljoen mogelijkheden. Bij 642 voorkomens is er 1% kans op minimaal één botsing.

<details closed markdown="block">
  <summary>
    Voorbeeldcode
  </summary>
  {: .text-delta }
  <pre>
  <b9dqx> a skos:Concept ;
      dct:identifier "b9dqx" ;
      skos:prefLabel "aansluiting"@nl .
  </pre>
</details>

---

{: .note-title }
> TIP
>
> NanoID's kunnen eenvoudig worden gegenereerd met hulpmiddelen in bijvoorbeeld Visual Studio Code of via diverse websites zoals [nanoid.jormaechea.com.ar](https://nanoid.jormaechea.com.ar/?alphabet=2346789abcdefghijkmnpqrstwxyz&length=5) of [nanoid.yuuniworks.com](https://nanoid.yuuniworks.com/).
>
> In Visual Studio Code kun je [Mentor](https://marketplace.visualstudio.com/items?itemName=faubulous.mentor) gebruiken om bij een NanoID de voorkeursterm te tonen.
