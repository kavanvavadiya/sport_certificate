from PIL import Image, ImageFont,ImageDraw
import pandas as pd

def main():
    print("Initializing Script!")
    names = pd.read_csv('IITBSports.csv')
    for i,row in names.iterrows():
        name = str(row['Name'])
        Callage_name = str(row['College Name'])
        name = name.title()
        empty_img = Image.open("certificate.jpeg")
        font_size = 26
        font = ImageFont.truetype("arial",font_size)
        image_editable = ImageDraw.Draw(empty_img)
        image_editable.text((135,435),name,(50,57,253),font=font)
        image_editable.text((550,435),Callage_name,(50,57,250),font=font)
        empty_img.save("{}.jpg".format(name.replace(" ", "_")))
        if i % 50 == 0: 
            print('Processed {} Rows'.format(i))
    print("Process Complete!")
    # code
 
if __name__ == "__main__":
    main()