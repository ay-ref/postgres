# postgres

- initial new postgres app

```shell
sudo /usr/bin/postgresql-setup --initdb
```

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
