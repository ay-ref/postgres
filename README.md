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

## commands

- initial new postgres app

```shell
sudo /usr/bin/postgresql-setup --initdb
```

## psql shell

- find data directory

```shell
SHOW data_directory;
```

- see the password encryption

```shell
SHOW password_encryption;
```

- see the port

```shell
show port;
```

## files

### `somedirectory/postgresql.conf`

- general configs

- possible pathes
  - `/etc/postgresql/<version>/main/`
  - `/etc/pgsql/<version>/main/`
  - `/var/lib/postgresql/data/`
