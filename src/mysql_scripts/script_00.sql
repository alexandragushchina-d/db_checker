
/*Simple SELECT query*/

select a.anr, a.bezeichnung, a.preis
from Artikel as a, Lieferung as l
where a.anr = l.anr and l.bestellt between 0 and 9;
