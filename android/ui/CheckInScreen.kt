package com.safeconnect.app.ui

import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.safeconnect.app.network.CheckInType
import com.safeconnect.app.viewmodel.CheckInViewModel

@Composable
fun CheckInScreen(viewModel: CheckInViewModel) {

    val status by viewModel.status.collectAsState()
    val history by viewModel.history.collectAsState()

    Column(
        modifier = Modifier.fillMaxSize().padding(20.dp),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center
    ) {
        Text("SafeConnect", style = MaterialTheme.typography.headlineLarge)

        Spacer(Modifier.height(20.dp))

        Button(
            onClick = { viewModel.sendCheckIn(CheckInType.OK) },
            modifier = Modifier.fillMaxWidth()
        ) {
            Text("I'm OK ✔️")
        }

        Spacer(Modifier.height(10.dp))

        Button(
            onClick = { viewModel.sendCheckIn(CheckInType.NEED_TO_TALK) },
            modifier = Modifier.fillMaxWidth()
        ) {
            Text("Need to Talk ☎️")
        }

        Spacer(Modifier.height(20.dp))
        Text("Status: $status")

        Spacer(Modifier.height(20.dp))
        Text("History:")
        history.forEach { Text("• $it") }
    }
}
