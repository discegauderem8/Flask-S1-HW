import click
from flask import Flask, request
from flask.cli import FlaskGroup
import requests
import threading
import multiprocessing
import asyncio
import aiohttp
import time
from markupsafe import escape

app = Flask(__name__)
cli = FlaskGroup(app)


def download_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        image_name = url.split('/')[-1]
        folder = r"S4_HW/downloads/"
        with open(folder + image_name, 'wb') as f:
            f.write(response.content)
        print(f"Загружено {image_name}")
    else:
        print(f"Не удалось загрузить файл по ссылке: {url}")


def download_with_threads(urls):
    start_time = time.time()
    threads = []
    for url in urls:
        thread = threading.Thread(target=download_image, args=(url,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    end_time = time.time()
    print(f"Время затрачено в многопоточном режиме: {end_time - start_time} секунд")


def download_with_processes(urls):
    start_time = time.time()
    processes = []
    for url in urls:
        process = multiprocessing.Process(target=download_image, args=(url,))
        process.start()
        processes.append(process)
    for process in processes:
        process.join()
    end_time = time.time()
    print(f"Времени затрачено в многопроцессорном режиме: {end_time - start_time} секунд")

async def download_image_async(session, url):
    async with session.get(url) as response:
        if response.status == 200:
            image_name = url.split('/')[-1]
            with open(image_name, 'wb') as f:
                f.write(await response.read())
            print(f"Загружено {image_name}")
        else:
            print(f"Не удалось загрузить по ссылке: {url}")

async def download_with_async(urls):
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [download_image_async(session, url) for url in urls]
        await asyncio.gather(*tasks)
    end_time = time.time()
    print(f"Времени затрачено в асинхронном режиме: {end_time - start_time} секунд")

@app.route('/download', methods=['POST'])
def download_images():
    urls = request.form.getlist('urls')
    download_with_threads(urls)
    download_with_processes(urls)
    asyncio.run(download_with_async(urls))
    return "Загрузка завершена"

@cli.command("download-images")
@click.argument('urls', nargs=-1)
def download_images_command(urls):
    download_with_threads(urls)
    download_with_processes(urls)
    asyncio.run(download_with_async(urls))
    print("Загрузка завершена")

if __name__ == "__main__":
    cli()



