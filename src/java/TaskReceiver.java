// https://github.com/kamenchunathan/kivy-android-alarm-manager-example/tree/main
package org.test.myapp;

import android.content.Context;
import android.content.Intent;
import android.content.BroadcastReceiver;
import android.media.MediaPlayer;
import android.provider.Settings;
import android.os.Bundle;
import android.util.Log;


import androidx.work.OneTimeWorkRequest;
import androidx.work.WorkManager;
import androidx.work.PeriodicWorkRequest;

import org.test.myapp.ServiceHandletask;
import org.test.myapp.NotificationWorker;

public class TaskReceiver extends BroadcastReceiver {
    private static final String APP_TAG = "org.test.myapp.task.receiver";

    // The onReceive method will start the service defined in the buildozer.spec file
    @Override
    public void onReceive(Context context, Intent intent){
        // set argument to pass to python code
        Bundle extras = intent.getExtras();
        if (extras != null) {
            String argument = extras.getString("pythonServiceArgument");
            if (argument != null) {
                Log.i(APP_TAG, argument);
            } else {
                Log.w(APP_TAG, "Missing key: pythonServiceArgument");
            }
        } else {
            Log.w(APP_TAG, "Intent extras are null");
        }


        Log.i(APP_TAG, "on receive (before)");
        /*
            The ServiceHandleTask class corresponds to the class defined in the the buildozer.spec file as:
                services = handletask:tasks.py
        */
        OneTimeWorkRequest workRequest = new OneTimeWorkRequest.Builder(NotificationWorker.class).build();
        WorkManager.getInstance(context).enqueue(workRequest);
        Log.i(APP_TAG, "on receive (after)");
    }
}
