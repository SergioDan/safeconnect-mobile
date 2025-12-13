package com.safeconnect.app

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import com.safeconnect.app.storage.LocalStore
import com.safeconnect.app.ui.CheckInScreen
import com.safeconnect.app.viewmodel.CheckInViewModel

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val store = LocalStore(applicationContext)
        val viewModel = CheckInViewModel(store)

        setContent {
            CheckInScreen(viewModel = viewModel)
        }
    }
}
