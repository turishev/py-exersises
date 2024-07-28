import sys
import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gio, Gdk, Graphene, GLib

# Реализация приложения в стиле объектно-ориентированного программирования (ООП), что вовсе необязатено, но допустим.
# Мы описываем КЛАССЫ объектов, это как бы инструкция по созданию ЭКЗЕМПЛЯРА объекта.
# Экземпляр - это то, что реально создаётся и потом работает. Класс - инструкция, описание.
# На базе одного класса можно создать много экземпляров объектов (или, иначе, просто объектов).

# Один класс может наследоваться от другого, таким образом его экземпляры могут использовать методы роджительского класса,
# и мы можем пользоваться кодом, который написан не нами.


# Создаём свой класс для главного окна приложения, который наследует классу Gtk.ApplicationWindow
# что означает, что он унаследует МЕТОДЫ Gtk.ApplicationWindow и они будут доступны для нашего приложения
# Реально мы определяем здесь  лишь несколько методов:  show_open_dialog, open_response, hello, bye и конструктор __init__
# Полное описание Gtk.ApplicationWindow здесь, но это для gtk-3 и по-английски
# https://python-gtk-3-tutorial.readthedocs.io/en/latest/application.html
#
# 
class MainWindow(Gtk.ApplicationWindow):
    # __init__ - конструктор класса - код который АВТОМАТИЧЕСКИ вызывается при создании, объекта,
    # имя с двумя подчеркиваниями, обычно означает некую специальную функцию
    # self - это собственно объект нашего класса, и мы его как-то настраиваем в конструкторе
    # Каждый метод класса будет получать первым параметром self АВТОМАТИЧЕСКИ, но мы должны его указывать в сигнатруе метода
    # Имя self - условное, можно называть иначе (первый параметр в сигнатуре), но так принято, и редакторы тоже это знают и подсвечивают
    # 
    # Собственно в конструкторе мы и строим всё окно.
    # 
    def __init__(self, *args, **kwargs):
        # нужно вызвать конструктор родительского класса, возможно там что-то тоже делается
        # super() - это получить родительский класс, после точки вызов его метода, т.е. __init__ - конструктора в данном случае
        # и передать ему те же аргументы:  *args, **kwargs
        super().__init__(*args, **kwargs)

        # поставить размеры окна и заголовок - унаследованные методы от Gtk.ApplicationWindow
        # формат любого вызова метода объекта: ЭКЗЕМПЛЯР_ОБЪЕКТА.НАЗВАНИЕ_МЕТОДА(АРГУМЕНТЫ)
        # здесь объект - это self
        self.set_default_size(600, 250) 
        self.set_title("Ex1")

        # далее создаём три менеджера раскладки (layout containers), которые позволяю аккуратно размещать компоненты в окне
        # каждому передаются именовынный параметр orientation, чтобы указать горизонтально или вертикально располагаются дочерние элементы 
        # Gtk.Orientation.HORIZONTAL, Gtk.Orientation.VERTICAL - это некие волшебные цифры непосредственно в библиотеке Gtk, написанно на си,
        # которые условно это указывают https://docs.gtk.org/gtk3/enum.Orientation.html (как тут видно это лишь 0 и 1)
        # созданные контейнеры присваиваем полям нашего объекта (окна) под названиям box1 box2 box3
        # Поля в питоне создаюются в момен присваивания им,
        # т..е их не нужно  описывать зараниее как в C++ Java Ada Pascal и других статически типизированных языках
        self.box1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL) # этот делит окно по горизонтали и элементы размещаются горизонтально
        self.box2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)  # вертикальный
        self.box3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL) # вертикальный

        # настраиваем некоторые параметры контейнеров (их намного  больше)
        self.box2.set_spacing(10)  # пространство между элеменатами внутри бокса  
        self.box2.set_margin_top(10) # отступ сверху
        self.box2.set_margin_bottom(10)
        self.box2.set_margin_start(10)
        self.box2.set_margin_end(10)

        self.set_child(self.box1)  # box1 добавляем как основной контент нашего окна
        self.box1.append(self.box2)  # помещаем box2 внутрь box1, это то что будет слева окна
        self.box1.append(self.box3)  # помещаем box3 внутрь box1,  это то что будет справа,
        # в этом примере он не используется, но можно что-то сюда дабавить потом

        # создаём кнопку, Gtk.Button - это конструктор этого класса, мы передаём ему именованный параметр label, это будет надпись на кнопке
        self.button = Gtk.Button(label="Hello")
        self.button.connect('clicked', self.hello) # ключевой момент - подключаем кнопку к обработчику события, 'clicked' - событие,
        # self.hello - метод данного класса под названием hello, он будет вызван при нажатии на кнопку
        self.box2.append(self.button)  # помещаем кнопку в первый (левый вертикальный бокс)

        # ещё кнопка
        self.button2 = Gtk.Button(label="Bye")
        self.button2.connect('clicked', self.bye)  # подключаем кнопку к другому обработчику события - self.bye
        self.box2.append(self.button2) # тоже в первый вертикальный бокс, она будет ниже  

        # делаем главную панель окна
        self.header = Gtk.HeaderBar()
        self.set_titlebar(self.header) # добавляем её в окно

        # делаем кнопку для запуска диалога открытия файлов
        self.open_button = Gtk.Button(label="Open") # open_button - это снова просто поле в нашем классе, которое мы сами так назвали
        self.header.pack_start(self.open_button) # добавляем кнопку в заголовок
        self.open_button.set_icon_name("document-open-symbolic") # навешиваем на кнопку иконку

        # создаём диалог открытия файла, но пока не запускаем
        self.open_dialog = Gtk.FileChooserNative.new(title="Открой этот файл же",
                                                     parent=self, action=Gtk.FileChooserAction.OPEN)

        self.open_dialog.connect("response", self.open_response) # назначаем диалогу обработчик события по результату (выбора файлов)
        self.open_button.connect("clicked", self.show_open_dialog) # кнопка open_button будет запускать диалог вызывая обработчик show_open_dialog

        # делаем модный стиль для приложения
        app = self.get_application() # из объекта окна получаем объект приложения
        sm = app.get_style_manager() # получаем style_manager приложения
        sm.set_color_scheme(Adw.ColorScheme.PREFER_DARK) # ставим тёмную тему
        # есть некая штука для стилизации приложения - adwaita, дока здесь
        # https://gnome.pages.gitlab.gnome.org/libadwaita/doc/main/styles-and-appearance.html
        # в ней определена константа Adw.ColorScheme.PREFER_DARK а также и другие PREFER_LIGHT, FORCE_LIGHT, FORCE_DARK

        # метод нашего класса MainWindow -  обработчик события кнопки запуска диалога открытия файла
    def show_open_dialog(self, button):
        self.open_dialog.show() # у диалога есть метод  show и мы его здесь вызываем, сам диалог ранее сохранён в поле open_dialog нашего окна

    def open_response(self, dialog, response):
        if response == Gtk.ResponseType.ACCEPT: # обрабатываем если только пользователь на выбрал файл
            # другие результаты диталога описан в https://docs.gtk.org/gtk3/enum.ResponseType.html
            file = dialog.get_file() # получаем из диалога то что выбрал юзер
            filename = file.get_path() 
            print(filename)

    # далее пара примитивных обработчиков кнопок, они просто печатают что-то на консоль        
    def hello(self, button):
        print("Hello")

    def bye(self, button):
        print("Bye bye")


# далее просто некое стандартное заклинание для запуска приложения        
class MyApp(Adw.Application): # создаём класс приложения, наследуя его  от Adw.Application
    def __init__(self, **kwargs): # конструктор класса
        super().__init__(**kwargs) # вызвать конструктор родительского класса
        self.connect('activate', self.on_activate) # подключить сигнал 'activate' к нашему обработчику on_activate

    def on_activate(self, app):
        self.win = MainWindow(application=app) # созадаём наше окно со всеми панельками и кнопками, сохраняем его в поле win приложения
        self.win.present() # показываем это окно


app = MyApp() # создать объект приложения, вызвав конструктор класса MyApp
app.run(sys.argv) # запустить приложение методом run, и передать ему аргументы (возможно ему интересно), что пользователь передал ему на консоли sys.argv
