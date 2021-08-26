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



pic = pyautogui.screenshot(region=(645,58,448,239))

width, height = pic.size

for x in range(0,width,5):
    for y in range(0,height,5):
        while keyboard.is_pressed('q') == False:
            
            lino = pyautogui.locateOnScreen('lino2.png', region=(645,58,448,239), confidence=0.70) 
            lino2 = pyautogui.locateOnScreen('lino3.png', region=(645,58,448,239), confidence=0.70) 
            lino3 = pyautogui.locateOnScreen('lino4.png', region=(645,58,448,239), confidence=0.80) 
            lino4 = pyautogui.locateOnScreen('lino5.png', region=(645,58,448,239), confidence=0.70) 
            lino5 = pyautogui.locateOnScreen('lino6.png', region=(645,58,448,239), confidence=0.70) 
            lino6 = pyautogui.locateOnScreen('lino8.png', region=(645,58,448,239), confidence=0.70) 
            lino8 = pyautogui.locateOnScreen('lino9.png', region=(645,58,448,239), confidence=0.70) 
            lino9 = pyautogui.locateOnScreen('lino10.png', region=(645,58,448,239), confidence=0.70) 
            
            
            if lino != None:
                linoPoint = pyautogui.center(lino)
                print(linoPoint,"1")
                linox, linoy = linoPoint
                pyautogui.click(linox, linoy)
                time.sleep(3.5)
                break
            else:
                if lino2 != None:
                    linoPoint = pyautogui.center(lino2)
                    print(linoPoint,"2")
                    linox, linoy = linoPoint
                    pyautogui.click(linox, linoy)
                    time.sleep(3.5)
                    break
                else:
                    if lino3 != None:
                        linoPoint = pyautogui.center(lino3)
                        print(linoPoint,"3")
                        linox, linoy = linoPoint
                        pyautogui.click(linox, linoy)
                        time.sleep(3.5)
                        break
                    else:
                        if lino4 != None:
                            linoPoint = pyautogui.center(lino4)
                            print(linoPoint,"4")
                            linox, linoy = linoPoint
                            pyautogui.click(linox, linoy)
                            time.sleep(3.5)
                            break
                        else:
                            if lino5 != None:
                                linoPoint = pyautogui.center(lino5)
                                print(linoPoint,"5")
                                linox, linoy = linoPoint
                                pyautogui.click(linox, linoy)
                                time.sleep(3.5)
                                break
                            else:
                                if lino6 != None:
                                    linoPoint = pyautogui.center(lino6)
                                    print(linoPoint,"6")
                                    linox, linoy = linoPoint
                                    pyautogui.click(linox, linoy)
                                    time.sleep(3.5)
                                    break
                                else:
                                    if lino8 != None:
                                        linoPoint = pyautogui.center(lino8)
                                        print(linoPoint,"8")
                                        linox, linoy = linoPoint
                                        pyautogui.click(linox, linoy)
                                        time.sleep(3.5)
                                        break
                                    else:
                                        if lino9 != None:
                                            linoPoint = pyautogui.center(lino9)
                                            print(linoPoint,"9")
                                            linox, linoy = linoPoint
                                            pyautogui.click(linox, linoy)
                                            time.sleep(3.5)
                                            break
                                        else:
                                            print("no lo puedo ver")
                                            time.sleep(0.5)
                                                