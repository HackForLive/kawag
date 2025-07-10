// https://github.com/kamenchunathan/kivy-android-alarm-manager-example/tree/main
package org.test.myapp;

import androidx.work.OneTimeWorkRequest;
import android.content.Intent;
import android.content.Context;
import android.util.Log;
import java.util.concurrent.TimeUnit;

import androidx.annotation.NonNull;
import androidx.work.Worker;
import androidx.work.WorkerParameters;
import androidx.work.WorkManager;


import org.test.myapp.ServiceHandletask;

public class NotificationWorker extends Worker {

    private static final String APP_TAG = "org.test.myapp.task.worker";

    public NotificationWorker(@NonNull Context context, @NonNull WorkerParameters params) {
        super(context, params);
    }

    @NonNull
    @Override
    public Result doWork() {
            Context context = getApplicationContext();
            Intent intentS = ServiceHandletask.getDefaultIntent(context, "", "My Application", "Handletask", "");
            context.startService(intentS);
            Log.i(APP_TAG, "on receive (after)");
            // Reschedule next run
            OneTimeWorkRequest nextWork = new OneTimeWorkRequest.Builder(NotificationWorker.class)
                .setInitialDelay(15, TimeUnit.MINUTES)
                .build();

            WorkManager.getInstance(getApplicationContext()).enqueue(nextWork);

            return Result.success();

    }
}
