# System Architecture – Smart Resource Finder

## 1. Data Flow

1. The user enters a topic in the Streamlit interface.
2. The application receives the topic and sorting preference.
3. Python sends an HTTP request to the GitHub Search API.
4. GitHub returns repository information in JSON format.
5. The application processes the response.
6. Streamlit displays repository names, descriptions, stars, forks, and links.

## 2. Design Choices

- **Python:** Used for application logic.
- **Streamlit:** Used to build the web interface.
- **Requests:** Used to communicate with the GitHub API.
- **GitHub Search API:** Used as the repository data source.

## 3. Efficiency

- The application requests a limited number of repositories per search.
- Results are sorted by stars or forks.
- Only relevant repository information is displayed.

## 4. Resilience

- The application checks the API response status.
- It handles unsuccessful requests.
- It displays a message when no repositories are found.
- Network and API errors should be handled gracefully.
