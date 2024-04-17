from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest 

@pytest.mark.usefixtures("setup")
class Test_homepage2:
    def test_üst_menü_linklerini_dogrula(Self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://demowebshop.tricentis.com/")
        

        expected_menu = ["BOOKS", "COMPUTERS", "ELECTRONICS", "APPAREL & SHOES", "DIGITAL DOWNLOADS","JEWELRY", "GIFT CARDS"]
        elements= driver.find_elements(By.CSS_SELECTOR,"ul.top-menu > li > a")

        actual_menu_items = [] #Gerçek üst menü öğelerini depolamak için boş bir liste oluşturur.
        for i in elements: # Her bir üst menü öğesi için döngü oluşturur.
            actual_menu_items.append(i.text) #Her bir üst menü öğesinin metnini gercek_menu_elemanlari listesine ekler.

        for i in range(len(expected_menu)): # Beklenen menü öğeleri ve gerçek menü öğeleri arasında karşılaştırma yapmak için bir döngü başlatır.
            assert expected_menu[i]==actual_menu_items[i] # Her iki menü öğesini karşılaştırır ve eşleşmezse bir hata döndürür.
        
        driver.quit()

    def test_urun_sayfasina_tiklayinca_urun_detaylari_sayfasi_acilir(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://demowebshop.tricentis.com/")
        
        ilk_urun_linki= driver.find_element(By.CSS_SELECTOR,"div.product-item h2 a")
        urun_ismi = ilk_urun_linki.text
        urun_fiyati=driver.find_element(By.CSS_SELECTOR,"span.price.actual-price").text 
        ilk_urun_linki.click()
        urun_ismi_detay_sayfasi= driver.find_element(By.CSS_SELECTOR,"div.product-name h1").text.strip() #strip boşlukları kaldıracak
        urun_fiyati_detay_sayfasi = driver.find_element(By.CSS_SELECTOR,"div.product-price span").text.strip()


        assert urun_ismi == urun_ismi_detay_sayfasi
        assert urun_fiyati == urun_fiyati_detay_sayfasi
        driver.quit()