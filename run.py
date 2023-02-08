from app import app
import os
host_ip = os.environ['HOST_IP'] if  os.environ['HOST_IP'] else "127.0.0.1"

if __name__ == "__main__":
    app.config['ENV']="development"
    app.run(debug=True, host=host_ip)

