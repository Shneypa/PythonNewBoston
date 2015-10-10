from PIL import Image
from PIL import ImageFilter

brian = Image.open("145.jpg")

brian_blurred = brian.filter(ImageFilter.BLUR)
brian_detailed = brian.filter(ImageFilter.DETAIL)
brian_edges = brian.filter(ImageFilter.FIND_EDGES)

brian_blurred.show()
brian.show()
brian_detailed.show()
brian_edges.show()

