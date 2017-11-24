# Rhode Island laws-bot
This goal of this project is to create a web scraper to access the RI General Statutes ([webserver.rilin.state.ri.us/Statutes/](webserver.rilin.state.ri.us/Statutes/)) and convert the HTML into structured data files for future use and analysis.

## Usage
In the project folder, run `scrapy crawl laws -o <output_file>.json`.

## Work in progress
This scraper is a work in progress. Next steps on the TODO list:
* Implement `ItemPipeline`s to clean up the scraped data.
* Finalize `Section` fields to align with other standard legal code formats.

## Other information
### Technologies Used
* `scrapy` ([https://docs.scrapy.org/en/latest/index.html](https://docs.scrapy.org/en/latest/index.html)) - Python web crawler package used for the project. This repository was created using the `scrapy startproject` command.
