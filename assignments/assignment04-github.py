import os
from git import Repo
from config import apikeys as cfg 

def replace_and_commit():
    # Configuration variables
    GITHUB_TOKEN = cfg['github_assignment']
    REPO_OWNER = "atacanbt"
    REPO_NAME = "WSAA-coursework"
    FILE_PATH = "assignments/andrew.txt"
    MY_NAME = "Atacan"

    # Clone the repository using HTTPS with token authentication
    repo_url = f"https://{GITHUB_TOKEN}@github.com/{REPO_OWNER}/{REPO_NAME}.git"
    local_dir = "assignments/temp_repo_github"  # Temporary directory for cloning

    # Clone repository if it doesn't exist locally
    if not os.path.exists(local_dir):
        Repo.clone_from(repo_url, local_dir)

    repo = Repo(local_dir)

    # Ensure we're working with the latest version
    repo.remotes.origin.pull()

    # Read and modify file
    full_path = os.path.join(local_dir, FILE_PATH)
    with open(full_path, 'r') as file:
        content = file.read()

    # Replace all instances of 'Andrew'
    modified_content = content.replace("Andrew", MY_NAME)

    # Write changes back to file
    with open(full_path, 'w') as file:
        file.write(modified_content)

    # Commit changes
    repo.git.add(update=True)
    repo.index.commit(f"Replaced Andrew with {MY_NAME}")

    # Configure author (replace with your details)
    with repo.config_writer() as git_config:
        git_config.set_value("atacanbt", "name", "Atacan")
        git_config.set_value("atacanbt", "email", "atacanbt@gmail.com")

    # Push changes
    origin = repo.remote(name='origin')
    origin.push()

    print("Changes committed and pushed successfully")

if __name__ == "__main__":
    replace_and_commit()