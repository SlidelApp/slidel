# Slidel

## Development Instructions

Both the frontend and backend are stored in this repository. The frontend is
located in the `frontend` directory and the backend is located in the `backend`
directory.

### Install Dependencies

#### Frontend

This project uses [Node.js](https://nodejs.org/) lts v20.
Dependency Management for the frontend is done with [Yarn](https://yarnpkg.com/).
After installing yarn, to install dependencies, run:

```bash
cd frontend
yarn install
```

#### Backend

Dependency Management for the backend is done with
[Poetry](https://python-poetry.org/). After installing poetry, to install
dependencies, run:

```bash
cd backend
poetry install
```

For further instructions on how to add and manage dependencies please refer to
the [Poetry Documentation](https://python-poetry.org/docs/).

### Development Server

#### Frontend Vite Server

To start the frontend development server, run:

```bash
cd frontend
yarn start
```

### Linting

#### Backend pre-commit linting

To automatically lint the python code for the backend, run:

```bash
cd backend
poetry run pre-commit run --all-files
```

within the `backend` directory.

### Git Workflow

Please make a new branch, preferably off of `main`, for each feature you are
working on. When you are done with your feature, please open a pull request.

Please make sure resolve any merge conflicts and make sure linting and tests
pass before merging a pull request.

All pull requests must be reviewed by at least one other person before being
merged into `main`.



