    // Функция ymaps.ready() будет вызвана, когда загрузятся все компоненты API
    ymaps.ready(init);

    // Массив объектов
    var Placemarks = [
        {
            latitude: 52.704187,
            longitude: 41.413628,
            hintContent: 'Питомник «Ацель Хоф»',
            balloonContent: 'г. Тамбов, ул. 1-й Сенной проезд, 5'
        },
        {
            latitude: 51.913755,
            longitude: 39.295428,
            hintContent: 'Питомник «Of sunny glen»',
            balloonContent: 'Воронежская область, Рамонский район, п. ВНИИСС, д.66'
        },
        {
            latitude: 51.654154,
            longitude: 39.335169,
            hintContent: 'Питомник «Choice of the queen»',
            balloonContent: 'Воронежская обл., Новоусманский р-он, п.Отрадное'
        },
        {
            latitude: 55.622929,
            longitude: 38.026369,
            hintContent: 'Питомник «Linnwood»',
            balloonContent: 'Московская обл., Раменский р-н, ВЭИ им. Ленина, Островского 17'
        },
        {
            latitude: 55.991178,
            longitude: 38.198585,
            hintContent: 'Питомник «Сап Алтын»',
            balloonContent: 'Московская область, Щелковский район, д. Мишнево'
        },
        {
            latitude: 56.360322,
            longitude: 37.171954,
            hintContent: 'Питомник «Маир Хоф»',
            balloonContent: 'Московская область, Дмитровский район, д. Бородино'
        },
        {
            latitude: 55.885903,
            longitude: 38.093158,
            hintContent: 'Питомник «Зимняя вишня»',
            balloonContent: 'Московская область, Щелковский район, деревня Леониха'
        },
        {
            latitude: 55.624037,
            longitude: 37.485134,
            hintContent: 'Питомник «Из Ксаро Честная игра»',
            balloonContent: 'Москва, улица генерала Тюленева, дом 7 кор.1'
        },
        {
            latitude: 56.106007,
            longitude: 36.917075,
            hintContent: 'Питомник «Ice Guard»',
            balloonContent: 'Московская область, Солнечногорский район, д. Мелечкино, д.98, коттеджный посёлок Истра-Вилладж'
        },
        {
            latitude: 47.237779,
            longitude: 39.69551,
            hintContent: 'Питомник «Линия Судьбы»',
            balloonContent: 'г. Ростов-на-Дону, ул. Мечникова 126А'
        },
        {
            latitude: 58.004685,
            longitude: 56.202521,
            hintContent: 'Питомник «От серых псов»',
            balloonContent: 'г. Пермь, улица Ленина, 98'
        },
        {
            latitude: 54.198753,
            longitude: 37.667977,
            hintContent: 'Питомник «Eigenschaft»',
            balloonContent: 'г. Тула, 3-й Песчаный проезд, 11'
        },
        {
            latitude: 54.999924,
            longitude: 36.4519,
            hintContent: 'Питомник «ФАНКОРГИ»',
            balloonContent: 'Калужская область, Малоярославец, улица Российских Газовиков, 21к1'
        },
        {
            latitude: 53.330381,
            longitude: 34.287455,
            hintContent: 'Питомник «Priori Inkantatum»',
            balloonContent: 'г. Брянск ул. Литейная д.64-7'
        },
        {
            latitude: 59.88227,
            longitude: 29.890246,
            hintContent: 'Питомник «Макшерри»',
            balloonContent: 'г. Санкт-Петербург, Петергоф, Санкт-Петербургский проспект, 60'
        },
        {
            latitude: 59.569144,
            longitude: 30.551065,
            hintContent: 'Питомник «Макшерри»',
            balloonContent: 'г. Санкт-Петербург, Ленинградская область, Тосненский р-н, пос. Форносово.'
        }
    ];

    function init() {
        // Создание карты.
        var myMap = new ymaps.Map("map", {
            // Координаты центра карты (широта, долгота)
            center: [52.7317, 41.4433],
            // Уровень масштабирования
            zoom: 6,
            // Элементы управления
            controls:[ 'zoomControl' ], // Ползунок масштаба
            //Список поведений карты
            behaviors: [
                'drag',                 // Перемещение карты при нажатой левой кнопке мыши
                'scrollZoom'            // Изменение масштаба колесом мыши
            ]
        });

        Placemarks.forEach(function(obj) {
            // Создание метки
            var myPlacemark = new ymaps.Placemark([obj.latitude, obj.longitude], {
            // Всплывающая подсказка при наведении мышкой на метку
            hintContent: obj.hintContent,
            // Окно с информацией при нажатии на метку
            balloonContent: obj.balloonContent
            });
            // Добавление метки на карту.
            myMap.geoObjects.add(myPlacemark);
        });
    }
