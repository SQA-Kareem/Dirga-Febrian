import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class SystemTest(unittest.TestCase):
    def setUp(self):
        # Inisialisasi WebDriver
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # Tambahkan penundaan waktu sebelum menutup WebDriver
        time.sleep(5)

        # Menutup WebDriver
        self.driver.quit()
        
    def login(self):
        email_input = self.driver.find_element(By.ID, "email")
        password_input = self.driver.find_element(By.ID, "hs-toggle-password")

        # Memasukkan nama pengguna dan kata sandi
        email_input.send_keys("xixixi@gmail.com")
        password_input.send_keys("fghjkliow")

        time.sleep(2)

        button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        button.click()

        time.sleep(2)

        # Menunggu pesan kesalahan atau popup
        error_message = self.driver.find_element(By.TAG_NAME, "h2")
        error = error_message.text
        if error == "Login Failed":
            swal = self.driver.find_element(By.CLASS_NAME, "swal2-confirm")
            swal.click()

            time.sleep(5)

            # Mengosongkan inputan
            email_input.clear()
            password_input.clear()
            
            # Mengganti nilai email dan password
            email_input.send_keys("dimasmhs@gmail.com")
            password_input.send_keys("fghjkliow")

            time.sleep(2)

            button.click()

            time.sleep(2)

            # Cari dan klik tombol OK pada popup
            swal = self.driver.find_element(By.CLASS_NAME, "swal2-confirm")
            swal.click()
        else:
            # Cari dan klik tombol OK pada popup
            swal = self.driver.find_element(By.CLASS_NAME, "swal2-confirm")
            swal.click()


    def test_login(self):
        # Membuka halaman web
        self.driver.get("https://intermoni.my.id/")

        time.sleep(2)

        button = self.driver.find_element(By.XPATH, "//a[@href='pages/signIn.html']")
        button.click()

        time.sleep(2)

        # Login dengan email dan password tertentu
        self.login()


if __name__ == "__main__":
    unittest.main()
