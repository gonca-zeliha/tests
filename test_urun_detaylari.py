import time
import pytest
from selenium.webdriver.common.by import By
import re
from pages import Anasayfa
from pages import UrunDetaySayfasi

@pytest.mark.usefixtures("setup")
class Test_UrunDetaylari:

    def test_add_to_cart_button_adds_product_to_cart(self):
        self.driver.get("https://demowebshop.tricentis.com/")
        anasayfa = Anasayfa()
        urun_detay_sayfasi = UrunDetaySayfasi()

        anasayfa.gift_card_olmayan_ilk_urun_ismine_tikla()
        oncesi= urun_detay_sayfasi.sepetteki_urun_sayisini_ver()
        quantity = urun_detay_sayfasi.quantity_sayfasiini_ver()
        urun_detay_sayfasi.add_to_cart_buttonuna_tikla()
        time.sleep(1) # sepetteki urun sayisinin degismesini bekliyor
        sonrasi = urun_detay_sayfasi.sepetteki_urun_sayisini_ver()
        

        assert sonrasi ==  (oncesi + quantity)
        