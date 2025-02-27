


# Scientific Calculator DevOps

## Overview

This project is a simple yet functional scientific calculator implemented as a FastAPI web API.The project also includes unit tests, Dockerization, and a CI/CD pipeline setup using Jenkins and Ansible for automated building, testing, and deployment.

## Features

*   **API Endpoints for:**
    *   **Square Root (`/sqrt/{number}`):** Calculates the square root of a non-negative number.
    *   **Factorial (`/factorial/{number}`):** Calculates the factorial of a non-negative integer (limited to numbers <= 100 for performance).
    *   **Natural Logarithm (`/ln/{number}`):** Calculates the natural logarithm of a positive number.
    *   **Power (`/power/{base}/{exponent}`):** Calculates the power of a base raised to an exponent.
*  **HTML User Interface (`/ui`):** A web-based UI built with HTML, CSS, and JavaScript to interact with the API.
*   **Input Validation:** API endpoints include validation to handle invalid inputs (e.g., negative numbers for square root and logarithm, negative factorial, large factorials).
*   **Unit Tests:** Comprehensive unit tests using `unittest` to ensure the API endpoints function correctly.
*   **Dockerized Application:** The API is containerized using Docker for easy deployment and consistency across environments.
*   **CI/CD Pipeline with Jenkins:** Automated build, test, and deployment pipeline using Jenkins, Docker, and Docker Hub.
*   **Ansible Deployment:** Automated deployment of the Docker container to a local machine (can be extended for remote servers).

## Tech Stack

