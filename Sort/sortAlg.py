import pygame,random,time,os

pygame.init()

h_display = 800
v_display = 500
box = [h_display-20, v_display-60]
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((h_display, v_display+40))
white = (255, 255, 255)
black = (0,0,0)
gray = (128, 128, 128)
green = (0, 255, 128)
red = (255, 64, 64)
lastPos = 0
size = 10
pygame.display.set_caption("Sorting Algorithm")

BG = (217, 210, 238) #LIGHT_PINK
#BG = (149, 233, 175) #LIGHT_GREEN
#BG = (233, 185, 185) #LIGHT_RED
IN_BOX = (30,30,30)
#BTN_COLOR = (235,232,247)
#BTN_PRESSED_COLOR = (180,167,224)
BTN_COLOR = (BG[0]+18,BG[1]+22,BG[2]+9)
BTN_PRESSED_COLOR = (BTN_COLOR[0]-55,BTN_COLOR[1]-65,BTN_COLOR[2]-23)

def getTextRectSize(txt, pos, size, fnt, bold, txtColor, bgColor, center=True):
    font = pygame.font.Font(os.path.join(os.getcwd(), "times.ttf"), size)
    text = font.render(txt, True, txtColor)
    rect = text.get_rect()
    rect.center = pos
    #print(rect.left, rect.top, rect.width, rect.height)
    if not center:
        rect.left = pos[0]
        rect.top = pos[1]
    #print(rect.left, rect.top, rect.width, rect.height)    
    return [rect.left-(size/2), rect.top-(size/2), rect.width+size, rect.height+size]   

def renderTextWithRectangle(txt, pos, size, fnt, bold, txtColor, bgColor, center=True):
    font = pygame.font.SysFont(fnt, size, bold)
    text = font.render(txt, True, txtColor)
    rect = text.get_rect()
    rect.center = pos
    if not center:
        rect.left = pos[0]
        rect.top = pos[1]
    pygame.draw.rect(gameDisplay, bgColor, [int(rect.left-(size/2)), int(rect.top-(size/2)), rect.width+size, rect.height+size])
    gameDisplay.blit(text, rect)

def renderText(txt, pos, size, fnt, bold, center=True):
    font = pygame.font.SysFont(fnt, size, bold)
    text = font.render(txt, True, black)
    rect = text.get_rect()
    rect.center = pos
    if not center:
        rect.left = pos[0]
    gameDisplay.blit(text, rect)

class Rect:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
    def get(self):
        return [self.x,self.y,self.w,self.h]

