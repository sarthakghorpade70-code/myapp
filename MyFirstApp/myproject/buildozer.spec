[app]

title = My First App
package.name = myfirstapp
# IMPORTANT: Replace this with a domain you own/control before publishing.
# Example: com.yourbrand (package IDs cannot be changed after publishing).
package.domain = com.example

source.dir = .
source.include_exts = py,png,kv,txt,md
source.exclude_dirs = .git,.venv,venv,bin,__pycache__

version = 1.0.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0

# Classic launcher icon and native startup presplash.
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/splash.png
android.presplash_color = #07142F

# Android adaptive launcher icon (Android 8.0+).
icon.adaptive_foreground.filename = %(source.dir)s/assets/icon_adaptive_foreground.png
icon.adaptive_background.filename = %(source.dir)s/assets/icon_adaptive_background.png

# Google Play submission requirement as of 4 Nov 2026: API 36 or higher.
android.api = 36
android.minapi = 23
android.ndk = 28c
android.archs = arm64-v8a
android.accept_sdk_license = True
android.enable_androidx = True

# A calculator does not need Internet, location, camera, or storage permissions.
android.permissions =

# Buildozer uses this for the app's Android package metadata.
android.allow_backup = False

[buildozer]
log_level = 2
warn_on_root = 1
