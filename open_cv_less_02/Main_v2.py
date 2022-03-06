# библиотека си ви ту читается на англ. яз. для работы с изображ.
import cv2

#----------- ПРИМЕР РАБОТЫ С ИЗОБРАЖЕНИЯМИ
#заводим переменную img
#вызываем библиотеку cv2 и метод imread() для чтения файла
#imread('ИмяФайла')

img = cv2.imread('images/OpenCV.jpg')
##заводим переменную new_img для resize
new_img = cv2.resize(img,(300,500))
cv2.imshow('Result', new_img)
#вызываем метод imshow()
#cv2.imshow('Result', img)
# method waitKey(time) if time = 1000 ~ 1 sec
cv2.waitKey(0) #ждать вечно

#--------------- КОНЕЦ ПРИМЕРА РАБОТЫ С ИЗОБРАЖЕНИЯМИ




