# GitHub CLI Tool
![Terminal Screenshot](GithubCLI.png)
## Overview
The GitHub CLI Tool is a command-line interface that allows you to manage your GitHub repositories with ease. You can make repositories private or public, and delete repositories directly from your terminal.

## Features
- **Make Repositories Private**
- **Make Repositories Public**
- **Delete Repositories**

## Prerequisites
- Python 3.x
- GitHub Personal Access Token

## Setup

1. **Clone the Repository**

    ```bash
    git clone https://github.com/your-username/github-cli-tool.git
    cd github-cli-tool
    ```

2. **Install Required Packages**

    Make sure you have `requests`, `pyfiglet`, and `termcolor` installed. You can install them using pip:

    ```bash
    pip install requests pyfiglet termcolor
    ```

3. **Run the CLI Tool**

    Execute the script using Python:

    ```bash
    python github_cli_tool.py
    ```

## Usage

1. When you run the script, you will be prompted to enter your GitHub personal access token:

    ```bash
    🔑 Enter your GitHub personal access token: your_token_here
    ```

2. Next, you will see the main menu with options to manage your repositories:

    ```bash
    Choose your option:
           1- Make repositories Private 🔒
           2- Make repositories Public 🌍
           3- Delete repositories 🗑️
    ```

3. Enter the number corresponding to your choice. For example, to make repositories private, type `1` and press Enter.

4. The script will then display your repositories. Enter the numbers of the repositories you want to manage, separated by commas:

    ```bash
    Enter the numbers of the repositories you want to make private, separated by commas: 1, 3, 5
    ```

5. Follow the prompts to complete the desired actions.

## Example

Here's a step-by-step example of how to make repositories private:

1. **Run the script:**

    ```bash
    python github_cli_tool.py
    ```

2. **Enter your GitHub personal access token:**

    ```bash
    🔑 Enter your GitHub personal access token: your_token_here
    ```

3. **Choose the option to make repositories private:**

    ```bash
    Choose your option:
           1- Make repositories Private 🔒
           2- Make repositories Public 🌍
           3- Delete repositories 🗑️
    ```

    Type `1` and press Enter.

4. **Enter the numbers of the repositories you want to make private:**

    ```bash
    Enter the numbers of the repositories you want to make private, separated by commas: 1, 2
    ```

5. **The tool will update the visibility of the selected repositories to private.**



