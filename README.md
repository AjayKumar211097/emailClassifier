# emailClassifier
🔧 Prepare Dependencies for Azure Functions
Azure Functions requires Python dependencies to be placed specifically within the .python_packages/lib/site-packages directory. Use this command from your project root to install requirements:

pip install -r requirements.txt --target=".python_packages/lib/site-packages"
This will explicitly install your dependencies in the correct structure needed by Azure Functions for deployment.
