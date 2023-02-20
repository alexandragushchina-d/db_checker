
/*DELETE the third client as it is blocked*/

set FOREIGN_KEY_CHECKS = 0;

delete from Auftragsposten
  where auftrnr = (select a.auftrnr from Auftrag as a where a.kundnr=3);

delete from Auftrag
  where kundnr = 3;

delete from Kunde
  where nr = 3;

set FOREIGN_KEY_CHECKS = 1;
