from fastapi import FastAPI, File
from fastapi.responses import FileResponse
from starlette.requests import Request
from starlette.routing import Route
from createImageFromText2 import createImageFromText
from googleTranslate import googleTranslate

app = FastAPI()

#@app.post("/prompt")
#async def getPromptTemp(promptTextTemp: str):
#    PromptTextJp = googleTranslate(promptTextTemp)
#    img = createImageFromText(PromptTextJp)
#    return Response(img, mimetype="image/png")

@app.post("/prompt")
async def getPromptTemp(request: Request, promptTextTemp: str):
    PromptTextJp = await googleTranslate(promptTextTemp)
    img, imageName = await createImageFromText(PromptTextJp)
    return FileResponse(img, media_type="image/png"), imageName