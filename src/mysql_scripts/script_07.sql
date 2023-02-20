
/*Create indices for one frequently read table*/

select if (
    exists(
        select distinct index_name from information_schema.statistics
        where table_schema = database()
        and table_name = 'Artikel' and index_name like 'id_artikel'
    )
    ,'select ''index id_artikel exists'' _______;'
    ,'create index id_artikel on Artikel(bezeichnung)') into @a;
prepare stmt1 FROM @a;
execute stmt1;
deallocate prepare stmt1;
