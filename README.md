## Aiogram Bot Example

<center> 

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</center>

## Description
An example aiogram project with architecture.
## Installation
1. Clone repo to your pc
    ```bash
    git clone git@github.com:withoutforget/AioExample.git
    cd AioExample
    ```
2. Then you need to install direnv and [hook](https://direnv.net/docs/hook.html) it.
   ```bash
   sudo apt install direnv # and hook
   direnv allow .
   ```
3. Clone config
    ```bash
    cp ./infra/example.config.toml ./infra/config.toml
    ```
## Running
First of all set your API key to config file and then you can do these things:
- Use `make build` to build, or also use `docker compose build`
- Use `make run` to up with detach, or also use `docker compose up --detach`
- Use `make watch` to watch, or also use `docker compose up --watch`
  