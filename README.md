# OCDS Kingfisher - Process

This is the "Process" side of the OCDs Kingfisher app.

This receives data from the "Scrape" side, stores it, checks and transforms it.

For more info, please see https://kingfisher-process.readthedocs.io/en/latest/

For the "Scrape" side, please see https://github.com/open-contracting/kingfisher-scrape


# Webapps0 server

FLASK_APP=ocdskingfisherprocess.web.app FLASK_ENV=development KINGFISHER_PROCESS_WEB_API_KEYS=cat flask run --host 0 --port 9090
FLASK_APP=ocdskingfisherprocess.web.app FLASK_ENV=development KINGFISHER_PROCESS_WEB_API_KEYS=1234 flask run --host 0 --port 9090
flask run --host 0 --port 9090


python ocdskingfisher-process-cli local-load 6 /Users/sim/git/kingfisher/scrape/data/mexico_administracion_publica_federal2/20190508_203532 record_package_list_in_results

python ocdskingfisher-process-cli new-collection mexico_administracion_publica_federal  "2019-05-09 16:00:00"
python ocdskingfisher-process-cli local-load 7 /home/snbot/git/kingfisher-scrape/data/mexico_administracion_publica_federal/20190508_220102 record_package_list_in_results


scrapy crawl mexico_administracion_publica_federal
scrapy crawl chile_compra_releases


python ocdskingfisher-process-cli new-collection mexico_administracion_publica_federal  "2019-05-09 16:00:00"

### Delete old collections

python ocdskingfisher-process-cli delete-collection 2
python ocdskingfisher-process-cli delete-collections

# Web interface 
Setup nginx for

104.155.19.156:5000
104.155.19.156:9090

