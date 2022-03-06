# библиотека си ви ту читается на англ. яз. для работы с изображ.
import cv2

#----------- ПРИМЕР РАБОТЫ С ИЗОБРАЖЕНИЯМИ
#заводим переменную img
#вызываем библиотеку cv2 и метод imread() для чтения файла
#imread('ИмяФайла')

#img = cv2.imread('images/OpenCV.jpg')
#вызываем метод imshow()
#cv2.imshow('Result', img)
# method waitKey(time) if time = 1000 ~ 1 sec
#cv2.waitKey(1000)
#--------------- КОНЕЦ

#----------- ПРИМЕР РАБОТЫ С ВИДЕО
#заводим переменную cap сокр. capture (захват)
#вызываем библиотеку cv2 и метод VideoCapture(параметр) если файл имя файла пишем
#VideoCapture(0) - одна единственная камера (текушая)
#VideoCapture(1) если веб камер много пишем цифры, номер камеры
cap = cv2.VideoCapture('videos/shmara.avi')

#можно подключить эффекты, если поток c камеры
#id ширины 3 id высоты 4
#cap.set(3,500)
#cap.set(4,300)

while True:
   success, img = cap.read()
   cv2.imshow('Result', img)

   cv2.waitKey(100)



