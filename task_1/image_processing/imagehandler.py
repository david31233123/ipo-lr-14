"""
Модуль ImageHandler - базовые операции с изображениями.
"""
from PIL import Image, ImageDraw, ImageFont
import os


class ImageHandler:
    """Класс для базовой работы с изображениями."""
    
    def __init__(self, image_path: str):
        """
        Инициализация обработчика изображений.
        
        Args:
            image_path (str): Путь к изображению
        """
        self.image_path = image_path
        self.image = None
        self.load_image()
    
    def load_image(self):
        """Загрузка изображения из файла."""
        print(f"Загружаем изображение из: {self.image_path}")
        try:
            self.image = Image.open(self.image_path)
            print(f"Изображение загружено. Размер: {self.image.size}, Формат: {self.image.format}")
        except FileNotFoundError:
            print(f"Ошибка: Файл {self.image_path} не найден!")
            self.image = None
        except Exception as e:
            print(f"Ошибка при загрузке изображения: {e}")
            self.image = None
    
    def save_image(self, output_path: str, format: str = 'PNG'):
        """
        Сохранение изображения.
        
        Args:
            output_path (str): Путь для сохранения
            format (str): Формат файла (по умолчанию PNG)
        """
        if self.image is None:
            print("Ошибка: Изображение не загружено!")
            return
        
        print(f"Сохраняем изображение в: {output_path} (формат: {format})")
        try:
            self.image.save(output_path, format)
            print(f"Изображение успешно сохранено!")
        except Exception as e:
            print(f"Ошибка при сохранении: {e}")
    
    def resize_to_300x300(self):
        """Изменение размера изображения до 300x300 пикселей."""
        if self.image is None:
            print("Ошибка: Изображение не загружено!")
            return
        
        print(f"Изменяем размер изображения с {self.image.size} до 300x300...")
        self.image = self.image.resize((300, 300))
        print("Размер изменен успешно!")
    
    def get_image(self):
        """Получение изображения для передачи в ImageProcessor."""
        return self.image
    
    def show_info(self):
        """Показать информацию об изображении."""
        if self.image:
            print("=" * 50)
            print("ИНФОРМАЦИЯ ОБ ИЗОБРАЖЕНИИ:")
            print(f"Размер: {self.image.size} пикселей")
            print(f"Режим: {self.image.mode}")
            print(f"Формат: {self.image.format}")
            print("=" * 50)
        else:
            print("Изображение не загружено!")