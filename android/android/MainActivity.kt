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
import com.safeconnect.app.network.CheckInRequest
import com.safeconnect.app.network.CheckInType
import com.safeconnect.app.network.CreateUserRequest
import com.safeconnect.app.network.RetrofitClient
import kotlinx.coroutines.launch

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContent {
            AppUI()
        }
    }
}

@Composable
fun AppUI() {
    var userId by remember { mutableStateOf<String?>(null) }
    var history by remember { mutableStateOf(listOf<String>()) }
    var status by remember { mutableStateOf("") }

    val api = RetrofitClient.api
    val scope = rememberCoroutineScope()

    fun sendCheck(type: CheckInType) {
        scope.launch {
            status = "Sending..."

            if (userId == null) {
                val user = api.createUser(CreateUserRequest("Android User"))
                userId = user.id
            }

            val id = userId!!
            val response = api.createCheckIn(id, CheckInRequest(type))
            history = history + "${type.name} → ${response.timestamp}"

            status = "Done!"
        }
    }

    Column(
        modifier = Modifier.fillMaxSize().padding(20.dp),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center
    ) {

        Text("SafeConnect App", style = MaterialTheme.typography.headlineLarge)

        Spacer(Modifier.height(20.dp))

        Button(onClick = { sendCheck(CheckInType.OK) }, modifier = Modifier.fillMaxWidth()) {
            Text("I'm OK ✔️")
        }

        Spacer(Modifier.height(10.dp))

        Button(onClick = { sendCheck(CheckInType.NEED_TO_TALK) }, modifier = Modifier.fillMaxWidth()) {
            Text("Need to Talk ☎️")
        }

        Spacer(Modifier.height(20.dp))

        Text("Status: $status")

        Spacer(Modifier.height(20.dp))

        Text("History:")
        history.forEach { Text("• $it") }
    }
}
