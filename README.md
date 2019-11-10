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

### cURL example requests

1. Create a product

    ```bash
    curl -X POST \
    http://127.0.0.1:5000/products \
    -H 'Content-Type: application/json' \
    -d '{
        "title": "Jamón serrano",
        "productDescription": "Jamón serrano Fud 290g",
        "productBrand": "Fud",
        "price": 48.5
    }'
    ```

2. Get products list

    ```bash
    curl -X GET \
    http://127.0.0.1:5000/products \
    -H 'Content-Type: application/json'
    ```

3. Retrieve a product

    ```bash
    curl -X GET \
    http://127.0.0.1:5000/products/1 \
    -H 'Content-Type: application/json'
    ```

4. Update a product

    ```bash
    curl -X PUT \
    http://127.0.0.1:5000/products/1 \
    -H 'Content-Type: application/json' \
    -d '{
        "price": 53
    }'
    ```

5. Delete a product

    ```bash
    curl -X DELETE \
    http://127.0.0.1:5000/products/1 \
    -H 'Content-Type: application/json'
    ```
