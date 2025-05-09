# emailClassifier


# Azure Functions Python Dependencies Setup

To explicitly install your Python dependencies into the required folder structure (`.python_packages/lib/site-packages`) for deployment of your FastAPI app via Azure Functions.
Do this in your local terminal (in backend folder, and check if .python_packages/lib/site-packages are created)

```bash
pip install -r requirements.txt --target=".python_packages/lib/site-packages"
```

This will explicitly install your dependencies in the correct structure needed by Azure Functions for deployment.
