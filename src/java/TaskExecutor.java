package org.test.myapp;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.util.Log;

public class TaskExecutor{
    private static final String APP_TAG = "org.test.myapp.task.executor";

    Context appContext;

    public TaskExecutor(Context context){
        this.appContext = context;
    }

    public void triggerTask(){
        Log.i(APP_TAG, "Preparing an intent to be broadcasted.");
        Intent intent = new Intent(appContext, TaskAlarmReceiver.class);
        appContext.sendBroadcast(intent);
        Log.i(APP_TAG, "Intent is broadcasted to TaskReceiver.class.");
    }

    // public void cancelTask(){
    //     Log.i("python", "-------------------- cancel scheduling");
    //     Log.i("python", taskArgument);
    //     AlarmManager alarmManager = (AlarmManager) appContext.getSystemService(Context.ALARM_SERVICE);

    //     // The TaskReceiver class is the BroadcastReceiver set to handle the task when it is fired
    //     Intent intent = new  Intent(appContext, TaskReceiver.class);

    //     PendingIntent pendingIntent = PendingIntent.getBroadcast(appContext, 0, intent, PendingIntent.FLAG_UPDATE_CURRENT);
    //     alarmManager.cancel(pendingIntent);
    //     Log.i("python", "-------------------- cancelled");
    // }
}
