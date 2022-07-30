## Raptor

A site scanner and vulnerability scanner / exposer.

Supported frameworks:

- Laravel
- WordPress

### Commands

#### Scan a site commandos

Run default command the supports multiple arguments

```commandline
./main.py
```

Run command with login brute force

```commandline
./main.py withLogin
```
Run command with browser 
```commandline
./main.py withBrowser
``````

Run command with scraper

```commandline
./main.py withScraper
```

Set url by arg

```commandline
./main.py u=localhost
```

Set proxy server ip

```commandline
./main.py p=127.0.0.1
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

#### scrape website

Scrape the given url and save the result to a file inside _scraper folder.

```commandline
./scraper.py
```

With url argument

```commandline
./scraper.py u=https://localhost
```


# Disclaimer    
Only use this tool for research purposes and with permission from the owner of the site.
