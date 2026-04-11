#!/usr/bin/env python3
"""Generate localized support pages from a single template."""
import os

LANGS = {
    "de": {"file": "index.html", "dir": "ltr", "code": "de"},
    "en": {"file": "en.html", "dir": "ltr", "code": "en"},
    "fr": {"file": "fr.html", "dir": "ltr", "code": "fr"},
    "es": {"file": "es.html", "dir": "ltr", "code": "es"},
    "tr": {"file": "tr.html", "dir": "ltr", "code": "tr"},
    "uk": {"file": "uk.html", "dir": "ltr", "code": "uk"},
    "ar": {"file": "ar.html", "dir": "rtl", "code": "ar"},
    "pl": {"file": "pl.html", "dir": "ltr", "code": "pl"},
}

LANG_LABELS = {
    "de": "Deutsch",
    "en": "English",
    "fr": "Français",
    "es": "Español",
    "tr": "Türkçe",
    "uk": "Українська",
    "ar": "العربية",
    "pl": "Polski",
}

T = {
    "de": {
        "title": "SagWas – Support",
        "meta_desc": "Support, Hilfe und häufige Fragen zur iPad-App SagWas.",
        "tagline": "AAC-Kommunikations-App für iPad",
        "contact_note": "Kontakt: ",
        "about_h": "Über SagWas",
        "about_p": "SagWas ist eine Audio- und Kommunikations-App (AAC – Augmentative and Alternative Communication) für das iPad. Aufnahmen, Piktogramme, Fotos und Text-to-Speech lassen sich zu einfachen Sprach-Boards kombinieren. Verfügbar in acht Sprachen.",
        "start_h": "Erste Schritte",
        "start_button_h": "Button-Modus",
        "start_button_p": "Ein großer Sprechknopf füllt den Bildschirm. 3 Sekunden halten startet eine Aufnahme, tippen spielt sie ab. Über den Track-Switcher wechselst du zwischen bis zu 9 Spuren.",
        "start_talkpad_h": "TalkPad-Modus",
        "start_talkpad_p": "Ein Raster aus Kacheln auf mehreren Seiten. Jede Kachel kann Audio, Video, Foto, ARASAAC-Symbol und einen Text (der vorgelesen werden kann) enthalten.",
        "start_settings_h": "Einstellungen öffnen",
        "start_settings_p": "Auf das Zahnrad oben rechts tippen. Falls ein PIN gesetzt ist, diesen eingeben. Dort lassen sich Track-Anzahl, Farben, Fotos, Sprachen und TalkPad-Seiten konfigurieren.",
        "faq_h": "Häufige Fragen (FAQ)",
        "faqs": [
            ("Wie nehme ich eine neue Sprachnachricht auf?",
             "Im Button-Modus den großen Knopf 3 Sekunden gedrückt halten. Ein Countdown erscheint, dann startet die Aufnahme. Loslassen beendet die Aufnahme. Maximale Länge: 2 Minuten pro Track."),
            ("Wie teile ich einen Track oder eine Seite?",
             "In den Einstellungen auf „Teilen\" tippen. Du erhältst eine 6-stellige Share-ID. Auf dem Zielgerät unter „Empfangen\" eingeben – die Inhalte werden über Apple iCloud (CloudKit) synchronisiert. Ohne Internet wird der Upload in eine Warteschlange gelegt und später automatisch ausgeführt."),
            ("Warum hört sich die Text-to-Speech-Stimme roboterhaft an?",
             "iOS liefert für manche Sprachen nur Kompakt-Stimmen. Unter iOS-Einstellungen → Bedienungshilfen → Gesprochene Inhalte → Stimmen kannst du eine hochwertige Stimme herunterladen. SagWas verwendet diese automatisch."),
            ("Die Piktogramm-Suche zeigt keine Ergebnisse.",
             "Die Piktogramm-Suche nutzt die ARASAAC-API und benötigt eine Internetverbindung. Prüfe deine Verbindung und versuche andere Suchbegriffe."),
            ("Ich habe mein PIN vergessen.",
             "Deinstalliere die App und installiere sie neu. Achtung: Dabei gehen alle lokalen Aufnahmen verloren. Vorher ggf. Tracks oder Seiten über die Teilen-Funktion sichern."),
            ("Funktioniert SagWas auch auf dem iPhone?",
             "Ja, SagWas läuft auf iPhone und iPad ab iOS 17. Optimiert ist die App für das iPad (Portrait + Landscape). Auf dem iPhone ist nur Portrait-Modus verfügbar."),
            ("Wie importiere ich eine Audio-Datei?",
             "In den Einstellungen eines Tracks auf „Audio importieren\" tippen, .mp3/.m4a/.wav aus der Dateien-App auswählen und ggf. über den Trim-Editor Start- und Endpunkt festlegen."),
            ("Welche Daten sammelt die App?",
             "Keine. SagWas speichert alle Aufnahmen lokal. Geteilte Inhalte gehen ausschließlich über deinen eigenen iCloud-Account. Es gibt kein Tracking, keine Werbung, keine Analytics."),
        ],
        "contact_h": "Kontakt & Support",
        "contact_p1": "Bei Fragen, Fehlern oder Feedback schreib eine E-Mail an",
        "contact_p2": "Bitte gib iOS-Version, iPad-Modell und eine kurze Beschreibung des Problems an. Ich antworte in der Regel innerhalb von 48 Stunden.",
        "privacy_h": "Datenschutz",
        "privacy": [
            "Alle Aufnahmen werden lokal auf dem Gerät gespeichert.",
            "Geteilte Seiten werden verschlüsselt über Apple iCloud (CloudKit) übertragen.",
            "Es werden keine personenbezogenen Daten an Dritte weitergegeben.",
            "Die App enthält keine Werbung und kein Tracking.",
            "Piktogramme werden über die ARASAAC-API geladen (nur Bildsymbole, keine Nutzerdaten).",
        ],
        "privacy_full": "Vollständige Datenschutzerklärung",
    },
    "en": {
        "title": "SagWas – Support",
        "meta_desc": "Support, help and frequently asked questions for the iPad app SagWas.",
        "tagline": "AAC communication app for iPad",
        "contact_note": "Contact: ",
        "about_h": "About SagWas",
        "about_p": "SagWas is an audio and communication app (AAC – Augmentative and Alternative Communication) for iPad. Recordings, pictograms, photos and text-to-speech can be combined into simple communication boards. Available in eight languages.",
        "start_h": "Getting Started",
        "start_button_h": "Button Mode",
        "start_button_p": "A large speak button fills the screen. Hold for 3 seconds to start recording, tap to play. Use the track switcher to switch between up to 9 tracks.",
        "start_talkpad_h": "TalkPad Mode",
        "start_talkpad_p": "A grid of tiles across multiple pages. Each tile can hold audio, video, a photo, an ARASAAC symbol and a text label (with text-to-speech).",
        "start_settings_h": "Open Settings",
        "start_settings_p": "Tap the gear icon in the top right. If a PIN is set, enter it. From there you can configure the number of tracks, colors, photos, languages and TalkPad pages.",
        "faq_h": "Frequently Asked Questions",
        "faqs": [
            ("How do I record a new voice message?",
             "In Button Mode, press and hold the big button for 3 seconds. A countdown appears, then recording starts. Release to stop. Maximum length: 2 minutes per track."),
            ("How do I share a track or a page?",
             "In Settings tap \"Share\". You will receive a 6-digit Share-ID. On the target device, enter it under \"Receive\" – the content is synced via Apple iCloud (CloudKit). When offline, the upload is queued and sent automatically later."),
            ("Why does the text-to-speech voice sound robotic?",
             "iOS ships only compact voices for some languages. Under iOS Settings → Accessibility → Spoken Content → Voices you can download a high-quality voice. SagWas will use it automatically."),
            ("The pictogram search shows no results.",
             "The pictogram search uses the ARASAAC API and requires an internet connection. Check your connection and try different search terms."),
            ("I forgot my PIN.",
             "Uninstall and reinstall the app. Warning: this will delete all local recordings. Back up tracks or pages via the Share function first."),
            ("Does SagWas work on iPhone?",
             "Yes, SagWas runs on iPhone and iPad from iOS 17. The app is optimized for iPad (portrait + landscape). On iPhone, only portrait mode is supported."),
            ("How do I import an audio file?",
             "In a track's settings tap \"Import audio\", pick an .mp3/.m4a/.wav from the Files app, and optionally set start and end points using the trim editor."),
            ("What data does the app collect?",
             "None. SagWas stores all recordings locally. Shared content goes exclusively through your own iCloud account. There is no tracking, no ads, no analytics."),
        ],
        "contact_h": "Contact & Support",
        "contact_p1": "For questions, bug reports or feedback, email",
        "contact_p2": "Please include your iOS version, iPad model, and a short description of the issue. I usually reply within 48 hours.",
        "privacy_h": "Privacy",
        "privacy": [
            "All recordings are stored locally on the device.",
            "Shared pages are transmitted encrypted via Apple iCloud (CloudKit).",
            "No personal data is shared with third parties.",
            "The app contains no ads and no tracking.",
            "Pictograms are loaded from the ARASAAC API (image symbols only, no user data).",
        ],
        "privacy_full": "Full privacy policy",
    },
    "fr": {
        "title": "SagWas – Support",
        "meta_desc": "Support, aide et questions fréquentes pour l'application iPad SagWas.",
        "tagline": "Application de communication AAC pour iPad",
        "contact_note": "Contact : ",
        "about_h": "À propos de SagWas",
        "about_p": "SagWas est une application audio et de communication (AAC – Communication Augmentée et Alternative) pour iPad. Enregistrements, pictogrammes, photos et synthèse vocale peuvent être combinés en tableaux de communication simples. Disponible en huit langues.",
        "start_h": "Premiers pas",
        "start_button_h": "Mode Bouton",
        "start_button_p": "Un grand bouton de parole remplit l'écran. Maintenez 3 secondes pour enregistrer, appuyez pour lire. Utilisez le sélecteur de piste pour basculer entre jusqu'à 9 pistes.",
        "start_talkpad_h": "Mode TalkPad",
        "start_talkpad_p": "Une grille de tuiles sur plusieurs pages. Chaque tuile peut contenir audio, vidéo, photo, symbole ARASAAC et une étiquette texte (avec synthèse vocale).",
        "start_settings_h": "Ouvrir les réglages",
        "start_settings_p": "Appuyez sur l'engrenage en haut à droite. Si un code PIN est défini, saisissez-le. Vous pourrez y configurer le nombre de pistes, les couleurs, les photos, les langues et les pages TalkPad.",
        "faq_h": "Questions fréquentes",
        "faqs": [
            ("Comment enregistrer un nouveau message vocal ?",
             "En mode Bouton, maintenez le grand bouton appuyé pendant 3 secondes. Un compte à rebours apparaît, puis l'enregistrement démarre. Relâchez pour arrêter. Durée maximale : 2 minutes par piste."),
            ("Comment partager une piste ou une page ?",
             "Dans les réglages, appuyez sur « Partager ». Vous recevrez un identifiant de partage à 6 chiffres. Sur l'appareil cible, saisissez-le sous « Recevoir » – le contenu est synchronisé via Apple iCloud (CloudKit). Hors ligne, le transfert est mis en file d'attente."),
            ("Pourquoi la voix de synthèse vocale semble-t-elle robotique ?",
             "iOS ne fournit que des voix compactes pour certaines langues. Dans Réglages iOS → Accessibilité → Contenu énoncé → Voix, vous pouvez télécharger une voix de haute qualité. SagWas l'utilisera automatiquement."),
            ("La recherche de pictogrammes n'affiche aucun résultat.",
             "La recherche utilise l'API ARASAAC et nécessite une connexion Internet. Vérifiez votre connexion et essayez d'autres termes."),
            ("J'ai oublié mon code PIN.",
             "Désinstallez et réinstallez l'application. Attention : cela supprime tous les enregistrements locaux. Sauvegardez d'abord vos pistes ou pages via la fonction de partage."),
            ("SagWas fonctionne-t-il sur iPhone ?",
             "Oui, SagWas fonctionne sur iPhone et iPad à partir d'iOS 17. L'application est optimisée pour iPad (portrait + paysage). Sur iPhone, seul le mode portrait est disponible."),
            ("Comment importer un fichier audio ?",
             "Dans les réglages d'une piste, appuyez sur « Importer audio », choisissez un .mp3/.m4a/.wav depuis l'app Fichiers, et définissez éventuellement les points de début et fin avec l'éditeur de découpe."),
            ("Quelles données l'application collecte-t-elle ?",
             "Aucune. SagWas stocke tous les enregistrements localement. Le contenu partagé passe exclusivement par votre propre compte iCloud. Pas de pistage, pas de publicité, pas d'analytique."),
        ],
        "contact_h": "Contact et support",
        "contact_p1": "Pour toute question, rapport de bug ou commentaire, écrivez à",
        "contact_p2": "Merci d'indiquer votre version iOS, le modèle d'iPad et une brève description du problème. Je réponds généralement sous 48 heures.",
        "privacy_h": "Confidentialité",
        "privacy": [
            "Tous les enregistrements sont stockés localement sur l'appareil.",
            "Les pages partagées sont transmises chiffrées via Apple iCloud (CloudKit).",
            "Aucune donnée personnelle n'est transmise à des tiers.",
            "L'application ne contient ni publicité ni pistage.",
            "Les pictogrammes sont chargés via l'API ARASAAC (symboles uniquement, aucune donnée utilisateur).",
        ],
        "privacy_full": "Politique de confidentialité complète",
    },
    "es": {
        "title": "SagWas – Soporte",
        "meta_desc": "Soporte, ayuda y preguntas frecuentes para la aplicación iPad SagWas.",
        "tagline": "Aplicación de comunicación CAA para iPad",
        "contact_note": "Contacto: ",
        "about_h": "Acerca de SagWas",
        "about_p": "SagWas es una aplicación de audio y comunicación (CAA – Comunicación Aumentativa y Alternativa) para iPad. Grabaciones, pictogramas, fotos y síntesis de voz se combinan en tableros de comunicación sencillos. Disponible en ocho idiomas.",
        "start_h": "Primeros pasos",
        "start_button_h": "Modo Botón",
        "start_button_p": "Un gran botón de habla llena la pantalla. Mantén pulsado 3 segundos para grabar, toca para reproducir. Usa el selector de pista para cambiar entre hasta 9 pistas.",
        "start_talkpad_h": "Modo TalkPad",
        "start_talkpad_p": "Una cuadrícula de fichas en varias páginas. Cada ficha puede contener audio, vídeo, foto, símbolo ARASAAC y una etiqueta de texto (con síntesis de voz).",
        "start_settings_h": "Abrir ajustes",
        "start_settings_p": "Toca el engranaje en la esquina superior derecha. Si hay un PIN, introdúcelo. Allí puedes configurar el número de pistas, colores, fotos, idiomas y páginas TalkPad.",
        "faq_h": "Preguntas frecuentes",
        "faqs": [
            ("¿Cómo grabo un nuevo mensaje de voz?",
             "En Modo Botón, mantén pulsado el botón grande durante 3 segundos. Aparece una cuenta atrás y luego comienza la grabación. Suelta para detener. Duración máxima: 2 minutos por pista."),
            ("¿Cómo comparto una pista o una página?",
             "En Ajustes toca «Compartir». Recibirás un ID de 6 dígitos. En el dispositivo destino, introdúcelo en «Recibir» – el contenido se sincroniza vía Apple iCloud (CloudKit). Sin conexión, la subida queda en cola."),
            ("¿Por qué la voz de síntesis suena robótica?",
             "iOS solo proporciona voces compactas para algunos idiomas. En Ajustes iOS → Accesibilidad → Contenido hablado → Voces puedes descargar una voz de alta calidad. SagWas la usará automáticamente."),
            ("La búsqueda de pictogramas no muestra resultados.",
             "La búsqueda usa la API de ARASAAC y requiere conexión a Internet. Comprueba tu conexión y prueba otros términos."),
            ("Olvidé mi PIN.",
             "Desinstala y reinstala la app. Atención: esto borra todas las grabaciones locales. Primero respalda pistas o páginas con la función de compartir."),
            ("¿SagWas funciona en iPhone?",
             "Sí, SagWas funciona en iPhone y iPad desde iOS 17. La app está optimizada para iPad (vertical + horizontal). En iPhone solo el modo vertical está disponible."),
            ("¿Cómo importo un archivo de audio?",
             "En los ajustes de una pista toca «Importar audio», elige un .mp3/.m4a/.wav desde la app Archivos, y opcionalmente ajusta los puntos de inicio y fin con el editor de recorte."),
            ("¿Qué datos recopila la app?",
             "Ninguno. SagWas almacena todas las grabaciones localmente. El contenido compartido va exclusivamente por tu propia cuenta de iCloud. Sin seguimiento, sin anuncios, sin analíticas."),
        ],
        "contact_h": "Contacto y soporte",
        "contact_p1": "Para preguntas, errores o comentarios, escribe a",
        "contact_p2": "Incluye tu versión de iOS, modelo de iPad y una breve descripción del problema. Normalmente respondo en 48 horas.",
        "privacy_h": "Privacidad",
        "privacy": [
            "Todas las grabaciones se almacenan localmente en el dispositivo.",
            "Las páginas compartidas se transmiten cifradas vía Apple iCloud (CloudKit).",
            "No se comparten datos personales con terceros.",
            "La aplicación no contiene publicidad ni seguimiento.",
            "Los pictogramas se cargan vía la API de ARASAAC (solo símbolos, sin datos de usuario).",
        ],
        "privacy_full": "Política de privacidad completa",
    },
    "tr": {
        "title": "SagWas – Destek",
        "meta_desc": "SagWas iPad uygulaması için destek, yardım ve sık sorulan sorular.",
        "tagline": "iPad için AAC iletişim uygulaması",
        "contact_note": "İletişim: ",
        "about_h": "SagWas Hakkında",
        "about_p": "SagWas, iPad için bir ses ve iletişim uygulamasıdır (AAC – Artırıcı ve Alternatif İletişim). Kayıtlar, piktogramlar, fotoğraflar ve metin okuma basit iletişim panolarında birleştirilebilir. Sekiz dilde mevcuttur.",
        "start_h": "Başlarken",
        "start_button_h": "Düğme Modu",
        "start_button_p": "Büyük bir konuşma düğmesi ekranı kaplar. Kayıt için 3 saniye basılı tutun, çalmak için dokunun. Parça değiştiriciyi kullanarak 9'a kadar parça arasında geçiş yapın.",
        "start_talkpad_h": "TalkPad Modu",
        "start_talkpad_p": "Birden çok sayfada kutucuklardan oluşan bir ızgara. Her kutucuk ses, video, fotoğraf, ARASAAC sembolü ve metin etiketi (metin okuma ile) içerebilir.",
        "start_settings_h": "Ayarları açma",
        "start_settings_p": "Sağ üstteki dişli simgesine dokunun. PIN ayarlandıysa girin. Oradan parça sayısı, renkler, fotoğraflar, diller ve TalkPad sayfalarını yapılandırabilirsiniz.",
        "faq_h": "Sık Sorulan Sorular",
        "faqs": [
            ("Yeni bir sesli mesajı nasıl kaydederim?",
             "Düğme Modunda büyük düğmeyi 3 saniye basılı tutun. Geri sayım görünür, ardından kayıt başlar. Bırakmak kaydı durdurur. Parça başına maksimum 2 dakika."),
            ("Bir parçayı veya sayfayı nasıl paylaşırım?",
             "Ayarlarda \"Paylaş\"a dokunun. 6 haneli bir paylaşım kimliği alırsınız. Hedef cihazda \"Al\" altına girin – içerik Apple iCloud (CloudKit) üzerinden senkronize edilir. Çevrimdışıyken yükleme kuyruğa alınır."),
            ("Metin okuma sesi neden robotik geliyor?",
             "iOS bazı diller için yalnızca kompakt sesler sağlar. iOS Ayarları → Erişilebilirlik → Konuşulan İçerik → Sesler altından yüksek kaliteli bir ses indirebilirsiniz. SagWas onu otomatik kullanır."),
            ("Piktogram arama sonuç göstermiyor.",
             "Piktogram araması ARASAAC API'sini kullanır ve internet bağlantısı gerektirir. Bağlantınızı kontrol edin ve farklı terimler deneyin."),
            ("PIN'imi unuttum.",
             "Uygulamayı kaldırıp yeniden yükleyin. Uyarı: bu tüm yerel kayıtları siler. Önce parçaları veya sayfaları paylaşım işlevi ile yedekleyin."),
            ("SagWas iPhone'da çalışır mı?",
             "Evet, SagWas iOS 17'den itibaren iPhone ve iPad'de çalışır. Uygulama iPad için optimize edilmiştir (dikey + yatay). iPhone'da yalnızca dikey mod mevcuttur."),
            ("Ses dosyasını nasıl içe aktarırım?",
             "Bir parçanın ayarlarında \"Ses içe aktar\"a dokunun, Dosyalar uygulamasından .mp3/.m4a/.wav seçin ve isteğe bağlı olarak kırpma düzenleyiciyle başlangıç ve bitiş noktalarını ayarlayın."),
            ("Uygulama hangi verileri toplar?",
             "Hiçbiri. SagWas tüm kayıtları yerel olarak saklar. Paylaşılan içerik yalnızca kendi iCloud hesabınız üzerinden gider. İzleme, reklam veya analiz yoktur."),
        ],
        "contact_h": "İletişim ve Destek",
        "contact_p1": "Sorular, hata raporları veya geri bildirim için e-posta adresi:",
        "contact_p2": "Lütfen iOS sürümünüzü, iPad modelinizi ve sorunun kısa bir açıklamasını ekleyin. Genellikle 48 saat içinde yanıtlıyorum.",
        "privacy_h": "Gizlilik",
        "privacy": [
            "Tüm kayıtlar cihazda yerel olarak saklanır.",
            "Paylaşılan sayfalar Apple iCloud (CloudKit) üzerinden şifreli olarak iletilir.",
            "Üçüncü taraflarla kişisel veri paylaşılmaz.",
            "Uygulamada reklam ve izleme yoktur.",
            "Piktogramlar ARASAAC API'si üzerinden yüklenir (yalnızca semboller, kullanıcı verisi yok).",
        ],
        "privacy_full": "Tam gizlilik politikası",
    },
    "uk": {
        "title": "SagWas – Підтримка",
        "meta_desc": "Підтримка, довідка та часті питання щодо iPad-додатку SagWas.",
        "tagline": "Комунікаційний додаток AAC для iPad",
        "contact_note": "Контакт: ",
        "about_h": "Про SagWas",
        "about_p": "SagWas — це аудіо- та комунікаційний додаток (AAC — Допоміжна та Альтернативна Комунікація) для iPad. Записи, піктограми, фото та синтез мовлення можна поєднувати в прості комунікаційні дошки. Доступний вісьмома мовами.",
        "start_h": "Перші кроки",
        "start_button_h": "Режим кнопки",
        "start_button_p": "Велика кнопка мовлення заповнює екран. Утримуйте 3 секунди для запису, торкніться для відтворення. Використовуйте перемикач доріжок для перемикання між до 9 доріжками.",
        "start_talkpad_h": "Режим TalkPad",
        "start_talkpad_p": "Сітка плиток на кількох сторінках. Кожна плитка може містити аудіо, відео, фото, символ ARASAAC і текстову мітку (із синтезом мовлення).",
        "start_settings_h": "Відкрити налаштування",
        "start_settings_p": "Торкніться шестерні у верхньому правому куті. Якщо встановлено PIN, введіть його. Там можна налаштувати кількість доріжок, кольори, фото, мови та сторінки TalkPad.",
        "faq_h": "Часті питання",
        "faqs": [
            ("Як записати нове голосове повідомлення?",
             "У режимі кнопки утримуйте велику кнопку натиснутою 3 секунди. З'явиться зворотний відлік, потім почнеться запис. Відпустіть, щоб зупинити. Максимум 2 хвилини на доріжку."),
            ("Як поділитися доріжкою або сторінкою?",
             "У налаштуваннях торкніться «Поділитися». Ви отримаєте 6-значний ідентифікатор. На цільовому пристрої введіть його в «Отримати» — вміст синхронізується через Apple iCloud (CloudKit). Без мережі завантаження буде поставлено в чергу."),
            ("Чому голос синтезу мовлення звучить роботизовано?",
             "iOS надає лише компактні голоси для деяких мов. У Налаштуваннях iOS → Доступність → Озвучування → Голоси ви можете завантажити високоякісний голос. SagWas використовуватиме його автоматично."),
            ("Пошук піктограм не показує результатів.",
             "Пошук використовує API ARASAAC і вимагає підключення до Інтернету. Перевірте з'єднання та спробуйте інші пошукові терміни."),
            ("Я забув свій PIN.",
             "Видаліть і перевстановіть додаток. Увага: це видалить усі локальні записи. Спочатку збережіть доріжки або сторінки через функцію обміну."),
            ("Чи працює SagWas на iPhone?",
             "Так, SagWas працює на iPhone та iPad з iOS 17. Додаток оптимізовано для iPad (портрет + пейзаж). На iPhone доступний лише портретний режим."),
            ("Як імпортувати аудіофайл?",
             "У налаштуваннях доріжки торкніться «Імпортувати аудіо», виберіть .mp3/.m4a/.wav із додатку Файли та за потреби встановіть початок і кінець у редакторі обрізки."),
            ("Які дані збирає додаток?",
             "Жодних. SagWas зберігає всі записи локально. Спільний вміст проходить виключно через ваш власний обліковий запис iCloud. Без відстеження, реклами та аналітики."),
        ],
        "contact_h": "Контакт і підтримка",
        "contact_p1": "З питаннями, звітами про помилки чи відгуками пишіть на",
        "contact_p2": "Вкажіть вашу версію iOS, модель iPad і короткий опис проблеми. Зазвичай відповідаю протягом 48 годин.",
        "privacy_h": "Конфіденційність",
        "privacy": [
            "Усі записи зберігаються локально на пристрої.",
            "Спільні сторінки передаються зашифровано через Apple iCloud (CloudKit).",
            "Персональні дані не передаються третім сторонам.",
            "Додаток не містить реклами чи відстеження.",
            "Піктограми завантажуються через API ARASAAC (лише символи, без даних користувача).",
        ],
        "privacy_full": "Повна політика конфіденційності",
    },
    "ar": {
        "title": "SagWas – الدعم",
        "meta_desc": "الدعم والمساعدة والأسئلة الشائعة لتطبيق iPad من SagWas.",
        "tagline": "تطبيق تواصل AAC لجهاز iPad",
        "contact_note": "للتواصل: ",
        "about_h": "حول SagWas",
        "about_p": "SagWas هو تطبيق صوتي وتواصل (AAC - التواصل المعزز والبديل) لجهاز iPad. يمكن دمج التسجيلات والرموز والصور وتحويل النص إلى كلام في لوحات تواصل بسيطة. متوفر بثماني لغات.",
        "start_h": "البدء",
        "start_button_h": "وضع الزر",
        "start_button_p": "زر تحدث كبير يملأ الشاشة. اضغط مع الاستمرار لمدة 3 ثوانٍ للتسجيل، انقر للتشغيل. استخدم مبدل المسارات للتبديل بين ما يصل إلى 9 مسارات.",
        "start_talkpad_h": "وضع TalkPad",
        "start_talkpad_p": "شبكة من البطاقات عبر صفحات متعددة. يمكن لكل بطاقة أن تحتوي على صوت وفيديو وصورة ورمز ARASAAC وعنوان نصي (مع تحويل النص إلى كلام).",
        "start_settings_h": "فتح الإعدادات",
        "start_settings_p": "انقر على أيقونة الترس في الزاوية العلوية اليمنى. إذا كان هناك رمز PIN، فأدخله. يمكنك من هناك تكوين عدد المسارات والألوان والصور واللغات وصفحات TalkPad.",
        "faq_h": "الأسئلة الشائعة",
        "faqs": [
            ("كيف أسجل رسالة صوتية جديدة؟",
             "في وضع الزر، اضغط مع الاستمرار على الزر الكبير لمدة 3 ثوانٍ. يظهر عد تنازلي ثم يبدأ التسجيل. حرره للإيقاف. الحد الأقصى: دقيقتان لكل مسار."),
            ("كيف أشارك مسارًا أو صفحة؟",
             "في الإعدادات، انقر \"مشاركة\". ستتلقى معرف مشاركة مكونًا من 6 أرقام. على الجهاز الهدف، أدخله تحت \"استلام\" - تتم مزامنة المحتوى عبر Apple iCloud (CloudKit). عند عدم الاتصال، يُوضع التحميل في قائمة انتظار."),
            ("لماذا يبدو صوت تحويل النص إلى كلام آليًا؟",
             "يوفر iOS فقط أصواتًا مضغوطة لبعض اللغات. ضمن إعدادات iOS ← إمكانية الوصول ← المحتوى المنطوق ← الأصوات يمكنك تنزيل صوت عالي الجودة. سيستخدمه SagWas تلقائيًا."),
            ("لا يظهر بحث الرموز أي نتائج.",
             "يستخدم البحث واجهة ARASAAC API ويتطلب اتصالاً بالإنترنت. تحقق من اتصالك وجرب مصطلحات مختلفة."),
            ("نسيت رمز PIN الخاص بي.",
             "قم بإلغاء تثبيت التطبيق وإعادة تثبيته. تحذير: سيؤدي هذا إلى حذف جميع التسجيلات المحلية. قم بنسخ احتياطي للمسارات أو الصفحات عبر وظيفة المشاركة أولاً."),
            ("هل يعمل SagWas على iPhone؟",
             "نعم، يعمل SagWas على iPhone وiPad من iOS 17. التطبيق مُحسَّن لجهاز iPad (عمودي + أفقي). على iPhone، يتوفر فقط الوضع العمودي."),
            ("كيف أستورد ملفًا صوتيًا؟",
             "في إعدادات المسار، انقر على \"استيراد صوت\"، واختر .mp3/.m4a/.wav من تطبيق الملفات، واضبط اختياريًا نقاط البداية والنهاية باستخدام محرر القص."),
            ("ما البيانات التي يجمعها التطبيق؟",
             "لا شيء. يخزن SagWas جميع التسجيلات محليًا. يمر المحتوى المشترك حصريًا عبر حساب iCloud الخاص بك. لا يوجد تتبع ولا إعلانات ولا تحليلات."),
        ],
        "contact_h": "الاتصال والدعم",
        "contact_p1": "للأسئلة أو تقارير الأخطاء أو الملاحظات، راسل",
        "contact_p2": "يرجى تضمين إصدار iOS وطراز iPad ووصف موجز للمشكلة. عادة ما أرد خلال 48 ساعة.",
        "privacy_h": "الخصوصية",
        "privacy": [
            "يتم تخزين جميع التسجيلات محليًا على الجهاز.",
            "تُرسل الصفحات المشتركة مشفرة عبر Apple iCloud (CloudKit).",
            "لا تتم مشاركة البيانات الشخصية مع أطراف ثالثة.",
            "لا يحتوي التطبيق على إعلانات أو تتبع.",
            "يتم تحميل الرموز عبر واجهة ARASAAC API (الرموز فقط، بدون بيانات المستخدم).",
        ],
        "privacy_full": "سياسة الخصوصية الكاملة",
    },
    "pl": {
        "title": "SagWas – Pomoc",
        "meta_desc": "Pomoc, wsparcie i często zadawane pytania dotyczące aplikacji iPad SagWas.",
        "tagline": "Aplikacja komunikacyjna AAC dla iPada",
        "contact_note": "Kontakt: ",
        "about_h": "O SagWas",
        "about_p": "SagWas to aplikacja audio i komunikacyjna (AAC – Komunikacja Wspomagająca i Alternatywna) dla iPada. Nagrania, piktogramy, zdjęcia i synteza mowy mogą być łączone w proste tablice komunikacyjne. Dostępna w ośmiu językach.",
        "start_h": "Pierwsze kroki",
        "start_button_h": "Tryb Przycisku",
        "start_button_p": "Duży przycisk mówienia wypełnia ekran. Przytrzymaj przez 3 sekundy, aby nagrać, dotknij, aby odtworzyć. Użyj przełącznika ścieżek, aby przełączać między maksymalnie 9 ścieżkami.",
        "start_talkpad_h": "Tryb TalkPad",
        "start_talkpad_p": "Siatka kafelków na wielu stronach. Każdy kafelek może zawierać audio, wideo, zdjęcie, symbol ARASAAC i etykietę tekstową (z syntezą mowy).",
        "start_settings_h": "Otwieranie ustawień",
        "start_settings_p": "Dotknij ikony koła zębatego w prawym górnym rogu. Jeśli ustawiono PIN, wprowadź go. Tam możesz skonfigurować liczbę ścieżek, kolory, zdjęcia, języki i strony TalkPad.",
        "faq_h": "Najczęstsze pytania",
        "faqs": [
            ("Jak nagrać nową wiadomość głosową?",
             "W Trybie Przycisku przytrzymaj duży przycisk przez 3 sekundy. Pojawi się odliczanie, a następnie rozpocznie się nagrywanie. Puść, aby zatrzymać. Maksymalna długość: 2 minuty na ścieżkę."),
            ("Jak udostępnić ścieżkę lub stronę?",
             "W Ustawieniach dotknij „Udostępnij\". Otrzymasz 6-cyfrowy identyfikator. Na urządzeniu docelowym wprowadź go w „Odbierz\" – zawartość jest synchronizowana przez Apple iCloud (CloudKit). W trybie offline przesyłanie jest kolejkowane."),
            ("Dlaczego głos syntezy mowy brzmi robotycznie?",
             "iOS dostarcza tylko kompaktowe głosy dla niektórych języków. W Ustawienia iOS → Dostępność → Treść mówiona → Głosy możesz pobrać głos wysokiej jakości. SagWas użyje go automatycznie."),
            ("Wyszukiwanie piktogramów nie pokazuje wyników.",
             "Wyszukiwanie korzysta z API ARASAAC i wymaga połączenia internetowego. Sprawdź połączenie i wypróbuj inne terminy."),
            ("Zapomniałem kodu PIN.",
             "Odinstaluj i zainstaluj aplikację ponownie. Uwaga: spowoduje to usunięcie wszystkich lokalnych nagrań. Najpierw wykonaj kopię zapasową ścieżek lub stron za pomocą funkcji udostępniania."),
            ("Czy SagWas działa na iPhonie?",
             "Tak, SagWas działa na iPhonie i iPadzie od iOS 17. Aplikacja jest zoptymalizowana dla iPada (pionowo + poziomo). Na iPhonie dostępny jest tylko tryb pionowy."),
            ("Jak zaimportować plik audio?",
             "W ustawieniach ścieżki dotknij „Importuj audio\", wybierz .mp3/.m4a/.wav z aplikacji Pliki i opcjonalnie ustaw punkty początku i końca za pomocą edytora przycinania."),
            ("Jakie dane zbiera aplikacja?",
             "Żadne. SagWas przechowuje wszystkie nagrania lokalnie. Udostępniana zawartość przechodzi wyłącznie przez Twoje własne konto iCloud. Bez śledzenia, bez reklam, bez analityki."),
        ],
        "contact_h": "Kontakt i pomoc",
        "contact_p1": "W sprawie pytań, błędów lub opinii pisz na",
        "contact_p2": "Podaj wersję iOS, model iPada i krótki opis problemu. Zwykle odpowiadam w ciągu 48 godzin.",
        "privacy_h": "Prywatność",
        "privacy": [
            "Wszystkie nagrania są przechowywane lokalnie na urządzeniu.",
            "Udostępniane strony są przesyłane szyfrowane przez Apple iCloud (CloudKit).",
            "Żadne dane osobowe nie są udostępniane stronom trzecim.",
            "Aplikacja nie zawiera reklam ani śledzenia.",
            "Piktogramy są ładowane przez API ARASAAC (tylko symbole, bez danych użytkownika).",
        ],
        "privacy_full": "Pełna polityka prywatności",
    },
}


