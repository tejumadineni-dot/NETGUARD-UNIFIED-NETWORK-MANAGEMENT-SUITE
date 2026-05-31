# Flask framework import
from flask import Flask

# Swagger UI import
from flasgger import Swagger

# Import all API routes
from routes import api_routes


# Create Flask application
app = Flask(__name__)


# Swagger configuration
app.config['SWAGGER'] = {
    'title': 'NetGuard Network Health API',
    'uiversion': 3
}


# Initialize Swagger
swagger = Swagger(app)


# Register all routes
app.register_blueprint(api_routes)


# Start application
if __name__ == "__main__":
    app.run(debug=True)