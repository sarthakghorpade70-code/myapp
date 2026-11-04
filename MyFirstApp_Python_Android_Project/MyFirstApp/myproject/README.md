# My First App — Python/Kivy Android Calculator

A dark, premium-styled calculator built with Python 3 and Kivy. It includes basic arithmetic, decimal input, percentage, sign toggle, delete, clear, and an in-session calculation history.

## Project contents

```text
MyFirstApp/
├── main.py
├── buildozer.spec
├── icon.png
├── splash.png
├── assets/
│   ├── icon_adaptive_foreground.png
│   └── icon_adaptive_background.png
└── README.md
```

## 1. Run on Windows (desktop preview)

Use Python 3.10 or 3.11 for a straightforward Kivy setup.

```powershell
py -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install "kivy[base]"
python main.py
```

The desktop preview helps test the calculator UI and logic. Android packaging is done in Linux/WSL2.

## 2. Build Android APK/AAB from Windows using WSL2

### Install WSL2 (PowerShell as Administrator)

```powershell
wsl --install -d Ubuntu
```

Restart if Windows asks, then launch Ubuntu and create your Linux username/password.

### Install build dependencies in Ubuntu

```bash
sudo apt update
sudo apt install -y git zip unzip openjdk-17-jdk python3-pip python3-venv \
  build-essential autoconf automake libtool pkg-config zlib1g-dev \
  libncurses5-dev libncursesw5-dev libtinfo6 cmake libffi-dev libssl-dev
```

Keep the project inside the Linux filesystem (recommended), not `/mnt/c`, for example:

```bash
mkdir -p ~/projects
cd ~/projects
```

Copy/extract the `MyFirstApp` folder there. Then:

```bash
cd ~/projects/MyFirstApp
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install buildozer cython
```

Check `buildozer.spec` before building:
- Change `package.domain = com.example` to a unique reverse-domain identifier you control, such as `in.yourbrand`.
- Keep `package.name = myfirstapp` lowercase.
- The Play target API is set to 36 (Android 16), the current requirement on 4 November 2026. Re-check Google's policy when submitting because it can change.
- This project targets `arm64-v8a`.

### Build a debug APK for a real phone

```bash
buildozer -v android debug
```

The APK is written into `bin/`. Install it with:

```bash
buildozer android deploy run
```

Or copy the APK to your phone and install it (allow installs from that source when Android asks).

### Build a release Android App Bundle

```bash
buildozer -v android release
```

Check the `bin/` directory for the generated `.aab` (and/or release artifact depending on your Buildozer/python-for-android versions). Google Play accepts Android App Bundles for new app publishing. If your toolchain only emits an APK, update Buildozer/python-for-android and verify the AAB build option in the version-specific documentation; do not upload an APK as a substitute for a required AAB.

## 3. Sign the AAB with an upload key

Create the upload keystore once. Store it securely outside your project and back it up. Never commit it to Git or share it.

```bash
keytool -genkeypair -v \
  -keystore my-first-app-upload.jks \
  -alias myfirstapp-upload \
  -keyalg RSA -keysize 2048 -validity 10000
```

Move the `.jks` to a safe location and make a backup. Set a shell variable to the actual AAB path:

```bash
AAB="bin/REPLACE_WITH_YOUR_RELEASE_FILE.aab"
```

Sign it with `jarsigner` (AAB signing uses jarsigner, not apksigner):

```bash
jarsigner -verbose -sigalg SHA256withRSA -digestalg SHA-256 \
  -keystore /secure/path/my-first-app-upload.jks \
  "$AAB" myfirstapp-upload
```

Verify:

```bash
jarsigner -verify -verbose -certs "$AAB"
```

Upload this signed AAB to Play Console. Enrol in Play App Signing when prompted; Google manages the app-signing key while you retain your upload key. Keep the upload keystore and passwords safe. If you lose the upload key, use Play Console's upload-key reset process.

**Important:** Never put keystore passwords in source code, `buildozer.spec`, screenshots, or a public repository.

## 4. Adaptive icon

The spec uses Buildozer's current adaptive icon options:
- `icon.adaptive_foreground.filename`
- `icon.adaptive_background.filename`

These create adaptive launcher layers on Android 8.0+ when supported by your installed Buildozer/python-for-android toolchain. The classic `icon.png` is also supplied as a 512×512 PNG. Inspect the built app on a device with a circular, squircle, and rounded-square launcher mask before release. If your installed packaging version does not recognize adaptive icon settings, update Buildozer/python-for-android rather than manually editing generated build files as a permanent solution.

## 5. Google Play publishing checklist

1. Create a Google Play Console developer account and complete identity/contact verification.
2. Pay the registration fee shown in Play Console (currently US$25, one time).
3. Create the app named **My First App** and choose App/Game and Free/Paid.
4. Complete the store listing: app name, short description, full description, screenshots, 512×512 high-resolution icon, and 1024×500 feature graphic.
5. Complete the App content forms: privacy policy if required, Data safety, ads declaration, app access, content rating, target audience, and any other declarations shown.
6. Upload the signed `.aab` to an internal testing track first.
7. If your account is a new personal developer account created after 13 Nov 2023, Google generally requires a closed test with at least 12 testers opted in continuously for 14 days before you can apply for production access. Follow the exact requirement displayed in your Play Console account.
8. Review the pre-launch report, fix crashes and policy issues, then apply for production access / submit for review.
9. After approval, monitor Android vitals, reviews, and policy messages.

Official resources:
- Play Console: https://play.google.com/console/
- Target API policy: https://support.google.com/googleplay/android-developer/answer/11926878
- Kivy Android packaging: https://kivy.org/doc/stable/guide/packaging-android.html
- Buildozer spec: https://buildozer.readthedocs.io/en/latest/specifications/

## 6. Notes and limitations

- Calculation history is kept in memory during the current app session; it is not yet persisted after the app is closed.
- No special Android permissions are requested.
- Before public release, test on several Android screen sizes and Android versions.
- This source project is prepared for you, but an APK/AAB has not been compiled or tested on a physical Android device in this environment.
- Choose a unique package ID before the first Play upload. Google Play package IDs are permanent for that listing.
