# main.py
from fastapi import FastAPI

from deployment import deployment_router
from user import user_router
from template import template_router

from core.util.logging import setup_logging

app = FastAPI()

# Set up logging
setup_logging()

# Include routers from domain modules
app.include_router(user_router)
app.include_router(deployment_router)
app.include_router(template_router)

# Additional setup (e.g., middleware for security) can be added here

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
