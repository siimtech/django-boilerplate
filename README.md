# Django Server Boilerplate

This boilerplate project is designed to kickstart development of web applications using Django 5.0.3. It integrates a variety of technologies to cover common web application needs, including AWS services (S3, EC2, Lambda), environment variable management, uWSGI for application serving, Nginx as a reverse proxy, and PostgreSQL for database services.

## Features

- **Django 5.0.3**: A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- **AWS S3**: For storing static and media files.
- **AWS EC2**: For hosting the application.
- **AWS Lambda**: For running serverless computing functions.
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