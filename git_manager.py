import os

def commit_and_push(message="Updated project files"):
    os.system("git add .")
    os.system(f'git commit -m "{message}"')
    os.system("git push origin main")

if __name__ == "__main__":
    commit_and_push()
