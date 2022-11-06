from fastapi import FastAPI, Form, File, UploadFile
from augraphy import *
import cv2

app = FastAPI()

@app.post("/crappify")
def crappify(
    inkPhase: list[str] = [],
    paperPhase: list[str] = [],
    postPhase: list[str] = [],
    imageFile: bytes = File(),
):

    turn the lists of augmentation names into augmentation functions
    inks = []
    papers = []
    posts = []
    for s in inkPhase:
        inks += globals()[s]
    for s in paperPhase:
        papers += globals()[s]
    for s in postPhase:
        posts += globals()[s]

    # save the file to tmp
    with open("imageFile.png", "wb") as f:
        f.write(imageFile)

    # by now we have a list of augmentations per phase,
    # so we produce the final pipeline
    pipeline = AugraphyPipeline(inks, papers, posts)

    # now we run the pipeline over the image
    img = cv2.imread("imageFile.png")
    crappified = pipeline.augment(img) # default_augraphy_pipeline().augment(img)
    #cv2.imwrite("imagefile-crappified.png", crappified["output"])
    return crappified["output"]
