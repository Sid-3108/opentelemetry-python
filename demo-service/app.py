# Import Flask class from the flask package
# Flask is used to create a web service (server)
from flask import Flask

# Import Flask auto-instrumentation from OpenTelemetry
# This automatically captures HTTP request traces for Flask apps
from opentelemetry.instrumentation.flask import FlaskInstrumentor

# Import the OpenTelemetry trace API
# This provides functions to create and manage traces
from opentelemetry import trace

# Import TracerProvider
# This is the core engine that creates tracers and spans
from opentelemetry.sdk.trace import TracerProvider

# Import span processor and console exporter
# SpanProcessor decides WHAT to do with spans
# ConsoleSpanExporter prints spans to terminal
from opentelemetry.sdk.trace.export import (
    SimpleSpanProcessor,
    ConsoleSpanExporter,
)

from opentelemetry.sdk.resources import Resource

# Create a Flask application instance
# __name__ tells Flask where this app is located
app = Flask(__name__)

# Create a resource with a service name
# This tells OpenTelemetry: "this telemetry comes from demo-service"
resource = Resource.create({
    "service.name": "demo-service"
})

# Set tracer provider with resource attached
trace.set_tracer_provider(
    TracerProvider(resource=resource)
)


# Create a span processor that sends spans to the console
# "Simple" means: export span immediately when it ends
span_processor = SimpleSpanProcessor(ConsoleSpanExporter())

# Attach the span processor to the tracer provider
# Now every span created will be printed to terminal
trace.get_tracer_provider().add_span_processor(span_processor)

# Automatically instrument the Flask app
# This means:
# - Every HTTP request is traced
# - Spans are created without writing manual code
FlaskInstrumentor().instrument_app(app)

# Define a route for HTTP GET requests to "/"
# This runs when someone opens http://localhost:8080/
@app.route("/")
def home():
    # This is the HTTP response body
    return "Hey there, my service is running!"

# This block ensures the app runs only when this file
# is executed directly (not imported by another file)
if __name__ == "__main__":
    # Start the Flask web server
    # host="0.0.0.0" allows access from any network interface
    # port=8080 means the service listens on port 8080
    app.run(host="0.0.0.0", port=8080)
