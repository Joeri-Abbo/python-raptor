## Raptor

A site scanner and vulnerability scanner / exposer.

Supported frameworks:

- Laravel
- WordPress

### Commands

#### Scan a site commandos

Run default command

```commandline
./main.py
```

Run command with login brute force

```commandline
./main.py withLogin
```

Set url by arg

```commandline
./main.py u=localhost
```

#### Scan composer / npm lock files.

As argument pass the url to the lock file and json file.

For example composer.json and composer.lock.
The command automatic downloads the files and run the `snyk test` to check for vulnerabilities.

snyk need to be installed to let this command work. You can install it with `npm install -g snyk`. And after installing
run `snyk auth` to authenticate .

```commandline
./vulnerabilities-scanner.py https://localhost/package.json https://localhost/yarn.lock
```