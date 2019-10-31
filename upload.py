from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateEntry, Region
import os

ENDPOINT = ""

# Replace with a valid key
training_key = "<>"

trainer = CustomVisionTrainingClient(training_key, endpoint=ENDPOINT)

project = trainer.get_projects()[0]

balloon_tag = trainer.get_tags(project.id)[0]

balloon_image_regions = {}

for filename in os.listdir("./out/"):
    if filename.endswith(".txt"):
        f=open("./out/" + filename,"r")
        regions=[]
        
        for line in f.readlines():
            line=line.replace("\n","")
            regions.append(line.split(" "))
        jpgName=filename.replace(".txt",".jpg")
        balloon_image_regions[jpgName]=regions

print(balloon_image_regions)

# Update this with the path to where you downloaded the images.
base_image_url = "./images/"

# Go through the data table above and create the images
print ("Adding images...")
tagged_images_with_regions = []

for filename in balloon_image_regions.keys():
    regions = []
    for region in balloon_image_regions[filename]:
        x,y,w,h = region
        regions.append(Region(tag_id=balloon_tag.id, left=x,top=y,width=w,height=h))
    
    with open(base_image_url + filename, mode="rb") as image_contents:
        tagged_images_with_regions.append(ImageFileCreateEntry(name=filename, contents=image_contents.read(), regions=regions))

upload_result = trainer.create_images_from_files(project.id, images=tagged_images_with_regions)
if not upload_result.is_batch_successful:
    print("Image batch upload failed.")
    for image in upload_result.images:
        print("Image status: ", image.status)
    exit(-1)