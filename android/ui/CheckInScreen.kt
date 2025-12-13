package com.safeconnect.app.ui

import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.safeconnect.app.network.CheckInType
import com.safeconnect.app.viewmodel.CheckInViewModel

@Composable
fun CheckInScreen(viewModel: CheckInViewModel) {

    val status by viewModel.status.collectAsState()
    val history by viewModel.history.collectAsState()
    val isLoading by viewModel.isLoading.collectAsState()
    val error by viewModel.error.collectAsState()

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(20.dp)
    ) {
        Text("SafeConnect", style = MaterialTheme.typography.headlineLarge)

        Spacer(Modifier.height(16.dp))

        if (error != null) {
            Text(
                text = error!!,
                color = MaterialTheme.colorScheme.error
            )
            Spacer(Modifier.height(8.dp))
        }

        if (isLoading) {
            LinearProgressIndicator(modifier = Modifier.fillMaxWidth())
            Spacer(Modifier.height(12.dp))
        }

        Button(
            onClick = { viewModel.sendCheckIn(CheckInType.OK) },
            modifier = Modifier.fillMaxWidth(),
            enabled = !isLoading
        ) {
            Text("I'm OK ✔️")
        }

        Spacer(Modifier.height(8.dp))

        Button(
            onClick = { viewModel.sendCheckIn(CheckInType.NEED_TO_TALK) },
            modifier = Modifier.fillMaxWidth(),
            enabled = !isLoading,
            colors = ButtonDefaults.buttonColors(
                containerColor = MaterialTheme.colorScheme.errorContainer
            )
        ) {
            Text("Need to Talk ☎️")
        }

        Spacer(Modifier.height(12.dp))

        OutlinedButton(
            onClick = { viewModel.clearHistory() },
            modifier = Modifier.fillMaxWidth(),
            enabled = history.isNotEmpty() && !isLoading
        ) {
            Text("Clear history")
        }

        Spacer(Modifier.height(16.dp))

        Text("Status: $status")

        Spacer(Modifier.height(16.dp))

        Text("History", style = MaterialTheme.typography.titleMedium)
        Spacer(Modifier.height(8.dp))

        LazyColumn {
            items(history) { item ->
                Card(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(vertical = 4.dp)
                ) {
                    Text(
                        text = item,
                        modifier = Modifier.padding(12.dp)
                    )
                }
            }
        }
    }
}