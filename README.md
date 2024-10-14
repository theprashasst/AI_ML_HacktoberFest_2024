## Welcome to ACM-JEC's official ML repository for Hacktoberfest 2024!!

---

<img width="1383" alt="image" src="https://github.com/user-attachments/assets/3af0672a-93f0-4fb2-af86-f65976b2b21b">

---


We are  developing a **GitHub Triage Issue AI Bot** in this HacktoberFest to streamline issue and pull request (PR) management within code repositories. This bot is designed to enhance the efficiency of project maintainers and contributors by offering the following key features:

1. **Issue Analysis and Solution Suggestions**: When an issue is raised, the bot automatically scans the entire codebase to identify the file and specific line where the problem originates. It also suggests potential solutions to address the issue, reducing the time developers spend on debugging.
2. **Automatic Labeling**: The bot automatically assigns appropriate labels to each issue based on the problem description, ensuring better categorization and faster resolution.
3. **PR Feedback and Code Corrections**: Upon receiving a pull request, the bot analyzes the submitted code, providing detailed feedback or corrections directly in the form of a comment. This ensures that code quality and standards are maintained efficiently.

---

## Flow Diagram

---

Before understanding the flow, let's clear out any unnecessary jargon (i.e., complicated tech words).

- **GitHub Webhook Event**: A message GitHub sends to notify the bot when something happens, like an issue or pull request (PR) being created.
- **Embeddings** help represent text in a way that makes it easier for machines to understand relationships between different pieces of text.
- **LLMs** are powerful models that can generate and analyze text based on the input they receive.
- CodeBert is a specifically trained AI model for code generation, code transformation and creation of embeddings

[Additional Info](https://www.notion.so/Additional-Info-11a2832a465080609c17f3c093427c2b?pvs=21)

---
![image](https://github.com/user-attachments/assets/aae46dea-683f-4c1b-990d-0b222c127196)


---

### **Issue Processing Flow**:

1. **Event Received**: When a new issue is created on GitHub, the bot receives the webhook event notification.
2. **Determine Event Type**:
    - **Issue**: The bot identifies that this is an issue event.
3. **Processing the Issue**:
    - The bot begins processing and analyzing the issue details.
4. **AI Analysis**:
    - The AI, powered by a language model (LLM), analyzes the issue’s content to understand its context, language, and intent.
5. **Validate the Issue**:
    - The bot checks if the issue is valid based on the provided details (e.g., is it actionable, understandable, and related to the codebase?).
6. **Valid Issue**:
    1. **Analyze Code**:
        - The bot identifies the relevant part of the codebase where the issue might exist.
    2. **Create Code Embeddings**:
        - The bot uses **CodeBERT** to create embeddings for the related code. These embeddings represent the code in a numerical format that AI models can understand.
    3. **Search Codebase Using Embeddings**:
        - The bot searches the codebase for similar code patterns using the created embeddings to narrow down the location of the problem.
    4. **Find Problem Location**:
        - Based on the results from the codebase search, the bot identifies the exact file and line(s) where the issue occurs.
    5. **Generate Solution**:
        - The bot generates a possible solution to the problem using the information gathered and its AI model.
    6. **Post Response**:
        - The bot responds to the GitHub issue with:
            1. The **file location** where the problem is found.
            2. The **specific line numbers** where the issue exists.
            3. The **steps** to solve the issue, detailing potential code fixes.
7. **Invalid Issue**:
    - If the issue is deemed invalid:
        - The bot posts a response indicating that the issue is not valid and explains why.

---

### **Pull Request (PR) Processing Flow**:

1. **PR Received**:
    - When a new pull request (PR) is submitted on GitHub, the bot is notified via the webhook event.
2. **Get PR Changes**:
    - The bot retrieves the list of code changes made in the pull request.
3. **Create Code Embeddings for Changes**:
    - The bot uses **CodeBERT** to generate embeddings for the new code introduced in the PR. This helps the bot analyze the changes at a deeper level.
4. **Analyze Changes with AI**:
    - The bot uses an AI model to review the changes in the PR. It checks for code improvements, potential issues, and how the changes integrate with the rest of the codebase.
5. **Generate Review**:
    - The bot generates a detailed review of the pull request, including:
        1. **Code Quality Feedback**:
            - Overall comments on the quality of the submitted code.
        2. **Suggested Improvements**:
            - Recommendations for enhancing or fixing the code.
        3. **Specific Line Comments**:
            - Feedback on specific lines where issues were found or improvements can be made

---

---

### Examples:

- **For an Issue**:
    - If a bug is reported and the bot identifies an error in `app.js` at line 45, the bot would respond: “The issue is in `app.js` on line 45. Here’s a suggested fix: [insert steps].”
- **For a Pull Request**:
    - If a pull request adds new code, the bot might say: “This part of the code looks good, but here’s an improvement suggestion for line 20: [insert suggestion].”
