
/*INSERT some rows in the already created table*/

do
$do$
declare
  i int;
begin
for i in 600..700
loop
  insert into artikel (anr, bezeichnung, netto, steuer, preis, mass, einheit, typ)
  values (6000+i, substr(concat('Motorbike_', random()), 1, 15),
          random()::numeric(7,2), random()::numeric(7,2),
          random()::numeric(7,2), substr(cast(random() as varchar), 1, 15),
          'ST', 'E')
  on conflict (anr) do update
    set preis = excluded.preis,
        netto = excluded.netto,
        steuer = excluded.steuer,
        mass = excluded.mass;
end loop;
end;
$do$;
