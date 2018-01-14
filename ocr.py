from PIL import Image 
from PIL import ImageEnhance
from PIL import ImageGrab
import pytesseract


tessdata_dir_config = '--tessdata-dir "C:/Program Files (x86)/Tesseract-OCR/tessdata"'
# Example config: '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
# It's important to include double quotes around the dir path.
image = Image.open('3.jpg')

#色度增强  
enh_col = ImageEnhance.Color(image)   
image_colored = enh_col.enhance(12)  

#对比度增强  
# enhancer = ImageEnhance.Contrast(image_colored)
# image_enhancer = enhancer.enhance(3)

# #锐度增强 
# enh_sha = ImageEnhance.Sharpness(image_enhancer)  
# image_sharped = enh_sha.enhance(1)  

text=pytesseract.image_to_string(image_colored,lang='chi_sim', config=tessdata_dir_config)
print(text)

im = ImageGrab.grab((654, 0, 1264, 1080))
im.save('a.png', 'png')