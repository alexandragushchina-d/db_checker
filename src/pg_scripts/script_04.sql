
/*Optimized SELECT for the table Lieferung*/

select liefnr from lieferung
where anr in (select anr from lieferung where liefnr = 1)
and not liefnr  = 1
group by liefnr
having count(*) = (select count(*) from lieferung where liefnr = 1);
