from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import csv
import time


url = "https://accounts.google.com/v3/signin/identifier?opparams=%253F&dsh=S1225602608%3A1706165883000363&access_type=offline&client_id=370947398364-4ei5612p3evupc6qm8frglhfk356l7ib.apps.googleusercontent.com&o2v=1&redirect_uri=https%3A%2F%2Fwww.vinted.es%2Fmember%2Fsignup%2Fselect_type&response_type=code&scope=email+profile&service=lso&state=eyJyZWRpcmVjdF91cmkiOiIvP3JlZl91cmw9JTJGIiwicmFuZG9tX3N0cmlu%0AZyI6Ijc3ZWZkM2FmYTUifQ%3D%3D%0A&theme=glif&flowName=GeneralOAuthFlow&continue=https%3A%2F%2Faccounts.google.com%2Fsignin%2Foauth%2Fconsent%3Fauthuser%3Dunknown%26part%3DAJi8hAOy5wLAvFc8FOVER1f79bvPfqQf6a2t3NYsB1UKmhWxasiwGJPQPDAX1O58ORMkcPBkbovEeVAtCmnbqsUvx5JPa2VNeyZQpN542z7DHPoXF8Mb7iWIMfuxASBiC7ket7aDuRaoe9e-BVWSp-HzasQOQcDioLsh5B5yiBPF0CFCJnCRRu_UMs7mVJnnNqsDOir7KpvO-qFzXdKbMdte9lrC5HX-0uV0QYBW-Wwi6pW6hh3qSx1JNbOq2CcLNZuc6BbvrrHJtPSK8vf0R9alIlkW9ANKcNSTkgNSosITtI5V50btjJ-PeqcbsQsrUTeDJ8lE5kaS67ceUd0RbnbnRk1wbi3DjJH83eXe1gfC57KvMdlunJlw8FTJhVxCsES74fk38jbtfTOJ-32wDaH_-IPKHOn41brHJI8L-dPxb2ZCR7QNcshIlvM_5Vt8U_tM8fYT2fyN0AMLc4caK4ddRs7UnmshCw%26as%3DS1225602608%253A1706165883000363%26client_id%3D370947398364-4ei5612p3evupc6qm8frglhfk356l7ib.apps.googleusercontent.com%26theme%3Dglif%23&app_domain=https%3A%2F%2Fwww.vinted.es&rart=ANgoxcdyetfExE-vOAUHFP__gaUx9soJBJ-iegtaqQ1j4kFjJp9GXdwUYFtzx0w9OIPwG1QPafg3HME4jB3eQf8ajNwflAAk7rWxRyDhVUfvehW9vhkmO4I"

# Configurar el navegador Chrome
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# Iniciar el navegador Chrome
driver = webdriver.Chrome(options=options)

# Abrir la URL en el navegador
driver.get(url)

#Aceptar cookies

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'onetrust-accept-btn-handler'))).click()

#iniciar sesion

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/div[2]/div/div[2]/span[2]/span'))).click()

time.sleep(1000)

driver.quit()