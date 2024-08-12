# Django Server Boilerplate

This boilerplate project is designed to kickstart development of web applications using Django 5.0.3. It integrates a variety of technologies to cover common web application needs, including AWS services (S3, EC2, Lambda), environment variable management, uWSGI for application serving, Nginx as a reverse proxy, and PostgreSQL for database services.

## Features

- **Django 5.0.3**: A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- **Django Ninja**: For building fast APIs with Django and Python 3.6+ type hints.
- **Django SimpleJWT**: Provides JSON Web Token (JWT) authentication for Django.
- **Django Swagger**: For generating interactive API documentation.
- **AWS S3**: For storing static and media files.
- **AWS EC2**: For hosting the application.
- **AWS Cloudwatch Logs**: For monitoring and logging application and infrastructure performance.
- **AWS Lambda**: For running serverless computing functions.
- **AWS IAM**: For managing access to AWS services and resources securely.
- **.env**: For managing environment variables securely.
- **uWSGI**: As the application server, interfacing with Nginx.
- **Nginx**: Serving as a reverse proxy to uWSGI, handling HTTP requests.
- **PostgreSQL**: A powerful, open-source object-relational database system.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip and virtualenv
- AWS CLI configured with your credentials
- PostgreSQL installed and running

### Installation

1. Clone the repository:

```bash
git clone https://github.com/siimtech/django-boilerplate.git
cd django-boilerplate
```

2. Create a virtual environment:

```bash
virtualenv venv
source venv/bin/activate
```

3. Install Pre-installed packages:

```bash
pip install -r requirements.txt
```

### Running the Project

1. Apply database migrations:

```bash
python manage.py migrate
```

2. Run the development server:

```bash
python manage.py runserver
```

3. Access the application:
    - Open a web browser and navigate to http://127.0.0.1:8000/.


### Api Docs
Django Swagger and Ninja provide interactive API documentation. Access it at:

- Django Swagger
```bash
http://your-domain/swagger/
```

- Django Ninja
```bash
http://your-domain/api/docs/
```

### Contributing
Contributions are welcome! Please submit a pull request or open an issue for any improvements or bug fixes.

