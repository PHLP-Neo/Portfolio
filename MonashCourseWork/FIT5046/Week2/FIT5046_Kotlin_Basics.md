# FIT5046 — Kotlin Basics

**Unit:** Mobile and Distributed Computing Systems  
**Semester:** Semester 2, 2026  
**Lecturer:** Dr Pari Delir Haghighi

## Contents

- Kotlin classes
- Properties and variables
- Null safety
- Functions
- Constructors and inheritance
- Lambdas
- Lists and additional Kotlin concepts

---

## 1. Android and Kotlin

- Kotlin was designed by JetBrains.
- Kotlin is a modern, concise, and safe programming language.
- Kotlin is interoperable with Java.
- Kotlin is statically typed and supports type inference.
- Kotlin is Google's recommended language for Android application development.

References:

- <https://kotlinlang.org/docs/home.html>
- <https://developer.android.com/kotlin/first>

---

## 2. Kotlin Classes

A class is a template for creating objects, similar to a class in Java.

A Kotlin class can contain:

- **Properties:** values associated with an object.
- **Functions:** operations that an object can perform.

Classes are declared with the `class` keyword:

```kotlin
class Person {
    // ...
}
```

Kotlin classes are `final` by default, meaning that they cannot be inherited from unless they are explicitly marked as `open`.

Reference: <https://kotlinlang.org/docs/classes.html>

---

## 3. Properties and Variables

`Variable` is a general term for a named value. More specific terminology depends on where the declaration appears:

- A declaration inside a class, interface, or object is a **property**.
- A declaration inside a function is a **local variable**.

### 3.1 Declaring Properties and Local Variables

General syntax:

```kotlin
var propertyName: PropertyType = initializer
val propertyName: PropertyType = initializer
```

Use `var` for a mutable declaration:

```kotlin
var message: String = "Hello"
message = "Goodbye"
```

Use `val` for a read-only declaration:

```kotlin
val number: Int = 1
number = 5 // Error: val cannot be reassigned
```

References:

- <https://kotlinlang.org/docs/properties.html>
- <https://developer.android.com/kotlin/learn#variables>

### 3.2 Type Inference

The declared type is optional when Kotlin can infer it from the initializer:

```kotlin
val number = 1       // Inferred as Int
var message = "Hello" // Inferred as String
```

Reference: <https://kotlinlang.org/docs/basic-types.html>

### 3.3 Initialisation

Properties and local variables must be initialised before they are used.

Uninitialised class properties produce an error:

```kotlin
class Test(name: String) {
    val number: Int
    var message: String
}
```

A local variable may be declared first and assigned before use:

```kotlin
fun display() {
    var message: String
    message = "Hello"
    println(message)
}
```

### 3.4 Late Initialisation

Use `lateinit` when a property will be assigned later:

```kotlin
class Test {
    private lateinit var lateMessage: String

    fun testLateinit() {
        lateMessage = "Hello"
    }
}
```

Rules for `lateinit`:

- The property must be non-nullable.
- It must be declared with `var`, not `val`.
- It cannot be used with primitive types.

Reference: <https://kotlinlang.org/docs/properties.html#late-initialized-properties-and-variables>

---

## 4. Null Safety

Kotlin uses null safety to reduce null-reference errors such as Java's `NullPointerException`.

Variables are non-nullable by default:

```kotlin
var name: String = null // Error
```

Add `?` to the type to allow `null`:

```kotlin
var name: String? = null
```

Reference: <https://kotlinlang.org/docs/null-safety.html>

### 4.1 Working with Nullable Values

#### Option 1: Explicit null check

```kotlin
if (message != null) {
    println(message.length)
}
```

#### Option 2: Safe-call operator `?.`

```kotlin
val msgLength = message?.length
```

The expression calls `length` only when `message` is not `null`. The inferred result type is `Int?`.

#### Option 3: Non-null assertion operator `!!`

```kotlin
val msgLength = message!!.length
```

The expression treats `message` as non-null and returns an `Int`, but throws an exception when `message` is `null`.

References:

- <https://kotlinlang.org/docs/null-safety.html#safe-calls>
- <https://kotlinlang.org/docs/null-safety.html#the-operator>

---

## 5. Functions

Functions are declared with the `fun` keyword.

A function:

- Performs a specific task.
- May accept arguments.
- May return a value.
- Cannot declare parameters with `var` or `val`.
- Has a return type of `Unit` when it does not return a meaningful value.

`Unit` is similar to Java's `void`.

```kotlin
fun printHello(name: String?) {
    println("Hello, $name")
}
```

The explicit form is:

```kotlin
fun printHello(name: String?): Unit {
    println("Hello, $name")
    return Unit
}
```

### 5.1 Default Parameters

A default value allows an argument to be omitted:

```kotlin
fun display(
    name: String,
    surname: String,
    age: Int,
    isStudying: Boolean = true
) {
    // ...
}
```

The last argument can be omitted:

```kotlin
display("Helen", "Jones", 28)
```

### 5.2 Named Arguments

Arguments can be passed by parameter name:

```kotlin
fun display(name: String, age: Int) {
    // ...
}

display(name = "Alice", age = 20)
display(age = 20, name = "Alice")
```

Named arguments allow the argument order to be changed.

---

## 6. Constructors

### 6.1 Primary Constructor

A primary constructor is declared in the class header:

```kotlin
class Person(firstName: String) {
    // ...
}
```

The default visibility modifier in Kotlin is `public`.

References:

