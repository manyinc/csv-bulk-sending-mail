Opis aplikacji
--------------

Program do wysyłania maili z ankietami/opiniami do klientów z listy zawartej w pliku CSV. Każdy klient otrzymuje maila z treścią w formacie HTML, zawierającą pytanie o opinię.

Jak zainstalować i uruchomić
----------------------------

Wymagania wstępne:
- Python 3.x z zainstalowanymi bibliotekami `smtplib` i `ssl`.
- Jeżeli nie posiadasz tych bibliotek, doinstaluj je:
  ```bath
  pip install smtplib ssl
  ```

Konfiguracja:
- Skonfiguruj dane dostępowe do konta pocztowego, z którego będą wysyłane maile:
  - `user`: Adres email używany do logowania
  - `passw`: Hasło do konta email
  - `smtp_server`: Adres serwera SMTP
  - `port`: Port serwera SMTP (domyślnie 465 dla SSL)

Instalacja:
- Pobierz pliki z repozytorium GitHub.

Uruchomienie:
- Umieść plik CSV `data.csv` w katalogu głównym programu.
- Uruchom program poprzez wykonanie skryptu Pythona:

```bath
python main.py
```

Upewnij się, że jesteś w katalogu zawierającym plik `main.py`.

Plik CSV:
- Plik `data.csv` powinien zawierać kolumnę `E-mail`, gdzie znajdują się adresy email odbiorców.

Uwagi:
- Program wysyła maile w formacie HTML z treścią zawartą w zmiennej `html_msg`.
- Pomiędzy wysyłkami maili program losowo oczekuje od 10 do 40 sekund, aby uniknąć nadmiernego obciążenia serwera pocztowego.
