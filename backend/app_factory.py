from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes_conversions import router as conv_router

def create_app() -> FastAPI:
    app = FastAPI(title="File Converter API")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(conv_router)
    return app