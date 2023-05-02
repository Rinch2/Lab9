def one():
    from PIL import Image, ImageDraw, ImageFont
    import os

    images_folder = r"images"

    if not os.path.isdir("gotovoe"):
        os.mkdir("gotovoe")

    images_list = os.listdir(images_folder)

    for image in images_list:
        img = Image.open(os.path.join(images_folder, image))
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", 36)

        text = "Watermark"
        color = (18, 154, 228)

        x = 0
        y = 0

        draw.text((x, y), text, fill=color, font=font)
        img.show()

        img.save(os.path.join("gotovoe", "watermarked_" + image))

def two():

    from PIL import Image, ImageDraw, ImageFont
    import os

    images_folder = r"images"
    if not os.path.isdir("gotovoe"):
        os.mkdir("gotovoe")

    images_list = os.listdir(images_folder)

    for image in images_list:
        ext = os.path.splitext(image)
        if ext[1] not in ['.jpg', '.png']:
            print("Файл {} с расширением {}. Данное расширение не поддерживается".format(ext[0], ext[1]))
            continue
        else:
            img = Image.open(os.path.join(images_folder, image))
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype("arial.ttf", 36)

            text = "Watermark"
            color = (18, 154, 228)

            x = 0
            y = 0

            draw.text((x, y), text, fill=color, font=font)
            img.show()

def three():
    import csv

    total_price = 0
    items_list = []

    with open('goods.csv') as products:
        reader = csv.reader(products)
        headers = next(reader)  # получение заголовков и переход к следующей строке
        print("Нужно купить: ")

        for row in reader:
            try:
                name, quantity, price = row
                quantity = int(quantity)
                price = int(price)
            except ValueError:
                print(f"Ошибка данных в строке: {row}")
                continue

            items_list.append((name, quantity, price))

        for name, quantity, price in items_list:
            total_price += quantity * price
            print(f"{name} - {quantity} шт. за {price} руб.")

    print(f"Итоговая сумма: {total_price}")
# one()
# two()
# three()