"""
Модуль ImageProcessor - обработка изображений.
"""
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os


class ImageProcessor:
    """Класс для обработки изображений."""
    
    def __init__(self, image):
        """
        Инициализация процессора изображений.
        
        Args:
            image: Объект изображения PIL
        """
        self.image = image
        if image is None:
            print("Предупреждение: Передано пустое изображение!")
    
    def apply_blur_filter(self, radius: int = 2):
        """
        Применение фильтра размытия.
        
        Args:
            radius (int): Радиус размытия
        """
        if self.image is None:
            print("Ошибка: Изображение не загружено!")
            return
        
        print(f"Применяем фильтр размытия (радиус: {radius})...")
        self.image = self.image.filter(ImageFilter.GaussianBlur(radius))
        print("Фильтр применен успешно!")
    
    def add_text(self, text: str = "Вариант 1", position: str = "bottom_right"):
        """
        Добавление текста на изображение.
        
        Args:
            text (str): Текст для добавления
            position (str): Позиция текста ('bottom_right', 'top_left', 'center')
        """
        if self.image is None:
            print("Ошибка: Изображение не загружено!")
            return
        
        print(f"Добавляем текст: '{text}' в позицию: {position}")
        
        # Создаем объект для рисования
        draw = ImageDraw.Draw(self.image)
        
        try:
            # Пытаемся использовать системный шрифт
            font = ImageFont.truetype("arial.ttf", 20)
        except:
            # Если системный шрифт не найден, используем стандартный
            font = ImageFont.load_default()
            print("Используется стандартный шрифт")
        
        # Определяем позицию текста
        if position == "bottom_right":
            text_position = (self.image.width - 150, self.image.height - 30)
        elif position == "top_left":
            text_position = (10, 10)
        elif position == "center":
            text_position = (self.image.width // 2 - 50, self.image.height // 2 - 10)
        else:
            text_position = (10, 10)
        
        # Добавляем текст
        draw.text(text_position, text, fill="white", font=font, stroke_width=2, stroke_fill="black")
        print("Текст добавлен успешно!")
    
    def rotate_image(self, angle: float = 90):
        """
        Поворот изображения.
        
        Args:
            angle (float): Угол поворота в градусах
        """
        if self.image is None:
            print("Ошибка: Изображение не загружено!")
            return
        
        print(f"Поворачиваем изображение на {angle} градусов...")
        self.image = self.image.rotate(angle, expand=True)
        print("Поворот выполнен успешно!")
    
    def get_processed_image(self):
        """Получение обработанного изображения."""
        return self.image