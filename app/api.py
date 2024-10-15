import aiohttp
import asyncio

from app.settings import api_key


async def get_weather(city: str):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return_str = (f"Погода в городе {city}:\n"
                              f"Координаты: широта {data['coord']['lat']}, долгота {data['coord']['lon']}\n"
                              f"Температура: {data['main']['temp']}°C\n"
                              f"Ощущается как: {data['main']['feels_like']}°C\n"
                              f"Минимальная температура: {data['main']['temp_min']}°C\n"
                              f"Максимальная температура: {data['main']['temp_max']}°C\n"
                              f"Давление: {data['main']['pressure']} гПа\n"
                              f"Влажность: {data['main']['humidity']}%\n"
                              f"Видимость: {data['visibility']} м\n"
                              f"Скорость ветра: {data['wind']['speed']} м/с\n")
                return return_str
            else:
                return (
                    f"Ошибка при получении данных для города {city}: проверьте название города и попробуйте еще раз")
