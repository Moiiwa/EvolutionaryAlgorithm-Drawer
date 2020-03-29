import numpy
import sys
from PIL import Image, ImageChops, ImageDraw
from numpy import random
def comparePics(pic1,pic2):
    return numpy.sum(numpy.absolute(numpy.array(ImageChops.difference(pic1, pic2))))

def mutation(pic,new):
    initial_fit=comparePics(target,pic)
    buf=Image.new("RGB",(512,512),"white")
    buf.paste(new)
    draw = ImageDraw.Draw(buf)
    draw.polygon(((random.randint(0,512),random.randint(0,512)),(random.randint(0,512),random.randint(0,512)),(random.randint(0,512),random.randint(0,512)),
                  (random.randint(0,512),random.randint(0,512)),(random.randint(0,512),random.randint(0,512))),
                 fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    if(comparePics(target,buf)<initial_fit):
       return buf
    else:
        return None

def sortbyfit(pair):
    return pair[1]

def generate_pop(population):
    pairs=[]
    sum=0
    num=0
    new_pop=[]
    while(len(new_pop)<6):
        new_pop = []
        #for each chromosome
        for chromosome in population:
        #make 100 mutations
            for i in range(10):
                buf = Image.new("RGB", (512, 512), "white")
                buf.paste(chromosome)
                buf=mutation(chromosome,buf)
                if buf!=None:
                    fit=comparePics(target,buf)
                    pair=(buf,fit)
                    sum+=fit
                    num+=1
                    pairs.append(pair)
        if(len(pairs)>6):
            average=sum/num
            print(average)
            #take the best
            pairs.sort(key=sortbyfit)
            added=0
            for i in range(10):
                new_pop.append(pairs[0][0])
            new_pop[0].save("draw_Hands.jpg")
            print(comparePics(target,new_pop[0]))
    generate_pop(new_pop)
sys.setrecursionlimit(2147483647)
target=Image.open("hands512.jpg")
draw=Image.new("RGB",(512,512),"white")
population=[]
while(len(population)<1):
    for i in range(6):
        buf=Image.new("RGB",(512,512),"white")
        buf=mutation(draw,buf)
        if buf!=None:
            population.append(buf)
generate_pop(population)

