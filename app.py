from fastapi import FastAPI
import os

app = FastAPI(
	title = "Python Jenkins App",
	version = os.getenv("BUILD_ID", "build id not found")
)


@app.get("/")
async def root():
	return {
		"message" : "Server is running",
		"version" : app.version
	}