- <https://kotlinlang.org/docs/classes.html#constructors>
- <https://kotlinlang.org/docs/visibility-modifiers.html>

### 6.2 Constructor Parameters as Properties

Use `val` or `var` to make a constructor parameter a class property:

```kotlin
class Test(var name: String) {
    fun rename() {
        name = "John"
    }
}
```

Without `val` or `var`, the constructor parameter is not a mutable class property:

```kotlin
class Test(name: String) {
    fun rename() {
        // name = "John" // Not valid here
    }
}
```

### 6.3 Multiple Parameters

```kotlin
class Person(
    val firstName: String,
    val lastName: String,
    var age: Int,
)
```

A trailing comma may be used.

---

## 7. Inheritance

Kotlin classes are final by default. Mark a base class as `open` to allow inheritance:

```kotlin
open class Test(name: String) {
    // ...
}
```

A subclass uses a colon followed by the base-class constructor:

```kotlin
class TestSub : Test("Hello") {
    // ...
}
```

Android activities commonly follow the same syntax:

```kotlin
class MainActivity : ComponentActivity() {
    // ...
}
```

---

## 8. Function-Type Parameters and Lambdas

A function-type parameter expects another function rather than an ordinary value.

A lambda is an anonymous function that can be passed directly as an argument.

```kotlin
fun calculate(num: Int, doubleIt: (Int) -> Int): Int {
    return doubleIt(num)
}
```

Pass a lambda as an argument:

```kotlin
calculate(7, { x: Int -> x * 2 })
```

When the lambda is the final parameter, trailing-lambda syntax may be used:

```kotlin
calculate(7) { x: Int -> x * 2 }
```

### 8.1 Higher-Order Functions

A higher-order function accepts a function as a parameter or returns a function.

```kotlin
fun calculate(num: Int, doubleIt: (Int) -> Int): Int {
    val result = doubleIt(num)
    return result
}
```

Equivalent calls:

```kotlin
val result1 = calculate(7, { x: Int -> x * 2 })

val result2 = calculate(7) { x: Int ->
    x * 2
}

val result3 = calculate(7) {
    it * 2
}

val result4 = calculate(
    7,
    doubleIt = { it * 2 }
)
```

When a lambda has one parameter, Kotlin allows the implicit name `it`.

Reference: <https://kotlinlang.org/docs/lambdas.html#higher-order-functions>

### 8.2 `it` in Jetpack Compose

`OutlinedTextField` uses a function-type parameter for `onValueChange`:

```kotlin
OutlinedTextField(
    value = name,
    onValueChange = { name = it },
    label = { Text("Name") },
    modifier = Modifier.padding(bottom = 8.dp)
)
```

The concise lambda:

```kotlin
onValueChange = { name = it }
```

is equivalent to:

```kotlin
onValueChange = { newName ->
    name = newName
}
```

Its expected type is:

```kotlin
onValueChange: (String) -> Unit
```

---

## 9. Lists in Kotlin

A `List<T>` stores ordered items and supports indexed access beginning at index `0`.

### Immutable List

```kotlin
val fruits = listOf("orange", "pear", "apple")
```

### Mutable List

```kotlin
val fruits = mutableListOf("orange", "pear", "apple")

fruits.remove("pear")
fruits.add("mango")
```

A mutable collection is normally assigned to `val`. This prevents replacing the collection reference while still allowing its contents to change.

Reference: <https://kotlinlang.org/docs/collections-overview.html#list>

---

## 10. Additional Concepts

- Arrays: <https://kotlinlang.org/docs/arrays.html>
- Sets: <https://kotlinlang.org/docs/collections-overview.html#set>
- Maps: <https://kotlinlang.org/docs/collections-overview.html#map>
- Elvis operator: <https://kotlinlang.org/docs/null-safety.html#elvis-operator>
- Named arguments: <https://kotlinlang.org/docs/functions.html#named-arguments>

---

## 11. Code-Reading Exercise

Identify the following elements:

- Class
- Primary constructor and parameters
- `var` and `val` properties
- Functions, parameters, and return values
- Nullable variables
- Safe calls and non-null assertions
- Lambda parameters

```kotlin
class Calculation(private val num: Int) {
    private val inchConverter = 0.393701

    fun echoThis(count: Int): Int {
        var total = 0

        for (i in 1..count) {
            total += i
        }

        return total
    }

    fun convertCMtoInch(): Double {
        return num * inchConverter
    }

    fun changeToUpperCase(word: String?): String? {
        return word?.uppercase()
    }

    fun changeToUpperCase1(word: String?): String {
        return word!!.uppercase()
    }

    fun changeToUpperCase2(word: String?): String {
        var result = ""

        if (word != null) {
            result = word.uppercase()
        }

        return result
    }

    fun wordLength(word: String?): Int {
        return word!!.length
    }

    fun calculate(doubleIt: (Int) -> Int): Int {
        return doubleIt(num)
    }
}
```

### Output Exercise

Determine what the following code prints:

```kotlin
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val calculator = Calculation(7)

        val result = calculator.calculate { it * 2 }
        println("lambda double function: $result")

        val result2 = calculator.changeToUpperCase("hello")
        println("Change to uppercase function: $result2")

        val result3 = calculator.wordLength("hello")
        println("Word length function: $result3")

        val result4 = calculator.echoThis(5)
        println("Counter function: $result4")
    }
}
```

Expected output:

```text
lambda double function: 14
Change to uppercase function: HELLO
Word length function: 5
Counter function: 15
```
