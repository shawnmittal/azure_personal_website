# Entry point for the application.
from . import app    # For application discovery by the 'flask' command. 

if __name__ == '__main__':
    # for local testing
    app.run(host='127.0.0.1', port=5000, debug=True)