def render_lang_switcher(current):
    links = []
    for code, label in LANG_LABELS.items():
        href = LANGS[code]["file"]
        if code == current:
            links.append(f'<strong>{label}</strong>')
        else:
            links.append(f'<a href="{href}">{label}</a>')
    return ' · '.join(links)


def render_faq(faqs):
    return '\n'.join(
        f'            <details>\n                <summary>{q}</summary>\n                <p>{a}</p>\n            </details>'
        for q, a in faqs
    )


def render_privacy(items):
    return '\n'.join(f'                <li>{it}</li>' for it in items)


TEMPLATE = '''<!DOCTYPE html>
<html lang="{lang}" dir="{dir}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{meta_desc}">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            min-height: 100vh;
            padding: 40px 20px;
            color: #1a1a1a;
        }}
        .card {{
            background: white;
            border-radius: 20px;
            padding: 48px;
            max-width: 760px;
            margin: 0 auto;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        }}
        header {{ text-align: center; margin-bottom: 40px; }}
        .icon {{
            width: 80px; height: 80px;
            background: #e74c3c;
            border-radius: 20px;
            display: inline-flex;
            align-items: center; justify-content: center;
            margin-bottom: 16px;
        }}
        .icon svg {{ width: 40px; height: 40px; fill: white; }}
        h1 {{ font-size: 30px; margin-bottom: 6px; }}
        .tagline {{ color: #666; font-size: 16px; }}
        .langs {{
            margin-top: 14px;
            font-size: 13px;
            color: #888;
        }}
        .langs a {{ color: #e74c3c; text-decoration: none; }}
        .langs a:hover {{ text-decoration: underline; }}
        .langs strong {{ color: #1a1a1a; }}
        h2 {{
            font-size: 20px;
            margin-top: 32px; margin-bottom: 12px;
            padding-bottom: 6px;
            border-bottom: 2px solid #f0f0f0;
        }}
        h3 {{ font-size: 16px; margin-top: 18px; margin-bottom: 6px; color: #222; }}
        p, li {{ color: #444; font-size: 15px; line-height: 1.65; }}
        ul {{ padding-{list_pad}: 22px; margin-top: 6px; }}
        a {{ color: #e74c3c; text-decoration: none; font-weight: 500; }}
        a:hover {{ text-decoration: underline; }}
        .contact-box {{
            background: #f8f9fa;
            border-radius: 12px;
            padding: 20px 24px;
            margin-top: 14px;
        }}
        details {{
            background: #f8f9fa;
            border-radius: 10px;
            padding: 14px 18px;
            margin-top: 10px;
        }}
        details summary {{ cursor: pointer; font-weight: 600; color: #222; }}
        details[open] summary {{ margin-bottom: 10px; }}
        footer {{
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #eee;
            text-align: center;
            color: #999;
            font-size: 13px;
        }}
    </style>
</head>
<body>
    <main class="card">
        <header>
            <div class="icon">
                <svg viewBox="0 0 24 24"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3zm0 18c-3.87 0-7-3.13-7-7H3c0 4.72 3.51 8.59 8 9.29V23h2v-1.71c4.49-.7 8-4.57 8-9.29h-2c0 3.87-3.13 7-7 7z"/></svg>
            </div>
            <h1>{title}</h1>
            <p class="tagline">{tagline}</p>
            <p class="langs">{lang_switcher}</p>
            <p class="langs">{contact_note}<a href="mailto:simonch@gmx.de">simonch@gmx.de</a></p>
        </header>

        <section>
            <h2>{about_h}</h2>
            <p>{about_p}</p>
        </section>

        <section>
            <h2>{start_h}</h2>
            <h3>{start_button_h}</h3>
            <p>{start_button_p}</p>
            <h3>{start_talkpad_h}</h3>
            <p>{start_talkpad_p}</p>
            <h3>{start_settings_h}</h3>
            <p>{start_settings_p}</p>
        </section>

        <section>
            <h2>{faq_h}</h2>
{faq_block}
        </section>

        <section>
            <h2>{contact_h}</h2>
            <div class="contact-box">
                <p>
                    {contact_p1}<br>
                    <a href="mailto:simonch@gmx.de?subject=SagWas%20Support">simonch@gmx.de</a>.
                </p>
                <p style="margin-top:10px;">{contact_p2}</p>
            </div>
        </section>

        <section>
            <h2>{privacy_h}</h2>
            <ul>
{privacy_block}
                <li><a href="https://simonchrz.github.io/sagwas/privacy.html">{privacy_full}</a></li>
            </ul>
        </section>

        <footer>
            &copy; 2026 Simon Chrzanowski · SagWas · <a href="mailto:simonch@gmx.de">simonch@gmx.de</a>
        </footer>
    </main>
</body>
</html>
'''


