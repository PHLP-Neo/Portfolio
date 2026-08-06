# FIT5046 — Jetpack Compose, Part I

**Unit:** Mobile and Distributed Computing Systems  
**Semester:** Semester 2, 2026  
**Lecturer:** Dr Pari Delir Haghighi

## Contents

- Jetpack Compose
- Composable functions
- UI previews
- Layouts
- Compose phases
- Modifiers
- Surface and Scaffold
- Buttons, Toasts, and text fields

---

## 1. Jetpack Compose

Jetpack Compose is Android's recommended modern declarative toolkit for building user interfaces in Kotlin.

Previously, Android interfaces were commonly defined using XML files. These interfaces often required manual updates, increasing the possibility of errors. Compose allows a UI to be created with Kotlin using a simpler syntax that is easier to update and maintain.

References:

- <https://developer.android.com/compose>
- <https://developer.android.com/jetpack/compose/mental-model>

---

## 2. Composable Functions

Composable functions build the UI.

They differ from ordinary Kotlin functions because they use the `@Composable` annotation.

A composable function:

- Receives data.
- Describes or emits UI elements.

```kotlin
@Composable
fun Greeting(name: String) {
    Text("Hello $name")
}
```

---

## 3. Previewing the UI

To preview a composable function without running the application, create another composable function annotated with `@Preview`.

The preview function must call the function being previewed and provide any required parameters.

```kotlin
@Preview(showBackground = true)
@Composable
fun PreviewDisplayMessage() {
    DisplayMessage("FIT5046")
}
```

In Android Studio, use the **Split** view to show the code and preview together.

---

## 4. Composable Components

Compose provides many reusable UI components.

Common components include:

- `Text`
- `Button`
- `TextField`
- `OutlinedTextField`
- `Surface`
- `Scaffold`

Component reference:

<https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#components>

---

## 5. Layouts

Layouts control the order, alignment, and arrangement of components on the screen.

Common layouts:

- `Column`: places children vertically.
- `Row`: places children horizontally.
- `Box`: places children within the same area and supports alignment or overlap.

Layouts can be nested inside other layouts.

Reference: <https://developer.android.com/jetpack/compose/layouts/basics>

### 5.1 Column

```kotlin
@Composable
fun ColumnTest(modifier: Modifier = Modifier) {
    Column(modifier = modifier.padding(24.dp)) {
        Text("the first Text")
        Text("the second Text")
    }
}
```

### 5.2 Row and Nested Column

```kotlin
@Composable
fun RowAndColumn() {
    Row(
        verticalAlignment = Alignment.CenterVertically
    ) {
        Icon(
            imageVector = Icons.Default.Person,
            contentDescription = "Person"
        )

        Column {
            Text("the first Text")
            Text("the second Text")
        }
    }
}
```

### 5.3 Common Layout Parameters

Simplified `Column` structure:

```kotlin
@Composable
fun Column(
    modifier: Modifier = Modifier,
    verticalArrangement: Arrangement.Vertical = Arrangement.Top,
    horizontalAlignment: Alignment.Horizontal = Alignment.Start,
    content: @Composable ColumnScope.() -> Unit
)
```

Simplified `Row` structure:

```kotlin
@Composable
fun Row(
    modifier: Modifier = Modifier,
    horizontalArrangement: Arrangement.Horizontal = Arrangement.Start,
    verticalAlignment: Alignment.Vertical = Alignment.Top,
    content: @Composable RowScope.() -> Unit
)
```

### 5.4 Box

A `Box` can align an element relative to the available space:

```kotlin
@Composable
fun Greeting(
    name: String,
    modifier: Modifier = Modifier
) {
    Box(Modifier.fillMaxSize()) {
        Text(
            text = "Welcome to $name!",
            fontSize = 30.sp,
            modifier = Modifier.align(Alignment.Center)
        )
    }
}
```

---

## 6. Compose Phases

Compose transforms data into visible UI through three main phases:

```text
Data → Composition → Layout → Drawing → UI
```

### 6.1 Composition

The Compose runtime executes composable functions and creates a tree describing what the UI should contain.

### 6.2 Layout

Compose measures the UI elements and places them at two-dimensional coordinates.

### 6.3 Drawing

Compose traverses the layout tree and draws the UI elements on the device screen.