class Button:
    def __init__(self, name, pos, txtSize):
        self.name = name
        self.pos = pos
        self.txtSize = txtSize
        self.collision = False
        self.rect = getTextRectSize(self.name, self.pos, self.txtSize, "Times", False, black, (206,198,235), False)
        
    def render(self):
        if self.collision: renderTextWithRectangle(self.name, self.pos, self.txtSize, "Times", False, black, BTN_PRESSED_COLOR, False)
        else: renderTextWithRectangle(self.name, self.pos, self.txtSize, "Times", False, black, BTN_COLOR, False)   
        
        #if self.collision: pygame.draw.rect(gameDisplay, (206,198,235), self.rect.get())
        #else: pygame.draw.rect(gameDisplay, (235,232,247), self.rect.get())
        #renderText(self.name, (self.rect.x+(self.rect.w/2),self.rect.y+(self.rect.h/2)), 15, "Times", False, True)
    
    def update(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if mouse[0] > self.rect[0] and mouse[0] < self.rect[0]+self.rect[2] and \
           mouse[1] > self.rect[1] and mouse[1] < self.rect[1]+self.rect[3]:
            self.collision = True
            if click[0] == 1: 
                time.sleep(0.1)
                return 1
            if click[2] == 1:
                time.sleep(0.1)
                return 2
            #print(self.name, "BTN Collision")
        else: self.collision = False
        return 0

class SortingVisual:
    def __init__(self,size):
        self.size = size
        #self.arr = [i for i in range(int((box[0] - int(box[0]/size))/size))]
        self.arr = [i for i in range(int(box[0]/size))]
        self.scale = float(box[1]/len(self.arr))
        pygame.display.set_caption("Sorting Algorithm [Rect:"+str(len(self.arr))+"]")
        random.shuffle(self.arr)
        self.sorted = True
        self.size -= 1
        self.options = []
    
    def refresh(self,size):
        self.size = size
        #self.arr = [i for i in range(int((box[0] - int(box[0]/size))/size))]
        self.arr = [i for i in range(int(box[0]/size))]
        self.scale = float(box[1]/len(self.arr))
        pygame.display.set_caption("Sorting Algorithm [Rect:"+str(len(self.arr))+"]")
        random.shuffle(self.arr)
        self.sorted = True
        self.size -= 1
        self.options = []        
    
    def shuffleArr(self):
        random.shuffle(self.arr)
        self.sorted = True
    
    def render(self):
        left = 11-self.size
        top = 49
        for i in range(len(self.arr)):
            y = int(((top+box[1]) - (self.arr[i]*self.scale))-(self.arr[i]*self.scale))
            if len(self.options) > 0 and i in self.options[0]:
                pygame.draw.rect(gameDisplay, self.options[1][self.options[0].index(i)], [int(left+(self.size*(i+1))), (top+box[1]), self.size, -int(self.arr[i]*self.scale)])
            else:
                pygame.draw.rect(gameDisplay, (255,174,94), [int(left+(self.size*(i+1))), (top+box[1]), self.size, -int(self.arr[i]*self.scale)])
            
            left+=1

class BubbleSort:
    def __init__(self,arr):
        self.arr = arr
        self.lastPos = 0
    
    def sort(self):
        change = False
        for i in range(self.lastPos, len(self.arr)-1):
            if self.arr[i] > self.arr[i+1]:
                change = True
                self.arr[i+1], self.arr[i] = self.arr[i], self.arr[i+1]
                self.lastPos = i
                sv.arr = self.arr
                sv.options = [[i,i+1],[(255,40,40),(13,91,138)]]
                return not change
        if self.lastPos != 0: 
            self.lastPos = 0
            return self.sort()
        return not change

class InsertionSort:
    def __init__(self, arr):
        self.arr = arr
        self.lastPos1 = 0
        self.lastPos2 = 0
        self.mode = 0
    
    def sort(self):
        if self.mode == 0:
            if self.lastPos1 == len(self.arr): return True
            for i in range(self.lastPos1,len(self.arr)):
                if self.arr[i] < self.arr[i-1]:
                    sv.options = [[i],[(255,40,40)]]
                    self.arr[i],self.arr[i-1] = self.arr[i-1],self.arr[i]
                    self.lastPos1 = i+1
                    sv.arr = self.arr
                    sv.options = [[i,i-1],[(255,40,40),(13,91,138)]]
                    if i-1 > 0:
                        self.mode = 1
                        self.lastPos2 = i-1
                    return False
            return True
        elif self.mode == 1:
            for i in range(self.lastPos2-1,-1,-1):
                if self.arr[i] > self.arr[self.lastPos2]:
                    self.arr[i],self.arr[self.lastPos2] = self.arr[self.lastPos2],self.arr[i]
                    sv.options = [[i,self.lastPos2,self.lastPos1],[(255,40,40),(13,91,138),(91,255,91)]]
                    self.lastPos2 = i
                    sv.arr = self.arr
                    if self.lastPos2 == 0: self.mode = 0
                    return False
                else:
                    self.mode = 0
                    return False

class MergeSort:
    def __init__(self,arr):
        self.arr = arr
        self.subArr = [[i] for i in self.arr]
        self.subArr2 = []
        self.lastPos = 0
        self.mode = 0
        self.arr1=[];self.arr2 = []
        self.arr1Pos = 0; self.arr2Pos = 0
        self.midArr = []
    
    def combineArr(self,arr):
        ret = []
        for i in arr:
            for j in i:
                if isinstance(j,list):
                    for k in j: ret.append(k)
                else: ret.append(j)
        #print(ret)
        return ret
    
    def mergeArr(self,arr1,arr2):
        if self.arr1Pos == len(arr1):
            if self.arr2Pos == len(arr2):
                self.mode = 0
                self.subArr2.append(self.midArr)
                self.midArr = []
                self.arr1Pos = 0
                self.arr2Pos = 0
                return False
            for i in range(self.arr2Pos,len(arr2)): 
                self.midArr.append(arr2[i])
                self.arr2Pos += 1
            sv.options = [[sv.arr.index(arr2[i])],[(255,40,40)]]
            sv.arr = self.combineArr([self.subArr2,self.midArr,arr1[self.arr1Pos:],arr2[self.arr2Pos:],self.subArr[self.lastPos:]])
            return False
        elif self.arr2Pos == len(arr2):
            if self.arr1Pos == len(arr1):
                self.mode = 0
                self.subArr2.append(self.midArr)
                self.midArr = []
                self.arr1Pos = 0
                self.arr2Pos = 0 
                return False
            for i in range(self.arr1Pos,len(arr1)): 
                self.midArr.append(arr1[i])
                self.arr1Pos += 1
            sv.options = [[sv.arr.index(arr1[i])],[(255,40,40)]]
            sv.arr = self.combineArr([self.subArr2,self.midArr,arr1[self.arr1Pos:],arr2[self.arr2Pos:],self.subArr[self.lastPos:]])
            return False
        for i in range(self.arr1Pos,len(arr1)):
            for j in range(self.arr2Pos,len(arr2)):
                if arr1[i] < arr2[j]:
                    self.midArr.append(arr1[i])
                    self.arr1Pos += 1
                    sv.options = [[sv.arr.index(arr1[i]),sv.arr.index(arr2[j])],[(255,40,40),(13,91,138)]]
                    sv.arr = self.combineArr([self.subArr2,self.midArr,arr1[self.arr1Pos:],arr2[self.arr2Pos:],self.subArr[self.lastPos:]])
                    return False
                    #sv.options = [[],[]]
                elif arr1[i] > arr2[j]:
                    self.midArr.append(arr2[j])
                    self.arr2Pos += 1
                    sv.options = [[sv.arr.index(arr1[i]),sv.arr.index(arr2[j])],[(255,40,40),(13,91,138)]]
                    sv.arr = self.combineArr([self.subArr2,self.midArr,arr1[self.arr1Pos:],arr2[self.arr2Pos:],self.subArr[self.lastPos:]])
                    return False
                else:
                    self.midArr.append(arr1[i])
                    self.midArr.append(arr2[j])
                    self.arr1Pos += 1
                    self.arr2Pos += 1
                    sv.options = [[sv.arr.index(arr1[i]),sv.arr.index(arr2[j])],[(255,40,40),(13,91,138)]]
                    sv.arr = self.combineArr([self.subArr2,self.midArr,arr1[self.arr1Pos:],arr2[self.arr2Pos:],self.subArr[self.lastPos:]])
                    return False
    
    def sort(self):
        #print(self.subArr)
        if self.mode == 0:
            if self.lastPos+2 >= len(self.subArr):
                self.subArr = self.subArr2 + self.subArr[self.lastPos:]
                if len(self.subArr) == 1:
                    sv.arr = self.subArr[0]
                    return True
                self.subArr2 = []
                self.lastPos = 0
            for i in range(self.lastPos,len(self.subArr),2):
                self.arr1 = self.subArr[i]; self.arr2 = self.subArr[i+1]
                self.mode = 1
                self.lastPos+=2
                return self.mergeArr(self.arr1,self.arr2)
        elif self.mode == 1:
            return self.mergeArr(self.arr1,self.arr2)
        
class QuickSort:
    def __init__(self,arr):
        self.arr = arr
        self.arr2 = arr
        self.sorted = [0] * len(self.arr)
        self.lastPos = 0
        self.pivot = len(self.arr)-1
        self.pos = [0,self.pivot]
        self.mode = 1
        
    def checkIfSorted(self,arr):
        for i in range(1,len(arr)):
            if arr[i-1] > arr[i]:
                return False
        return True    
    
    def qSort(self,arr):
        #print(arr,self.sorted,self.arr,self.pos)
        if len(arr) <= 1:
            self.arr2 = arr
            for j in range(len(self.arr2)): self.arr[j+self.pos[0]] = self.arr2[j]
            sv.arr = self.arr
            self.sorted[self.pos[0]+self.pivot] = 1
            self.mode = 0            
            return False
        i=self.lastPos
        while i < self.pivot:
            sv.options = [[self.pos[0]+self.pivot,self.pos[0]+i],[(255,40,40),(13,91,138)]]
            if arr[i] > arr[self.pivot] or arr[i] == arr[self.pivot]:
                tmp = arr[i]
                del arr[i]
                arr.insert(self.pivot,tmp)
                self.pivot-=1
                self.arr2 = arr
                #self.arr[self.pos[0]:self.pos[1]+1] = arr
                for j in range(len(self.arr2)): self.arr[j+self.pos[0]] = self.arr2[j]
                sv.arr = self.arr
                return False
            self.lastPos+=1
            i+=1
            #return False
        if self.checkIfSorted(arr):
            for i in range(self.pos[0],self.pos[1]+1): self.sorted[i] = 1
            self.mode = 0
        else:
            self.sorted[self.pos[0]+self.pivot] = 1
            self.mode = 0
        return False
               
    def sort(self):
        if self.mode == 0:
            if self.checkIfSorted(self.arr):
                return True
            self.arr2 = []
            self.pos = [-1,-1]
            for i in range(len(self.sorted)):
                if self.sorted[i] == 0:
                    if len(self.arr2) == 0: self.pos[0] = i
                    self.arr2.append(self.arr[i])
                elif len(self.arr2) > 0:
                    break
            self.pos[1] = self.pos[0]+len(self.arr2)-1
            self.mode = 1
            self.pivot = len(self.arr2)-1
            self.lastPos = 0
        elif self.mode == 1:
            self.qSort(self.arr2)

class SelectionSort:
    def __init__(self,arr):
        self.arr = arr
        self.lastPos = 0
        self.index = 0
        self.minIndex = 0
        self.min = self.arr[0]
    
    def sort(self):
        if self.lastPos >= len(self.arr):
            del self.arr[self.minIndex]
            self.arr.insert(self.index,self.min)
            sv.arr = self.arr
            self.index += 1   
            self.lastPos = self.index
            self.minIndex = self.index
            self.min = self.arr[self.index]            
        if self.index >= len(self.arr)-1:
            return True
        for i in range(self.lastPos,len(self.arr)):
            if self.arr[i] < self.min:
                self.minIndex = i
                self.min = self.arr[i]
            sv.options = [[self.minIndex,i,self.index],[(255,40,40),(13,91,138),(91,255,91)]]
            self.lastPos = i+1
            if self.lastPos % 2 == 0: return False
        return False
    
class Handler:
    def __init__(self):
        self.running = False
        self.mode = 'None'
        self.sorting = None
        self.sTime = time.time()
        self.eTime = self.sTime
    
    def render(self):
        for bnt in btns: bnt.render()
        sv.render()
    
    def update(self):
        global size
        self.eTime = time.time()
        if self.mode != 'None':
            if self.eTime - self.sTime >= .00:
                self.sTime = self.eTime
                if self.sorting.sort():
                    sv.sorted = True
                    self.mode = 'None'
                    sv.options = []
                    self.sorting = None
            #else: self.sTime = self.eTime
        for btn in btns:
            if btn.update()==2:
                if btn.name.find('Size') != -1 and size > 3:
                    size -= 1
                    btn.name = "Size:"+str(size)
                    sv.sorted = True
                    self.mode = 'None'
                    sv.options = []
                    self.sorting = None                    
                    sv.refresh(size)                
            elif btn.update()==1:
                if btn.name == "Bubble":
                    self.mode = 'Bubble'
                    sv.sorted = False
                    self.sorting = BubbleSort(sv.arr)
                elif btn.name == 'Insertion':
                    self.mode = 'Insertion'
                    sv.sorted = False
                    self.sorting = InsertionSort(sv.arr)
                elif btn.name == 'Merge':
                    self.mode = 'Merge'
                    sv.sorted = False
                    self.sorting = MergeSort(sv.arr)
                elif btn.name == 'Selection':
                    self.mode = 'Selection'
                    sv.sorted = False
                    self.sorting = SelectionSort(sv.arr)
                elif btn.name == 'Quick':
                    self.mode = 'Quick'
                    sv.sorted = False
                    self.sorting = QuickSort(sv.arr)
                elif btn.name == 'Shuffle':
                    sv.shuffleArr()
                    sv.sorted = True
                    self.mode = 'None'
                    sv.options = []
                    self.sorting = None
                elif btn.name == 'Random':
                    sv.arr = [random.randrange(len(sv.arr)) for i in range(len(sv.arr))]
                    sv.sorted = True
                    self.mode = 'None'
                    sv.options = []
                    self.sorting = None
                elif btn.name.find('Size') != -1:
                    size += 1
                    sv.sorted = True
                    self.mode = 'None'
                    sv.options = []
                    self.sorting = None                    
                    btn.name = "Size:"+str(size)
                    sv.refresh(size)
            
def bubbleSort(arr):
    global lastPos
    change = False
    for i in range(lastPos,len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
            lastPos = i
            change = True
            return arr, not change
    if lastPos != 0: 
        lastPos = 0
        return bubbleSort(arr)
    return arr, not change

sv = SortingVisual(size)
bubbleBtn = Button("Bubble", (15,15), 15)
insertionBtn = Button("Insertion", (int(bubbleBtn.rect[0]+bubbleBtn.rect[2]+15),15), 15)
mergeBtn = Button("Merge", (int(insertionBtn.rect[0]+insertionBtn.rect[2]+15),15), 15)
selectionBtn = Button("Selection", (int(mergeBtn.rect[0]+mergeBtn.rect[2]+15),15), 15)
quickBtn = Button("Quick", (int(selectionBtn.rect[0]+selectionBtn.rect[2]+15),15), 15)

shuffle = Button("Shuffle", (15,box[1]+70), 15)
randomNums = Button("Random", (int(shuffle.rect[0]+shuffle.rect[2]+15),box[1]+70), 15)

sizeBtn = Button("Size:"+str(size), (int(randomNums.rect[0]+randomNums.rect[2]+15),box[1]+70), 15)

btns = [bubbleBtn, insertionBtn, mergeBtn, selectionBtn, quickBtn, shuffle, randomNums, sizeBtn]

handler = Handler()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            quit()
    gameDisplay.fill( BG )
    #gameDisplay.fill( gray )
    pygame.draw.rect(gameDisplay, gray, [10,50,h_display-19,1])
    pygame.draw.rect(gameDisplay, gray, [10,50,1,v_display-60])
    pygame.draw.rect(gameDisplay, gray, [h_display-10,50,1,v_display-60])
    pygame.draw.rect(gameDisplay, gray, [10,v_display-10,h_display-19,1])
    pygame.draw.rect(gameDisplay, IN_BOX, [10,50,box[0],box[1]])
    pygame.display.set_caption("Sorting Algorithm [Rect:"+str(len(sv.arr))+"]")
    handler.render()
    handler.update()
    pygame.display.update()
    clock.tick(100)
        
        
        