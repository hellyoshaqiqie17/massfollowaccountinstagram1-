from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import proxy_service

# Akun yang akan difollow
akun_tujuan = "https://www.instagram.com/hellyoshaqiqieeee/"

# Membuka browser
browser = webdriver.Chrome('88.0.4324.96')

# Membaca file akuninstagram.txt dan mengambil setiap baris sebagai tuple username dan password
with open('akuninstagram.txt', 'r') as file:
    akun_list = [tuple(line.strip().split(':')) for line in file]

# Melakukan login pada setiap akun dan memfollow akun tujuan
for akun in akun_list:
    username, password = akun
    
    # Masuk ke halaman login Instagram
    browser.get('https://www.instagram.com/accounts/login/')
    
    # Mengisi username dan password
    username_input = browser.find_element(By.CSS_SELECTOR, "input[name='username']")
    username_input.send_keys(username)
    
    password_input = browser.find_element(By.CSS_SELECTOR, "input[name='password']")
    password_input.send_keys(password)
    
    # Menekan tombol login
    login_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    sleep(5)
    
    # Memfollow akun tujuan
    browser.get(f'https://www.instagram.com/hellyoshaqiqieeee/')
    follow_button = browser.find_element(By.CSS_SELECTOR, "button:contains('Follow')")
    follow_button.click()
    sleep(5)
    
    # Logout dari akun saat ini
    profile_button = browser.find_element(By.CSS_SELECTOR, "a[href='/" + username + "/']")
    profile_button.click()
    sleep(2)
    
    logout_button = browser.find_element(By.XPATH, "//div[@role='menuitem'][position()=last()]")
    logout_button.click()
    sleep(2)