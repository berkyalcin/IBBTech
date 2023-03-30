from cv2 import imread, imwrite, inRange, bitwise_and, COLOR_BGR2RGB, erode, cvtColor
from numpy import ones, uint8

EROSION_KERNEL = (5,5)
EROSION_ITERATION = 2

UPPER_BOUND = (40,40,40)
LOWER_BOUND = (0,0,0)

READ_FILE_PATH = "Test/Test1.jpg"
WRITE_FILE_PATH = "Test/Result1.jpg"

#Dosyayı okur
img = imread(READ_FILE_PATH)

#Resmi, BGR renk formatından RGB'ye çevirir
#img = cvtColor(img, COLOR_BGR2RGB)

#Resimde, belirtilen aralıktaki pikselleri bulur ve maskeler
mask = inRange(img,LOWER_BOUND,UPPER_BOUND)
img = bitwise_and(img,img,mask=mask)

#Çizginin öne çıkması için parçalı bölümleri çıkarır
kernel = ones(EROSION_KERNEL,uint8)
result = erode(img,kernel,iterations=EROSION_ITERATION)

#Sonucu belirtilen formatta kaydeder
imwrite(WRITE_FILE_PATH,result)


