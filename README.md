# Anvil Labs Integration Testing
A repo for running integration tests against the Anvil Labs code.

## Prerequisites

* Install [Docker Engine](https://docs.docker.com/engine/install/)
* Install [Docker Compose](https://docs.docker.com/compose/install/)

Note - you can instead install [Docker Desktop](https://docs.docker.com/desktop/) which includes both the above tools.

* Clone this reposistory to your local machine
```
git clone --recursive https://github.com/anvilistas/anvil-labs-tests.git
```
* Clone the Anvil Labs repository to your local machine
```
git clone https://github.com/anvilistas/anvil-labs.git
```

## Configuration
* Copy the file 'env.example' to a new file named '.env'
* Open '.env' with your preferred editor and replace the placeholder text with the path to your clone of the Anvil Labs repository.
* Save the file

## Running the Tests
* Start the anvil app server
```
docker-compose up -d app
```
For the first run, this will take some time as it will download the necessary docker images to your machine.
Subsequent runs will not need to do this.

The `-d` options starts the database and app server containers and then detaches from them.
If you prefer to see the output from those whilst they are running, omit that option. You will
then need to use a new terminal session for the next step.
* Run the tests
```
docker-compose up test_runner
```
* Stop the anvil app server
```
docker-compose down
```

## Updating
As we update this repo, the images you have downloaded for the containers will become out
of date. To fetch the latest images:
```
docker-compose pull
``

