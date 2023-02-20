
/*SELECT with the limited indices*/

select a.anr, a.bezeichnung, ((sum(l.bestellt) + sum(r.anzahl))*a.preis)
as sumPerArtikel, min(li.name), min(li.ort)
from Artikel as a inner join Lieferung as l on a.anr = l.anr
inner join Reservierung as r on r.artnr=a.anr
inner join Lieferant as li on l.liefnr = li.nr
group by a.anr;
