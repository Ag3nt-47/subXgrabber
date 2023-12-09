import sys
from my_colors import fw, fr, fy, fg, fb, fc, fm, black, reset
from termcolor import colored
import time
import os
import platform


def get_operating_system():
    system_info = platform.system()
    return system_info


current_directory = os.getcwd()


def print_choose(lang):
    if lang == 'en':
        print(f"\n"
              f"{fw}Which option do you want to scan?:\n"
              f"{fc}1) {fg}Fast scan (2k subdomains)\n"
              f"{fc}2) {fy}Normal scan (31k subdomains)\n"
              f"{fc}3) {fr}Big scan (101k subdomains)\n"
              f"{fc}4) {black}Monster scan (650k subdomains)\n")

    elif lang == 'nl':
        print("\n"
              f"{fw}Welke optie wilt u scannen?:\n"
              f"{fc}1) {fg}Snelle scan (2k subdomeinen)\n"
              f"{fc}2) {fy}Normaal scan (31k subdomeinen)\n"
              f"{fc}3) {fr}Grote scan (101k subdomeinen)\n"
              f"{fc}4) {black}Monster scan (650k subdomeinen)\n")

    elif lang == 'ru':
        print("\n"
              f"{fw}Какой вариант вы хотите сканировать?:\n"
              f"{fc}1) {fg}Быстрое сканирование (2 тыс. поддоменов)\n"
              f"{fc}2) {fy}Обычное сканирование (31 тыс. поддоменов)\n"
              f"{fc}3) {fr}Большое сканирование (101 тыс. поддоменов)\n"
              f"{fc}4) {black}Сканирование монстров (650 тысяч поддоменов)\n")

    elif lang == 'tr':
        print("\n"
              f"{fw}Hangi şekilde tarama yapmak istiyorsun:\n"
              f"{fc}1) {fg}Hızlı tarama (2k subdomain)\n"
              f"{fc}2) {fy}Normal tarama (31k subdomain)\n"
              f"{fc}3) {fr}Büyük tarama (101k subdomain)\n"
              f"{fc}4) {black}Canavar tarama (650k subdomain)\n")

    elif lang == 'pl':
        print("\n"
              f"{fw}Którą opcję chcesz przeskanować?:\n"
              f"{fc}1) {fg}Szybkie skanowanie (2 tys. subdomen)\n"
              f"{fc}2) {fy}Normalne skanowanie (31 tys. subdomen)\n"
              f"{fc}3) {fr}Duże skanowanie (101 tys. subdomen)\n"
              f"{fc}4) {black}Skanowanie potworów (650 tys. subdomen)\n")

    else:
        sys.exit()


def print_target(lang):
    if lang == 'en':
        print(f"{fw}Enter the {fr}target site{fw}: ")
    elif lang == 'nl':
        print(f"{fw}Voer de {fr}doelsite{fw} in{fw}: ")
    elif lang == 'ru':
        print(f"{fw}введите {fr}целевой сайт{fw}: ")
    elif lang == 'tr':
        print(f"{fr}Hedef siteyi{fw} gir{fw}: ")
    elif lang == 'pl':
        print(f"{fw}Wpisz {fr}witrynę docelową{fw}: ")


def exit_message(lang, file_name):

    if get_operating_system() == "Windows":
        saved_file = rf"{current_directory}\Success\{file_name}"
    else:
        saved_file = rf"{current_directory}/Success/{file_name}"

    if lang == 'en':
        print(f"\n{fc}The results were saved in file '{fw}{saved_file}{fc}'.\n"
               f"{fy}The same results may have been written more than once, to remove the same results:\n"
               f"{fg}'{fr}https://www.textfixer.com/tools/remove-duplicate-lines-online.php{fg}' you can use this site.")

    elif lang == 'nl':
        print(f"\n{fc}De resultaten zijn opgeslagen in bestand '{fw}{saved_file}{fc}'.\n"
                f"{fy}Dezelfde resultaten kunnen meer dan eens zijn geschreven om dezelfde resultaten te verwijderen:\n"
                f"{fg}'{fr}https://www.textfixer.com/tools/remove-duplicate-lines-online.php{fg}' kunt u deze site gebruiken.")

    elif lang == 'ru':
        print(f"\n{fc}Результаты были сохранены в файле '{fw}{saved_file}{fc}'.\n"
                f"{fy}Одни и те же результаты могли быть записаны более одного раза, чтобы удалить одни и те же результаты:\n"
                f"{fg}'{fr}https://www.textfixer.com/tools/remove-duulate-lines-online.php{fg}' вы можете использовать этот сайт.")

    elif lang == 'tr':
        print(f"\n{fc}Sonuçlar '{fw}{saved_file}{fc}' dosyasına kaydedildi.\n"
                f"{fy}Aynı sonuçlar birden fazla kez yazılmış olabilir, aynı sonuçları kaldırmak için:\n"
                f"{fg}'{fr}https://www.textfixer.com/tools/remove-duplicate-lines-online.php{fg}' bu siteyi kullanabilirsiniz.")

    elif lang == 'pl':
        print(f"\n{fc}Wyniki zostały zapisane w pliku „{fw}{saved_file}{fc}”\n"
                f"{fy}Te same wyniki mogły zostać zapisane więcej niż raz, aby usunąć te same wyniki:\n"
                f"{fg}„{fr}https://www.textfixer.com/tools/remove-duplicate-lines-online.php{fg}”, możesz korzystać z tej witryny.")
