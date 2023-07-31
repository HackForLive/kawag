// https://github.com/kamenchunathan/kivy-android-alarm-manager-example/tree/main
package org.test.myapp;

import android.content.Context;
import android.content.Intent;
import android.content.BroadcastReceiver;
import android.media.MediaPlayer;
import android.provider.Settings;
import android.os.Bundle;
import android.util.Log;

import org.test.myapp.ServiceHandletask;

public class TaskReceiver extends BroadcastReceiver {

    // The onReceive method will start the service defined in the buildozer.spec file
    @Override
    public void onReceive(Context context, Intent intent){
        // set argument to pass to python code
        Bundle extras = intent.getExtras();
        String argument = extras.getString("pythonServiceArgument");
        Log.i("python", argument);
        Log.i("python", "on receive (before)");
        /*
            The ServiceHandleTask class corresponds to the class defined in the the buildozer.spec file as:
                services = handletask:tasks.py
        */
        // service start - do not work due to permission 
        // ServiceHandletask.start(context, "");
        // rewritten logic for service start in foreground
        Intent intentS = ServiceHandletask.getDefaultIntent(context, "", "My Application", "Handletask", "");
        context.startForegroundService(intentS);
        Log.i("python", "on receive (after)");
    }
}
