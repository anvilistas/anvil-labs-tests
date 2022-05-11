# Anvil Labs Integration Testing
A repo for running integration tests against the Anvil Labs code.

## Prerequisites

* Install [Docker Engine](https://docs.docker.com/engine/install/)
* Install [Docker Compose](https://docs.docker.com/compose/install/)
* Clone this reposistory to your local machine
* Clone the Anvil Labs repository to your local machine

Note - you can instead install [Docker Desktop](https://docs.docker.com/desktop/) which includes both the above tools.

## Configuration
* Copy the file 'env.example' to a new file named '.env'
* Open '.env' with your preferred editor and replace the placeholder text with the path to your clone of the Anvil Labs repository.
* Save the file
* In your terminal, run 'docker compose up'

For the first run, this will take some time as it will download the necessary docker images to your machine.
Subsequent runs will not need to do this.