def build():
    here = os.path.dirname(os.path.abspath(__file__))
    for code, meta in LANGS.items():
        t = T[code]
        html = TEMPLATE.format(
            lang=meta["code"],
            dir=meta["dir"],
            list_pad="right" if meta["dir"] == "rtl" else "left",
            title=t["title"],
            meta_desc=t["meta_desc"],
            tagline=t["tagline"],
            lang_switcher=render_lang_switcher(code),
            contact_note=t["contact_note"],
            about_h=t["about_h"],
            about_p=t["about_p"],
            start_h=t["start_h"],
            start_button_h=t["start_button_h"],
            start_button_p=t["start_button_p"],
            start_talkpad_h=t["start_talkpad_h"],
            start_talkpad_p=t["start_talkpad_p"],
            start_settings_h=t["start_settings_h"],
            start_settings_p=t["start_settings_p"],
            faq_h=t["faq_h"],
            faq_block=render_faq(t["faqs"]),
            contact_h=t["contact_h"],
            contact_p1=t["contact_p1"],
            contact_p2=t["contact_p2"],
            privacy_h=t["privacy_h"],
            privacy_block=render_privacy(t["privacy"]),
            privacy_full=t["privacy_full"],
        )
        with open(os.path.join(here, meta["file"]), "w", encoding="utf-8") as f:
            f.write(html)
        print(f"wrote {meta['file']}")


if __name__ == "__main__":
    build()
