# el-teniente-gtfs-builder

Program to transform operation data (given by "El Teniente") to GTFS format

## Requirements

This project was built using python 3.9 and python dependencies can be viewed in requirements.txt file and
requirements-dev.txt file. The second one has dependencies used by notebooks.

### Windows

In this operating system we could have problems with some libraries because they have GDAL as a dependency. To fix this
problem you should install the following whl files:

- GDAL
- Fiona

These files have to be downloaded from https://www.lfd.uci.edu/~gohlke/pythonlibs.

The procedure to install these files once you downloaded it, it is executing the
command `pip install /path/to/wheel/file`.

## Inputs

To run this project we need to provide three files:

- operation program: excel file (.xlsx) with operation data
- stops: kmz file with buses stops
- shapes: kmz file with

## Notebooks

There are modules (see `notebooks` folder) to check functions with jupyter notebooks. If you intend to use this, you
have to install additional requirements in the requirements-dev.txt file.

## Commands

The following commands make the magic. You should execute them in the same order to get, as a result, a suitable GTFS
file.

The way to execute each of them is as follows: `python main.py command-name params...`.

### process-stop-file

```
 Usage: main.py process-stop-file [OPTIONS] FILES...

 Process mkz files that contain stop data. With these files, we build the following GTFS files: - stops.txt

╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    files      FILES...  List of kmz files with stop data [default: None] [required]                                                                                                                                                │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                                                                                                                                                          │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

### process-shape-file

```
 Usage: main.py process-shape-file [OPTIONS] FILES...

 Process mkz files that contain shape data. With these files, we build the following GTFS files: - shapes.txt

╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    files      FILES...  List of kmz files with shape data [default: None] [required]                                                                                                                                               │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                                                                                                                                                          │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

### process-operation-program-file

```
 Usage: main.py process-operation-program-file [OPTIONS]

 Process DBF files given by Link+. With these files, we build the following GTFS files: - calendar.txt - calendar_dates.txt - routes.txt - trips.txt - stop_times.txt

╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                                                                                                                                                          │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

### build-gtfs-file

```
 Usage: main.py build-gtfs-file [OPTIONS]

 Build GTFS file. This command assumes that you previously executed other commands (process-shape-file, process-stop-file, process-operation-program-file) to create all GTFS files. Additionally, it reduces the size of the
 shapes.txt file by removing unused shapes.

╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                                                                                                                                                          │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

### retrieve-recent-dbf-files

```
 Usage: main.py retrieve-recent-dbf-files [OPTIONS] EMAIL PASSWORD

 Search and download DBF files from Gmail account

╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    email         TEXT  email where DBF are sent [default: None] [required]                                                                                                                                                         │
│ *    password      TEXT  Email password [default: None] [required]                                                                                                                                                                   │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                                                                                                                                                          │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

It is important to know the Gmail password it should be the "App password" because that password does not require
additional information to log in. More
info [here](https://towardsdatascience.com/how-to-easily-automate-emails-with-python-8b476045c151).

### send-file-to

```
 Usage: main.py send-file-to [OPTIONS] MAILGUN_DOMAIN MAILGUN_KEY FILE_PATH
                             EMAIL_DEST_LIST...

 Send a file to list of email destinations

╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    mailgun_domain       TEXT                Mailgun domain to send email [default: None] [required]                                                                                                                                │
│ *    mailgun_key          TEXT                Mailgun key to authenticate in mailgun service [default: None] [required]                                                                                                              │
│ *    file_path            PATH                file path of file to attach in email [default: None] [required]                                                                                                                        │
│ *    email_dest_list      EMAIL_DEST_LIST...  List of destination emails [default: None] [required]                                                                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                                                                                                                                                          │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

## Send logs to file

Sometimes you will need to save the command's output to a file to analyze it in the future. In these situations, you
should
modify the file `main.py` by adding the followings lines:

```
- line 9: from gtfs_builder.config import OUTPUT_PATH
- line 87: filename = os.path.join(OUTPUT_PATH, 'output.log')
- line 88: logging.basicConfig(filename=filename, level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
```

## Docker

Build image:

```
docker build -f docker\Dockerfile -t el-teniente-gtfs-builder:latest .
```

Run container:

Before executing this line, you have to modify `docker/docker_env` file adding values to variables in there. These
variables are:

- MAILGUN_DOMAIN: domain configured in mailgun account
- MAILGUN_KEY: mailgun key to authenticate on mailgun service
- EMAIL_TO_RETRIEVE_DBF_FILE: email where dbf files are sent every day
- EMAIL_PASSWORD_TO_RETRIEVE_DBF_FILE: app password to access to email account without additional verifications
- EMAIL_DESTINATION_LIST: list of emails that will receive the gtfs file divided by spaces

To get mailgun data you have to go to: https://app.mailgun.com/app/sending/domains/, choose a domain (or add one) and
then, create an API KEY in the "Sending API keys" tab.

Concerning to email app password, we recommend seeing this
link: https://towardsdatascience.com/how-to-easily-automate-emails-with-python-8b476045c151

```
docker run --env-file docker\docker_env el-teniente-gtfs-builder:latest
```