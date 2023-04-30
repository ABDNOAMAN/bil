
BOT_NAME = "bilbasen"

SPIDER_MODULES = ["bilbasen.spiders"]
NEWSPIDER_MODULE = "bilbasen.spiders"

DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}


OBOTSTXT_OBEY = True

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"


TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

PLAYWRIGHT_LAUNCH_OPTIONS = {
    "headless": False,
    #"timeout": 2000 * 1000,  # 20 seconds
}
