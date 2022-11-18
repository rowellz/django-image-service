# Template for Django Project

Common setup for django project as a template

## Tech Stack

**Backend:** Django>=3.2.4,<3.3.0

**Database:** Postgres:latest

**Platform:** Docker

**Container Manage:** docker-compose

## Run Locally

You can fork this repository or
click the `Use this template` button. to customize.
Otherwise.

Clone the project

```bash
  git clone https://github.com/njmsaikat/django-postgres-setup-docker-compose.git
```

Go to the project directory

```bash
  cd django-postgres-setup-docker-compose
```

Run command

```bash
  docker-compose up --build
```

## Used Ports

- Django runs on port `8000`

- Postgresql runs on port `5432`

## Environment Variables

All environment variables for the development environment are stored in directory

.env > dev.env

## Support

For support, email njmsaikat@gmail.com

## Authors

- [@Saikat Roy](https://www.github.com/njmsaikat)

## LICENSE

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)
