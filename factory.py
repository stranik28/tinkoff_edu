from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routers.tournament import router as tournament_router
# from app.api.routers.


def create_app():
    app = FastAPI(
        title="FastAPI",
        description="FastAPI",
        version="0.1.0",
        openapi_url="/api/v1/openapi.json",
        docs_url="/docs",
        redoc_url="/redoc",
    )

    app.include_router(tournament_router)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app
