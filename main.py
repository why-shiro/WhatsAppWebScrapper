import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.common.action_chains import ActionChains
import data_parser
import excelparser
opts = FirefoxOptions()
opts.add_argument("--width=1920")
opts.add_argument("--height=1080")
driver = webdriver.Firefox(options=opts)
dataContainer = data_parser.NumberProcessor()
ep = excelparser.Excel()
driver.get("https://web.whatsapp.com/")
time.sleep(6)

# WhatsApp Web'e giriş yapana kadar bekle
wait = WebDriverWait(driver, 600)
wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@data-testid,'drawer-left')]")))
print("Pass")

time.sleep(5)

addedList = []
userNameList = []
scrollbarSize = driver.find_elements(By.XPATH, "//div[@id='pane-side']")[0].get_attribute("scrollHeight")
print("ScrollBar Size: ", scrollbarSize)
# Kullanıcıları listele
for i in range(0, int(scrollbarSize), 1295):
    scrollbar = driver.find_elements(By.XPATH, "//div[@id='pane-side']")[0]
    driver.execute_script("arguments[0].scrollTo(0, " + str(i) + ");", scrollbar)
    time.sleep(0.2)
    # //div[contains(@class,'y_sn4')]
    users = driver.find_elements(By.XPATH, "//div[@id='pane-side']//div[contains(@class,'lhggkp7q ln8gz9je rx9719l')]")
    driver.execute_script("arguments[0].scrollTo(0, " + str(i) + ");", scrollbar)
    time.sleep(1)
    correctListuser = []
    for x in users:
        px = int(x.get_attribute("style").split("translateY(")[1].split("px)")[0])
        correctListuser.append([px,x])
    tt = sorted(correctListuser)
    print(tt)
    for user in tt:
        try:
            driver.execute_script("arguments[0].scrollTo(0, " + str(i) + ");", scrollbar)
            time.sleep(0.8)
            styleElement = user[1].get_attribute("style")
            pixels = styleElement.split("translateY(")[1].split("px)")[0]
            print("Pixel: " + pixels)
            driver.execute_script("arguments[0].scrollTo(0, " + str(pixels) + ");", scrollbar)
            time.sleep(0.2)
            action = ActionChains(driver)
            action.context_click(user[1]).perform()
            time.sleep(0.4)
            isGroupQuery = driver.find_elements(By.XPATH, "//div[@aria-label='Gruptan çık']")
            gr = ""
        except:
            print("Last users!")

        if len(isGroupQuery) > 0:
            gr = "true"
        else:
            gr = "false"
        time.sleep(0.8)
        if gr == "false":
            if not (addedList.__contains__(user[1].get_attribute("innerText").split("\n")[0])):
                try:
                    user[1].click()
                    userInfo = driver.find_elements(By.XPATH,
                                                    "//span[contains(@data-testid,'conversation-info-header-chat-title')]")[
                        0]
                    time.sleep(0.4)
                    userInfo.click()
                    time.sleep(0.4)
                    telephoneNumber = driver.find_elements(By.XPATH, "//div[contains(@class,'a4ywakfo qt60bha0')]")[
                        0].get_attribute("innerText")
                    print(user[1].get_attribute("innerText").split("\n")[0], gr, pixels, telephoneNumber)
                    addedList.append(user[1].get_attribute("innerText").split("\n")[0])
                except:
                    print("Bulunan hesaap işletme hesabıdır.")
                    continue
        else:
            if not (addedList.__contains__(user[1].get_attribute("innerText").split("\n")[0])):
                user[1].click()
                time.sleep(0.8)
                userInfo = driver.find_elements(By.XPATH,
                                                "//span[contains(@data-testid,'conversation-info-header-chat-title')]")[
                    0]
                time.sleep(0.5)
                userInfo.click()
                scrollableObjext = driver.find_elements(By.XPATH,
                                                        "//div[contains(@class,'g0rxnol2 g0rxnol2 thghmljt p357zi0d rjo8vgbg ggj6brxn f8m0rgwh gfz4du6o ag5g9lrv bs7a17vp ov67bkzj')]")[
                    0]
                time.sleep(0.5)
                driver.execute_script("arguments[0].scrollTo(0, 600);", scrollableObjext)
                button = driver.find_elements(By.XPATH,
                                              "//div[contains(@data-testid,'section-participants')]")
                if not (len(button) == 0):
                    time.sleep(0.4)
                    button[0].click()
                    time.sleep(0.3)
                    registeredUsers = []
                    sizeOfList = driver.find_elements(By.XPATH,
                                                      "//div[contains(@class,'g0rxnol2 g0rxnol2 thghmljt p357zi0d rjo8vgbg ggj6brxn f8m0rgwh gfz4du6o ag5g9lrv bs7a17vp ov67bkzj')]//div[contains(@tabindex,0)]")[
                        0].size['height']
                    print("Size of height", sizeOfList)
                    for j in range(0, int(sizeOfList), 1000):
                        innerList = driver.find_elements(By.XPATH,
                                                         "//div[contains(@class,'g0rxnol2 g0rxnol2 thghmljt p357zi0d "
                                                         "rjo8vgbg ggj6brxn f8m0rgwh gfz4du6o ag5g9lrv bs7a17vp "
                                                         "ov67bkzj')]")[
                            0]
                        driver.execute_script("arguments[0].scrollTo(0, " + str(j) + ");", innerList)
                        correctList = []
                        driver.execute_script("arguments[0].scrollTo(0, " + str(j) + ");", innerList)
                        time.sleep(1)
                        innerUsers = driver.find_elements(By.XPATH,
                                                          "//div[contains(@class,'g0rxnol2 g0rxnol2 thghmljt p357zi0d "
                                                          "rjo8vgbg ggj6brxn f8m0rgwh gfz4du6o ag5g9lrv bs7a17vp "
                                                          "ov67bkzj')]//div[contains(@tabindex,'0')]//div//div//div["
                                                          "contains(@class,'lhggkp7q ln8gz9je rx9719la')]")
                        for pa in innerUsers:
                            userStyle = pa.get_attribute("style")
                            userPoint = int(userStyle.split("translateY(")[1].split("px)")[0])
                            correctList.append([userPoint, pa])
                        newList = sorted(correctList)
                        print(newList)
                        time.sleep(0.5)
                        for lastUser in newList:
                            try:
                                print("Current User: ", lastUser[1].get_attribute("innerText"))
                                styleObjext = lastUser[1].get_attribute("style")
                                objectPoint = styleObjext.split("translateY(")[1].split("px)")[0]
                                driver.execute_script("arguments[0].scrollTo(0, " + str(objectPoint) + ");",
                                                      innerList)
                                time.sleep(0.2)
                                if len(lastUser[1].get_attribute("innerText")) > 1 and \
                                        lastUser[1].get_attribute("innerText").split("\n")[0].split(" ")[0][
                                        :1] == "+":
                                    print("Found Letter = ",
                                          lastUser[1].get_attribute("innerText").split("\n")[0].split(" ")[0][:1])
                                    if not (
                                            addedList.__contains__(
                                                (lastUser[1].get_attribute("innerText").split("\n")[0]))):
                                        phoneNum = lastUser[1].get_attribute("innerText").split("\n")[0]
                                        print("Phone Number: ", phoneNum)
                                        ep.addContact(phoneNum)
                                        addedList.append(lastUser[1].get_attribute("innerText").split("\n")[0])
                                    else:
                                        print("Added Already")
                                elif not (len(lastUser[1].get_attribute("innerText")) == 1):
                                    if not (userNameList.__contains__(lastUser[1].get_attribute("innerText"))):
                                        print("User Name: ", lastUser[1].get_attribute("innerText").split("\n")[0])
                                        userNameList.append(lastUser[1].get_attribute("innerText").split("\n")[0])
                                    else:
                                        print("This user already added to list")
                                else:
                                    print("Letter Found")
                                driver.execute_script("arguments[0].scrollTo(0, " + str(j) + ");", innerList)
                                time.sleep(0.2)
                            except:
                                print("Skipping registered user")
                        innerUsers = None
                        innerList = None
                    check_user_list = driver.find_elements(By.XPATH, "//div[contains(@title,'Katılımcılarda Ara')]")
                    if not (len(check_user_list) == 0):
                        driver.find_elements(By.XPATH, "//div[contains(@data-testid,'btn-closer-drawer')]")[
                            0].click()
            else:
                addedList.append(user[1].get_attribute("innerText").split("\n")[0])

        try:
            if addedList.__contains__(user[1].get_attribute("innerText").split("\n")[0]):
                print("Already contained")
            else:
                print("Added New")
                name = user[1].get_attribute("innerText").split("\n")[0]
                addedList.append(name)
                dataContainer.addElement(name, "052", gr, int(pixels))
        except:
            print("Counterpane")
        driver.execute_script("arguments[0].scrollTo(0, " + str(i) + ");", scrollbar)


print("All List: ")
print(addedList)
print("Username List: ")
print(userNameList)
time.sleep(60)

# Tarayıcıyı kapat
driver.quit()
