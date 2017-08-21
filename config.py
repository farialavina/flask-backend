# Create dummy secrey key so we can use sessions

SECRET_KEY = 'our-very-first-project-in-flask'

# Create database
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Lavina@123456@localhost/project_event'
SQLALCHEMY_ECHO = True

# Flask-Security URLs, overridden because they don't put a / at the end
SECURITY_LOGIN_URL = "/login/"
SECURITY_LOGOUT_URL = "/logout/"