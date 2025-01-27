# postgres

## installation

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

## psql shell

### configs

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

### sql

## files

### `somedirectory/postgresql.conf`

- general configs

- possible pathes
  - `/etc/postgresql/<version>/main/`
  - `/etc/pgsql/<version>/main/`
  - `/var/lib/postgresql/data/`
