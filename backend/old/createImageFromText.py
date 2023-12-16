import getpass, os

os.environ['STABILITY_HOST'] = 'grpc.stability.ai:443'
os.environ['STABILITY_KEY'] = 'sk-g21oswWJJHsWu4NrtGWaQzaGfkmZ7yVuYTb1Omz5x1kpcWZG'

import io
import os
import warnings

from IPython.display import display
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation


stability_api = client.StabilityInference(
    key=os.environ['STABILITY_KEY'], 
    verbose=True, 
    engine="stable-diffusion-v1-5", 
    # Available engines: stable-diffusion-v1 stable-diffusion-v1-5 stable-diffusion-512-v2-0 stable-diffusion-768-v2-0 stable-inpainting-v1-0 stable-inpainting-512-v2-0
    ) 

answers = stability_api.generate(
    prompt="(((super realistic))), (((best quality))),((masterpiece)), ((ultra-detailed)), a girl, smile, (((super realistic black hair))), shirt, black eyes, an anime style",
    seed=992446758, 
    steps=30, 
    cfg_scale=8.0,
    width=512, 
    height=512, 
    samples=1, 
    sampler=generation.SAMPLER_K_DPMPP_2M 
    )

for resp in answers:
    for artifact in resp.artifacts:
        if artifact.finish_reason == generation.FILTER:
            warnings.warn(
                "Your request activated the API's safety filters and could not be processed."
                "Please modify the prompt and try again.")
        if artifact.type == generation.ARTIFACT_IMAGE:
            img = Image.open(io.BytesIO(artifact.binary))
            display(img)