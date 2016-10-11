
BOT_NAME = 'kohsantepheap'

SPIDER_MODULES = ['kohsantepheap.spiders']
NEWSPIDER_MODULE = 'kohsantepheap.spiders'

ROBOTSTXT_OBEY = True
LOG_LEVEL = 'WARNING'

ITEM_PIPELINES = {
    'kohsantepheap.pipelines.MySQLPipeline': 2
}

DB_HOST = 'localhost'
DB_PORT = 3306
DB_USER = 'root'
DB_PASSWD = 'tU/x@168rY'
DB_DB = 'khmergoo_sequelize'
