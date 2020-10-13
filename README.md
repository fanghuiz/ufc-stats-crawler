# UFC Stats Crawler

## Table of Contents

- [About](#about)
- [Building and Running with Docker](#docker)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [TODO](#to_do)

## About <a name = "about"></a>

This is a web scraper to get data from [UFC Stats](http://ufcstats.com/), built using [Scrapy](https://github.com/scrapy/scrapy). Scraped data are organized as follows:

All completed UFC fights:

- `fight_info` <a name = "fight_info"></a> table, contains fight/match-up level meta-data.
- `fighter_stats`<a name = "fighter_stats"></a> table, contains fighter level data of fighters' career summary statistics.
- `fight_stats` <a name="fight_stats"></a> contains fighter-level performance data within each match-up.

Upcoming fights:

- `upcoming`<a name = "upcoming"></a> table contains match-up level information of all the upcoming fights in the next UFC event, according to this page http://ufcstats.com/statistics/events/completed.

Let me know if you've used the crawler or data to make something cool :wave:

## Building and Running with Docker <a name = "docker"></a>
Logs will be written to standard output in json format.

```
make build       # Builds the docker container
make ufcFights   # Run the ufcFights crawler
make ufcFighters # Run the ufcFighters crawler
make upcoming    # Run the upcoming crawler
```

## Getting Started <a name = "getting_started"></a>

### Prerequisites
* Python 3
* Scrapy

Install required packages.

```
pip install -r requirements.txt
```

If you have trouble installing Scrapy, see the install section in Scrapy documentation at https://docs.scrapy.org/en/latest/intro/install.html for more details.

### Installing

Clone or fork the repo. Or download a local copy. Then crawl away.

## Usage <a name = "usage"></a>

_Note: in the current version, running the spider will crawl the entire site, so it will take some time._

Call `scrapy crawl spider_name` to start the crawler. There are 3 spiders you can run:

```
scrapy crawl ufcFights
```

The `ufcFights` spider will return

- [`fight_info`](#fight_info) table as a `.csv` file saved in `data/fight_info` directory.
- [`fight_stats`](#fight_stats) table as `.jl` file (newline-delimited JSON) saved in `data/fight_stats` directory. One line per fight.

*If you prefer other output formats, you can modify the respective feed exports pipelines in `pipelines.py`. Or file an issue and let me know.*


```
scrapy crawl ufcFighters
```

The `ufcFighters` spider will return the [`fighter_stats`](#fighter_stats) table as a `.csv` file saved in `data/fighter_stats` directory.

```
scrapy crawl upcoming
```

The `upcoming` spider will return [`upcoming`](#upcoming) table as a `.csv` file, saved in `data/upcoming` directory.

All output files use timestamp as file names, stored in different folders.

## TODO <a name = "to_do"></a>

- [x] Add a spider to scrape upcoming fights
- [ ] Add options to limit the spider's scope, e.g. only scrape the new matches rather than the entire site.
