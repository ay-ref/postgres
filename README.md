# postgres

## installation


- **if you dont install or make the `contrib` some postgress features does not work, for example complete `restore`.**

- installation of postgres 9.4

```shell
wget https://ftp.postgresql.org/pub/source/v9.4.26/postgresql-9.4.26.tar.gz
tar -xvzf postgresql-9.4.26.tar.gz
cd postgresql-9.4.26
```

```shell
./configure --without-readline --without-zlib
make
sudo make install

echo 'export PATH=/usr/local/pgsql/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

- installation of postgres last version

```shell
sudo apt install postgresql postgresql-contrib postgresql-server
```

## cli

- initial new postgres app

```shell
sudo /usr/bin/postgresql-setup --initdb
```

```shell
initdb your_path
```

- backup database

```shell
pg_dump -U myuser -h localhost -p 5432 mydatabase > mydatabase_backup.sql
```

- restore database

```shell
psql -U myuser -h localhost -p 5432 -d mydatabase -f mydatabase_backup.sql
```

```shell
pg_restore -U myuser -h localhost -p 5432 -d mydatabase mydatabase_backup.dump
```

- vacuum on database

```shell
vacuumdb -h hostname -p port_number -U postgres -j 4 -z -v db_name
```

- on entire instance

```shell
vacuumdb -h hostname -p port_number -U postgres -j 4 -z -v -a
```

## psql shell

### configs

- version

```shell
select version();
```

- find data directory

```shell
SHOW data_directory;
```

- see the password encryption

```shell
SHOW password_encryption;
```

- see the port and ip

```shell
show port;
```

```shell
SELECT inet_server_addr();
```

- see available extensions

```shell
select * from pg_available_extension;
```

```shell
select * from pg_extension;
```

### controls

- see databases

```shell
\l
```

- see users

```shell
\du
```

- see table

```shell
\dt
```

- quit

```shell
\q
```

- help

```shell
\?
```

- change the database

```shell
\c mydatabase;
```

- vacuum your table

```shell
vacuum table_name;
```

- vacuum and analyze table

```shell
vacuum analyze table_name;
```

- vacuum and analyze table with verbose

```shell
vacuum verbose analyze table_name;
```

### sql

- just remember in tech we are not logical

```sql
SELECT 1 WHERE NULL=NULL;
-- nothing output

SELECT 1 WHERE NULL!=NULL;
-- nothing output
```

- **SO BE CAREFUL AT UNIQUE INDEX THAT IS NULL-ABLE**

## files

### `somedirectory/postgresql.conf`

- general configs

- possible pathes
  - `/etc/postgresql/<version>/main/`
  - `/etc/pgsql/<version>/main/`
  - `/var/lib/postgresql/data/`

## pgadmin

- this is very funny, but just now happened for someone:
  - **the copy server in the pgadmin menu toolbar just copy the
    connection not the files :/**

## what the hells

- scenario
  - assume you have a table with `id autoincrement` and `field unique`
  - you go to insert new record with already existed unique field and get error
  - but id incremented by one, it seems strange! 
