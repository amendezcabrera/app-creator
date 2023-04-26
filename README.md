This is a small Python script that uses the OpenAI GPT language model to automatically generate source code for various tasks, including generating screens for web or mobile applications. The script takes natural language descriptions of the task as input and produces code snippets as output.

## Configuration

To use this script, you will need to obtain an OpenAI API key. You can obtain a key by visiting this [link](https://platform.openai.com/account/api-keys). Once you have obtained it create a `.env` file in the same directory as the script, using the following format:

> OPENAI_API_KEY=sk-wUC9W2Ye04a0dYZzZwl7T...

## Installation

You need install the required Python packages using pip:
```bash
pip install openai
pip install python-dotenv
```

## Usage

Before running it you can modify the `screens` list in the script to add or remove screens and their descriptions. This script generates `Flutter` code but you can adapt it to your requirements.

Then simply run the `app-creator` script with the following command-line arguments:

```bash
python app-creator.py
```

After requesting tests and source code from ChatGPT you will receive a response containing the generated tests and code, which can be easily integrated and compiled into your project.

## License

This script is released under the MIT License. See LICENSE.md for details.