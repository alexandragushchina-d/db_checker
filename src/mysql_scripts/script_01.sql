-- /*E.g., UPDATE after we've received a lot of invoices and CREATE a new column
--  with the corresponding sum for every order then print the result into console*/

update Lieferung as l
set l.bestellt = floor(rand()*(100-5+1)+5)
where l.anr > 0;

update Lieferung as l
set Nettosum = l.bestellt * l.nettopreis
where l.anr > 0;

select * from Lieferung;
