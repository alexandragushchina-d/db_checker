
/*Delete the created indices*/

select if (
    exists(
        select distinct index_name from information_schema.statistics
        where table_schema = database()
        and table_name = 'Artikel' and index_name like 'id_artikel'
    )
    ,'select ''index id_artikel exists'' _______;'
    ,'drop index id_artikel on Artikel(bezeichnung, netto, steuer, preis, farbe)') into @a;
prepare stmt1 FROM @a;
execute stmt1;
deallocate prepare stmt1;

select if (
    exists(
        select distinct index_name from information_schema.statistics
        where table_schema = database()
        and table_name = 'Lieferung' and index_name like 'id_lieferung'
    )
    ,'select ''index id_lieferung exists'' _______;'
    ,'drop index id_lieferung on Lieferung(lieferzeit, nettopreis, bestellt)') into @a;
prepare stmt1 FROM @a;
execute stmt1;
deallocate prepare stmt1;

select if (
    exists(
        select distinct index_name from information_schema.statistics
        where table_schema = database()
        and table_name = 'Lieferant' and index_name like 'id_lieferant'
    )
    ,'select ''index id_lieferant exists'' _______;'
    ,'drop index id_lieferant on Lieferant(name, strasse, plz, ort)') into @a;
prepare stmt1 FROM @a;
execute stmt1;
deallocate prepare stmt1;