*   **Backend API:**
    *   [FastAPI](https://fastapi.tiangolo.com/):  A modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
    *   [Python 3.9+](https://www.python.org/): The programming language used for the API and tests.
    *   [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/):  A modern and designer-friendly templating language for Python, used for rendering the HTML UI.
    *   [Uvicorn](https://www.uvicorn.org/): An ASGI web server, used to run the FastAPI application.
*   **Frontend UI:**
    *   [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML):  For structuring the web page.
    *   [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS): For styling the web page.
    *   [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript): For handling user interactions and API calls in the UI.
*   **Testing:**
    *   [unittest](https://docs.python.org/3/library/unittest.html): Python's built-in testing framework used for unit testing.
    *   [FastAPI `TestClient`](https://fastapi.tiangolo.com/tutorial/testing/):  Used for testing FastAPI applications.
*   **Containerization:**
    *   [Docker](https://www.docker.com/):  Platform for developing, shipping, and running applications in containers.
*   **CI/CD:**
    *   [Jenkins](https://www.jenkins.io/):  An open-source automation server for CI/CD.
    *   [Docker Hub](https://hub.docker.com/):  A Docker registry service for storing and sharing Docker images.
*   **Deployment:**
    *   [Ansible](https://www.ansible.com/): An open-source automation tool used for application deployment, configuration management, and task automation.

## Setup Instructions

### Prerequisites

*   [Python 3.9+](https://www.python.org/downloads/) installed on your system.
*   [Docker](https://www.docker.com/products/docker-desktop) installed and running if you plan to build and run the Docker image.
*   [Jenkins](https://www.jenkins.io/doc/book/getting-started/docker/) installed and running if you plan to use the CI/CD pipeline.
*   [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/index.html) installed if you plan to use Ansible for deployment.

### Local Setup

1.  **Clone the repository:**
    ```bash
    git clone <YOUR_REPOSITORY_URL>
    cd SPE_mini_project # Or the name of your cloned repository
    ```

2.  **Create a virtual environment :**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**
    ```bash
    python3 -m pip install --upgrade pip
    python3 -m pip install -r requirements.txt
    ```

4.  **Run the FastAPI application:**
    ```bash
    uvicorn main:app --reload --host 0.0.0.0 --port 8000
    ```
    
    *   `--host 0.0.0.0`:  Makes the server accessible from outside your local machine (if needed).
    *   `--port 8000`: Runs the server on port 8000.

5.  **Access the API and UI:**
    *   **API Endpoints:** You can access the API endpoints directly using tools like `curl`, `Postman`, or your browser. For example:
        *   Square root of 25:  `http://localhost:8000/sqrt/25`
        *   Factorial of 5: `http://localhost:8000/factorial/5`
        *   Natural log of 2.71828: `http://localhost:8000/ln/2.71828`
        *   2 to the power of 3: `http://localhost:8000/power/2/3`
    *   **HTML UI:** Open your web browser and go to: `http://localhost:8000/ui`

## API Endpoints

### 1. Square Root (`/sqrt/{number}`)

*   **Method:** `GET`
*   **Path Parameter:**
    *   `number` (float): The number for which to calculate the square root. Must be non-negative.
*   **Response (JSON):**
    *   `result` (float): The square root of the input number.
    *   **Error Responses:**
        *   `400 Bad Request`: If the input `number` is negative.

**Example Request:**

```bash
curl http://localhost:8000/sqrt/25
```

**Example Response:**

```json
{"result": 5.0}
```

### 2. Factorial (`/factorial/{number}`)

*   **Method:** `GET`
*   **Path Parameter:**
    *   `number` (int): The integer for which to calculate the factorial. Must be a non-negative integer less than or equal to 100.
*   **Response (JSON):**
    *   `result` (int): The factorial of the input number.
    *   **Error Responses:**
        *   `400 Bad Request`: If the input `number` is negative or greater than 100.

**Example Request:**

```bash
curl http://localhost:8000/factorial/5
```

**Example Response:**

```json
{"result": 120}
```

### 3. Natural Logarithm (`/ln/{number}`)

*   **Method:** `GET`
*   **Path Parameter:**
    *   `number` (float): The number for which to calculate the natural logarithm. Must be a positive number.
*   **Response (JSON):**
    *   `result` (float): The natural logarithm of the input number.
    *   **Error Responses:**
        *   `400 Bad Request`: If the input `number` is zero or negative.

**Example Request:**

```bash
curl http://localhost:8000/ln/2.71828
```

**Example Response:**

```json
{"result": 0.9999987992495201}
```

### 4. Power (`/power/{base}/{exponent}`)

*   **Method:** `GET`
*   **Path Parameters:**
    *   `base` (float): The base number.
    *   `exponent` (float): The exponent.
*   **Response (JSON):**
    *   `result` (float): The result of `base` raised to the power of `exponent`.

**Example Request:**

```bash
curl http://localhost:8000/power/2/3
```

**Example Response:**

```json
{"result": 8.0}
```

### 5. Root Endpoint (`/`)

*   **Method:** `GET`
*   **Description:**  A welcome message for the API.
*   **Response (JSON):**
    *   `message` (str):  Welcome message and instructions on how to use the API.

**Example Request:**

```bash
curl http://localhost:8000/
```

**Example Response:**

```json
{"message": "Welcome to the Scientific Calculator API. Access operations via /sqrt, /factorial, /ln, /power endpoints. For UI, go to /ui"}
```

### 6. HTML UI (`/ui`)

*   **Method:** `GET`
*   **Description:** Serves the HTML user interface for the calculator.
*   **Response (HTML):**
    *   Renders the `calculator.html` template.

**Example Request:**

Open your browser and navigate to `http://localhost:8000/ui`.

## Running Unit Tests

To run the unit tests, execute the following command in your project directory:

```bash
python3 -m unittest test_main.py
```

This will run all the test cases defined in `test_main.py` and report the results. All tests should pass if the application is functioning correctly.

**Example Test Output (Successful):**
```
...
----------------------------------------------------------------------
Ran 18 tests in 0.020s

OK
```

## Dockerization

The project is Dockerized to ensure consistent execution across different environments.

### Building the Docker Image

1.  Build the Docker image using the following command:

    ```bash
    docker build -t scientific_calculator .
    ```
    *   `-t scientific_calculator`: Tags the image with the name `scientific_calculator`.
    *   `.`: Specifies the build context as the current directory.

### Running the Docker Container

```bash
docker run -d -p 8000:8000 scientific_calculator
```
*   `-d`: Runs the container in detached mode (in the background).
*   `-p 8000:8000`: Maps port 8000 of the host to port 8000 of the container, making the application accessible on `http://localhost:8000`.

You can then access the API and UI in your browser or using `curl` as described in the "API Endpoints" section, using `http://localhost:8000`.

### Pushing to Docker Hub (CI/CD)

The Jenkins pipeline automates the process of building and pushing the Docker image to Docker Hub. 

1.  Have a Docker Hub account.
2.  Update the `DOCKER_TAG` environment variable in the `Jenkinsfile` with your Docker Hub username and repository name.
3.  Configure Docker credentials in Jenkins (as specified by `DOCKER_CREDENTIALS_ID` in the `Jenkinsfile`).

## CI/CD Pipeline with Jenkins

A Jenkins pipeline is set up to automate the following stages:

1.  **Checkout Code:** Clones the project repository from GitHub.
2.  **Install Dependencies:** Sets up a Python virtual environment and installs required Python packages from `requirements.txt`.
3.  **Run Unit Tests:** Executes the unit tests to ensure code quality and functionality.
4.  **Build Docker Image:** Builds a Docker image from the `Dockerfile`.
5.  **Login to Docker Hub:** Logs in to Docker Hub using provided credentials.
6.  **Push to Docker Hub:** Tags and pushes the Docker image to your Docker Hub repository.
7.  **Clean Up Docker Images:** Removes local Docker images to save space.
8.  **Deploy using Ansible:**  Deploys the Docker container to a target environment using Ansible.


## Ansible Deployment

Ansible is used for deploying the Docker container. The `deploy.yml` playbook is configured to:

1.  Ensure Docker is installed on the target machine.
2.  Pull the latest Docker image from Docker Hub.
3.  Remove any existing container (if running).
4.  Run a new Docker container with the latest image, mapping port 8000.

**To use Ansible for deployment:**

1.  Ensure Ansible is installed on your control machine

    ```bash
    ansible-playbook -i inventory deploy.yml
    ```
    *   `-i inventory`: Specifies the inventory file.
    *   `deploy.yml`: The Ansible playbook file.

**Ansible Playbook Structure (`deploy.yml`)**
**Individual Task Breakdown (within `tasks` section)**

1.  **Ensure Docker is installed:**

    ```yaml
    - name: Ensure Docker is installed
      command: docker --version
      register: docker_installed
      ignore_errors: yes
    ```
    *   **`name: Ensure Docker is installed`**: Task description.
    *   **`command: docker --version`**: Executes `docker --version` command.
    *   **`register: docker_installed`**: Saves command output to `docker_installed` variable.
    *   **`ignore_errors: yes`**: Continue playbook even if this task fails.

2.  **Install Docker if not installed:**

    ```yaml
    - name: Install Docker if not installed
      when: docker_installed.rc != 0
      block:
        - name: Install Homebrew (if needed)
          command: /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
          args:
            creates: /opt/homebrew/bin/brew
        - name: Install Docker using Homebrew
          command: brew install --cask docker
    ```
    *   **`name: Install Docker if not installed`**: Task description.
    *   **`when: docker_installed.rc != 0`**: Run this task *only if* the previous task's return code (`rc`) was not 0 (meaning Docker check failed).
    *   **`block:`**: Group of tasks to execute if `when` condition is true.
        *   **`- name: Install Homebrew (if needed) ...`**: Installs Homebrew (package manager for macOS) if not already present.
        *   **`- name: Install Docker using Homebrew ...`**: Installs Docker Desktop using Homebrew (i use macos). 

3.  **Start Docker (if not running):**

    ```yaml
    - name: Start Docker (if not running)
      shell: open -a Docker
      ignore_errors: yes
    ```
    *   **`name: Start Docker (if not running)`**: Task description.
    *   **`shell: open -a Docker`**: Executes `open -a Docker` command (macOS) to start Docker Desktop.
    *   **`ignore_errors: yes`**: Continue even if starting Docker fails.

4.  **Wait for Docker to be available:**

    ```yaml
    - name: Wait for Docker to be available
      command: docker info
      register: docker_status
      until: docker_status.rc == 0
      retries: 10
      delay: 5
    ```
    *   **`name: Wait for Docker to be available`**: Task description.
    *   **`command: docker info`**: Executes `docker info` to check Docker status.
    *   **`register: docker_status`**: Saves command output to `docker_status` variable.
    *   **`until: docker_status.rc == 0`**: Retry task until `docker info` succeeds (return code 0).
    *   **`retries: 10`**: Maximum retries.
    *   **`delay: 5`**: Wait 5 seconds between retries.

5.  **Install required Ansible collections:**

    ```yaml
    - name: Install required Ansible collections
      ansible.builtin.command: ansible-galaxy collection install community.docker
    ```
    *   **`name: Install required Ansible collections`**: Task description.
    *   **`ansible.builtin.command: ansible-galaxy collection install community.docker`**: Installs the `community.docker` Ansible collection needed for Docker modules.

6.  **Pull the latest Docker image:**

    ```yaml
    - name: Pull the latest Docker image
      community.docker.docker_image:
        name: "dhruva1098/scientific-calculator"
        source: pull
    ```
    *   **`name: Pull the latest Docker image`**: Task description.
    *   **`community.docker.docker_image:`**: Uses `docker_image` module from `community.docker` collection.
    *   **`name: "dhruva1098/scientific-calculator"`**: Docker image name to pull.
    *   **`source: pull`**:  Instruction to pull the image from registry.

7.  **Remove existing container (if running):**

    ```yaml
    - name: Remove existing container (if running)
      community.docker.docker_container:
        name: calculator-container
        state: absent
    ```
    *   **`name: Remove existing container (if running)`**: Task description.
    *   **`community.docker.docker_container:`**: Uses `docker_container` module.
    *   **`name: calculator-container`**: Container name to manage.
    *   **`state: absent`**: Ensure container is absent (stopped and removed).

8.  **Run the container:**

    ```yaml
    - name: Run the container
      community.docker.docker_container:
        name: calculator-container
        image: "dhruva1098/scientific-calculator:latest"
        state: started
        restart_policy: always
        ports:
          - "8000:8000"
    ```
    *   **`name: Run the container`**: Task description.
    *   **`community.docker.docker_container:`**: Uses `docker_container` module.
    *   **`name: calculator-container`**: Container name.
    *   **`image: "dhruva1098/scientific-calculator:latest"`**: Docker image to use.
    *   **`state: started`**: Ensure container is started.
    *   **`restart_policy: always`**: Restart container automatically if it stops.
    *   **`ports: - "8000:8000"`**: Map host port 8000 to container port 8000.

