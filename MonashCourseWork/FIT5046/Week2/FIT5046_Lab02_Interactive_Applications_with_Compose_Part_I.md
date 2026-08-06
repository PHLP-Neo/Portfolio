# FIT5046 Lab 2 — Interactive Applications with Compose, Part I

## Lab Focus

This lab introduces Jetpack Compose and basic UI elements, including:

- Layouts
- Buttons
- Toast messages

## Objectives

By the end of the lab, you should be able to:

- Use multiple Compose layouts, particularly `Row` and `Column`.
- Create an interactive application using a button and Toast message.

## Lab Structure

### Part 1 — Demonstration

The tutor demonstrates a simple application that:

- Uses different layouts.
- Uses a button to display a Toast.

### Part 2 — Step-by-Step Exercises

Recreate the demonstrated application using the supplied instructions and code.

### Part 3 — Problem-Solving Exercise

Work in groups to develop a more advanced application based on the concepts covered in the lab.

Online resources may be used, but students should be able to:

- Explain why a source or tool was selected.
- Explain any changes made to the supplied material.
- Present the solution to the class when requested.

A sample solution will be made available on Moodle at the end of the week.

---

# Part 2 — Step-by-Step Exercises

## Task 1 — Column Layout

### Step 1: Create the Project

Create a new Android project named:

```text
LayoutLab
```

### Step 2: Display the Four Seasons Vertically

Create a composable function that displays the season names using a `Column`:

```kotlin
@Composable
fun ColumnLayoutCompose(
    modifier: Modifier = Modifier
) {
    Column(modifier) {
        Text(text = "Spring")
        Text(text = "Summer")
        Text(text = "Autumn")
        Text(text = "Winter")
    }
}
```

> In Android Studio, press **Alt + Enter** to import unresolved classes.

### Step 3: Preview the Composable

Use Android Studio's **Split** view to show the code and preview.

A `@Preview` function must be defined and must call `ColumnLayoutCompose()`:

```kotlin
@Preview(showBackground = true)
@Composable
fun ColumnLayoutPreview() {
    ColumnLayoutCompose()
}
```

For more complex code, the preview may not always work as expected.

### Step 4: Run the Composable

Update both:

- The preview function
- The `onCreate()` method

The original `Greeting` function accepts a `String` parameter. `ColumnLayoutCompose` does not, so remove the unnecessary string argument.

### Step 5: Add a Surface and Padding

Use `Surface` to apply a Material theme colour and add `24.dp` of padding:

```kotlin
@Composable
fun ColumnLayoutCompose(
    modifier: Modifier = Modifier
) {
    Surface(
        color = MaterialTheme.colorScheme.primary
    ) {
        Column(
            modifier = modifier.padding(24.dp)
        ) {
            Text(text = "Spring")
            Text(text = "Summer")
            Text(text = "Autumn")
            Text(text = "Winter")
        }
    }
}
```

Run the preview again to inspect the updated UI.

---

## Task 2 — Row Layout

### Step 6: Display the Seasons Horizontally

Create a `RowLayoutCompose` function:

```kotlin
@Composable
fun RowLayoutCompose(
    modifier: Modifier = Modifier
) {
    Surface(
        color = MaterialTheme.colorScheme.primary
    ) {
        Row(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.SpaceBetween
        ) {
            Text(text = "Spring")
            Text(text = "Summer")
            Text(text = "Autumn")
            Text(text = "Winter")
        }
    }
}
```

`Arrangement.SpaceBetween` distributes the available space between the children.

### Step 7: Update the Preview

Call `RowLayoutCompose()` from the preview function:

```kotlin
@Preview(showBackground = true)
@Composable
fun RowLayoutPreview() {
    RowLayoutCompose()
}
```

---

## Task 3 — Nested Layouts, Button, and Toast

Create a composable function named `ButtonCompose`.

The interface should:

- Display the four seasons at the centre of the screen.
- Place a button below the season names.
- Display a Toast when the button is clicked.

A `Column` is nested inside a `Box` so the content can be centred instead of appearing in the upper-left corner.

```kotlin
@Composable
fun ButtonCompose(
    modifier: Modifier = Modifier
) {
    val context = LocalContext.current

    Box(
        modifier = Modifier.fillMaxSize(),
        contentAlignment = Alignment.Center
    ) {
        Surface(
            color = MaterialTheme.colorScheme.primary
        ) {
            Column(
                modifier = modifier.padding(24.dp),
                horizontalAlignment = Alignment.CenterHorizontally
            ) {
                Text(text = "Spring")
                Text(text = "Summer")
                Text(text = "Autumn")
                Text(text = "Winter")

                Spacer(
                    modifier = Modifier.height(20.dp)
                )

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
        }
    }
}
```

---

# Part 3 — Problem-Solving Exercise

Create a composable application that displays four buttons representing the seasons.

## Requirements

- Display four season buttons.
- Space the buttons equally across the screen.
- When a season button is clicked, show a Toast containing the three Australian months associated with that season.
- Add a large title at the top:

```text
Seasons and Months
```

- Add an appropriate licence-free image.
- Use nested layouts.
- Match the design shown in the lab document.

Suggested image:

<https://www.pexels.com/photo/four-leaves-on-wooden-board-691067/>

## Australian Seasons and Months

| Season | Months |
|---|---|
| Spring | September, October, November |
| Summer | December, January, February |
| Autumn | March, April, May |
| Winter | June, July, August |

## Image Tutorial

Refer to the Android Compose image codelab:

<https://developer.android.com/codelabs/basic-android-kotlin-compose-add-images#0>
