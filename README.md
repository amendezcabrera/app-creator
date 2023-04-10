This is a small Python script that uses the OpenAI GPT language model to automatically generate source code for various tasks, including generating screens for web or mobile applications. The script takes natural language descriptions of the task as input and produces code snippets as output.

## Installation

To use this script, you need to have an OpenAI, get an API [here](https://platform.openai.com/account/api-keys). Once you have your API key, create a `.env` file in the same level following the next format:

> OPENAI_API_KEY=sk-wUC9W2Ye04a0dYZzZwl7T...

You need install the required Python packages using pip:
```bash
pip install openai
pip install python-dotenv
```

## Usage

Before running it you can modify the `screens` list in the script to add or remove screens and their descriptions.

Then simply run the `app-creator` with the following command-line arguments:

```bash
python app-creator.py
```

## License

This script is released under the MIT License. See LICENSE.md for details.