from pyautogui import * 
import pyautogui 
import time 
import keyboard 
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)



pic = pyautogui.screenshot(region=(75,40,1000,700))

width, height = pic.size

for x in range(0,width,5):
    for y in range(0,height,5):
        while keyboard.is_pressed('q') == False:
            
            levelup = pyautogui.locateOnScreen('levelup.png', region=(75,40,1000,700), confidence=0.75)
            battle = pyautogui.locateOnScreen('battle.png', region=(75,40,1000,700), confidence=0.75) 
            trigo = pyautogui.locateOnScreen('trigo2.png', region=(75,40,1000,700), confidence=0.75) 
            trigo2 = pyautogui.locateOnScreen('trigo3.png', region=(75,40,1000,700), confidence=0.75) 
            trigo3 = pyautogui.locateOnScreen('trigo4.png', region=(75,40,1000,700), confidence=0.75) 
            trigo4 = pyautogui.locateOnScreen('trigo5.png', region=(75,40,1000,700), confidence=0.75) 
            trigo5 = pyautogui.locateOnScreen('trigo6.png', region=(75,40,1000,700), confidence=0.75) 
            trigo6 = pyautogui.locateOnScreen('trigo8.png', region=(75,40,1000,700), confidence=0.85) 
            trigo8 = pyautogui.locateOnScreen('trigo9.png', region=(75,40,1000,700), confidence=0.75) 
            trigo9 = pyautogui.locateOnScreen('trigo10.png', region=(75,40,1000,700), confidence=0.75) 
            trigo10 = pyautogui.locateOnScreen('trigo11.png', region=(75,40,1000,700), confidence=0.75) 

            if battle != None:

                print("batalla")
                pyautogui.click(962, 475)#listo
                time.sleep(12.0)
                pyautogui.click(1123, 184)#flecha 4pa
                time.sleep(3.0)
                pyautogui.click(827, 470)#enemigo
                time.sleep(3.0)
                pyautogui.click(962, 475)#pasar turno
                time.sleep(12.0)
                pyautogui.click(1123, 184)#flecha
                time.sleep(3.0)
                pyautogui.click(827, 470)#enemigo
                time.sleep(3.0)
                pyautogui.click(962, 475)#pasar turno
                time.sleep(12.0)
                pyautogui.click(1123, 184)#flecha
                time.sleep(3.0)
                pyautogui.click(827, 470)#enemigo
                time.sleep(7.0)
                pyautogui.click(1082,231)
                break
            else:
                if levelup != None:
                    levelPoint = pyautogui.center(levelup)
                    print(levelPoint,"levelup")
                    trigox, trigoy = levelPoint
                    pyautogui.click(trigox, trigoy)
                    time.sleep(3.5)
                    break
                else:
                    if trigo != None:
                        trigoPoint = pyautogui.center(trigo)
                        print(trigoPoint,"1")
                        trigox, trigoy = trigoPoint
                        pyautogui.click(trigox, trigoy)
                        time.sleep(3.5)
                        break
                    else:
                        if trigo2 != None:
                            trigoPoint = pyautogui.center(trigo2)
                            print(trigoPoint,"2")
                            trigox, trigoy = trigoPoint
                            pyautogui.click(trigox, trigoy)
                            time.sleep(3.5)
                            break
                        else:
                            if trigo3 != None:
                                trigoPoint = pyautogui.center(trigo3)
                                print(trigoPoint,"3")
                                trigox, trigoy = trigoPoint
                                pyautogui.click(trigox, trigoy)
                                time.sleep(3.5)
                                break
                            else:
                                if trigo4 != None:
                                    trigoPoint = pyautogui.center(trigo4)
                                    print(trigoPoint,"4")
                                    trigox, trigoy = trigoPoint
                                    pyautogui.click(trigox, trigoy)
                                    time.sleep(3.5)
                                    break
                                else:
                                    if trigo5 != None:
                                        trigoPoint = pyautogui.center(trigo5)
                                        print(trigoPoint,"5")
                                        trigox, trigoy = trigoPoint
                                        pyautogui.click(trigox, trigoy)
                                        time.sleep(3.5)
                                        break
                                    else:
                                        if trigo6 != None:
                                            trigoPoint = pyautogui.center(trigo6)
                                            print(trigoPoint,"6")
                                            trigox, trigoy = trigoPoint
                                            pyautogui.click(trigox, trigoy)
                                            time.sleep(3.5)
                                            break
                                        else:
                                            if trigo8 != None:
                                                trigoPoint = pyautogui.center(trigo8)
                                                print(trigoPoint,"8")
                                                trigox, trigoy = trigoPoint
                                                pyautogui.click(trigox, trigoy)
                                                time.sleep(3.5)
                                                break
                                            else:
                                                if trigo9 != None:
                                                    trigoPoint = pyautogui.center(trigo9)
                                                    print(trigoPoint,"9")
                                                    trigox, trigoy = trigoPoint
                                                    pyautogui.click(trigox, trigoy)
                                                    time.sleep(3.5)
                                                    break
                                                else:
                                                    if trigo10 != None:
                                                        trigoPoint = pyautogui.center(trigo10)
                                                        print(trigoPoint,"10")
                                                        trigox, trigoy = trigoPoint
                                                        pyautogui.click(trigox, trigoy)
                                                        time.sleep(3.5)
                                                        break
                                                    else:
                                                        print("no lo puedo ver")
                                                        time.sleep(0.05)
                                                        