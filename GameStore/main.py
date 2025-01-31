from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controller.UserController import router as user_router
from controller.GameController import router as game_router
from database import Base, engine

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware to allow requests from all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


# Create tables at startup
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


# Include the routers
app.include_router(user_router)
app.include_router(game_router)


# Sample endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the GameStore API"}


# Run the app using Uvicorn
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
