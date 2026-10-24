class DevelopmentConfig():
    DEBUG=True
    MYSQL_HOST='localhost'
    MYSQL_USER='paola'
    MYSQL_PASSWORD='12345678'
    MYSQL_DB='api_utl'
    MYSQL_CURSORCLASS = 'Cursor'

config={
    'development': DevelopmentConfig
}