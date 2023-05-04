# ChatGPT XBlock for Open edX
The ChatGPT XBlock is a plugin for Open edX that allows you to integrate ChatGPT, an AI language model developed by OpenAI, into your Open edX courses. This XBlock enables students to ask questions and receive answers from the ChatGPT model in real-time.

**Features**
* Add ChatGPT Assistant to your Open edX course
* Customizable display name, model name, API key, description, and context text
* Easy integration with OpenAI API
* Seamless rendering of chat interface in Open edX platform

**Installation**
Install the XBlock in your Open edX environment using pip:
```
pip install https://github.com/isankadn/chatgpt-xblock.git
```
Add 'chatgptxblock' to the INSTALLED_APPS list in your Open edX environment settings.

Restart the Open edX platform.

**Usage**
1. Navigate to the Open edX Studio for the course you want to add the ChatGPT Assistant to.
2. Click on the "Advanced" tab and add 'chatgptxblock' to the "Advanced Module List".
3. Click on the "Save Changes" button.
4. Navigate to the unit where you want to add the ChatGPT Assistant.
5. Click on the "Advanced" button in the "Add New Component" area.
6. Select "ChatGPT Assistant" from the list.
7. Configure the XBlock settings as desired, including display name, model name, API key, description, and context text.
8. Publish the unit to make the ChatGPT Assistant available to students.

**Customization**
You can customize the ChatGPT XBlock by editing the following fields:

1. display_name: Display name for this module
2. model_name: ChatGPT model to use (text-davinci-003, text-davinci-002, text-curie-001, text-babbage-001, text-ada-001)
3. api_key: Your OpenAI API key, which can be found at https://platform.openai.com/account/api-keys
4. description: Description of the ChatGPT Assistant
5. context_text: Context text that will be sent to the ChatGPT model along with the user's question

**Notes**
The API key used in the default settings is a placeholder and will not work. You need to replace it with your own OpenAI API key.
The ChatGPT XBlock is built on Open edX's XBlock framework and is compatible with the Open edX platform.

**License**
This project is licensed under the terms of the AGPLv3 license. Please see the LICENSE file for more details.
