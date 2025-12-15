// _includes/lunr/custom-index.js -- DEBUG-VERSIE

const title = docs[i].title.trim();
const content = docs[i].content.trim();

// Log de waarden naar de console om ze te inspecteren
console.log("--- Pagina:", docs[i].url);
console.log("Titel uit front matter: '" + title + "'");
console.log("Begin van content:     '" + content.substring(0, 100) + "'"); // Log de eerste 100 tekens

// De vervangingslogica
docs[i].content = content.replace(title, '').trim();

// Log het resultaat om te zien of de vervanging is gelukt
console.log("Content na vervanging: '" + docs[i].content.substring(0, 100) + "'");
