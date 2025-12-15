// Verwijder de paginatitel uit de content die wordt geïndexeerd.
// Dit voorkomt dubbele zoekresultaten als een zoekterm in de titel staat.
// 'docs[i]' is het huidige document dat wordt verwerkt voor de zoekindex.

const title = docs[i].title.trim();
const content = docs[i].content.trim();

if (content.startsWith(title)) {
  docs[i].content = content.substring(title.length).trim();
}
