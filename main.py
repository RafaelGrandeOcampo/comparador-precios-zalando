from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import csv

def buscar_productos_pretty_zalando():
    # Especifica la URL de Zalando
    url = "https://www.zalando.es/catalogo/pretty-ballerinas/?sold_by_zalando=true"

    # Configurar el navegador Chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    # Iniciar el navegador Chrome
    driver = webdriver.Chrome(options=options)

    # Abrir la URL en el navegador
    driver.get(url)

    try:
        # cookies

        cookies = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="uc-btn-accept-banner"]'))
        ).click()

        for _ in range(2):

            # Encontrar todos los elementos que contienen información sobre productos
            productos = driver.find_elements(By.CSS_SELECTOR, '._LM.JT3_zV.CKDt_l.CKDt_l.LyRfpJ')

            # Iterar sobre los productos y extraer los enlaces
            enlaces_productos = []
            for producto in productos:
                enlace_producto = producto.get_attribute(
                    'href')
                enlaces_productos.append(enlace_producto)

                datos = {}
            for n in enlaces_productos:
                # Abrir el enlace en una nueva pestaña
                driver.execute_script("window.open();")
                driver.switch_to.window(driver.window_handles[1])
                driver.get(n)

                try:
                    pvp_price = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH,
                                                        '//*[@id="main-content"]/div[1]/div/div[2]/x-wrapper-re-1-4/div[2]/div/p[2]/span[2]'))
                    )
                    pvp =pvp_price.text.split()[0]
                except:
                    # Manejar la excepción si el elemento PVP no está presente
                    pvp = None  # o asigna un valor predeterminado según tus necesidades

                finally:
                    articulo = n[-6:-19:-1][::-1]
                    precio = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH,
                                                        '//*[@id="main-content"]/div[1]/div/div[2]/x-wrapper-re-1-4/div[2]/div/div/p/span[1]'))
                    )


                    datos = {'Modelo': '', 'Articulo': articulo, 'PVP': pvp, 'Precio_actual': precio.text.split()[0], 'Stock': '', 'enlace': n}


                    with open('Articulos_Zalando_v3.csv', 'a', newline='', encoding='utf-8') as csvfile:
                        fieldnames = ['Modelo', 'Articulo', 'PVP', 'Precio_actual', 'enlace']
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        # Si el archivo está vacío, escribe el encabezado
                        if csvfile.tell() == 0:
                            writer.writeheader()
                        writer.writerow(datos)

                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])

            try:
                siguiente_pagina= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '// *[ @ id = "main-content"] / div / div[7] / div / div[2] / nav / div / a[2]')))
                siguiente_pagina.click()
            except:
                print("No hay mas paginas")
            finally:
                continue



    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Cerrar el navegador
        driver.quit()

if __name__ == "__main__":
    buscar_productos_pretty_zalando()
