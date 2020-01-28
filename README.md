# UFC Stats Scraper

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [TODO](#to_do)

## About <a name = "about"></a>

This is a web scraper to get data of all completed UFC fights from [UFC Stats](http://ufcstats.com/), built using [Scrapy](https://github.com/scrapy/scrapy). Scraped data are organized into 3 tables:

- `fight_info` <a name = "fight_info"></a> table, contains fight/match-up level meta-data.
- `fighter_stats`<a name = "fighter_stats"></a> table, contains fighter level data of fighters' career summary statistics.
- `fight_stats` <a name="fight_stats"></a> contains fighter-level performance data within each match-up.

## Getting Started <a name = "getting_started"></a>

### Prerequisites

You will need to install Scrapy and all relevant dependencies.

The quick way:

```
pip install scrapy
```

See the install section in the documentation at https://docs.scrapy.org/en/latest/intro/install.html for more details.

### Installing

Clone or fork the repo. Or download a local copy. Then crawl away.

## Usage <a name = "usage"></a>

Call `scrapy crawl spider_name` to start the crawler. There are two spiders you can run:

```
scrapy crawl ufcFights
```

The `ufcFights` spider will return

- [`fight_info`](#fight_info) table as a `.csv` file saved in `data/fight_info` directory.
- [`fight_stats`](#fight_stats) table as `.jl` file (newline-delimited JSON) saved in `data/fight_stats` directory. One line per fight.

```
scrapy crawl ufcFighters
```

The `ufcFighters` spider will return the [`fighter_stats`](#fighter_stats) table as a `.csv` file saved in `data/fighter_stats` directory.

All output files use timestamp as file names.

_Note: in the current version, running the spider will crawl the entire site, so it will take some time._

## TODO <a name = "to_do"></a>

- [ ] Add a spider to scrape upcoming fights
- [ ] Add options to limit the spider's scope, e.g. only scrape the new matches rather than the entire site.
