from PIL import Image as Img

'''
Ideolog should be its own class for all the stuff for your npc to speak out. :3
'''
main_image = 'main_npc_picture.jpg'
main_image_open = Img.open(main_image)

class npc:
    def __init__(self, name, ideolog):
        self.name = name
        self.ideolog = ideolog

class base_ideolog:
    def __init__(self,name,values):
        self.name = name
        self.values = values # Should be a list

def show():
    main_image_open.show()

def introduce(npc, printing = True):
        main_data = ("Hello, my name is", npc.name, "and I am a", npc.ideolog.name)
        if printing is True:
            print(main_data)
