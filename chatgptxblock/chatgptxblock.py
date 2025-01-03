import os
import pkg_resources
import openai
from xblock.core import XBlock
from xblock.fields import String, Scope
from xblock.fragment import Fragment
from xblockutils.studio_editable import StudioEditableXBlockMixin

class ChatgptXBlock(StudioEditableXBlockMixin, XBlock):
    display_name = String(
        display_name="Display Name",
        help="Display name for this module",
        default="ChatGPT Assistant",
        scope=Scope.settings,
    )
    question = String(
        default='',
        scope=Scope.user_state,
        help='The question asked by the user'
    )
    answer = String(
        default='',
        scope=Scope.user_state,
        help='The answer provided by ChatGPT'
    )

    api_key = String(
        default="your-openai-api-key-here",
        scope=Scope.settings,
        help="Your OpenAI API key",
    )

    # Provide the dropdown choices via the "values" parameter:
    model_name = String(
        display_name="Model name",
        default="gpt-3.5-turbo-0613",
        scope=Scope.settings,
        help="Select which ChatGPT model to use.",
        values=[
            {"display_name": "GPT-3.5 Turbo 0613", "value": "gpt-3.5-turbo-0613"},
            {"display_name": "GPT-3.5 Turbo",      "value": "gpt-3.5-turbo"},
            {"display_name": "GPT-3.5 Turbo 16k",  "value": "gpt-3.5-turbo-16k"},
            {"display_name": "GPT-4",              "value": "gpt-4"},
            {"display_name": "GPT-4o",              "value": "gpt-4o"},
            {"display_name": "o1",                  "value": "o1"},
            {"display_name": "o1-mini",             "value": "o1-mini"},
        ],
    )

    context_text = String(
        default="Your context here",
        scope=Scope.settings,
        help="Context text for the conversation"
    )

    description = String(
        default='Description here',
        scope=Scope.settings,
        help='Description'
    )

    # Make sure model_name is included in your editable fields list
    editable_fields = ['display_name', 'model_name', 'api_key', 'description', 'context_text']

    def resource_string(self, path):
        """Helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def student_view(self, context=None):
        """The primary view of the ChatgptXBlock, shown to students."""
        html = self.resource_string("static/html/chatgptxblock.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/chatgptxblock.css"))
        frag.add_javascript(self.resource_string("static/js/src/chatgptxblock.js"))
        frag.initialize_js('ChatgptXBlock')
        return frag

    @XBlock.json_handler
    def get_answer(self, data, suffix=''):
        """Handle the submission of the user's question and return an answer."""
        question = data['question']
        self.question = question

        # Set the API key for openai
        openai.api_key = self.api_key

        # Call the Chat Completion endpoint
        response = openai.ChatCompletion.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": self.context_text},
                {"role": "user",   "content": question}
            ]
        )

        # Extract and store the response
        if response.choices:
            first_choice = response.choices[0]
            if first_choice.message and first_choice.message.content:
                answer = first_choice.message.content.strip()
            else:
                answer = "Sorry, I couldn't generate a response. Please try again."
        else:
            answer = "No response received from the model."

        self.answer = answer
        return {'answer': answer}

    @staticmethod
    def workbench_scenarios():
        """Scenarios for display in the workbench."""
        return [
            ("ChatgptXBlock",
             """<chatgptxblock/>
             """),
            ("Multiple ChatgptXBlock",
             """<vertical_demo>
                <chatgptxblock/>
                <chatgptxblock/>
                <chatgptxblock/>
                </vertical_demo>
             """),
        ]
