# simple-crud-flask

### Database

Create a postgresql database

```sql
CREATE DATABASE simple_crud_flask;
CREATE USER simple_flask WITH PASSWORD 'pass_simple_flask';
GRANT ALL PRIVILEGES ON DATABASE simple_crud_flask TO simple_flask;
```

### Install and run

1. Install [pipenv](https://pypi.org/project/pipenv/)

2. Install pipenv packages

    ```bash
    pipenv install
    ```

3. Run flask application

    There are two ways to run the web application with pipenv

    1. Enabling first pipenv

        ```bash
        pipenv shell
        ```

        ```bash
        Flask run
        ```

    2. Directly running with pipenv

        ```bash
        pipenv run Flask run
        ```