Reference: <https://developer.android.com/develop/ui/compose/phases>

---

## 7. Modifiers

Modifiers decorate UI elements or add behaviour.

Examples include:

- Padding
- Background colour
- Size
- Alignment
- Click behaviour

Modifier order affects the result because each operation modifies the value returned by the previous operation.

```kotlin
Text(
    text = "Hello",
    modifier = Modifier
        .background(Color.Red)
        .padding(16.dp)
)
```

In this example:

1. The red background is applied.
2. Padding is added inside the red area around the text.

Reference: <https://developer.android.com/jetpack/compose/modifiers>

---

## 8. Surface

A `Surface` wraps composable elements and can provide:

- Background colours
- Borders
- Elevation and shadows

`Surface` is a central concept in Material Design.

```kotlin
@Composable
fun SeasonPanel() {
    Surface(
        color = MaterialTheme.colorScheme.primary
    ) {
        Text(
            text = "Spring",
            modifier = Modifier.padding(16.dp)
        )
    }
}
```

Reference:

<https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#surfaces-and-layout>

---

## 9. Scaffold

`Scaffold` provides a standard structure for complex Material Design interfaces.

It can organise elements such as:

- Top app bar
- Bottom app bar
- Floating action button
- Main content

The content lambda receives padding values that should be applied to prevent content from appearing underneath scaffold elements.

```kotlin
@Composable
fun ExampleScreen() {
    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Example") }
            )
        }
    ) { innerPadding ->
        Text(
            text = "Screen content",
            modifier = Modifier.padding(innerPadding)
        )
    }
}
```

Reference: <https://developer.android.com/jetpack/compose/components/scaffold>

---

## 10. Button

A button is a composable UI element. Material Design 3 provides several button styles, such as elevated, filled, tonal, outlined, and text buttons.

Simplified API:

```kotlin
@Composable
fun Button(
    onClick: () -> Unit,
    modifier: Modifier = Modifier,
    enabled: Boolean = true,
    content: @Composable RowScope.() -> Unit
)
```

- `onClick` is a lambda containing the code to run when the button is clicked.
- `content` is a composable lambda defining the UI inside the button.

Example:

```kotlin
Button(
    onClick = {
        println("Clicked")
    }
) {
    Text("Click")
}
```

Reference: <https://developer.android.com/jetpack/compose/components/button>

---

## 11. Toast

A Toast displays a short message in a small popup.

`Toast.makeText()` requires:

1. An activity context.
2. The text to display.
3. A duration: `Toast.LENGTH_SHORT` or `Toast.LENGTH_LONG`.

Call `.show()` to display the Toast.

```kotlin
@Composable
fun ToastButton() {
    val context = LocalContext.current

    ElevatedButton(
        onClick = {
            Toast.makeText(
                context,
                "This is a Toast",
                Toast.LENGTH_SHORT
            ).show()
        }
    ) {
        Text("Click")
    }
}
```

Reference: <https://developer.android.com/guide/topics/ui/notifiers/toasts>

---

## 12. TextField

A `TextField` captures user input. Text fields are commonly used in forms and dialogs.

Material Design provides:

- Filled text fields
- Outlined text fields

A text field typically has:

- A current `value`
- An `onValueChange` lambda
- A label

```kotlin
@Composable
fun NameField() {
    var name by remember {
        mutableStateOf("")
    }

    OutlinedTextField(
        value = name,
        onValueChange = {
            name = it
        },
        label = {
            Text("Name")
        }
    )
}
```

The relevant function type is:

```kotlin
onValueChange: (String) -> Unit
```

References:

- <https://m3.material.io/components/text-fields/overview>
- <https://m3.material.io/components/text-fields/specs>

---

## References

- <https://developer.android.com/compose>
- <https://developer.android.com/jetpack/compose/mental-model>
- <https://developer.android.com/develop/ui/compose/phases>
- <https://developer.android.com/jetpack/compose/layouts/basics>
- <https://developer.android.com/jetpack/compose/components/button>
- <https://developer.android.com/jetpack/compose/components/scaffold>
- <https://developer.android.com/jetpack/compose/modifiers>
- <https://m3.material.io/components/text-fields/overview>
- <https://www.youtube.com/watch?v=0yK7KoruhSM>
