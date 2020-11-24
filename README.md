# HomeworkSubmit

### How to Contribute?

Install pre-requisites

- Python3
- Python3-pip
- Docker
- Docker-Compose

##### On Windows

- Visit [Python official website](https://www.python.org/) to download Python ( Included pip )

- [Install DockerDesktop](https://docs.docker.com/get-docker/) 

##### On Linux

- Install Python & Python-pip
    - Ubuntu
        ```bash
        apt install python3 python3-pip -y
        ```

    - CentOS
        ```bash
        dnf install python3 python3-pip -y
        ```
- [Install Docker](https://docs.docker.com/get-docker/) 

- [Install Docker-Compose](https://docs.docker.com/compose/install)

### Restore dependencies

```bash
pip3 install -r requirements.txt
```

### Run

```bash
python3 src/main.py
```

### Build Docker Image

```base
docker build .
```

### Build Docker Image with FileBrowser

```bash
docker-compose up
```

### What is FileBrowser?

filebrowser provides a file managing interface within a specified directory and it can be used to upload, delete, preview, rename and edit your files. It allows the creation of multiple users and each user can have its own directory. It can be used as a standalone app or as a middleware.

[Repository](https://github.com/filebrowser/filebrowser)
