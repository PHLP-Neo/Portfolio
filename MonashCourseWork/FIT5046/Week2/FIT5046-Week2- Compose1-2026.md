

FIT5046: Mobile and Distributed Computing Systems
Dr Pari DelirHaghighi
## Semester 2, 2026
Jetpack Compose (Part I)

## Contents
•Jetpack Compose
•Composable functions
•Layouts
•Composable Components

## Jetpack Compose
•Jetpack Compose is Android’s recommended modern
declarative toolkit for building UIs in Kotlin
•Previously, XML files were used to build the UI, which
required manual updates, increasing the possibility of
errors.
•To address this, Compose was introduced.
•Compose allows creating UIs using a simple and
intuitive syntax, making it easier to update and maintain.
https://developer.android.com/compose
https://developer.android.com/jetpack/compose/mental-model

## Composable Functions
•Composablefunctions are used for building the UI
•They are different from other Kotlin functions. They have the
@Composable annotation
•A composable function takes in data and emit UI elements
https://developer.android.com/jetpack/compose/mental-model

How to preview the UI?
•To preview a @Composable function, you need to write
another function annotated with @Preview.
•The preview function must call the composable function and
pass any required parameters.
@Preview(showBackground = true)
@Composable
fun PreviewDisplayMessage() {
DisplayMessage(“FIT5046")
## }
Use the split (code and design)
to view both code and UI

•You can create the UI with different UI
components using a  number of
available @Composable components
•Common components: Text, Button,
and TextField
List of Composable Components
List of Components:
https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#components

## Layouts
•Layouts allow us to specify the order, alignment and arrangement of UI
components (e.g., a Text and a Button) on the screen
•Common layouts: Column, Row, and Box
•You can nest a layout in another layout
https://developer.android.com/jetpack/compose/layouts/basics

## Layout Examples
•Column
•Row
Source https://developer.android.com/jetpack/compose/layouts/basics
@Composable
fun RowAndColumn() {
Row(verticalAlignment = Alignment.CenterVertically) {
Icon(imageVector = Icons.Default.Person, contentDescription = "Person")
## Column {
Text(“the first Text")
Text(“the second Text")
## }
## }
## }
@Composable
fun ColumnTest() {
Column (modifier = modifier.padding(24.dp)){
Text(“the first Text")
Text(“the second Text")
## }
## }

@Composable
public inline fun Column(
modifier: Modifier = Modifier,
verticalArrangement: Arrangement. Vertical = Arrangement.Top,
horizontalAlignment: Alignment. Horizontal = Alignment.Start,
content: @Composable() (ColumnScope.() -> Unit)
## ): Unit
@Composable
public inline fun Row(
modifier: Modifier = Modifier,
horizontalArrangement: Arrangement. Horizontal = Arrangement.Start,
verticalAlignment: Alignment. Vertical = Alignment.Top,
content: @Composable() (RowScope.() -> Unit)
## ): Unit
Column API reference documentation
Row API reference documentation

## Box Layout
•Box
@Composable
fun Greeting(name: String, modifier: Modifier = Modifier) {
Box(Modifier.fillMaxSize()) {
## Text(
text = "Welcome to $name!",
fontSize = 30.sp,
modifier = Modifier.align(Alignment.Center))
## }
## }

## Compose Phases - Composition
Composition Phase: Compose runtime executes composable
functions to create a tree structure of what UI will show
DataCompositionLayoutDrawingUI
https://developer.android.com/develop/ui/compose/phases

Layout Phase: this phase involves measurement and placement of
layout elements in 2D coordinates
DataCompositionLayoutDrawingUI
https://developer.android.com/develop/ui/compose/phases
## Compose Phases - Layout

Drawing Phase: traversing the tree from top to bottom, and drawing
UI elements draw onto a device screen
DataCompositionLayoutDrawingUI
https://developer.android.com/develop/ui/compose/phases
## Compose Phases - Drawing

UI Components and Layouts: Modifiers
•Modifiers are used to decorate or add behavior to
UI elements
•Each modifier function makes changes to the Modifier
returned by the previous function, so the order of
modifiers affects the final result
•In this example, the background is applied first, creating
a red box.Then, padding is added inside that red box,
surrounding the text.
https://developer.android.com/jetpack/compose/modifiers
@Composable
fun Greeting(name: String, modifier: Modifier = Modifier) {
Box(Modifier.fillMaxSize()) {
## Text(
text = "Welcome to $name!",
fontSize = 30.sp,
modifier = Modifier.align(Alignment.Center))
## }
## }
## Text(
"Hello",
modifier = Modifier
.background(Color.Red)
## .padding(16.dp)
## )

## Surface
•A Surface is used to wrap composable UI elements, decorating them with background
colours, borders, or elevation to add shadows that represent depth
•Surface is the central metaphor in material design
https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#surfaces-and-layout

## Scaffold
•A scaffold is a key structure in Material
## Design
•It provides a standardised platform for
creating complex user interfaces, e.g., a
BottomBar
•It holds together different parts of the UI,
e.g., when using top and bottom app bars
•When using Scaffold, you must provide
padding values at the end to provide a
padding from start, end, top or bottom
https://developer.android.com/jetpack/compose/components/scaffold
https://developer.android.com/jetpack/compose/components/scaffold#example

## Button
•Button is a composable function used in the UI
•A button can have different appearances according to Material
Design 3 (M3)
https://m3.material.io/components/buttons/overview
Example of Elevated Button

Button API reference documentation
@Composable
@ComposableInferredTarget
public fun Button(
onClick: () -> Unit,
modifier: Modifier = COMPILED_CODE,
enabled: Boolean = COMPILED_CODE,
shape: Shape = COMPILED_CODE,
colors: ButtonColors = COMPILED_CODE,
elevation: ButtonElevation? = COMPILED_CODE,
border: BorderStroke? = COMPILED_CODE,
contentPadding: PaddingValues = COMPILED_CODE,
interactionSource: MutableInteractionSource = COMPILED_CODE,
content: @Composable() (RowScope.() -> Unit)
## ): Unit
The onClick() is a lambda function that specifies
the code to run when the button is clicked
The content is a lambda function that defines the
UI inside the Button, which will be placed
horizontally (Row)
https://developer.android.com/jetpack/compose/components/button

## Button Lambda Parameters
ElevatedButton(
onClick = {
Toast.makeText(
context,
“This is a Toast",
Toast.LENGTH_SHORT)
## .show()
## }
## ) {
Text("Click")
## }
@Composable
@ComposableInferredTarget
public fun Button(
onClick: () -> Unit,
modifier: Modifier = COMPILED_CODE,
enabled: Boolean = COMPILED_CODE,
shape: Shape = COMPILED_CODE,
colors: ButtonColors = COMPILED_CODE,
elevation: ButtonElevation? = COMPILED_CODE,
border: BorderStroke? = COMPILED_CODE,
contentPadding: PaddingValues = COMPILED_CODE,
interactionSource: MutableInteractionSource = COMPILED_CODE,
content: @Composable() (RowScope.() -> Unit)
## ): Unit

## A Toast
•A Toast can be used to display simple messages or feedback in
a small popup
•We call the Toast.makeText() method to return the Toast object
•It requires 3 parameters:
1.The activity Context (get Context by calling LocalContext.current )
2.The text to display
3.The duration that the toast should be displayed
(LENGTH_SHORT or LENGTH_LONG)
•The show() method is called on the returned object to display the
text
https://developer.android.com/guide/topics/ui/notifiers/toasts
Toast.makeText(
context,
“This is a Toast",
Toast.LENGTH_SHORT)
## .show()
## }
val context =LocalContext.current

TextField
•A TextField is used to capture input from the
user
•TextFields are usually used in forms and
dialogs
•Two types: filled and outlined
•TextField has a label and a value (to be entered
by the user)
https://m3.material.io/components/text-fields/overview
https://m3.material.io/components/text-fields/specs

TextField
TextField API reference documentation
OutlinedTextField code example
@Composable
@ComposableInferredTarget
public fun OutlinedTextField(
value: String,
onValueChange: (String) -> Unit,
modifier: Modifier = COMPILED_CODE,
enabled: Boolean = COMPILED_CODE,
readOnly: Boolean = COMPILED_CODE,
textStyle: TextStyle = COMPILED_CODE,
label: @Composable() (() -> Unit)? = COMPILED_CODE,
placeholder: @Composable() (() -> Unit)? = COMPILED_CODE,
leadingIcon: @Composable() (() -> Unit)? = COMPILED_CODE,
trailingIcon: @Composable() (() -> Unit)? = COMPILED_CODE,
prefix: @Composable() (() -> Unit)? = COMPILED_CODE,
suffix: @Composable() (() -> Unit)? = COMPILED_CODE,
supportingText: @Composable() (() -> Unit)? = COMPILED_CODE,
isError: Boolean = COMPILED_CODE,
visualTransformation: VisualTransformation = COMPILED_CODE,
keyboardOptions: KeyboardOptions = COMPILED_CODE,
keyboardActions: KeyboardActions = COMPILED_CODE,
singleLine: Boolean = COMPILED_CODE,
maxLines: Int = COMPILED_CODE,
minLines: Int = COMPILED_CODE,
interactionSource: MutableInteractionSource = COMPILED_CODE,
shape: Shape = COMPILED_CODE,
colors: TextFieldColors = COMPILED_CODE
## ): Unit
OutlinedTextField(
value = “Outlined”,
onValueChange = { //do something},
label = { Text(“Text field") }
## )
OutlinedTextField(
value = name,
onValueChange = { name = it },
label = { Text("Name") }
## )

## References
https://developer.android.com/compose
https://developer.android.com/jetpack/compose/mental-model
https://developer.android.com/develop/ui/compose/phases
https://developer.android.com/jetpack/compose/layouts/basics
https://developer.android.com/jetpack/compose/components/button
https://developer.android.com/jetpack/compose/components/scaffold
https://developer.android.com/reference/kotlin/androidx/compose/material/packag
e-summary#surfaces-and-layout
https://developer.android.com/jetpack/compose/modifiers
https://m3.material.io/components/text-fields/overview
From data to UI: Compose phases
https://www.youtube.com/watch?v=0yK7KoruhSM