#rhd

'''
pdf2png.py: 
	transforma .pdf em .png

dependencias:
	pip install pdf2image

digite:
	python pdf2png.py -p "diretorio_do_pdf"

output:
	cria um diretorio "png", contendo "*.png"
'''

import argparse
import os
import tempfile
import shutil
import atexit
from pdf2image import convert_from_path

class pdf2png(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        prospective_dir=values
        self.p2p(prospective_dir)
        print('outpath: \"local dir\"/png')

    def p2p(self, prospective_dir):
        # principal 
        if(not('png' in os.listdir())):
            os.mkdir('png')
        for pdf_file in os.listdir(prospective_dir):
            print(pdf_file)
            image = convert_from_path(prospective_dir+"/"+pdf_file)
            image[0].save("png/"+pdf_file[:len(pdf_file)-4]+".png")
    

def main():
    ldir = tempfile.mkdtemp()
    atexit.register(lambda dir=ldir: shutil.rmtree(ldir))

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '-p --pdf_path', action=pdf2png, default=ldir)
    path = parser.parse_args()

if __name__ == "__main__":
    main()
