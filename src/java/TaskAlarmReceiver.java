// https://github.com/kamenchunathan/kivy-android-alarm-manager-example/tree/main
package org.test.myapp;

import android.content.Context;
import android.content.Intent;
import android.content.BroadcastReceiver;
import android.media.MediaPlayer;
import android.provider.Settings;
import android.app.PendingIntent;
import android.app.AlarmManager;
import android.os.Bundle;
import android.util.Log;

import org.test.myapp.ServiceHandletask;

public class TaskAlarmReceiver extends BroadcastReceiver {
    private static final String APP_TAG = "org.test.myapp.alarm.receiver";

    // The onReceive method will start the service defined in the buildozer.spec file
    @Override
    public void onReceive(Context context, Intent intent){
        // set argument to pass to python code
        Log.d(APP_TAG, "TaskAlarmReceiver.onReceive() called");
		AlarmManager alarmManager = (AlarmManager) context.getSystemService(Context.ALARM_SERVICE);
		Intent i = new Intent(context, TaskReceiver.class); // explicit
	
        int minutes = 2;
        long triggerTime = System.currentTimeMillis() + 60000L * minutes;

        PendingIntent pendingIntent = PendingIntent.getBroadcast(context, 0, i, 
            PendingIntent.FLAG_CANCEL_CURRENT | PendingIntent.FLAG_IMMUTABLE); // cancel current if any
        alarmManager.setExact(AlarmManager.RTC_WAKEUP, triggerTime, pendingIntent);
        Log.i(APP_TAG, "Alarm set.");
    }
}
