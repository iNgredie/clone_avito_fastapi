import uvicorn

from avito.settings import settings

if __name__ == '__main__':
    uvicorn.run(
        'avito.app:app',
        host=settings.server_host,
        port=settings.server_port,
        reload=True
    )
