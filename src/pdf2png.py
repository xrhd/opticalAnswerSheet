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

from progressbar import progressbar
from joblib import Parallel, delayed
import multiprocessing

class pdf2png(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        prospective_dir=values
        self.p2p(prospective_dir)
        print('outpath: \"local dir\"/png')

    def p2p(self, prospective_dir):
        # principal 
        if(not('png' in os.listdir())):
            os.mkdir('png')
        if not(multprocess):
            for pdf_file in progressbar(os.listdir(prospective_dir)):
                try:
                    image = convert_from_path(prospective_dir+"/"+pdf_file)
                    image[0].save("png/"+pdf_file[:len(pdf_file)-4]+".png")
                except:
                    continue
        elif(multprocess):
            def process():
                try:
                    image = convert_from_path(prospective_dir+"/"+pdf_file)
                    image[0].save("png/"+pdf_file[:len(pdf_file)-4]+".png")
                except:
                    pass
            num_cores = multiprocessing.cpu_count()
            print('[INFO]Multprocess: {}'.format(num_cores))
            Parallel(n_jobs=num_cores)(delayed(process)(pdf_file) for pdf_file in progressbar(os.listdir(prospective_dir)))

def main():
    ldir = tempfile.mkdtemp()
    atexit.register(lambda dir=ldir: shutil.rmtree(ldir))

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '-p --pdf_path', action=pdf2png, default=ldir)
    path = parser.parse_args()

if __name__ == "__main__":
    main()
