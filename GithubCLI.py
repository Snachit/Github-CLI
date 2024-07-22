import requests
import pyfiglet
from termcolor import colored
import inquirer  

GITHUB_API_URL = "https://api.github.com"

def display_intro():
    """Displays an introductory message."""
    intro_text = pyfiglet.figlet_format("GitHub CLI")
    print(colored(intro_text, 'blue'))
    print(colored("Manage your GitHub repositories with ease.\n", 'green'))
    print(colored("💻🌟 Welcome to the GitHub CLI tool! 🌟💻\n", 'cyan'))

def get_access_token():
    """Prompts the user to input their GitHub access token."""
    return input("🔑 Enter your GitHub personal access token: ")

def get_repos(access_token):
    """Fetches all repositories of the authenticated user."""
    url = f"{GITHUB_API_URL}/user/repos"
    headers = {"Authorization": f"token {access_token}"}
    params = {"per_page": 100}  # To handle pagination if you have many repos
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def update_repo_visibility(username, repo_name, visibility, access_token):
    """Updates the visibility of the specified repository."""
    url = f"{GITHUB_API_URL}/repos/{username}/{repo_name}"
    headers = {"Authorization": f"token {access_token}"}
    data = {"private": visibility}
    response = requests.patch(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()

def delete_repo(username, repo_name, access_token):
    """Deletes the specified repository."""
    url = f"{GITHUB_API_URL}/repos/{username}/{repo_name}"
    headers = {"Authorization": f"token {access_token}"}
    response = requests.delete(url, headers=headers)
    response.raise_for_status()
    return response.status_code == 204

def display_repos(repos):
    """Displays a list of repositories."""
    for idx, repo in enumerate(repos, start=1):
        print(f"{idx}. {repo['name']} " + colored(f"(Private: {repo['private']})","red"))

def process_choices(repos, action, access_token):
    """Processes user choices to update repository visibility or delete repositories."""
    choices = input(colored(f"Enter the numbers of the repositories you want to {action}, separated by commas: ", 'magenta')).split(',')
    for choice in choices:
        try:
            repo_index = int(choice.strip()) - 1
            if 0 <= repo_index < len(repos):
                repo_name = repos[repo_index]['name']
                username = repos[repo_index]['owner']['login']
                if action == "delete":
                    print(f"🗑️ Deleting {repo_name}...")
                    delete_repo(username, repo_name, access_token)
                    print(f"{repo_name} has been deleted.")
                else:
                    visibility = action == "make private"
                    print(f"🔒 Updating {repo_name} visibility to {'private' if visibility else 'public'}...")
                    update_repo_visibility(username, repo_name, visibility, access_token)
                    print(f"{repo_name} is now {'Private' if visibility else 'Public'}.")
            else:
                print(f"⚠️ Invalid selection: {choice}")
        except ValueError:
            print(f"⚠️ Invalid input: {choice}")

if __name__ == "__main__":
    display_intro()
    access_token = get_access_token()

    while True:
        questions = [
            inquirer.List(
                'choice',
                message="Choose your option:",
                choices=[
                    '1- Make repositories Private 🔒',
                    '2- Make repositories Public 🌍',
                    '3- Delete repositories 🗑️'
                ]
            )
        ]
        
        answers = inquirer.prompt(questions)
        choice = answers['choice'].split('-')[0].strip()

        if choice in ['1', '2', '3']:
            repos = get_repos(access_token)
            if choice == '1':
                repos = [repo for repo in repos if not repo['private']]  # Only show public repos
            elif choice == '2':
                repos = [repo for repo in repos if repo['private']]  # Only show private repos

            display_repos(repos)
            
            if choice == '1':
                process_choices(repos, "make private", access_token)
            elif choice == '2':
                process_choices(repos, "make public", access_token)
            elif choice == '3':
                process_choices(repos, "delete", access_token)
        else:
            print(colored("⚠️ Invalid Option! Choose 1, 2, or 3.", 'red'))
        
        continue_choice = input("Do you want to continue? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            print(colored("👋 Goodbye!", 'cyan'))
            break
