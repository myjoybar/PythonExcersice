#!/usr/bin/python3
import requests
import os
import requests
from bs4 import BeautifulSoup


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}

amountGetMetaSuccess = 0
def getMetaInfo(url,html):
    soup = BeautifulSoup(html,'html.parser')
    #print('soup' + soup.prettify())
    # print('soup' + soup.head.string)
    if url.endswith('a/') or url.endswith('b/') or url.endswith('c/') or url.endswith('d/') or url.endswith('e/'):
        description = soup.find(attrs={"name": "description"})['content'].strip()
    if url.endswith('f/') or url.endswith('g/') or url.endswith('h/') or url.endswith('i/') or url.endswith('j/'):
        description = soup.find(attrs={"property": "og:description"})['content'].strip()
    #print('description=' + description)
    title = soup.find(attrs={"property": "og:title"})['content'].strip()
    # print('title=' + title)
    image = soup.find(attrs={"property": "og:image"})['content'].strip()
    #print('image=' + image)

    site_name = soup.find(attrs={"property": "og:site_name"})['content'].strip()
    #print('site_name=' + site_name)

    url = soup.find(attrs={"property": "og:url"})['content'].strip()
    # print('url=' + url)
    type = soup.find(attrs={"property": "og:type"})['content'].strip()
    # print('type=' + type)
    flag = False
    if 'ff' in url:
        # cn
        if 'cn' in url:
            if url.endswith('a/'):
                if description == '让你爱上一种全新的沟通方式！电话短信统统免费，立即体验！'.strip() and title == '说道免费电话'.strip() and image == 'http://resource.talkyou.me/images/share/cn/share_0.png' and url == 'http://talkyou.me/iv/ff/cn/a/' and type == 'article':
                    flag = True
            if url.endswith('b/'):
                if description == '这里有免费电话，免费短信，还有海量全球号码，快来一探究竟！'.strip() and title == '说道免费电话'.strip() and image == 'http://resource.talkyou.me/images/share/cn/share_1.png' and url == 'http://talkyou.me/iv/ff/cn/b/' and type == 'article':
                    flag = True
            if url.endswith('c/'):
                if description == '这是一个功能强大的APP，国内国际间电话及短信统统免费，快来省下你的话费！'.strip() and title == '说道国际电话及国际短信'.strip() and image == 'http://resource.talkyou.me/images/share/cn/share_2.png' and url == 'http://talkyou.me/iv/ff/cn/c/' and type == 'article':
                    flag = True
            if url.endswith('d/'):
                if description == '不用去营业厅，不用在网上买号，说道有百万全球号码，总有一个是你喜欢的！'.strip() and title == '说道海量国际号码'.strip() and image == 'http://resource.talkyou.me/images/share/cn/share_3.png' and url == 'http://talkyou.me/iv/ff/cn/d/' and type == 'article':
                    flag = True
            if url.endswith('e/'):
                if description == '你可以在这里发短信，打电话，好友之间完全免费，无限量！试一下？'.strip() and title == '说道免费电话及短信'.strip() and image == 'http://resource.talkyou.me/images/share/cn/share_4.png' and url == 'http://talkyou.me/iv/ff/cn/e/' and type == 'article':
                    flag = True
        # cnt
        if 'cnt' in url:
            if url.endswith('a/'):
                if description == '讓你愛上一種新的溝通方式！電話簡訊統統免費，立即體驗！ '.strip() and title == '說道免費電話'.strip() and image == 'http://resource.talkyou.me/images/share/cnt/share_0.png' and url == 'http://talkyou.me/iv/ff/cnt/a/' and type == 'article':
                    flag = True
            if url.endswith('b/'):
                if description == '這裡有免費電話，免費簡訊，還有海量全球號碼，快來一探究竟！'.strip() and title == '說道免費電話'.strip() and image == 'http://resource.talkyou.me/images/share/cnt/share_1.png' and url == 'http://talkyou.me/iv/ff/cnt/b/' and type == 'article':
                    flag = True
            if url.endswith('c/'):
                if description == '這是一個功能強大的APP，國內國際間電話及簡訊統統免費，快來省下你的話費！'.strip() and title == '說道國際電話及國際簡訊'.strip() and image == 'http://resource.talkyou.me/images/share/cnt/share_2.png' and url == 'http://talkyou.me/iv/ff/cnt/c/' and type == 'article':
                    flag = True
            if url.endswith('d/'):
                if description == '說道擁有百萬全球號碼，總有一個是你喜歡的！'.strip() and title == '說道海量國際號碼' and image == 'http://resource.talkyou.me/images/share/cnt/share_3.png' and url == 'http://talkyou.me/iv/ff/cnt/d/' and type == 'article':
                    flag = True
            if url.endswith('e/'):
                if description == '你可以在這裡發簡訊，打電話，好友之間完全免費，無限量！試一下？'.strip() and title == '說道免費電話及簡訊'.strip() and image == 'http://resource.talkyou.me/images/share/cnt/share_4.png' and url == 'http://talkyou.me/iv/ff/cnt/e/' and type == 'article':
                   flag = True
        # en
        if 'en' in url:
            if url.endswith('a/'):
                if description == 'Join TalkU to enjoy free calls and texts, you will like it. '.strip() and title == 'Free Calls & Free Texts'.strip() and image == 'http://resource.talkyou.me/images/share/en/share_0.png' and url == 'http://talkyou.me/iv/ff/en/a/' and type == 'article':
                    flag = True
            if url.endswith('b/'):
                if description == 'Free calling, free texting! Enjoy the free service with family & friends. '.strip() and title == 'Enjoy Free Calls'.strip() and image == 'http://resource.talkyou.me/images/share/en/share_1.png' and url == 'http://talkyou.me/iv/ff/en/b/' and type == 'article':
                    flag = True
            if url.endswith('c/'):
                if description == 'Send unlimted free texts everyday to any phone number. Text with fun! '.strip() and title == 'Text to Any Number'.strip() and image == 'http://resource.talkyou.me/images/share/en/share_2.png' and url == 'http://talkyou.me/iv/ff/en/c/' and type == 'article':
                    flag = True
            if url.endswith('d/'):
                if description == 'A free second phone number, millions of global numbers, find YOUR number in TalkU. '.strip() and title == 'Get a 2nd Line' and image == 'http://resource.talkyou.me/images/share/en/share_3.png' and url == 'http://talkyou.me/iv/ff/en/d/' and type == 'article':
                    flag = True
            if url.endswith('e/'):
                if description == 'Join TalkU now for free phone calls & free texts, even internationally!'.strip() and title == 'Free International Calls'.strip() and image == 'http://resource.talkyou.me/images/share/en/share_4.png' and url == 'http://talkyou.me/iv/ff/en/e/' and type == 'article':
                   flag = True
        # es
        if 'es' in url:
            if url.endswith('a/'):
                if description == 'Únete a TalkU para que disfrutes de llamadas y textos gratis, te va a gustar.  '.strip() and title == 'Llamadas y Textos Gratis'.strip() and image == 'http://resource.talkyou.me/images/share/es/share_0.png' and url == 'http://talkyou.me/iv/ff/es/a/' and type == 'article':
                    flag = True
            if url.endswith('b/'):
                if description == 'Llamar gratis, enviar textos gratis! Disfruta de este servicio gratuito con tu familia y amigos.'.strip() and title == 'Disfruta de Llamadas Gratis'.strip() and image == 'http://resource.talkyou.me/images/share/es/share_1.png' and url == 'http://talkyou.me/iv/ff/es/b/' and type == 'article':
                    flag = True
            if url.endswith('c/'):
                if description == 'Envía textos gratis ilimitados cada día a cualquier número de teléfono. Diviértete enviando textos!'.strip() and title == 'Textos a Cualquier Número'.strip() and image == 'http://resource.talkyou.me/images/share/es/share_2.png' and url == 'http://talkyou.me/iv/ff/es/c/' and type == 'article':
                    flag = True
            if url.endswith('d/'):
                if description == 'Una segunda línea telefónica gratuita, millones de números globales, encuentra TU número en TalkU'.strip() and title == 'Obtén una 2da Línea' and image == 'http://resource.talkyou.me/images/share/es/share_3.png' and url == 'http://talkyou.me/iv/ff/es/d/' and type == 'article':
                    flag = True
            if url.endswith('e/'):
                if description == 'Únete a TalkU para hacer llamadas y enviar textos gratis, incluso internacionales. '.strip() and title == 'Llamar y Enviar Textos Gratis'.strip() and image == 'http://resource.talkyou.me/images/share/es/share_4.png' and url == 'http://talkyou.me/iv/ff/es/e/' and type == 'article':
                   flag = True

        # fr
        if 'fr' in url:
            if url.endswith('a/'):
                if description == 'Rejoignez TalkU pour profiter d\'appels et SMS gratuits. Vous allez aimer.  '.strip() and title == 'Appels et SMS gratuits'.strip() and image == 'http://resource.talkyou.me/images/share/fr/share_0.png' and url == 'http://talkyou.me/iv/ff/fr/a/' and type == 'article':
                    flag = True
            if url.endswith('b/'):
                if description == 'Appels et SMS gratuits ! Profitez de ce service gratuit avec votre famille et vos amis. '.strip() and title == 'Profitez d\'appels gratuits  '.strip() and image == 'http://resource.talkyou.me/images/share/fr/share_1.png' and url == 'http://talkyou.me/iv/ff/fr/b/' and type == 'article':
                    flag = True
            if url.endswith('c/'):
                if description == 'Envoyez tous les jours des SMS gratuits et illimités vers n\'importe quel numéro. Faites-vous plaisir ! '.strip() and title == 'SMS vers n\'importe quel numéro'.strip() and image == 'http://resource.talkyou.me/images/share/fr/share_2.png' and url == 'http://talkyou.me/iv/ff/fr/c/' and type == 'article':
                    flag = True
            if url.endswith('d/'):
                if description == 'Un deuxième numéro de téléphone gratuit, des millions de numéros à l\'international, trouvez VOTRE numéro dans TalkU. '.strip() and title == 'Obtenez une 2e ligne' and image == 'http://resource.talkyou.me/images/share/fr/share_3.png' and url == 'http://talkyou.me/iv/ff/fr/d/' and type == 'article':
                    flag = True
            if url.endswith('e/'):
                if description == 'Rejoignez TalkU pour profiter d\'appels et SMS gratuits, même à l\'international !'.strip() and title == ' Appels et SMS gratuits'.strip() and image == 'http://resource.talkyou.me/images/share/fr/share_4.png' and url == 'http://talkyou.me/iv/ff/fr/e/' and type == 'article':
                   flag = True
        # pt
        if 'pt' in url:
            if url.endswith('a/'):
                if description == 'Cadastre-se no TalkU e faça ligações e SMS de graça - você vai adorar. '.strip() and title == 'Telefonemas & SMS Grátis'.strip() and image == 'http://resource.talkyou.me/images/share/pt/share_0.png' and url == 'http://talkyou.me/iv/ff/pt/a/' and type == 'article':
                    flag = True
            if url.endswith('b/'):
                if description == 'Llamar gratis, enviar textos gratis! Disfruta de este servicio gratuito con tu familia y amigos.'.strip() and title == 'Faça Ligações Gratuitas'.strip() and image == 'http://resource.talkyou.me/images/share/pt/share_1.png' and url == 'http://talkyou.me/iv/ff/pt/b/' and type == 'article':
                    flag = True
            if url.endswith('c/'):
                if description == 'Envie mensagens de textos ilimitadas todos os dias para qualquer número de telefone. Divirta-se enviando textos!'.strip() and title == 'Envie Mensagens para Qualquer Número'.strip() and image == 'http://resource.talkyou.me/images/share/pt/share_2.png' and url == 'http://talkyou.me/iv/ff/pt/c/' and type == 'article':
                    flag = True
            if url.endswith('d/'):
                if description == 'Um número de telefone adicional, milhares de números internacionais, encontre o SEU no TalkU.'.strip() and title == 'Tenha uma 2ª Linha' and image == 'http://resource.talkyou.me/images/share/pt/share_3.png' and url == 'http://talkyou.me/iv/ff/pt/d/' and type == 'article':
                    flag = True
            if url.endswith('e/'):
                if description == 'Cadastre-se no TalkU agora para ligações telefônicas e mensagens de texto grátis, mesmo internacionais!'.strip() and title == 'Ligações e SMS Grátis'.strip() and image == 'http://resource.talkyou.me/images/share/pt/share_4.png' and url == 'http://talkyou.me/iv/ff/pt/e/' and type == 'article':
                   flag = True

        # tr
        if 'tr' in url:
            if url.endswith('a/'):
                if description == 'Ücretsiz çağrı ve sms keyfini sürmek için TalkU\'a katılın, seveceksiniz. '.strip() and title == 'Ücretsiz Çağrı ve SMS'.strip() and image == 'http://resource.talkyou.me/images/share/tr/share_0.png' and url == 'http://talkyou.me/iv/ff/tr/a/' and type == 'article':
                    flag = True
            if url.endswith('b/'):
                if description == 'Ücretsiz arama, ücretsiz sms! Ailenizle, dostlarınızla bu ücretsiz servisin keyfini sürün.'.strip() and title == 'Ücretsiz Çağrının Keyfi Sür'.strip() and image == 'http://resource.talkyou.me/images/share/tr/share_1.png' and url == 'http://talkyou.me/iv/ff/tr/b/' and type == 'article':
                    flag = True
            if url.endswith('c/'):
                if description == 'Her gün, her cep telefonuna sınırsız sayıda SMS gönderin. Mesajla Eğlenin!'.strip() and title == 'Her Telefona SMS Çekin'.strip() and image == 'http://resource.talkyou.me/images/share/tr/share_2.png' and url == 'http://talkyou.me/iv/ff/tr/c/' and type == 'article':
                    flag = True
            if url.endswith('d/'):
                if description == 'Ücretsiz bir ikinci hat edinin, milyonlarca küresel numara, TalkU\'da KENDİ numaranızı bulun.'.strip() and title == 'İkinci bir hat edinin' and image == 'http://resource.talkyou.me/images/share/tr/share_3.png' and url == 'http://talkyou.me/iv/ff/tr/d/' and type == 'article':
                    flag = True
            if url.endswith('e/'):
                if description == 'Şimdi TalkU\'a katılın, ücretsiz çağrı yapın ve SMS gönderin, uluslararası da dahil!'.strip() and title == 'Ücretsiz Arama ve SMS'.strip() and image == 'http://resource.talkyou.me/images/share/tr/share_4.png' and url == 'http://talkyou.me/iv/ff/tr/e/' and type == 'article':
                   flag = True
