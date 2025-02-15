import telebot

botTimeWeb = telebot.TeleBot('7995267379:AAH11bd5w5rykYBIs5vdc3YcRlhKreaeAWM')

from telebot import types

@botTimeWeb.message_handler(commands=['start'])
def startBot(message):
  first_mess = "🫶 Привет, Друг!\n\nЯ бот «Психологическая помощь для подростков»\nСо мной будет интересно!\n\nЖелаешь продолжить?"
  markup = types.InlineKeyboardMarkup()
  button_yes = types.InlineKeyboardButton(text = 'Да, желаю продолжить!', callback_data='yes')
  markup.add(button_yes)
  botTimeWeb.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)

@botTimeWeb.callback_query_handler(func=lambda call:True)
def response(function_call2):
   if function_call2.message:
      if function_call2.data == "yes":
         third_mess = "Ознакомьтесь, пожалуйста, с информацией ниже: \n\n📍 В современном образовательном процессе важным аспектом является не только усвоение материала, но и психологическая поддержка учащихся.\nОсобенно это актуально для учеников 9-х и 11-х классов, которые готовятся к важным экзаменам — ОГЭ и ЕГЭ.\n\n🧠 Морально-психологическое состояние - это качественная определённость личности или коллектива, характеризующая направленность и динамику психических процессов, межличностных отношений\n\nНаш проект нацелен на поддержку обучающихся старших классов - подростков.\nЕсли ты сдаешь экзамены и сильно нерничаешь, знай, что здесь тебя точно поддержат!\n\nНО❗Если ты не сдаешь экзамены, нам тоже будет о чем поговорить!\n\nНадеюсь, что тебе всё пока что нравится!"
         markup = types.InlineKeyboardMarkup()
         button_neinformatsia = types.InlineKeyboardButton(text='Я ознакомился(сь) с ин-ей!', callback_data='yes2')
         markup.add(button_neinformatsia)
         botTimeWeb.send_message(function_call2.message.chat.id, third_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes2":
         fourth_mess = "Ответь, пожалуйста, на вопрос:\n\nКак ты себя чувствуешь? (не в физическом, а в психологическом плане)"
         markup = types.InlineKeyboardMarkup()
         button_neinformatsia2 = types.InlineKeyboardButton(text='Все плохо, нужна поддержка!', callback_data='yes3')
         markup.add(button_neinformatsia2)
         button_neinformatsia3 = types.InlineKeyboardButton(text='Все супер, справляюсь!', callback_data='yes4')
         markup.add(button_neinformatsia3)
         botTimeWeb.send_message(function_call2.message.chat.id, fourth_mess, parse_mode='html', reply_markup=markup)


      #поотрицательнымМЕНЮ
      if function_call2.data == "yes3":
         f_mess = "Какой у тебя тип состояния? (попробуй описать по шкале от 1 до 8, насколько ты себя плохо или хорошо чувствуешь) \n\n📍1. Лёгкая Грусть / Так Себе\n\nОписание: Небольшая печаль, раздражительность. Чувство, что день не задался, но ещё можно исправить. Лёгкая тоска по чему-то. \n\nТриггеры: Мелкие неудачи, плохая погода, скука. \n\nРеакция: Желание побыть одному, послушать музыку, посмотреть видео.\n\n📍2. Раздражение \n\nОписание: Повышенная раздражительность, нетерпение. Всё кажется неправильным и глупым. Лёгкое желание поспорить.\n\nТриггеры: Назойливые люди, несправедливость, технические проблемы.\n\nРеакция: Ворчание, сарказм, попытки избежать общения.\n\n📍3. Усталость / Всё Лень\n\n Описание: Физическая и эмоциональная усталость. Отсутствие мотивации что-либо делать. Ощущение, что энергии нет ни на что.\n\nТриггеры: Недостаток сна, переутомление, скучная работа.\n\nРеакция: Желание спать, избегать активной деятельности, апатия.\n\n📍4. Уныние\n\nОписание: Более глубокая печаль, чем на уровне 1. Чувство одиночества и бессмысленности. Потеря интереса к вещам, которые раньше нравились.\n\nТриггеры: Плохие новости, воспоминания, чувство потери.\n\nРеакция: Отстранённость, погружение в себя, прослушивание грустной музыки.\n\n📍5. Тревога\n\nОписание: Беспокойство, напряжение, ощущение надвигающейся опасности. Трудности с концентрацией.\n\nТриггеры: Школа, социальные ситуации, мысли о будущем.\n\nРеакция: Нервозность, избегание ситуаций, вызывающих тревогу, грызение ногтей.\n\n📍6. Злость\n\nОписание: Сильное раздражение, гнев, ярость. Желание кричать, ломать вещи. Чувство несправедливости и беспомощности.\n\nТриггеры: Предательство, оскорбления, потеря контроля.\n\nРеакция: Агрессия, словесные нападки, изоляция.\n\n📍7. Отчаяние\n\nОписание: Глубокая печаль, безнадёжность, чувство, что ничего не имеет значения. Потеря веры в себя и в будущее.\n\nТриггеры: Тяжёлые потери, неудачи, чувство вины\n\nРеакция: Плач, изоляция, мысли о самоповреждении\n\n📍8. Опустошение\n\nОписание: Отсутствие эмоций, чувство пустоты внутри. Потеря интереса ко всему, апатия. Ощущение, что жизнь проходит мимо.\n\nТриггеры: Хронический стресс, травмы, депрессия.\n\nРеакция: Безразличие, отстранённость, отсутствие мотивации что-либо делать."
         markup = types.InlineKeyboardMarkup()
         button_temperament = types.InlineKeyboardButton(text='🚀 1', callback_data='yes5')
         button_temperament2 = types.InlineKeyboardButton(text='🚀 2', callback_data='yes6')
         button_temperament3 = types.InlineKeyboardButton(text='🚀 3', callback_data='yes7')
         button_temperament4 = types.InlineKeyboardButton(text='🚀 4', callback_data='yes8')
         button_temperament5 = types.InlineKeyboardButton(text='🚀 5', callback_data='yes9')
         button_temperament6 = types.InlineKeyboardButton(text='🚀 6', callback_data='yes10')
         button_temperament7 = types.InlineKeyboardButton(text='🚀 7', callback_data='yes11')
         button_temperament8 = types.InlineKeyboardButton(text='🚀 8', callback_data='yes12')
         markup.add(button_temperament, button_temperament2, button_temperament3, button_temperament4, button_temperament5, button_temperament6, button_temperament7, button_temperament8)
         botTimeWeb.send_message(function_call2.message.chat.id, f_mess, parse_mode='html', reply_markup=markup)


      #поположительнымМЕНЮ
      if function_call2.data == "yes4":
         s_mess = "Какое у тебя настроение? (попробуй описать по шкале от 1 до 8, насколько ты себя плохо или хорошо чувствуешь)\n\n📍 1. Просто Нормально\n\nОписание: Отсутствие негативных эмоций уже воспринимается как положительное состояние. Ощущение, что ничего не раздражает и не беспокоит.\n\nТриггеры: Тихий вечер, отсутствие конфликтов, когда никто не трогает.\n\nРеакция: Расслабление, возможность заниматься своими делами без помех.\n\n📍 2. Лёгкое Удовольствие\n\nОписание: Небольшая радость от чего-то приятного. Лёгкая улыбка, хорошее настроение, но без сильного восторга.\n\nТриггеры: Забавное видео, вкусная еда, интересная игра.\n\nРеакция: Улыбка, смех, желание поделиться с кем-то увиденным/услышанным.\n\n📍 3. Воодушевление\n\nОписание: Появление интереса к чему-то новому, желание творить, учиться. Чувство, что есть силы и энергия для достижения целей.\n\nТриггеры: Хорошая музыка, интересный фильм, общение с вдохновляющим человеком.\n\nРеакция: Желание действовать, заниматься творчеством, искать новую информацию.\n\n📍 4. Принятие\n\nОписание: Чувство внутреннего спокойствия и гармонии с собой. Принятие своих недостатков и слабостей. Ощущение, что всё идёт своим чередом.\n\nТриггеры: Разговор с понимающим человеком, медитация, время наедине с собой.\n\nРеакция: Самоуверенность, отсутствие тревоги, способность спокойно реагировать на трудности.\n\n📍 5. Поддержка\n\nОписание: Чувство, что тебя любят и ценят. Ощущение поддержки со стороны близких людей. Знание, что ты не один.\n\nТриггеры: Проявление заботы, комплименты, искренние слова поддержки.\n\nРеакция: Открытость, благодарность, желание отвечать взаимностью.\n\n📍 6. Успех\n\nОписание: Радость от достижения цели, преодоления трудности. Чувство гордости за себя и свои способности.\n\nТриггеры: Хорошая оценка, победа в конкурсе, завершение сложного проекта.\n\nРеакция: Самоуверенность, мотивация, желание ставить новые цели.\n\n📍 7. Свобода\n\nОписание: Ощущение независимости и свободы от ограничений. Возможность делать то, что хочется, без страха и осуждения.\n\nТриггеры: Путешествие, выходные, время с друзьями, занимаясь любимым делом.\n\nРеакция: Радость, энтузиазм, чувство, что жизнь полна возможностей.\n\n📍 8. Эйфория\n\nОписание: Интенсивное чувство счастья, восторга и радости. Ощущение, что всё идеально и прекрасно.\n\nТриггеры: Общение с любимым человеком, достижение заветной мечты, важные события.\n\nРеакция: Неконтролируемый смех, слезы радости, чувство всемогущества (важно: часто, такая эйфория может быть временной и сменяться разочарованием, поэтому важно оценивать ситуацию реально)."
         markup = types.InlineKeyboardMarkup()
         button_temperamentforhappy = types.InlineKeyboardButton(text='🚀 1', callback_data='yes13')
         button_temperamentforhappy1 = types.InlineKeyboardButton(text='🚀 2', callback_data='yes14')
         button_temperamentforhappy2 = types.InlineKeyboardButton(text='🚀 3', callback_data='yes15')
         button_temperamentforhappy3 = types.InlineKeyboardButton(text='🚀 4', callback_data='yes16')
         button_temperamentforhappy4 = types.InlineKeyboardButton(text='🚀 5', callback_data='yes17')
         button_temperamentforhappy5 = types.InlineKeyboardButton(text='🚀 6', callback_data='yes18')
         button_temperamentforhappy6 = types.InlineKeyboardButton(text='🚀 7', callback_data='yes19')
         button_temperamentforhappy7 = types.InlineKeyboardButton(text='🚀 8', callback_data='yes20')
         markup.add(button_temperamentforhappy, button_temperamentforhappy1, button_temperamentforhappy2, button_temperamentforhappy3, button_temperamentforhappy4, button_temperamentforhappy5, button_temperamentforhappy6,button_temperamentforhappy7)
         botTimeWeb.send_message(function_call2.message.chat.id, s_mess, parse_mode='html', reply_markup=markup)
      #поотрицательным
      #ЛЕГКАЯ ГРУСТЬ
      if function_call2.data == "yes5":
         seven_mess = "😉 Вы выбрали тип состояния «Лёгкая Грусть / Так Себе»\n\n«Лёгкая Грусть» - Небольшая печаль, тоска. Чувствуешь, что день не супер, но ещё не всё потеряно.\n\nСпособы решения проблемы 👇\n\n- Отвлечься: Фильм, музыка, книга, игра - что-то, что тебя отвлечёт и поднимет настроение.\n\n- Движение: Прогулка на свежем воздухе, танцы под любимую музыку. Физическая активность помогает!\n\n- Поговорить: Если есть с кем. Просто выговориться может помочь.\n\n- Комфорт: Уютное одеяло, горячий чай, любимая еда. Забота о себе.\n\n- Не давить: Не ругай себя за грусть. Это нормально. Просто дай себе время."
         markup = types.InlineKeyboardMarkup()
         button_sure = types.InlineKeyboardButton(text='Да, это про меня! Cпасибо за советы!', callback_data='yes21')
         markup.add(button_sure)
         button_no = types.InlineKeyboardButton(text='Нет, не совсем.', callback_data='yes22')
         markup.add(button_no)
         botTimeWeb.send_message(function_call2.message.chat.id, seven_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes21":
         eight_mess = "В таком случае получай картинку из телеграмм-канала нашего проекта!\n\nhttps://t.me/pcycologi/3\n\nНадеемся, что мы тебе помогли!\n\nСпасибо за разговор, друг!\n\nДо новых встреч 🤍"
         botTimeWeb.send_message(function_call2.message.chat.id, eight_mess, parse_mode='html')
      if function_call2.data == "yes22":
         nine_mess = "Не отчаивайся, ведь всегда можно вернуться в меню и выбрать для себя подходяшую категорию!\n\nЕсли ты всё-таки ничего не нашел, не расстраивайся!\nМы подготовили для тебя милую картинку из телеграмм-канала нашего проекта!\n\nhttps://t.me/pcycologi/3\n\nНадеемся, что мы тебе помогли!\n\nСпасибо за разговор, друг!\n\nДо новых встреч 🤍"
         botTimeWeb.send_message(function_call2.message.chat.id, nine_mess, parse_mode='html')

      #РАЗДРАЖЕНИЕ
      if function_call2.data == "yes6":
         seven_mess = "😉 Вы выбрали тип состояния «Раздражение» \n\n«Раздражение» - Повышенная раздражительность, нетерпение. Всё вокруг кажется тупым и неправильным.\n\nСпособы решения проблемы 👇\n\n- Выдохнуть: Сделай несколько глубоких вдохов и выдохов. Звучит банально, но работает.\n\n- Уйти: Если источник раздражения рядом, уйди. Дай себе время остыть.\n\n- Выплеснуть: Физическая активность (побить подушку, попрыгать), порисовать (даже просто чиркать на бумаге), написать всё, что чувствуешь, а потом выкинуть.\n\n- Расслабиться: Медитация, дыхательные упражнения, послушать спокойную музыку.\n\n- Понять причину: Почему ты раздражён? Осознание проблемы – первый шаг к её решению.\n\n- Не копить: Поговори с кем-то о том, что тебя бесит (но не превращай это в нытье)."
         markup = types.InlineKeyboardMarkup()
         button_sure4 = types.InlineKeyboardButton(text='Да, это про меня! Cпасибо за советы!', callback_data='yes25')
         markup.add(button_sure4)
         button_no4 = types.InlineKeyboardButton(text='Нет, не совсем.', callback_data='yes26')
         markup.add(button_no4)
         botTimeWeb.send_message(function_call2.message.chat.id, seven_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes25":
         eight_mess = "В таком случае получай картинку из телеграмм-канала нашего проекта!\n\nhttps://t.me/pcycologi/4\n\nНадеемся, что мы тебе помогли!\n\nСпасибо за разговор, друг!\n\nДо новых встреч 🤍"
         botTimeWeb.send_message(function_call2.message.chat.id, eight_mess, parse_mode='html')
      if function_call2.data == "yes26":
         nine_mess ="Не отчаивайся, ведь всегда можно вернуться в меню и выбрать для себя подходяшую категорию!\n\nЕсли ты всё-таки ничего не нашел, не расстраивайся!\nМы подготовили для тебя милую картинку из телеграмм-канала нашего проекта!\n\nhttps://t.me/pcycologi/4\n\nНадеемся, что мы тебе помогли!\n\nСпасибо за разговор, друг!\n\nДо новых встреч 🤍"
         botTimeWeb.send_message(function_call2.message.chat.id, nine_mess, parse_mode='html', reply_markup=markup)

      #УСТАЛОСТЬ
      if function_call2.data == "yes7":
         ten_mess = "😉 Вы выбрали тип состояния «Усталость»\n\n«Усталость» - физическое и эмоциональное истощение, отсутствие мотивации.\n\nСпособы решения проблемы 👇\n\n- Сон: Постарайся выспаться. Наладить режим сна - важно.\n\n- Отдых: Не только сон, но и просто время для себя, чтобы ничего не делать.\n\n- Питание: Правильное питание даёт энергию. Избегай фастфуда и сладкого.\n\n- Движение: Лёгкая физическая активность (прогулка, йога) поможет взбодриться.\n\n- Делегирование: Если можешь, попроси кого-нибудь помочь тебе с делами.\n\n- Перерывы: Делай перерывы во время работы или учебы."
         markup = types.InlineKeyboardMarkup()
         button_sure7 = types.InlineKeyboardButton(text='Да, это про меня! Спасибо за советы!', callback_data='yes29')
         markup.add(button_sure7)
         button_no8 = types.InlineKeyboardButton(text='Нет, не совсем.', callback_data='yes30')
         markup.add(button_no8)
         botTimeWeb.send_message(function_call2.message.chat.id, ten_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes29":
         elvn_mess = "В таком случае получай картинку из телеграмм-канала нашего проекта!\n\nhttps://t.me/pcycologi/5\n\nНадеемся, что мы тебе помогли!\n\nСпасибо за разговор, друг!\n\nДо новых встреч 🤍"
         botTimeWeb.send_message(function_call2.message.chat.id, elvn_mess, parse_mode='html')
      if function_call2.data == "yes30":
         tw_mess = "Не отчаивайся, ведь всегда можно вернуться в меню и выбрать для себя подходяшую категорию!\n\nЕсли ты всё-таки ничего не нашел, не расстраивайся!\nМы подготовили для тебя милую картинку из телеграмм-канала нашего проекта!\n\nhttps://t.me/pcycologi/5\n\nНадеемся, что мы тебе помогли!\n\nСпасибо за разговор, друг!\n\nДо новых встреч 🤍"
         botTimeWeb.send_message(function_call2.message.chat.id, tw_mess, parse_mode='html')

      #УНЫНИЕ
      if function_call2.data == "yes8":
         thrt_mess = "😉 Вы выбрали тип состояния «Уныние»\n\n«Уныние» - глубокая печаль, одиночество, потеря интереса к жизни.\n\nСпособы решения проблемы 👇\n\n- Общение: Поговори с кем-то, кому доверяешь.\n\n- Занятие чем-то приятным: Даже если не хочется, заставь себя сделать что-то, что раньше приносило удовольствие.\n\n- Творчество: Вырази свои чувства через искусство (рисование, музыка, писательство).\n\n- Помощь другим: Помощь кому-то другому может помочь почувствовать себя лучше.\n\n- Прогулка на природе: Свежий воздух и природа могут поднять настроение."
         markup = types.InlineKeyboardMarkup()
         button_sure11 = types.InlineKeyboardButton(text='Да, это про меня! Спасибо за советы!', callback_data='yes33')
         markup.add(button_sure11)
         button_no12 = types.InlineKeyboardButton(text='Нет, не совсем.', callback_data='yes34')
         markup.add(button_no12)
         botTimeWeb.send_message(function_call2.message.chat.id, thrt_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes33":
         fourteen_mess = "В таком случае получай картинку из телеграмм-канала нашего проекта!\n\nhttps://t.me/pcycologi/6\n\nНадеемся, что мы тебе помогли!\n\nСпасибо за разговор, друг!\n\nДо новых встреч 🤍"
         botTimeWeb.send_message(function_call2.message.chat.id, fourteen_mess, parse_mode='html')
      if function_call2.data == "yes34":
         fifteen_mess = "Не отчаивайся, ведь всегда можно вернуться в меню и выбрать для себя подходяшую категорию!\n\nЕсли ты всё-таки ничего не нашел, не расстраивайся!\nМы подготовили для тебя милую картинку из телеграмм-канала нашего проекта!\n\nhttps://t.me/pcycologi/6\n\nНадеемся, что мы тебе помогли!\n\nСпасибо за разговор, друг!\n\nДо новых встреч 🤍"
         botTimeWeb.send_message(function_call2.message.chat.id, fifteen_mess, parse_mode='html')


      #ТРЕВОГА
      if function_call2.data == "yes9":
         sixteen_mess = "😉 Вы выбрали тип состояния «Тревога»\n\n«Тревога» - Беспокойство, напряжение, ощущение опасности.\n\nСпособы решения проблемы 👇\n\n- Дыхательные упражнения: Глубокое дыхание помогает успокоиться.\n\n- Медитация: Даже 5-10 минут медитации могут помочь снизить тревогу.\n\n- Заземление: Сосредоточься на настоящем моменте. Опиши, что видишь, слышишь, чувствуешь.\n\n- Физическая активность: Тревога часто связана с физическим напряжением.\n\n- Ограничение кофеина: Кофеин может усиливать тревогу.\n\n- Планирование: Если тревога связана с конкретной ситуацией, составь план действий."
         markup = types.InlineKeyboardMarkup()
         button_sure16 = types.InlineKeyboardButton(text='Да, это про меня! Cпасибо за советы!', callback_data='yes37')
         markup.add(button_sure16)
         button_no17 = types.InlineKeyboardButton(text='Нет, не совсем.', callback_data='yes38')
         markup.add(button_no17)
         botTimeWeb.send_message(function_call2.message.chat.id, sixteen_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes37":
         seventeen_mess = "В таком случае получай картинку из телеграмм-канала нашего проекта!\n\nhttps://t.me/pcycologi/7\n\nНадеемся, что мы тебе помогли!\n\nСпасибо за разговор, друг!\n\nДо новых встреч 🤍"
         botTimeWeb.send_message(function_call2.message.chat.id, seventeen_mess, parse_mode='html')
      if function_call2.data == "yes38":
         eighteen_mess = "Не отчаивайся, ведь всегда можно вернуться в меню и выбрать для себя подходяшую категорию!\n\nЕсли ты всё-таки ничего не нашел, не расстраивайся!\nМы подготовили для тебя милую картинку из телеграмм-канала нашего проекта!\n\nhttps://t.me/pcycologi/7\n\nНадеемся, что мы тебе помогли!\n\nСпасибо за разговор, друг!\n\nДо новых встреч 🤍"
         botTimeWeb.send_message(function_call2.message.chat.id, eighteen_mess, parse_mode='html')


      #ЗЛОСТЬ
      if function_call2.data == "yes10":
         nineyeen_mess = "😉 Вы выбрали тип состояния «Злость»\n\n«Злость» - cильное раздражение, гнев, ярость.\n\nСпособы решения проблемы 👇\n\n- Тайм-аут: Уйди из ситуации, которая вызывает злость.\n\n- Физическая активность: Выплесни злость через спорт, танцы или другие физические упражнения.\n\n- Дыхательные упражнения: Глубокое дыхание помогает успокоиться.\n\n- Выразить злость конструктивно: Напиши письмо, поговори с кем-то, вырази свои чувства словами, а не действиями.\n\n- Избегай триггеров: Постарайся избегать ситуаций, которые обычно вызывают у тебя злость.\n\n"
         markup = types.InlineKeyboardMarkup()
         button_sure16 = types.InlineKeyboardButton(text='Да, это про меня! Cпасибо за советы!', callback_data='yes41')
         markup.add(button_sure16)
         button_no17 = types.InlineKeyboardButton(text='Нет, не совсем.', callback_data='yes42')
         markup.add(button_no17)
         botTimeWeb.send_message(function_call2.message.chat.id, nineyeen_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes41":
         twony_mess = "В таком случае получай картинку из телеграмм-канала нашего проекта!\n\nhttps://t.me/pcycologi/9\n\nНадеемся, что мы тебе помогли!\n\nСпасибо за разговор, друг!\n\nДо новых встреч 🤍"
         botTimeWeb.send_message(function_call2.message.chat.id, twony_mess, parse_mode='html')
      if function_call2.data == "yes42":
         twony1_mess = "Не отчаивайся, ведь всегда можно вернуться в меню и выбрать для себя подходяшую категорию!\n\nЕсли ты всё-таки ничего не нашел, не расстраивайся!\nМы подготовили для тебя милую картинку из телеграмм-канала нашего проекта!\n\nhttps://t.me/pcycologi/9\n\nНадеемся, что мы тебе помогли!\n\nСпасибо за разговор, друг!\n\nДо новых встреч 🤍"
         botTimeWeb.send_message(function_call2.message.chat.id, twony1_mess, parse_mode='html')


      #ОТЧАЯНИЕ
      if function_call2.data == "yes11":
         twony2_mess = "😉 Вы выбрали тип состояния «Отчаяние»\n\n«Отчаяние» - глубокая печаль, безнадёжность, потеря веры в себя.\n\nСпособы решения проблемы 👇\n\n- Обратиться за помощью: Это критически важно. Поговори с родителями, друзьями, учителем, психологом. Не оставайся один на один со своими чувствами.\n\n- Не принимать важных решений: В состоянии отчаяния легко совершить ошибки.\n\n- Помни, что это временно: Даже самые трудные времена проходят.\n\n- Сосредоточься на малых шагах: Не пытайся решить все проблемы сразу. Начни с малого."
         markup = types.InlineKeyboardMarkup()
         button_sure20 = types.InlineKeyboardButton(text='Да, это про меня! Спасибо за советы!', callback_data='yes45')
         markup.add(button_sure20)
         button_no21 = types.InlineKeyboardButton(text='Нет, не совсем.', callback_data='yes46')
         markup.add(button_no21)
         botTimeWeb.send_message(function_call2.message.chat.id, twony2_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes45":
         twony3_mess = "В таком случае получай картинку из телеграмм-канала нашего проекта!\n\nhttps://t.me/pcycologi/10\n\nНадеемся, что мы тебе помогли!\n\nСпасибо за разговор, друг!\n\nДо новых встреч 🤍"
         botTimeWeb.send_message(function_call2.message.chat.id, twony3_mess, parse_mode='html')
      if function_call2.data == "yes46":
         twony4_mess = "Не отчаивайся, ведь всегда можно вернуться в меню и выбрать для себя подходяшую категорию!\n\nЕсли ты всё-таки ничего не нашел, не расстраивайся!\nМы подготовили для тебя милую картинку из телеграмм-канала нашего проекта!\n\nhttps://t.me/pcycologi/10\n\nНадеемся, что мы тебе помогли!\n\nСпасибо за разговор, друг!\n\nДо новых встреч 🤍"
         botTimeWeb.send_message(function_call2.message.chat.id, twony4_mess, parse_mode='html')


      #ОПУСТОШЕНИЕ
      if function_call2.data == "yes12":
         twony5_mess = "😉 Вы выбрали тип состояния «Опустошение»\n\n«Опустошение» - отсутствие эмоций, чувство «пустоты» внутри.\n\nСпособы решения проблемы 👇\n\n- Обратиться за помощью: Важно обратиться к специалисту, чтобы разобраться в причинах опустошения.\n\n- Вернуть чувства: Попробуй заняться чем-то, что раньше приносило удовольствие.\n\n- Новые впечатления: Путешествия, новые хобби, общение с новыми людьми.\n\n- Осознанность: Попробуй осознанно ощущать мир вокруг себя (запахи, звуки, вкусы).\n\n- Забота о себе: Полноценный сон, здоровое питание, физическая активность."
         markup = types.InlineKeyboardMarkup()
         button_sure23 = types.InlineKeyboardButton(text='Да, это про меня! Спасибо за советы!', callback_data='yes49')
         markup.add(button_sure23)
         button_no21 = types.InlineKeyboardButton(text='Нет, не совсем.', callback_data='yes50')
         markup.add(button_no21)
         botTimeWeb.send_message(function_call2.message.chat.id, twony5_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes49":
         twony6_mess = "В таком случае получай картинку из телеграмм-канала нашего проекта!\n\nhttps://t.me/pcycologi/11\n\nНадеемся, что мы тебе помогли!\n\nСпасибо за разговор, друг!\n\nДо новых встреч 🤍"
         botTimeWeb.send_message(function_call2.message.chat.id, twony6_mess, parse_mode='html')
      if function_call2.data == "yes50":
         twony7_mess = "Не отчаивайся, ведь всегда можно вернуться в меню и выбрать для себя подходяшую категорию!\n\nЕсли ты всё-таки ничего не нашел, не расстраивайся!\nМы подготовили для тебя милую картинку из телеграмм-канала нашего проекта!\n\nhttps://t.me/pcycologi/11\n\nНадеемся, что мы тебе помогли!\n\nСпасибо за разговор, друг!\n\nДо новых встреч 🤍"
         botTimeWeb.send_message(function_call2.message.chat.id, twony7_mess, parse_mode='html')







      #поположительным

      #Просто Нормально

      if function_call2.data == "yes13":
         seven_mess = "Ляляля трополя *пояснение типа состояния*\nВаше моральное состояние совпадает с утверждениями выше?"
         markup = types.InlineKeyboardMarkup()
         button_sure = types.InlineKeyboardButton(text='Да, это про меня!', callback_data='yes53')
         markup.add(button_sure)
         button_no = types.InlineKeyboardButton(text='Нет, не совсем.', callback_data='yes54')
         markup.add(button_no)
         botTimeWeb.send_message(function_call2.message.chat.id, seven_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes53":
         eight_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure2 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes23')
         markup.add(button_sure2)
         botTimeWeb.send_message(function_call2.message.chat.id, eight_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes54":
         nine_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure3 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes24')
         markup.add(button_sure3)
         botTimeWeb.send_message(function_call2.message.chat.id, nine_mess, parse_mode='html', reply_markup=markup)




      if function_call2.data == "yes14":
         seven_mess = "Ляляля трополя *пояснение типа состояния*\nВаше моральное состояние совпадает с утверждениями выше?"
         markup = types.InlineKeyboardMarkup()
         button_sure4 = types.InlineKeyboardButton(text='Да, это про меня!', callback_data='yes55')
         markup.add(button_sure4)
         button_no4 = types.InlineKeyboardButton(text='Нет, не совсем.', callback_data='yes56')
         markup.add(button_no4)
         botTimeWeb.send_message(function_call2.message.chat.id, seven_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes55":
         eight_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure5 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes27')
         markup.add(button_sure5)
         botTimeWeb.send_message(function_call2.message.chat.id, eight_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes56":
         nine_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure6 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes28')
         markup.add(button_sure6)
         botTimeWeb.send_message(function_call2.message.chat.id, nine_mess, parse_mode='html', reply_markup=markup)



      if function_call2.data == "yes15":
         ten_mess = "Ляляля трополя *пояснение типа состояния*\nВаше моральное состояние совпадает с утверждениями выше?"
         markup = types.InlineKeyboardMarkup()
         button_sure7 = types.InlineKeyboardButton(text='Да, это про меня!', callback_data='yes57')
         markup.add(button_sure7)
         button_no8 = types.InlineKeyboardButton(text='Нет, не совсем.', callback_data='yes58')
         markup.add(button_no8)
         botTimeWeb.send_message(function_call2.message.chat.id, ten_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes57":
         elvn_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure9 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes31')
         markup.add(button_sure9)
         botTimeWeb.send_message(function_call2.message.chat.id, elvn_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes58":
         tw_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure10 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes32')
         markup.add(button_sure10)
         botTimeWeb.send_message(function_call2.message.chat.id, tw_mess, parse_mode='html', reply_markup=markup)



      if function_call2.data == "yes16":
         thrt_mess = "Ляляля трополя *пояснение типа состояния*\nВаше моральное состояние совпадает с утверждениями выше?"
         markup = types.InlineKeyboardMarkup()
         button_sure11 = types.InlineKeyboardButton(text='Да, это про меня!', callback_data='yes59')
         markup.add(button_sure11)
         button_no12 = types.InlineKeyboardButton(text='Нет, не совсем.', callback_data='yes60')
         markup.add(button_no12)
         botTimeWeb.send_message(function_call2.message.chat.id, thrt_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes59":
         fourteen_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure13 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes35')
         markup.add(button_sure13)
         botTimeWeb.send_message(function_call2.message.chat.id, fourteen_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes60":
         fifteen_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure14 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes36')
         markup.add(button_sure14)
         botTimeWeb.send_message(function_call2.message.chat.id, fifteen_mess, parse_mode='html', reply_markup=markup)


      if function_call2.data == "yes17":
         sixteen_mess = "Ляляля трополя *пояснение типа состояния*\nВаше моральное состояние совпадает с утверждениями выше?"
         markup = types.InlineKeyboardMarkup()
         button_sure16 = types.InlineKeyboardButton(text='Да, это про меня!', callback_data='yes61')
         markup.add(button_sure16)
         button_no17 = types.InlineKeyboardButton(text='Нет, не совсем.', callback_data='yes62')
         markup.add(button_no17)
         botTimeWeb.send_message(function_call2.message.chat.id, sixteen_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes61":
         seventeen_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure18 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes39')
         markup.add(button_sure18)
         botTimeWeb.send_message(function_call2.message.chat.id, seventeen_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes62":
         eighteen_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure19 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes40')
         markup.add(button_sure19)
         botTimeWeb.send_message(function_call2.message.chat.id, eighteen_mess, parse_mode='html', reply_markup=markup)


      if function_call2.data == "yes18":
         nineyeen_mess = "Ляляля трополя *пояснение типа состояния*\nВаше моральное состояние совпадает с утверждениями выше?"
         markup = types.InlineKeyboardMarkup()
         button_sure16 = types.InlineKeyboardButton(text='Да, это про меня!', callback_data='yes63')
         markup.add(button_sure16)
         button_no17 = types.InlineKeyboardButton(text='Нет, не совсем.', callback_data='yes64')
         markup.add(button_no17)
         botTimeWeb.send_message(function_call2.message.chat.id, nineyeen_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes63":
         twony_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure18 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes43')
         markup.add(button_sure18)
         botTimeWeb.send_message(function_call2.message.chat.id, twony_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes64":
         twony1_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure19 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes44')
         markup.add(button_sure19)
         botTimeWeb.send_message(function_call2.message.chat.id, twony1_mess, parse_mode='html', reply_markup=markup)


      if function_call2.data == "yes19":
         twony2_mess = "Ляляля трополя *пояснение типа состояния*\nВаше моральное состояние совпадает с утверждениями выше?"
         markup = types.InlineKeyboardMarkup()
         button_sure20 = types.InlineKeyboardButton(text='Да, это про меня!', callback_data='yes65')
         markup.add(button_sure20)
         button_no21 = types.InlineKeyboardButton(text='Нет, не совсем.', callback_data='yes66')
         markup.add(button_no21)
         botTimeWeb.send_message(function_call2.message.chat.id, twony2_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes65":
         twony3_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure21 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes47')
         markup.add(button_sure21)
         botTimeWeb.send_message(function_call2.message.chat.id, twony3_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes66":
         twony4_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure22 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes48')
         markup.add(button_sure22)
         botTimeWeb.send_message(function_call2.message.chat.id, twony4_mess, parse_mode='html', reply_markup=markup)


      if function_call2.data == "yes20":
         twony5_mess = "Ляляля трополя *пояснение типа состояния*\nВаше моральное состояние совпадает с утверждениями выше?"
         markup = types.InlineKeyboardMarkup()
         button_sure23 = types.InlineKeyboardButton(text='Да, это про меня!', callback_data='yes67')
         markup.add(button_sure23)
         button_no21 = types.InlineKeyboardButton(text='Нет, не совсем.', callback_data='yes68')
         markup.add(button_no21)
         botTimeWeb.send_message(function_call2.message.chat.id, twony5_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes67":
         twony6_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure24 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes47')
         markup.add(button_sure24)
         botTimeWeb.send_message(function_call2.message.chat.id, twony6_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes68":
         twony7_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure25 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes48')
         markup.add(button_sure25)
         botTimeWeb.send_message(function_call2.message.chat.id, twony7_mess, parse_mode='html', reply_markup=markup)


botTimeWeb.polling(none_stop=True)