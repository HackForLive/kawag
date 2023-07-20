// https://github.com/kamenchunathan/kivy-android-alarm-manager-example/tree/main
package org.test.myapp;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.app.PendingIntent;
import android.app.AlarmManager;
import android.util.Log;


public class TaskScheduler{
    Context appContext;

    public TaskScheduler(Context context){
        this.appContext = context;
    }

    // This method will be called from python hence scheduling the task at a specific time
    public void scheduleTask(int seconds, String taskArgument){
        Log.i("python", "-------------------- scheduling");
        Log.i("python", taskArgument);
        AlarmManager alarmManager = (AlarmManager) appContext.getSystemService(Context.ALARM_SERVICE);

        // The TaskReceiver class is the BroadcastReceiver set to handle the task when it is fired
        Intent intent = new  Intent(appContext, TaskReceiver.class);

        // the task taskArgument is a string that will be retrieved by our TaskReceiver class and passed on to the
        // service. This is will then be made available to the python file via an environment variable by kivy
        intent.putExtra("pythonServiceArgument", taskArgument);

        PendingIntent pendingIntent = PendingIntent.getBroadcast(appContext, 0, intent, PendingIntent.FLAG_UPDATE_CURRENT);
        alarmManager.setRepeating(AlarmManager.RTC_WAKEUP, System.currentTimeMillis(), AlarmManager.INTERVAL_FIFTEEN_MINUTES, pendingIntent);
    }
}
