# wsb-15392-car-auctions-app
Aplikacja konsolowa napisana przy użyciu pythona. Realizuje temat zaliczeniowy nr.1 - Aukcje samochodowe.<br/>
Cel:<br>
Program realizuje wycinek działania serwisu aukcji samochodowych. Umożliwia wykonanie takich działań jak:<br/>
<li>Utworzenie użytkownika</li><br>
<li>Logowanie się na swoje konto w aplikacji</li><br>
<li>Wyświetlenie wszystkich dostępnych aukcji</li><br>
<li>Wyświetlenie aukcji, które zostały dodane przez zalogowanego użytkownika</li><br>
<li>Wyświetlenie aukcji, w których zalogowany użytkownik wział udział</li><br>
<li>Wyświetlenie szczegółów aukcji</li><br>
<li>Przefiltrowanie listy aukcji ze względu na cenę maksymalna, lokalizację, markę samochodu</li><br>
<li>Sortowanie listy aukcji ze względu na cenę lub czas zakończenia aukcji</li><br>
<li>Możliwość dodania własnej aukcji przez użytkownika</li><br>
<li>Możliwość wzięcia udziału w aukcji poprzez utworzenie oferty Kup Teraz</li><br>
<li>Możliwość wzięcia udziału w licytacji poprzez Licytacje</li><br>
<br>
Konfiguracja:<br>
Program wykorzystuje bazę mysql, dlatego istostnym elementem jest to by posiadać zainstalowany serwer lokalnie. Następnie należy podaj prawidłowy url do serwera wraz poświadczeniami w pliku db_service.py przy inicjalizacji zmiennej engine oraz w funkcji create_databate(), gdzie nie podajemy adresu naszej bazy.<br>
Domyślne ustawienie to 'mysql+mysqlconnector://root:root@localhost:3306/car_auctions' przy tworzeniu engine oraz 'mysql://root:root@localhost:3306' w funkcji tworzacej baze danych o nazwie car_auctions.<br>
Po uruchomieniu programu pojawi nam się menu z opcjami zalogowania lub utworzenia konta. Należy w pierwszej kolejności utworzyć sobie konto, aby móc się na nie zalogować i pracować na nim.<br>
<br>
Opis plików:<br>
<b>app.py</b> - zawiera szablon klasy App, będacy singletonem tak by w aplikacji aktualnie mogla byc zalogowana tylko jedna osoba, wiadomo, ze jesli mialby byc to webservice trzeba byloby pozwolić osobom na logowanie się w osobnych sesjach. Natomiast w tym programie zostało to nieco uproszczone. W planach również dodanie do tej klasy obecnego czasu aplikacji by zmieniał się co 5, tak by można było sprawdzać, które aukcje się zakończyły. Nie zostało to jednak zaimplementowane.<br>
<b>app_service.py</b>  - zawiera cała logikę działania aplikacji i wszystkie funkcje, które zajmuja sie interakcja z uzytkownikiem<br>
<b>db_service.py</b>  - zawiera DAOsy oraz wszystkie funkcje korzystajace z polaczenia z baza danych, majace za zadanie wyciagnac z odpowiednich tabel dane na podstawie podanych parametrów<br>
<b>app_exceptions.py</b>  - zawiera wyjatki wykorzystywane w aplikacji<br>
<b>main.py</b>  - plik startowy, zawiera funkcję rozpoczynajaca dzialanie aplikacji oraz wywoluje skrypty inicjalizujace
