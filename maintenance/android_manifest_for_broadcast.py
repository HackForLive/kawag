import os
from pathlib import Path

manifest_path = os.path.join(
    Path(os.path.dirname(os.path.abspath(__file__))).parent,
    '.buildozer/android/platform/build-arm64-v8a/dists/myapp/' + 
    'templates/AndroidManifest.tmpl.xml'
)


# ./.buildozer/android/platform/python-for-android/pythonforandroid/bootstraps/sdl2/build/templates/AndroidManifest.tmpl.xml
# ./.buildozer/android/platform/python-for-android/pythonforandroid/bootstraps/service_library/build/templates/AndroidManifest.tmpl.xml
# ./.buildozer/android/platform/python-for-android/pythonforandroid/bootstraps/service_only/build/templates/AndroidManifest.tmpl.xml
# ./.buildozer/android/platform/python-for-android/pythonforandroid/bootstraps/webview/build/templates/AndroidManifest.tmpl.xml
# ./.buildozer/android/platform/build-arm64-v8a/build/bootstrap_builds/sdl2/templates/AndroidManifest.tmpl.xml
# ./.buildozer/android/platform/build-arm64-v8a/dists/myapp/templates/AndroidManifest.tmpl.xml


print(manifest_path)

RECEIVER_STRING = """
    <receiver android:name=".TaskReceiver" android:enabled="true" android:exported="true">
        <intent-filter>
            <action android:name="android.intent.action.USER_PRESENT" />
            <action android:name="android.intent.action.BOOT_COMPLETED" />
            <action android:name="android.intent.action.QUICKBOOT_POWERON" />
            <action android:name="com.htc.intent.action.QUICKBOOT_POWERON" />
            <action android:name="android.intent.action.MAIN" />
            <action android:name="android.intent.action.DELETE" />
        </intent-filter>
    </receiver>
    </application>
"""

R_STRING = '</application>'

#read input file
with open(manifest_path, 'rt', encoding='UTF8') as fin:
    #read file contents to string
    data = fin.read()
#replace all occurrences of the required string
data = data.replace(R_STRING, RECEIVER_STRING)
#open the input file in write mode
with open(manifest_path, 'wt', encoding='UTF8') as fin:
    #overrite the input file with the resulting data
    fin.write(data)
