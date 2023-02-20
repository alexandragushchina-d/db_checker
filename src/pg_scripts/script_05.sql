
/*Unoptimized SELECT for the table Lieferung to compare the difference in
  execution time*/

select liefnr from lieferung
where anr in (select anr from lieferung where liefnr = 4)
group by liefnr
having count(*) = (select count(*) from lieferung where liefnr = 4);
