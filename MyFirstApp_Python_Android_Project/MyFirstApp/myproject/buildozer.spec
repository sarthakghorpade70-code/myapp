
[app]

title = My First App
package.name = myfirstapp
package.domain = com.sarthak
source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,atlas,txt

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/splash.png

android.permissions =
android.api = 36
android.minapi = 23
android.ndk = 29
android.archs = arm64-v8a

p4a.branch = develop
p4a.bootstrap = sdl2

[buildozer]

log_level = 2
warn_on_root = 1
