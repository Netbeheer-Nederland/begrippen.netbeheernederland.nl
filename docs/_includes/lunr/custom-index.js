// Verwijder de paginatitel uit de content die wordt geïndexeerd om dubbele resultaten te voorkomen.
// We gebruiken .replace() omdat dit robuuster is dan .startsWith().

const title = docs[i].title.trim();
const content = docs[i].content.trim();
docs[i].content = content.replace(title, '').trim();
