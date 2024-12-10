![Lint-free](https://github.com/nyu-software-engineering/containerized-app-exercise/actions/workflows/lint.yml/badge.svg)

# Containerized App Exercise

Build a containerized app that uses machine learning. See [instructions](./instructions.md) for details.


# Containerized Machine Learning Dashboard

## Project Description

This project demonstrates a containerized system for a Machine Learning Dashboard. It consists of three subsystems:
1. **Machine Learning Client:** A Python-based service that generates random sensor data (e.g., camera values) and performs basic analysis.
2. **Web App:** A Flask-based web interface that retrieves and displays the data from the database.
3. **MongoDB Database:** A containerized MongoDB instance for storing and retrieving data.

The system is fully containerized using Docker and orchestrated with `docker-compose`, allowing seamless deployment and scalability.


## Teammates

- [Finnick Li](https://github.com/FinnickL)


## Setup and Run Instructions

### Prerequisites

1. Install [Docker](https://docs.docker.com/get-docker/) and ensure `docker` and `docker-compose` are available.
2. Clone this repository:

### Configuration

1. Create a `.env` file in the root directory with the following contents:
   ```env
   MONGO_URI=mongodb://mongodb:27017/
   MONGO_DB_NAME=ml_dashboard
   ```

2. The `.env` file is ignored by Git for security purposes. Ensure teammates have access to this file through a secure channel.

### Run the System

1. Build and run all containers:
   ```bash
   docker compose up --build
   ```

2. Access the web app in your browser at [http://localhost:5001](http://localhost:5001).

### Stop the System

1. To stop the containers:
   ```bash
   docker compose down
   ```

### Testing

1. To test the Machine Learning Client:
   ```bash
   docker exec -it ml_client pytest
   ```

2. To test the Web App:
   ```bash
   docker exec -it web_app pytest
   ```

## Environment Variables and Data Setup

### Environment Variables

- `MONGO_URI`: The connection string for MongoDB. Set to `mongodb://mongodb:27017/` in development.
- `MONGO_DB_NAME`: The name of the MongoDB database used by the app.

### Starter Data

The database is populated with sensor data dynamically by the Machine Learning Client. No additional starter data is required.

```