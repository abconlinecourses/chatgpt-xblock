# ChatGPT XBlock for the Open edX® Platform

The ChatGPT XBlock is a plugin for the Open edX platform that integrates ChatGPT, an AI language model developed by OpenAI, into your Open edX courses. This XBlock allows students to ask questions, receive real-time answers, reflect on responses, and enhance their learning experience with an interactive assistant.

---

## **Features**

- **AI-Powered Chat Assistant**: Add a ChatGPT-powered assistant to your Open edX courses.
- **Multi-Turn Conversations**: Enables a threaded, conversation-like experience with ChatGPT.
- **Content Moderation**: Uses OpenAI’s Moderation API to flag and prevent inappropriate content.
- **Reflection Tool**: Encourages students to submit reflections after receiving an answer.
- **Customizable Settings**:
  - Display name
  - Model selection (e.g., GPT-3.5, GPT-4)
  - API key
  - Context text for tailoring ChatGPT's responses
  - Description
- **User-Friendly Interface**:
  - Intuitive chat layout for students
  - Supports disclaimers and guidance messages
- **Robust Error Handling**: Provides meaningful feedback to students in case of API issues or inappropriate questions.

---

## **Installation**

1. Install the XBlock in your Open edX environment using pip:
```bash
   pip install "git+https://github.com/abconlinecourses/chatgpt-xblock.git"

```
2. Add 'chatgptxblock' to the INSTALLED_APPS list in your Open edX environment settings.

3. Restart your Open edX platform.

**Usage**

1.  **Enable the XBlock**:
    
    -   Navigate to the Open edX Studio for the course where you want to add the ChatGPT Assistant.
    -   Click on the **Advanced** tab.
    -   Add `'chatgptxblock'` to the **Advanced Module List**.
    -   Click **Save Changes**.
2.  **Add the XBlock to a Unit**:
    
    -   Go to the desired unit in the course.
    -   Click **Advanced** in the "Add New Component" area.
    -   Select **ChatGPT Assistant** from the list.
3.  **Configure Settings**:
    
    -   Set the display name, model name, API key, context text, and description as needed.
4.  **Publish the Unit**:
    
    -   Click **Publish** to make the ChatGPT Assistant available to students.

**Customization**

### Editable Fields

You can customize the following fields directly from the Studio interface:

-   **`display_name`**: Display name for the ChatGPT Assistant module.
-   **`model_name`**: Select the desired ChatGPT model (e.g., GPT-3.5 Turbo, GPT-4).
-   **`api_key`**: Your OpenAI API key, which can be generated at [OpenAI API Keys](https://platform.openai.com/account/api-keys).
-   **`description`**: A short description of the assistant for students.
-   **`context_text`**: Context that guides the assistant's responses to align with your course content.


## **Reflection and Moderation**

### Reflection Feature

-   After receiving an answer, students are encouraged to reflect on how it aligns with their understanding of the topic.
-   Reflections are stored within the XBlock for potential review and analysis.

### Content Moderation

-   All student inputs are sent through OpenAI’s Moderation API to flag inappropriate or disallowed content.
-   If flagged, the assistant will notify the student and ask them to rephrase their query.



## **Developer Notes**

### Key Modifications in This Release

1.  **Threaded Conversations**: Multi-turn chats are now supported by maintaining a conversation history.
2.  **Reflection Submission**: Students can submit reflections for self-assessment or instructor review.
3.  **Content Moderation**: Questions are screened for inappropriate content using OpenAI’s Moderation API.
4.  **Token Limit Control**: ChatGPT responses are capped at 150 tokens by default, reducing costs and ensuring concise answers.
5.  **Error Handling**: Improved error messages and fallback mechanisms for API-related issues.
6.  **Customizable Frontend**: Updated HTML, CSS, and JavaScript for better user experience and responsiveness.



## **Notes**

-   The API key used in the default settings is a placeholder and will not work. Replace it with your own OpenAI API key.
-   Be mindful of potential costs associated with OpenAI API usage. Configure settings like `max_tokens` and rate limits to optimize usage.
-   Reflections are stored per student and can be reviewed later for insights.


## **License**

This project is licensed under the terms of the AGPLv3 license. Please see the `LICENSE` file for more details.



## **About the Developer**

**ABC Online Courses** is an official Open edX® Partner. Our latest development, the ChatGPT XBlock, aims to address the challenges of providing adequate teaching assistance in massive open online courses. By leveraging OpenAI's ChatGPT, this plugin acts as a real-time assistant for both learners and instructors.

We specialize in Open edX development and provide comprehensive services, including installation, configuration, and support for our plugins. Learn more at [www.abconlinecourses.com](https://www.abconlinecourses.com/).