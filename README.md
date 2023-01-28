# style_transfer_bot

Данный проект является финальным для курса по CV от МФТИ.

Задача: написать телеграм-бота, который будет получать на вход две картинки, а возвращать одну, которая будет результатом применения стиля одной исходной ко второй.

Архитектура модели была взята отсюда:
https://pytorch.org/tutorials/advanced/neural_style_tutorial.html

Для оптимальной работы было настроено разрешение входной и выходной картинки 200x200, это было сделано для ускорения работы, так как на сервере нет GPU. Это позволяет получать результат примерно за 2-3 минуты.

Были подобраны следующие параметры модели:
- num_steps=200
- style_weight=100000
- learning_rate=1

Через каждые 10 шагов модель сохраняет изображение и его значение лосса, при проходе всех 200 шагов, выбирает лучшее изображение (то, у которого лосс минимален среди всех сохраненных) и отправляет его обратно пользователю в разрешении 200x200.

Для демонстрации код также залит на HuggingFace, где упакован в docker-контейнер:
https://huggingface.co/spaces/MrSashkaman/StyleTransfer

Ссылка на самого бота в Telegram
https://t.me/af_style_transfer_bot








