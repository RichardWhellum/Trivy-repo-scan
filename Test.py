# Vulnerable dependencies for testing OWASP Dependency-Check v2
import flask  # Version 0.x of Flask had known vulnerabilities (update to latest if in production)
import requests  # Versions below 2.20.0 had SSL certificate validation issues

# Simulating functionality
def insecure_function():
    print("This function uses potentially vulnerable packages.")

if __name__ == "__main__":
    insecure_function() 