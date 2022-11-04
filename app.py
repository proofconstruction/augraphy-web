from fastapi import FastAPI, Form, File, UploadFile
from augraphy import AugraphyPipeline
import cv2

app = FastAPI()

@app.post("/crappify")
def crappify(
    inkPhase: list[str] = [],
    paperPhase: list[str] = [],
    postPhase: list[str] = [],
    imageFile: bytes = File(),
):
    inks = []
    papers = []
    posts = []
    for s in inkPhase:
        inks += globals()[s]
    for s in paperPhase:
        papers += globals()[s]
    for s in postPhase:
        posts += globals()[s]

    # by now we have a list of augmentations per phase,
    # so we produce the final pipeline
    pipeline = AugraphyPipeline(inks, papers, posts)

    # now we run the pipeline over the image
    img = cv2.imread(imageFile.file)
    output = pipeline.augment(img)
    return output
