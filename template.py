import os

# Define the structure as nested dictionaries
project_structure = {
    "debate_partner_ai": {
        "src": {
            "data": {},
            "models": {},
            "modules": {
                "data_loader.py": "",
                "retriever.py": "",
                "generator.py": "",
                "argument_mining.py": "",
                "feedback_loop.py": "",
                "evaluation.py": "",
            },
            "utils": {
                "preprocessing.py": "",
                "logging_utils.py": "",
                "prompt_templates.py": "",
            },
            "app.py": "",
            "config.py": "",
        },
        "notebooks": {
            "eda.ipynb": "",
            "model_testing.ipynb": "",
        },
        "saved_models": {},
        "requirements.txt": "transformers\nsentence-transformers\nfaiss-cpu\ndatasets\ntorch\nhuggingface-hub\nflask\nstreamlit\n",
        "README.md": "# AI Debate Partner\n\nThis project aims to build a conversational AI for debating various topics using NLP techniques.",
    }
}


def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, 'w') as file:
                file.write(content)


if __name__ == "__main__":
    base_dir = os.getcwd()  # Current directory
    create_structure(base_dir, project_structure)
    print("Project structure created successfully!")
