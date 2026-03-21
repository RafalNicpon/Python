🛡️ SOC Sentinel - System Analizy i Korelacji Incydentów (SIEM)
SOC Sentinel to autorskie narzędzie klasy SIEM (Security Information and Event Management) zaprojektowane do automatycznej analizy logów serwerowych, wzbogacania ich o dane geolokalizacyjne oraz inteligentnego powiadamiania o zagrożeniach typu Brute-Force.

🏗️ Architektura Systemu
Projekt został zrealizowany w architekturze modularnej, integrującej następujące warstwy:

Ingestia Danych: Parser logów tekstowych wyodrębniający adresy IP oraz metadane zdarzeń.

Enrichment (Wzbogacanie): Integracja z API IPStack w celu identyfikacji kraju pochodzenia agresora.

Persystencja: Baza danych PostgreSQL zapewniająca trwałe przechowywanie incydentów i historię ataków.

Silnik Korelacji: Algorytm statystyczny wykrywający powtarzalne wzorce ataków (Threshold-based detection).

Alerting: System powiadomień w czasie rzeczywistym zintegrowany z platformą Discord.

🚀 Technologia
Język: Python 3.x

Analiza Danych: Pandas, NumPy

Baza Danych: PostgreSQL (Psycopg2)

Interfejs: Jupyter Notebook (Playbook)

API zewnętrzne: IPStack (Geolocation), Discord Webhooks

⚙️ Konfiguracja i Instalacja
Wymagania:
Zainstaluj niezbędne biblioteki komendą:

Bash
pip install -r requirements.txt
Plik konfiguracyjny (.env):
W folderze głównym musi znajdować się plik .env o następującej strukturze:

Fragment kodu
DB_HOST=localhost
DB_NAME=Soc
DB_USER=postgres
DB_PASS=1qazxsW@
DB_PORT=5432
IPSTACK_KEY=d46578cdac45440dde5d083221f927ff
DISCORD_WEBHOOK_URL=https://discordapp.com/api/webhooks/1484604359714275328/X9ZFwB3G7KTlQzm7xM_Y85--EsOlaZXI__52DCVyTdWvSacJItkHWvc9nq3BsSc0tpro
Logi:
System analizuje plik serwer.log znajdujący się w folderze głównym projektu.

📊 Sposób użycia
Projekt jest udostępniony w formie interaktywnego dokumentu Projekt.ipynb. Aby uruchomić analizę:

Otwórz plik Projekt.ipynb w środowisku VS Code lub Jupyter Lab.

Uruchom komórki po kolei (Run All).

Wynik analizy korelacyjnej zostanie wyświetlony w formie tabeli pod ostatnią komórką, a wykryte incydenty zostaną wysłane na skonfigurowany kanał Discord.

📝 Funkcje SIEM
Detekcja Brute-Force: Automatyczne flagowanie adresów IP przekraczających próg 3 nieudanych prób logowania.

Raportowanie Geograficzne: Identyfikacja krajów, z których pochodzi najwięcej prób naruszeń.

Czyszczenie Bazy: Wbudowana funkcja resetowania tabeli incydentów przed nowym cyklem analizy.