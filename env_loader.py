import os
from dotenv import load_dotenv

load_dotenv()

def get_env_variable(var_name):
    return os.getenv(var_name, "Variable not found")

if __name__ == "__main__":
    print(get_env_variable("DATABASE_URL"))
