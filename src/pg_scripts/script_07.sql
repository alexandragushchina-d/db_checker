
/*Optimized select with the created index for the table Liederung*/

select liefnr from lieferung
where anr in (select anr from lieferung where liefnr = 1)
group by liefnr
having count(*) = (select count(*) from lieferung where liefnr = 1);
