package com.safeconnect.app

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            SafetyCheckInScreen()
        }
    }
}

@Composable
fun SafetyCheckInScreen() {
    var history by remember { mutableStateOf(listOf<String>()) }

    Surface(
        modifier = Modifier.fillMaxSize(),
        color = MaterialTheme.colorScheme.background
    ) {
        Column(
            modifier = Modifier
                .padding(20.dp)
                .fillMaxSize(),
            verticalArrangement = Arrangement.Center,
            horizontalAlignment = Alignment.CenterHorizontally
        ) {

            Text("Safety Check-in", style = MaterialTheme.typography.headlineMedium)
            Spacer(modifier = Modifier.height(20.dp))

            Button(
                onClick = {
                    history = history + "I'm OK ✔️ — ${java.time.LocalTime.now()}"
                },
                modifier = Modifier.fillMaxWidth()
            ) {
                Text("I'm OK ✔️")
            }

            Spacer(modifier = Modifier.height(10.dp))

            Button(
                onClick = {
                    history = history + "Need to Talk ☎️ — ${java.time.LocalTime.now()}"
                },
                modifier = Modifier.fillMaxWidth(),
                colors = ButtonDefaults.buttonColors(MaterialTheme.colorScheme.errorContainer)
            ) {
                Text("Need to Talk ☎️")
            }

            Spacer(modifier = Modifier.height(30.dp))

            Text("History:", style = MaterialTheme.typography.titleMedium)

            history.forEach {
                Text("• $it")
            }
        }
    }
}
