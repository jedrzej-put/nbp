https://github.com/ilia-gilmijarow/rentals/tree/main/tests
https://github.com/gilmijar?tab=repositories

0. Nie mam pronleow, ocena pozytywna, akceptacja

pyfake_fs

1. Testy:
   -krótkie
   -w nazwie mowia co sprawdzają
   -nie sprawdzaja gototwcych funkcjonalności(np. csv.writer zastapic jakism mockiem)
   -testy integracyjne sprawdzaja kilka funkcjonalosci, bez mockow
   -unit testy dzialaja na mockach
   -rgf - najpierw test ktory nie dziala, potem tak zeby dzialal, potem refactor
   -np. testowac wywolanie nie istniejacej funkcji, potem, napisac 'byle jak zeby dzialalo', potem 'sprawdzic czy mozna napisac lepiej
   -fixture do tworzenie mockow i dodatkowych obiektów, które nie są testowane
   -obiekty testowane poza fixture w testach
   -testowac danych tyle ile uwazamy, że trzeba(moze wystraczyć jedna linia z pliku)
   -do assert moze dawac predefinowe test_outputy.csv, czyli jakis pliki które są specjalne przygotowane do testcase'a
   -takie pliki przygotowac w kodzie, utowrzyc jakies excepted_output.csv, potem excepted_output.py który już wczyta te dane i potem się bedzie stąd imporotwac jako pythonowe obiekty
   -outputy kilku linkowe moge jeszcze byc w testach z assert jesli nie jest ich za duzo i sa czytelne

2. Dziedziczenie

- pojedyncze bez multiinhretience

3. Databricks
   -pyspark i python

4. AzureFunction i AwsLambda: python, serverless, troche inny python
