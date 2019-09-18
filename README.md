# OCDS Kingfisher - Process

This is the "Process" side of the OCDs Kingfisher app.

This receives data from the "Scrape" side, stores it, checks and transforms it.

For more info, please see https://kingfisher-process.readthedocs.io/en/latest/

For the "Scrape" side, please see https://github.com/open-contracting/kingfisher-scrape


FLASK_APP=ocdskingfisherprocess.web.app FLASK_ENV=development KINGFISHER_PROCESS_WEB_API_KEYS=cat flask run --host 0 --port 9090
flask run --host 0 --port 9090


python ocdskingfisher-process-cli local-load 6 /Users/sim/git/kingfisher/scrape/data/mexico_administracion_publica_federal2/20190508_203532 record_package_list_in_results

python ocdskingfisher-process-cli new-collection mexico_administracion_publica_federal  "2019-05-09 16:00:00"
python ocdskingfisher-process-cli local-load 7 /home/snbot/git/kingfisher-scrape/data/mexico_administracion_publica_federal/20190508_220102 record_package_list_in_results


scrapy crawl mexico_administracion_publica_federal
scrapy crawl uk_contracts_finder


python ocdskingfisher-process-cli new-collection mexico_administracion_publica_federal  "2019-05-09 16:00:00"

python ocdskingfisher-process-cli delete-collection 2
python ocdskingfisher-process-cli delete-collection 3
python ocdskingfisher-process-cli delete-collection 4
python ocdskingfisher-process-cli delete-collection 5
python ocdskingfisher-process-cli delete-collection 6

python ocdskingfisher-process-cli delete-collections

python ocdskingfisher-process-cli delete-collection 13
python ocdskingfisher-process-cli delete-collection 12
python ocdskingfisher-process-cli delete-collection 11
python ocdskingfisher-process-cli delete-collection 10
python ocdskingfisher-process-cli delete-collection 9
python ocdskingfisher-process-cli delete-collection 8

python ocdskingfisher-process-cli delete-collections