#========================
    if 'fm' in url:
        # cn
        if 'cn' in url:
            if url.endswith('a/'):
                if description == '让你爱上一种全新的沟通方式！电话短信统统免费，立即体验！'.strip() and title == '说道免费电话'.strip() and image == 'http://resource.talkyou.me/images/share/cn/share_0.png' and url == 'http://talkyou.me/iv/fm/cn/a/' and type == 'article':
                    flag = True
            if url.endswith('b/'):
                if description == '这里有免费电话，免费短信，还有海量全球号码，快来一探究竟！'.strip() and title == '说道免费电话'.strip() and image == 'http://resource.talkyou.me/images/share/cn/share_1.png' and url == 'http://talkyou.me/iv/fm/cn/b/' and type == 'article':
                    flag = True
            if url.endswith('c/'):
                if description == '这是一个功能强大的APP，国内国际间电话及短信统统免费，快来省下你的话费！'.strip() and title == '说道国际电话及国际短信'.strip() and image == 'http://resource.talkyou.me/images/share/cn/share_2.png' and url == 'http://talkyou.me/iv/fm/cn/c/' and type == 'article':
                    flag = True
            if url.endswith('d/'):
                if description == '不用去营业厅，不用在网上买号，说道有百万全球号码，总有一个是你喜欢的！'.strip() and title == '说道海量国际号码'.strip() and image == 'http://resource.talkyou.me/images/share/cn/share_3.png' and url == 'http://talkyou.me/iv/fm/cn/d/' and type == 'article':
                    flag = True
            if url.endswith('e/'):
                if description == '你可以在这里发短信，打电话，好友之间完全免费，无限量！试一下？'.strip() and title == '说道免费电话及短信'.strip() and image == 'http://resource.talkyou.me/images/share/cn/share_4.png' and url == 'http://talkyou.me/iv/fm/cn/e/' and type == 'article':
                    flag = True
        # cnt
        if 'cnt' in url:
            if url.endswith('a/'):
                if description == '讓你愛上一種新的溝通方式！電話簡訊統統免費，立即體驗！ '.strip() and title == '說道免費電話'.strip() and image == 'http://resource.talkyou.me/images/share/cnt/share_0.png' and url == 'http://talkyou.me/iv/fm/cnt/a/' and type == 'article':
                    flag = True
            if url.endswith('b/'):
                if description == '這裡有免費電話，免費簡訊，還有海量全球號碼，快來一探究竟！'.strip() and title == '說道免費電話'.strip() and image == 'http://resource.talkyou.me/images/share/cnt/share_1.png' and url == 'http://talkyou.me/iv/fm/cnt/b/' and type == 'article':
                    flag = True
            if url.endswith('c/'):
                if description == '這是一個功能強大的APP，國內國際間電話及簡訊統統免費，快來省下你的話費！'.strip() and title == '說道國際電話及國際簡訊'.strip() and image == 'http://resource.talkyou.me/images/share/cnt/share_2.png' and url == 'http://talkyou.me/iv/fm/cnt/c/' and type == 'article':
                    flag = True
            if url.endswith('d/'):
                if description == '說道擁有百萬全球號碼，總有一個是你喜歡的！'.strip() and title == '說道海量國際號碼' and image == 'http://resource.talkyou.me/images/share/cnt/share_3.png' and url == 'http://talkyou.me/iv/fm/cnt/d/' and type == 'article':
                    flag = True
            if url.endswith('e/'):
                if description == '你可以在這裡發簡訊，打電話，好友之間完全免費，無限量！試一下？'.strip() and title == '說道免費電話及簡訊'.strip() and image == 'http://resource.talkyou.me/images/share/cnt/share_4.png' and url == 'http://talkyou.me/iv/fm/cnt/e/' and type == 'article':
                    flag = True
        # en
        if 'en' in url:
            if url.endswith('a/'):
                if description == 'Join TalkU to enjoy free calls and texts, you will like it. '.strip() and title == 'Free Calls & Free Texts'.strip() and image == 'http://resource.talkyou.me/images/share/en/share_0.png' and url == 'http://talkyou.me/iv/fm/en/a/' and type == 'article':
                    flag = True
            if url.endswith('b/'):
                if description == 'Free calling, free texting! Enjoy the free service with family & friends. '.strip() and title == 'Enjoy Free Calls'.strip() and image == 'http://resource.talkyou.me/images/share/en/share_1.png' and url == 'http://talkyou.me/iv/fm/en/b/' and type == 'article':
                    flag = True
            if url.endswith('c/'):
                if description == 'Send unlimted free texts everyday to any phone number. Text with fun! '.strip() and title == 'Text to Any Number'.strip() and image == 'http://resource.talkyou.me/images/share/en/share_2.png' and url == 'http://talkyou.me/iv/fm/en/c/' and type == 'article':
                    flag = True
            if url.endswith('d/'):
                if description == 'A free second phone number, millions of global numbers, find YOUR number in TalkU. '.strip() and title == 'Get a 2nd Line' and image == 'http://resource.talkyou.me/images/share/en/share_3.png' and url == 'http://talkyou.me/iv/fm/en/d/' and type == 'article':
                    flag = True
            if url.endswith('e/'):
                if description == 'Join TalkU now for free phone calls & free texts, even internationally!'.strip() and title == 'Free International Calls'.strip() and image == 'http://resource.talkyou.me/images/share/en/share_4.png' and url == 'http://talkyou.me/iv/fm/en/e/' and type == 'article':
                    flag = True
        # es
        if 'es' in url:
            if url.endswith('a/'):
                if description == 'Únete a TalkU para que disfrutes de llamadas y textos gratis, te va a gustar.  '.strip() and title == 'Llamadas y Textos Gratis'.strip() and image == 'http://resource.talkyou.me/images/share/es/share_0.png' and url == 'http://talkyou.me/iv/fm/es/a/' and type == 'article':
                    flag = True
            if url.endswith('b/'):
                if description == 'Llamar gratis, enviar textos gratis! Disfruta de este servicio gratuito con tu familia y amigos.'.strip() and title == 'Disfruta de Llamadas Gratis'.strip() and image == 'http://resource.talkyou.me/images/share/es/share_1.png' and url == 'http://talkyou.me/iv/fm/es/b/' and type == 'article':
                    flag = True
            if url.endswith('c/'):
                if description == 'Envía textos gratis ilimitados cada día a cualquier número de teléfono. Diviértete enviando textos!'.strip() and title == 'Textos a Cualquier Número'.strip() and image == 'http://resource.talkyou.me/images/share/es/share_2.png' and url == 'http://talkyou.me/iv/fm/es/c/' and type == 'article':
                    flag = True
            if url.endswith('d/'):
                if description == 'Una segunda línea telefónica gratuita, millones de números globales, encuentra TU número en TalkU'.strip() and title == 'Obtén una 2da Línea' and image == 'http://resource.talkyou.me/images/share/es/share_3.png' and url == 'http://talkyou.me/iv/fm/es/d/' and type == 'article':
                    flag = True
            if url.endswith('e/'):
                if description == 'Únete a TalkU para hacer llamadas y enviar textos gratis, incluso internacionales. '.strip() and title == 'Llamar y Enviar Textos Gratis'.strip() and image == 'http://resource.talkyou.me/images/share/es/share_4.png' and url == 'http://talkyou.me/iv/fm/es/e/' and type == 'article':
                    flag = True

        # fr
        if 'fr' in url:
            if url.endswith('a/'):
                if description == 'Rejoignez TalkU pour profiter d\'appels et SMS gratuits. Vous allez aimer.  '.strip() and title == 'Appels et SMS gratuits'.strip() and image == 'http://resource.talkyou.me/images/share/fr/share_0.png' and url == 'http://talkyou.me/iv/fm/fr/a/' and type == 'article':
                    flag = True
            if url.endswith('b/'):
                if description == 'Appels et SMS gratuits ! Profitez de ce service gratuit avec votre famille et vos amis. '.strip() and title == 'Profitez d\'appels gratuits  '.strip() and image == 'http://resource.talkyou.me/images/share/fr/share_1.png' and url == 'http://talkyou.me/iv/fm/fr/b/' and type == 'article':
                    flag = True
            if url.endswith('c/'):
                if description == 'Envoyez tous les jours des SMS gratuits et illimités vers n\'importe quel numéro. Faites-vous plaisir ! '.strip() and title == 'SMS vers n\'importe quel numéro'.strip() and image == 'http://resource.talkyou.me/images/share/fr/share_2.png' and url == 'http://talkyou.me/iv/fm/fr/c/' and type == 'article':
                    flag = True
            if url.endswith('d/'):
                if description == 'Un deuxième numéro de téléphone gratuit, des millions de numéros à l\'international, trouvez VOTRE numéro dans TalkU. '.strip() and title == 'Obtenez une 2e ligne' and image == 'http://resource.talkyou.me/images/share/fr/share_3.png' and url == 'http://talkyou.me/iv/fm/fr/d/' and type == 'article':
                    flag = True
            if url.endswith('e/'):
                if description == 'Rejoignez TalkU pour profiter d\'appels et SMS gratuits, même à l\'international !'.strip() and title == ' Appels et SMS gratuits'.strip() and image == 'http://resource.talkyou.me/images/share/fr/share_4.png' and url == 'http://talkyou.me/iv/fm/fr/e/' and type == 'article':
                    flag = True
        # pt
        if 'pt' in url:
            if url.endswith('a/'):
                if description == 'Cadastre-se no TalkU e faça ligações e SMS de graça - você vai adorar. '.strip() and title == 'Telefonemas & SMS Grátis'.strip() and image == 'http://resource.talkyou.me/images/share/pt/share_0.png' and url == 'http://talkyou.me/iv/fm/pt/a/' and type == 'article':
                    flag = True
            if url.endswith('b/'):
                if description == 'Llamar gratis, enviar textos gratis! Disfruta de este servicio gratuito con tu familia y amigos.'.strip() and title == 'Faça Ligações Gratuitas'.strip() and image == 'http://resource.talkyou.me/images/share/pt/share_1.png' and url == 'http://talkyou.me/iv/fm/pt/b/' and type == 'article':
                    flag = True
            if url.endswith('c/'):
                if description == 'Envie mensagens de textos ilimitadas todos os dias para qualquer número de telefone. Divirta-se enviando textos!'.strip() and title == 'Envie Mensagens para Qualquer Número'.strip() and image == 'http://resource.talkyou.me/images/share/pt/share_2.png' and url == 'http://talkyou.me/iv/fm/pt/c/' and type == 'article':
                    flag = True
            if url.endswith('d/'):
                if description == 'Um número de telefone adicional, milhares de números internacionais, encontre o SEU no TalkU.'.strip() and title == 'Tenha uma 2ª Linha' and image == 'http://resource.talkyou.me/images/share/pt/share_3.png' and url == 'http://talkyou.me/iv/fm/pt/d/' and type == 'article':
                    flag = True
            if url.endswith('e/'):
                if description == 'Cadastre-se no TalkU agora para ligações telefônicas e mensagens de texto grátis, mesmo internacionais!'.strip() and title == 'Ligações e SMS Grátis'.strip() and image == 'http://resource.talkyou.me/images/share/pt/share_4.png' and url == 'http://talkyou.me/iv/fm/pt/e/' and type == 'article':
                    flag = True

        # tr
        if 'tr' in url:
            if url.endswith('a/'):
                if description == 'Ücretsiz çağrı ve sms keyfini sürmek için TalkU\'a katılın, seveceksiniz. '.strip() and title == 'Ücretsiz Çağrı ve SMS'.strip() and image == 'http://resource.talkyou.me/images/share/tr/share_0.png' and url == 'http://talkyou.me/iv/fm/tr/a/' and type == 'article':
                    flag = True
            if url.endswith('b/'):
                if description == 'Ücretsiz arama, ücretsiz sms! Ailenizle, dostlarınızla bu ücretsiz servisin keyfini sürün.'.strip() and title == 'Ücretsiz Çağrının Keyfi Sür'.strip() and image == 'http://resource.talkyou.me/images/share/tr/share_1.png' and url == 'http://talkyou.me/iv/fm/tr/b/' and type == 'article':
                    flag = True
            if url.endswith('c/'):
                if description == 'Her gün, her cep telefonuna sınırsız sayıda SMS gönderin. Mesajla Eğlenin!'.strip() and title == 'Her Telefona SMS Çekin'.strip() and image == 'http://resource.talkyou.me/images/share/tr/share_2.png' and url == 'http://talkyou.me/iv/fm/tr/c/' and type == 'article':
                    flag = True
            if url.endswith('d/'):
                if description == 'Ücretsiz bir ikinci hat edinin, milyonlarca küresel numara, TalkU\'da KENDİ numaranızı bulun.'.strip() and title == 'İkinci bir hat edinin' and image == 'http://resource.talkyou.me/images/share/tr/share_3.png' and url == 'http://talkyou.me/iv/fm/tr/d/' and type == 'article':
                    flag = True
            if url.endswith('e/'):
                if description == 'Şimdi TalkU\'a katılın, ücretsiz çağrı yapın ve SMS gönderin, uluslararası da dahil!'.strip() and title == 'Ücretsiz Arama ve SMS'.strip() and image == 'http://resource.talkyou.me/images/share/tr/share_4.png' and url == 'http://talkyou.me/iv/fm/tr/e/' and type == 'article':
                    flag = True
                    # ========================

    if 'fl' in url:
        # cn
        if 'cn' in url:
            if url.endswith('a/'):
                if description == '这里有免费电话，免费短信，还有海量全球号码，快来一探究竟！'.strip() and title == '说道免费电话'.strip() and image == 'http://resource.talkyou.me/images/share/app/TalkU.png' and url == 'http://talkyou.me/iv/fl/cn/a/' and type == 'article':
                    flag = True
        # cnt
        if 'cnt' in url:
            if url.endswith('a/'):
                if description == '這裡有免費電話，免費簡訊，還有海量全球號碼，快來一探究竟！'.strip() and title == '說道免費電話'.strip() and image == 'http://resource.talkyou.me/images/share/app/TalkU.png' and url == 'http://talkyou.me/iv/fl/cnt/a/' and type == 'article':
                    flag = True
        # en
        if 'en' in url:
            if url.endswith('a/'):
                if description == 'Free calling, free texting! Enjoy the free service with family & friends. '.strip() and title == 'Enjoy Free Calls'.strip() and image == 'http://resource.talkyou.me/images/share/app/TalkU.png' and url == 'http://talkyou.me/iv/fl/en/a/' and type == 'article':
                    flag = True
        # es
        if 'es' in url:
            if url.endswith('a/'):
                if description == 'Llamar gratis, enviar textos gratis! Disfruta de este servicio gratuito con tu familia y amigos.'.strip() and title == 'Disfruta de Llamadas Gratis'.strip() and image == 'http://resource.talkyou.me/images/share/app/TalkU.png' and url == 'http://talkyou.me/iv/fl/es/a/' and type == 'article':
                    flag = True

        # fr
        if 'fr' in url:
            if url.endswith('a/'):
                if description == 'Appels et SMS gratuits ! Profitez de ce service gratuit avec votre famille et vos amis. '.strip() and title == 'Profitez d\'appels gratuits  '.strip() and image == 'http://resource.talkyou.me/images/share/app/TalkU.png' and url == 'http://talkyou.me/iv/fl/fr/a/' and type == 'article':
                    flag = True
        # pt
        if 'pt' in url:
            if url.endswith('a/'):
                if description == 'Llamar gratis, enviar textos gratis! Disfruta de este servicio gratuito con tu familia y amigos.'.strip() and title == 'Faça Ligações Gratuitas'.strip() and image == 'http://resource.talkyou.me/images/share/app/TalkU.png' and url == 'http://talkyou.me/iv/fl/pt/a/' and type == 'article':
                    flag = True
        # tr
        if 'tr' in url:
            if url.endswith('a/'):
                if description == 'Ücretsiz arama, ücretsiz sms! Ailenizle, dostlarınızla bu ücretsiz servisin keyfini sürün.'.strip() and title == 'Ücretsiz Çağrının Keyfi Sür'.strip() and image == 'http://resource.talkyou.me/images/share/app/TalkU.png' and url == 'http://talkyou.me/iv/fl/tr/a/' and type == 'article':
                    flag = True
 # ========================
    if 'fwa' in url:
        # cn
        if 'cn' in url:
            if url.endswith('a/'):
                if description == '这里有免费电话，免费短信，还有海量全球号码，快来一探究竟！'.strip() and title == '说道免费电话'.strip() and image == 'http://resource.talkyou.me/images/share/app/TalkU.png' and url == 'http://talkyou.me/iv/fwa/cn/a/' and type == 'article':
                    flag = True
        # cnt
        if 'cnt' in url:
            if url.endswith('a/'):
                if description == '這裡有免費電話，免費簡訊，還有海量全球號碼，快來一探究竟！'.strip() and title == '說道免費電話'.strip() and image == 'http://resource.talkyou.me/images/share/app/TalkU.png' and url == 'http://talkyou.me/iv/fwa/cnt/a/' and type == 'article':
                    flag = True
        # en
        if 'en' in url:
            if url.endswith('a/'):
                if description == 'Free calling, free texting! Enjoy the free service with family & friends. '.strip() and title == 'Enjoy Free Calls'.strip() and image == 'http://resource.talkyou.me/images/share/app/TalkU.png' and url == 'http://talkyou.me/iv/fwa/en/a/' and type == 'article':
                    flag = True
        # es
        if 'es' in url:
            if url.endswith('a/'):
                if description == 'Llamar gratis, enviar textos gratis! Disfruta de este servicio gratuito con tu familia y amigos.'.strip() and title == 'Disfruta de Llamadas Gratis'.strip() and image == 'http://resource.talkyou.me/images/share/app/TalkU.png' and url == 'http://talkyou.me/iv/fwa/es/a/' and type == 'article':
                    flag = True

        # fr
        if 'fr' in url:
            if url.endswith('a/'):
                if description == 'Appels et SMS gratuits ! Profitez de ce service gratuit avec votre famille et vos amis. '.strip() and title == 'Profitez d\'appels gratuits  '.strip() and image == 'http://resource.talkyou.me/images/share/app/TalkU.png' and url == 'http://talkyou.me/iv/fwa/fr/a/' and type == 'article':
                    flag = True
        # pt
        if 'pt' in url:
            if url.endswith('a/'):
                if description == 'Llamar gratis, enviar textos gratis! Disfruta de este servicio gratuito con tu familia y amigos.'.strip() and title == 'Faça Ligações Gratuitas'.strip() and image == 'http://resource.talkyou.me/images/share/app/TalkU.png' and url == 'http://talkyou.me/iv/fwa/pt/a/' and type == 'article':
                    flag = True
        # tr
        if 'tr' in url:
            if url.endswith('a/'):
                if description == 'Ücretsiz arama, ücretsiz sms! Ailenizle, dostlarınızla bu ücretsiz servisin keyfini sürün.'.strip() and title == 'Ücretsiz Çağrının Keyfi Sür'.strip() and image == 'http://resource.talkyou.me/images/share/app/TalkU.png' and url == 'http://talkyou.me/iv/fwa/tr/a/' and type == 'article':
                    flag = True
                    # ========================

   #end
    global amountGetMetaSuccess
    if flag:
        amountGetMetaSuccess += 1
        print("meta 信息配置正确"+'\n')
    else:
        print('\033[5;31m meta 信息配置错误 \033[0m!'+'\n')

amount = 0
amountSuccess = 0
amountFailure = 0
def openUrl(url):
    try:
        global amount
        global amountSuccess
        global amountFailure
        response = requests.get(url, headers=headers, timeout=5)
        httpCode = response.status_code
        html = response.text
        amount += 1
        if httpCode == 200:
            amountSuccess += 1
            print(url + ':可打开')
            getMetaInfo(url, html)
        else:
            amountFailure += 1
            print(url + ':不可打开，' + str(httpCode))
    except Exception as e:
        print(e)


def readFile(filePath):
    for line in open(filePath):
        if line.startswith('http://talkyou.me/'):
            url = line.strip().replace('\r', '').replace('\n', '').replace('\t', '')
            openUrl(url)



filePath = './doc/TalkUUrl.txt'
readFile(filePath)

print("总共有：" + str(amount) +"个 URL")
print("成功" + str(amountSuccess) +"个 URL")
print("成功获取meta" + str(amountGetMetaSuccess) +"个 URL")
print("失败" + str(amountFailure) +"个 URL")
