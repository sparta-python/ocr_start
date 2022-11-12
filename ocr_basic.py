from PIL import Image
import pyocr

tools = pyocr.get_available_tools()
tool = tools[0]
# print(tool)
# print(tool.get_name())


# # english
# img = Image.open("sparta_camp_en.png")
# # img.show()

# txt = tool.image_to_string(img, lang="eng", builder=pyocr.builders.TextBuilder())

# print(txt)


# # japanese
# img = Image.open("sparta_camp_ja.png")

# txt = tool.image_to_string(img, lang="jpn", builder=pyocr.builders.TextBuilder())

# print(txt)


# english + japanese
img = Image.open("sparta_camp_en.png")

txt = tool.image_to_string(img, lang="eng+jpn", builder=pyocr.builders.TextBuilder())

print(txt)
