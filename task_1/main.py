"""
Основной файл программы для обработки изображений.
Вариант 1: Изменение размера, применение фильтров и добавление текста.
"""
import os
from image_processing.imagehandler import ImageHandler
from image_processing.imageprocessor import ImageProcessor


def main():
    """Основная функция программы."""
    print("=" * 60)
    print("ПРОГРАММА ОБРАБОТКИ ИЗОБРАЖЕНИЙ")
    print("Вариант 1: Изменение размера + фильтр размытия + текст")
    print("=" * 60)
    
    # 1. Запрос пути к изображению
    print("\n--- ШАГ 1: ВВОД ДАННЫХ ---")
    image_path = input("Введите путь к изображению (или нажмите Enter для использования test.jpg): ").strip()
    
    if not image_path:
        # Создаем тестовое изображение, если его нет
        if not os.path.exists("test.jpg"):
            print("Создаем тестовое изображение...")
            from PIL import Image, ImageDraw
            img = Image.new('RGB', (400, 300), color='lightblue')
            draw = ImageDraw.Draw(img)
            draw.rectangle([50, 50, 350, 250], fill='darkblue', outline='white', width=3)
            draw.text((150, 150), "Тестовое изображение", fill='white')
            img.save("test.jpg")
            print("Тестовое изображение создано: test.jpg")
        image_path = "test.jpg"
    
    # 2. Создание обработчика
    print(f"\n--- ШАГ 2: ЗАГРУЗКА ИЗОБРАЖЕНИЯ ---")
    handler = ImageHandler(image_path)
    
    if handler.image is None:
        print("Не удалось загрузить изображение. Завершение программы.")
        return
    
    # Показать информацию об исходном изображении
    handler.show_info()
    
    # 3. Изменение размера (требование варианта 1)
    print("\n--- ШАГ 3: ИЗМЕНЕНИЕ РАЗМЕРА ДО 300x300 ---")
    handler.resize_to_300x300()
    
    # 4. Передача изображения процессору
    print("\n--- ШАГ 4: ПЕРЕДАЧА ИЗОБРАЖЕНИЯ НА ОБРАБОТКУ ---")
    processor = ImageProcessor(handler.get_image())
    
    # 5. Применение фильтра размытия (требование варианта 1)
    print("\n--- ШАГ 5: ПРИМЕНЕНИЕ ФИЛЬТРА РАЗМЫТИЯ ---")
    processor.apply_blur_filter(radius=2)
    
    # 6. Добавление текста (требование варианта 1)
    print("\n--- ШАГ 6: ДОБАВЛЕНИЕ ТЕКСТА ---")
    processor.add_text(text="Вариант 1", position="bottom_right")
    
    # 7. Получение обработанного изображения
    print("\n--- ШАГ 7: СОХРАНЕНИЕ РЕЗУЛЬТАТА ---")
    handler.image = processor.get_processed_image()
    
    # 8. Сохранение в формате PNG (требование варианта 1)
    output_path = input("Введите путь для сохранения (или нажмите Enter для result.png): ").strip()
    if not output_path:
        output_path = "result.png"
    
    handler.save_image(output_path, format='PNG')
    
    # 9. Показать итоговую информацию
    print("\n--- ШАГ 8: ИТОГОВАЯ ИНФОРМАЦИЯ ---")
    handler.show_info()
    
    print("\n" + "=" * 60)
    print("ОБРАБОТКА ЗАВЕРШЕНА УСПЕШНО!")
    print(f"Результат сохранен в: {os.path.abspath(output_path)}")
    print("=" * 60)


if __name__ == "__main__":
    main()