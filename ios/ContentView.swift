import SwiftUI

struct ContentView: View {
    @State private var history: [String] = []

    var body: some View {
        VStack(spacing: 20) {
            Text("Safety Check-in")
                .font(.title)
                .bold()

            Button("I'm OK ✔️") {
                history.append("I'm OK ✔️ — \(Date())")
            }
            .buttonStyle(.borderedProminent)

            Button("Need to Talk ☎️") {
                history.append("Need to Talk ☎️ — \(Date())")
            }
            .buttonStyle(.bordered)

            Divider()

            Text("History")
                .font(.title3)
                .padding(.top)

            List(history, id: \.self) { item in
                Text(item)
            }
        }
        .padding()
    }
}

#Preview {
    ContentView()
}
