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

### Testing (continued)
```markdown
    ```bash
    python manage.py test
    ```

2. Coverage Report:
    - Generate a test coverage report using `coverage.py`.
    ```bash
    coverage run --source='.' manage.py test
    coverage html
    ```

    - Open the `htmlcov/index.html` file in your browser to view the coverage report.
```

### Code Quality and Linting
Add code quality checks using linters and formatters.
```markdown
## Code Quality and Linting

Ensure your code follows best practices and is free of common errors.

### Flake8 for Linting

Install Flake8:
```bash
pip install flake8
```

Run Flake8:
```bash
flake8 .
```

### Black for Code Formatting

Install Black:
```bash
pip install black
```

Format your code:
```bash
black .
```
```

### Security Best Practices
Include security best practices such as managing sensitive information and dependencies.
```markdown
## Security Best Practices

### Managing Environment Variables

Use environment variables to manage secret keys and sensitive data. Ensure you never commit your `.env` files to version control.

### Updating Dependencies

Regularly update your dependencies to patch known vulnerabilities:
```bash
pip install --upgrade -r requirements.txt
```

### Django Security Middleware

Ensure the following middleware is included in your `settings.py` for added security:

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # other middleware...
]

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
```

### Using HTTPS

Always use HTTPS to protect data in transit. Configure Nginx to support HTTPS with Let's Encrypt or another SSL/TLS certificate provider.
```

### Monitoring and Logging
Provide more detail about monitoring and logging setup using AWS CloudWatch.
```markdown
## Monitoring and Logging

### AWS CloudWatch Logs

Configure Django to send logs to AWS CloudWatch:

1. Install `watchtower`:
    ```bash
    pip install watchtower
    ```

2. Update your logging configuration in `settings.py`:
    ```python
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'watchtower': {
                'level': 'DEBUG',
                'class': 'watchtower.CloudWatchLogHandler',
                'boto3_session': boto3.Session(), # add boto3 session if needed
                'log_group': 'your-log-group',
            },
            # other handlers...
        },
        'loggers': {
            'django': {
                'handlers': ['watchtower'],
                'level': 'DEBUG',
                'propagate': True,
            },
        }
    }
    ```
```

### Deployment Instructions
Add detailed deployment instructions for AWS EC2, including setup scripts.
```markdown
## Deployment Instructions

### Setting up AWS EC2

1. Launch an EC2 instance with the appropriate AMI (e.g., Ubuntu).

2. SSH into your instance:
    ```bash
    ssh -i your-key.pem ubuntu@your-ec2-instance-ip
    ```

3. Install required software:
    ```bash
    sudo apt update
    sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl
    sudo pip3 install virtualenv
    ```

4. Clone your repository:
    ```bash
    git clone https://github.com/siimtech/django-boilerplate.git
    cd django-boilerplate
    ```

5. Follow the installation instructions to set up your virtual environment, install dependencies, and configure environment variables.

6. Configure uWSGI and Nginx:
    - Create a `uwsgi.ini` file:
        ```ini
        [uwsgi]
        module = yourproject.wsgi:application
        master = true
        processes = 10
        socket = /run/uwsgi/yourproject.sock
        chmod-socket = 660
        vacuum = true
        die-on-term = true
        ```

    - Update your Nginx configuration:
        ```nginx
        server {
            listen 80;
            server_name your-domain.com;
            
            location / {
                uwsgi_pass unix:/run/uwsgi/yourproject.sock;
                include uwsgi_params;
            }

            location /static/ {
                alias /home/ubuntu/yourproject/static/;
            }

            location /media/ {
                alias /home/ubuntu/yourproject/media/;
            }
        }
        ```

    - Start uWSGI and Nginx:
        ```bash
        sudo systemctl start uwsgi
        sudo systemctl enable uwsgi
        sudo systemctl restart nginx
        ```

7. Secure your deployment with HTTPS by obtaining an SSL certificate from Let's Encrypt:
    ```bash
    sudo apt-get install certbot python3-certbot-nginx
    sudo certbot --nginx -d your-domain.com
    ```

Now, your Django application should be live and accessible via your domain!
```

### Troubleshooting
Include common troubleshooting tips and solutions.
```markdown
## Troubleshooting

### Common Issues

#### Database Connection Error

- Ensure PostgreSQL is running and accessible.
- Verify `DATABASES` configuration in `settings.py`.

#### Static Files Not Displaying

- Run collectstatic:
    ```bash
    python manage.py collectstatic
    ```

- Check Nginx configuration for static and media files.

#### AWS Permissions Issues

- Check IAM roles and policies attached to your AWS resources.
- Ensure the correct AWS credentials are loaded.

#### Application Fails to Start

- Check logs in EC2 and CloudWatch.
- Validate `uwsgi.ini` and Nginx configuration syntax.
```

With these additions, your Django Server Boilerplate will be even more robust and ready for development and deployment scenarios.