# RamenGo Project (API)

The RamenGo API allows users to list available broths and proteins, and place an order for a delicious ramen meal.

![RamenGo](assets/ramengo.png)

## Getting Started

### Prerequisites

Make sure you have Python 3.7+ installed on your system.

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/jsrwell/ramengo_project
    cd ramengo_project
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Configuration and Secrets

The project uses environment variables for configuration. You can set these variables directly in your environment or create a `.env` file in the root directory of your project, areadly exists an `.env-example` file, rename it to `.env`. For this example, the API key is hardcoded in case of the `.env` file not exists, but in a real-world scenario, you would want to keep this key secret.

This project have two keys: 
- `API_KEY` - Key that have to be on each request for this API;
- `REDVENTURES_KEY` - Internal key to generate the order on external API.

*Change the keys if you need it!*

## Evaluating

### 1. Running the Application

To run the FastAPI application, use the following command:

```bash
uvicorn main:app --reload

# By default the application will run on http://127.0.0.1:8000
```

### 2. Testing With the RedVentures FrontEnd

Open on your browser https://tech.redventures.com.br/, insert the on the modal form:

- `API url` -> `http://127.0.0.1:8000`
- `API Key` -> `ac5923cd4de19298ce7e2f9dfaa2014a4dd782b1`

*This API default key is `ac5923cd4de19298ce7e2f9dfaa2014a4dd782b1`, but if you set other key on `.env` you must use the same.*

## Project Structure

```bash
.
├───.venv           # virtual envoirement
├───.vscode         # vscode configuration for python
├───.env-example    # rename to ".env" to set you own data
├───.gitignore      # git configurations
│
├───config.py       # project configurations
├───mocks.py        # mock data to handle the responses
├───schemas.py      # model schemas for responses
└───main.py         # main module with routes and api handlers
```

## Documentation of API

[Swagger UI](https://ramengo-project.onrender.com/docs) - Interactive API documentation (or access locally with `http://127.0.0.1/docs`)

## Online API Example

- [API Backend Ramengo](https://ramengo-project.onrender.com) - Access online API on (`https://ramengo-project.onrender.com`)
- API Key - `ac5923cd4de19298ce7e2f9dfaa2014a4dd782b1`
