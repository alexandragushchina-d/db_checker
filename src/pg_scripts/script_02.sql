
/*CREATE a new table and INSERT*/

create table accountsPersonal(
	user_id serial primary key,
	username varchar (50) unique not null,
	password varchar (50) not null,
	email varchar (255) unique not null,
	created_on timestamp not null,
        last_login timestamp
);

insert into accountsPersonal(user_id, username, password, email, created_on,last_login)
  select p.persnr, p.name, substring(
          'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789',
          (floor(random() * 30 + 1)::int), 10),
        concat(lower(replace(p.name, ' ', '')),'FM000','@firma.com'),
        current_timestamp, current_timestamp
  from Personal as p;
