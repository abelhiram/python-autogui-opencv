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
            
            levelup = pyautogui.locateOnScreen('levelup.png', region=(75,40,1000,700), confidence=0.65)
            battle = pyautogui.locateOnScreen('battle.png', region=(75,40,1000,700), confidence=0.65) 
            canamo = pyautogui.locateOnScreen('canamo2.png', region=(75,40,1000,700), confidence=0.65) 
            canamo2 = pyautogui.locateOnScreen('canamo3.png', region=(75,40,1000,700), confidence=0.65) 
            canamo3 = pyautogui.locateOnScreen('canamo4.png', region=(75,40,1000,700), confidence=0.80) 
            canamo4 = pyautogui.locateOnScreen('canamo5.png', region=(75,40,1000,700), confidence=0.65) 
            canamo5 = pyautogui.locateOnScreen('canamo6.png', region=(75,40,1000,700), confidence=0.65) 
            canamo6 = pyautogui.locateOnScreen('canamo8.png', region=(75,40,1000,700), confidence=0.65) 
            canamo8 = pyautogui.locateOnScreen('canamo9.png', region=(75,40,1000,700), confidence=0.65) 
            canamo9 = pyautogui.locateOnScreen('canamo10.png', region=(75,40,1000,700), confidence=0.65) 

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
                    canamox, canamoy = levelPoint
                    pyautogui.click(canamox, canamoy)
                    time.sleep(3.5)
                    break
                else:
                    if canamo != None:
                        canamoPoint = pyautogui.center(canamo)
                        print(canamoPoint,"1")
                        canamox, canamoy = canamoPoint
                        pyautogui.click(canamox, canamoy)
                        time.sleep(3.5)
                        break
                    else:
                        if canamo2 != None:
                            canamoPoint = pyautogui.center(canamo2)
                            print(canamoPoint,"2")
                            canamox, canamoy = canamoPoint
                            pyautogui.click(canamox, canamoy)
                            time.sleep(3.5)
                            break
                        else:
                            if canamo3 != None:
                                canamoPoint = pyautogui.center(canamo3)
                                print(canamoPoint,"3")
                                canamox, canamoy = canamoPoint
                                pyautogui.click(canamox, canamoy)
                                time.sleep(3.5)
                                break
                            else:
                                if canamo4 != None:
                                    canamoPoint = pyautogui.center(canamo4)
                                    print(canamoPoint,"4")
                                    canamox, canamoy = canamoPoint
                                    pyautogui.click(canamox, canamoy)
                                    time.sleep(3.5)
                                    break
                                else:
                                    if canamo5 != None:
                                        canamoPoint = pyautogui.center(canamo5)
                                        print(canamoPoint,"5")
                                        canamox, canamoy = canamoPoint
                                        pyautogui.click(canamox, canamoy)
                                        time.sleep(3.5)
                                        break
                                    else:
                                        if canamo6 != None:
                                            canamoPoint = pyautogui.center(canamo6)
                                            print(canamoPoint,"6")
                                            canamox, canamoy = canamoPoint
                                            pyautogui.click(canamox, canamoy)
                                            time.sleep(3.5)
                                            break
                                        else:
                                            if canamo8 != None:
                                                canamoPoint = pyautogui.center(canamo8)
                                                print(canamoPoint,"8")
                                                canamox, canamoy = canamoPoint
                                                pyautogui.click(canamox, canamoy)
                                                time.sleep(3.5)
                                                break
                                            else:
                                                if canamo9 != None:
                                                    canamoPoint = pyautogui.center(canamo9)
                                                    print(canamoPoint,"9")
                                                    canamox, canamoy = canamoPoint
                                                    pyautogui.click(canamox, canamoy)
                                                    time.sleep(3.5)
                                                    break
                                                else:
                                                    print("no lo puedo ver")
                                                    time.sleep(0.5)
                                                        