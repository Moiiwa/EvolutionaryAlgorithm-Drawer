import numpy
import sys
from PIL import Image, ImageChops, ImageDraw
from numpy import random
class EvolutionaryALgorithm:
    def comparePics(pic1,pic2):
        return numpy.sum(numpy.absolute(numpy.array(ImageChops.difference(pic1, pic2))))

    def mutation(pic,new):
        initial_fit=EvolutionaryALgorithm.comparePics(target,pic)
        buf=Image.new("RGB",(512,512),"white")
        buf.paste(new)
        draw = ImageDraw.Draw(buf)
        if (EvolutionaryALgorithm.gen_num<20):
            x1=random.randint(0,512)
            y1=random.randint(0,512)
            x2=random.randint(0,512)
            y2=random.randint(0,512)
            x3=random.randint(0,512)
            y3=random.randint(0,512)
            x4=random.randint(0,512)
            y4=random.randint(0,512)
            x5=random.randint(0,512)
            y5=random.randint(0,512)
        elif(EvolutionaryALgorithm.gen_num<100):
            xl = random.randint(0, 512)
            x_range = random.randint(1, 200)
            yl = random.randint(0, 512)
            y_range = random.randint(1, 200)
            if (512 - xl > xl):
                x1 = random.randint(xl, xl + x_range)
                x2 = random.randint(xl, xl + x_range)
                x3 = random.randint(xl, xl + x_range)
                x4 = random.randint(xl, xl + x_range)
                x5 = random.randint(xl, xl + x_range)
            else:
                x1 = random.randint(xl - x_range, xl)
                x2 = random.randint(xl - x_range, xl)
                x3 = random.randint(xl - x_range, xl)
                x4 = random.randint(xl - x_range, xl)
                x5 = random.randint(xl - x_range, xl)
            if (512 - yl > yl):
                y1 = random.randint(yl, yl + y_range)
                y2 = random.randint(yl, yl + y_range)
                y3 = random.randint(yl, yl + y_range)
                y4 = random.randint(yl, yl + y_range)
                y5 = random.randint(yl, yl + y_range)
            else:
                y1 = random.randint(yl - y_range, yl)
                y2 = random.randint(yl - y_range, yl)
                y3 = random.randint(yl - y_range, yl)
                y4 = random.randint(yl - y_range, yl)
                y5 = random.randint(yl - y_range, yl)

        elif(EvolutionaryALgorithm.gen_num<180):
            xl=random.randint(0,512)
            x_range=random.randint(1,100)
            yl=random.randint(0,512)
            y_range=random.randint(1,100)
            if(512 - xl > xl):
                x1 = random.randint(xl,xl+x_range)
                x2 = random.randint(xl, xl + x_range)
                x3 = random.randint(xl, xl + x_range)
                x4 = random.randint(xl, xl + x_range)
                x5 = random.randint(xl, xl + x_range)
            else:
                x1 = random.randint( xl - x_range, xl)
                x2 = random.randint(xl - x_range, xl)
                x3 = random.randint(xl - x_range, xl)
                x4 = random.randint(xl - x_range, xl)
                x5 = random.randint(xl - x_range, xl)
            if(512 - yl > yl):
                y1 = random.randint(yl,yl+y_range)
                y2 = random.randint(yl, yl + y_range)
                y3 = random.randint(yl, yl + y_range)
                y4 = random.randint(yl, yl + y_range)
                y5 = random.randint(yl, yl + y_range)
            else:
                y1 = random.randint( yl - y_range, yl)
                y2 = random.randint(yl - y_range, yl)
                y3 = random.randint(yl - y_range, yl)
                y4 = random.randint(yl - y_range, yl)
                y5 = random.randint(yl - y_range, yl)
        else:
            xl = random.randint(0, 512)
            x_range = random.randint(1, 50)
            yl = random.randint(0, 512)
            y_range = random.randint(1, 50)
            if (512 - xl > xl):
                x1 = random.randint(xl, xl + x_range)
                x2 = random.randint(xl, xl + x_range)
                x3 = random.randint(xl, xl + x_range)
                x4 = random.randint(xl, xl + x_range)
                x5 = random.randint(xl, xl + x_range)
            else:
                x1 = random.randint(xl - x_range, xl)
                x2 = random.randint(xl - x_range, xl)
                x3 = random.randint(xl - x_range, xl)
                x4 = random.randint(xl - x_range, xl)
                x5 = random.randint(xl - x_range, xl)
            if (512 - yl < yl):
                y1 = random.randint(yl, yl + y_range)
                y2 = random.randint(yl, yl + y_range)
                y3 = random.randint(yl, yl + y_range)
                y4 = random.randint(yl, yl + y_range)
                y5 = random.randint(yl, yl + y_range)
            else:
                y1 = random.randint(yl - y_range, yl)
                y2 = random.randint(yl - y_range, yl)
                y3 = random.randint(yl - y_range, yl)
                y4 = random.randint(yl - y_range, yl)
                y5 = random.randint(yl - y_range, yl)
        draw.polygon(((x1,y1),(x2,y2),(x3,y3),
                      (x4,y4),(x5,y5)),
                     fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        if(EvolutionaryALgorithm.comparePics(target,buf)<initial_fit):
            return buf
        else:
           return None

    def sortbyfit(pair):
        return pair[1]

    gen_num=0

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
                    buf=EvolutionaryALgorithm.mutation(chromosome,buf)
                    if buf!=None:
                        fit=EvolutionaryALgorithm.comparePics(target,buf)
                        pair=(buf,fit)
                        sum+=fit
                        num+=1
                        pairs.append(pair)
            if(len(pairs)>6):
                average=sum/num
                print(average)
                #take the best
                pairs.sort(key=EvolutionaryALgorithm.sortbyfit)
                added=0
                for i in range(10):
                    new_pop.append(pairs[0][0])
                new_pop[0].save("draw_mama.jpg")
                print(EvolutionaryALgorithm.comparePics(target,new_pop[0]))
        EvolutionaryALgorithm.gen_num+=1
        EvolutionaryALgorithm.generate_pop(new_pop)


sys.setrecursionlimit(2147483647)
target=Image.open("mama512.jpg")
draw=Image.new("RGB",(512,512),"white")
population=[]

while(len(population)<1):
    for i in range(6):
        buf=Image.new("RGB",(512,512),"white")
        buf=EvolutionaryALgorithm.mutation(draw,buf)
        if buf!=None:
            population.append(buf)
EvolutionaryALgorithm.generate_pop(population)

