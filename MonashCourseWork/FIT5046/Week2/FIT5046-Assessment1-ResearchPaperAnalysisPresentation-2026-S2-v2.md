

FIT5046: Mobile and Distributed Computing Systems
Dr Pari DelirHaghighi
## Semester 2, 2026
## Kotlin Basics

## Contents
•Kotlin Classes
•Properties and variables
•Null Safety
•Functions
•Constructor and inheritance
•Lambdas

Android and Kotlin
•Kotlin was designed by JetBrains
•Kotlin is a modern, concise, safe programming
language, interoperable with Java
•Kotlin is a statically typed programming language with
type inference
•Kotlin is Google's recommended language for Android
app development
https://kotlinlang.org/docs/home.html
https://developer.android.com/kotlin/first

## Kotlin – Classes
•Kotlin classes are like templates for objects (similar to Java)
•Each class can contain variables (properties) and methods
(functions) to operate on the object
•Classes in Kotlin are declared using the keyword class
class Person { /*...*/ }
•By default, Kotlin classes are final (cannot have a
subclass)
https://kotlinlang.org/docs/classes.html

## Kotlin Basics
•Kotlin Classes
•Properties and variables
•Null Safety
•Functions
•Constructor and inheritance
•Lambdas

Properties and Variables
•Variable is a general term for a named value
•In Kotlin, the more specific term depends on where it is
declared:
•A declaration inside a class, an interface or object is called
a property
•A declaration inside a function is called a local variable

Declaring Properties and Local Variables
•The syntax to declare a property/variable:
var/val <propertyName>[: <PropertyType>] [= <property_initializer>]
•Properties & variables in Kotlin classes are declared as var or val
•var is used for mutable declarations (values can be changed)
var message: String=“Hello“
•val is used for read-only declarations
val number: Int = 1
number = 5
https://kotlinlang.org/docs/properties.html
=> Error: val cannot be reassigned
https://developer.android.com/kotlin/learn#variables

Properties and Variables: Type Inference
•Declaring the type of a property or variable is optional
•It can be provided explicitly, or it can be inferred by the
complier from the initializer (type inference)
•Examples:
val number = 1 //inferred as Int
var message = “Hello”  // inferred as String
https://kotlinlang.org/docs/properties.html
https://kotlinlang.org/docs/basic-types.html
More information about types see:

Properties and Variables: Initialize
•Both properties and local variables must be initialised before
they are used
•Local variables can be declared first and initialised later
https://kotlinlang.org/docs/properties.html#late-initialized-properties-and-variables
class Test (name:String) {
val number:Int
var message:String
## ...
## }
-> both will give an error
fun display() {
var message: String
message = "Hello"
println(message)
## }
-> This will not give an error

## Late Initialization
•If you need to initialize the property/variable later in your code, you can use
the lateinit modifier. This means its value will be assigned later in the code.
•The rules about using the lateinit modifier
•The property must be non-nullable
•It can only be used on mutable (var) properties (cannot be used with val)
•It cannot be used with a primitive type
https://kotlinlang.org/docs/properties.html#late-initialized-properties-and-variables
class Test() {
private lateinit var lateMessage: String
fun testLateinit(){
lateMessage = "Hello"
## }
## }

## Kotlin – Null Safety
•Null Safety refers to how Kotlin tries to eliminate the big
problem of null references (NullPointerException in java)
•In Kotlin, variables are non-nullable by default (cannot be
assigned a null value to them)

•To allow a variable to become nullable and have a null value,
a safe call operator (?) is used
https://kotlinlang.org/docs/null-safety.html
var name: String = null
⇒ error
var name: String? = null

Nullable Types and Null Safety
After declaring a nullable variable, we must deal with nullable references:
Option 1: check for nullability explicitly with the if conditional expression
Option 2: make a safe call by using this symbol ?.
val msgLength = message?.length  //here the type of msgLength is inferred as Int?
‘?.’ means that if ‘message’ is not null‘, ‘length’ can be called on it
Option 3: Using the !! operator throws an exception if the value is null
val msgLength = message!!.length  //here the type of msgLength is inferred as Int
https://kotlinlang.org/docs/null-safety.html#the-operator
https://kotlinlang.org/docs/null-safety.html#safe-calls

## Kotlin Basics
•Kotlin Classes
•Properties
•Null Safety
•Functions
•Constructor and inheritance
•Lambdas

## Functions
https://kotlinlang.org/docs/properties.html
•Kotlin functions are declared using thefunkeyword
•A function is a block of code that performs a specific task
•It can accept arguments and can return a value
•var or val on a function parameter are not allowed
•If a function does not return a value, its return type is Unit
•Unit type is similar to the void type in Java
fun printHello(name: String?) {
## ...
## }
fun printHello(name: String?): Unit {
## ...
return Unit
## }

## Default Parameters
https://kotlinlang.org/docs/properties.html
•Functions can have parameters (default or required)
•If parameters have default values, we can omit them when
calling the function (if we don’t want to change its value)
//Example of a function
fun display(name: String,
surname: String,
age:Int,
isStudying: Boolean = true)
## { ...}
//Example of calling the function
display(“Helen", “Jones", 28)
//calling the display function without providing a value for the last
parameter because it has a default value.
isStudying is a default parameter

## Named Parameters
https://kotlinlang.org/docs/properties.html
•Functions can be called using named arguments.
•When using named arguments, you specify the parameter
name when passing a value.
•When using named arguments, we can change the order of
arguments
fun display(name: String, age: Int) { ... }
display(name = "Alice", age = 20)
display(age = 20, name = "Alice")

## Kotlin Basics
•Kotlin Classes
•Properties
•Null Safety
•Functions
•Constructor and inheritance
•Lambdas

## Primary Constructor
•In Kotlin, you can declare the primary constructor in the
class header
class Person(firstName: String) { /*...*/ }
•The default visibility modifier in Kotlin is public
https://kotlinlang.org/docs/visibility-modifiers.html
https://kotlinlang.org/docs/classes.html#constructors

Primary Constructor and Parameters
•When declaring parameters in the primary
constructor, you can use val or var to make them
class properties accessible within the class.
•If val or var is not used, the parameters are not
accessible directly from the class.
•Use var for mutable properties.
https://kotlinlang.org/docs/classes.html#constructors
class Test (var name:String) {
fun Naming(){
name ="John"
## }
## }
class Test (name:String) {
fun Naming(){
name ="John"
## }
## }

Constructor with Multiple Parameters
•To declare a primary constructor with multiple
parameters, a trailing comma can be used
https://kotlinlang.org/docs/classes.html#constructors
class Person(
val firstName: String,
val lastName: String,
var age: Int)
## { /*...*/ }

## Kotlin – Inheritance
•To make a class inheritable, use the open keyword
•To inherit from a class, the subclass (the derived class) must
include a colon : followed by the base class name and its
constructor
•An example from Android Main Activity:
https://kotlinlang.org/docs/classes.html
class MainActivity : ComponentActivity() {
open class Test  (name:String) {
## }
class TestSub: Test("Hello"){
## }

## Kotlin Basics
•Kotlin Classes
•Properties
•Null Safety
•Functions
•Constructor and inheritance
•Lambdas

Function Type Parameters and Lambdas
•Functions can have parameters of a function type.
•A function-type parameter expects another function as its
argument, rather than a value
•When calling such a function, we commonly provide the
function as a lambda expression.
•A lambda is an anonymous function (a function without a
name) that can be passed directly as an argument to
another function.
•Lambdas are widely used in Kotlin, especially in Compose

// Function with a parameter of function type
fun calculate(num: Int, doubleIt: (Int) -> Int) {
val result = doubleIt(num) // Calling the function passed as an argument return result
## }
// Passing a lambda as an argument
calculate(7, { x: Int -> x * 2 } )
// Using trailing lambda syntax
calculate(7) { x: Int -> x * 2 }

## Higher Order Functions
•A higher-order function can accept functions as
parameters or return a function
•Its second parameter (doubleIt) has a lambda type
(Int) ->Int
•To call the calculate(), we must provide a lambda
expression
•Trailing Lambda: when the lambda is the last
parameter, we can move it out of the parentheses
•When the lambda has one parameter, we can use ‘it’
•You can assign it to a parameter (e.g., doubleIt)
https://kotlinlang.org/docs/lambdas.html#higher-order-functions
fun calculate(num:Int, doubleIt: (Int) -> Int ): Int
## {
val result = doubleIt (num)
return result
## }
val result = calculate( 7, { x:Int -> x * 2} )
val result = calculate(7)
{ x:Int -> x * 2}
val result = calculate(7)
{ it * 2}
val result = calculate(7,
doubleIt= { it * 2}
## )
Declaring the calculate() function
Calling calculate()
## Trailing Lambda
Using the it keyword and
moving it out of parentheses
Using the parameter name, and
including it inside parentheses

The it Keyword
•In the OutlinedTextField composable,
onValueChange is one of the arguments that has a
function/lambda type of (String) -> Unit, and when
calling it, we have provided the lambda expression
of { name = it } as the argument
•The it keyword can be used in a lambda to replace
a single argument that we pass to the lambda
https://kotlinlang.org/docs/lambdas.html#higher-order-functions
OutlinedTextField(
value = name,
onValueChange = { name = it },
label = { Text("Name") },
modifier = Modifier.padding(bottom = 8.dp)
## )
onValueChange = { name = it }
onValueChange = { newName -> name = newName }
onValueChange: (String) -> Unit,

Lists in Kotlin
•A List<T> is used to store items in order and provides indexed
access to them (starting from zero)
•To declare an immutable list that cannot be changed we use listOf()
•To declare a list that its contents can be changed, we use:
mutableListOf()
•We assign a mutable collection/list to a val (not var) because it
protects the reference from modification
val fruits = listOf(“orange", “pear", “apple")
val fruits = mutableListOf(“orange", “pear", “apple")
fruits.remove(“pear")
fruits.add(“mango")
Lists: https://kotlinlang.org/docs/collections-overview.html#list

Additional concepts:
•Arrays: https://kotlinlang.org/docs/arrays.html
•Set:https://kotlinlang.org/docs/collections-overview.html#set
## •map:https://kotlinlang.org/docs/collections-overview.html#map
•Elvis operator to deal with null safety
https://kotlinlang.org/docs/null-safety.html#elvis-operator
•Named arguments/parameters
## •https://kotlinlang.org/docs/functions.html#named-arguments
•not allowed

Identify these parts in this code:
•Class
•Primary constructor and its parameters
•Property (var and val, type)
•Function (its parameters, return value)
•Nullable variable
•Null safety (safe call)
class Calculation (private val num:Int) {
private val inchConverter = 0.393701
fun echoThis(count: Int): Int {
var total = 0
for (i in 1..count) {
total += i
## }
return total
## }
fun convertCMtoInch(): Double {
return num * inchConverter
## }
fun changeToUpperCase(word: String?): String? {
return word?.uppercase()
## }
fun changeToUpperCase1(word: String?): String {
return word!!.uppercase()
## }
fun changeToUpperCase2(word: String?): String {
var result = ""
if (word != null)
result = word.uppercase()
return result
## }
fun wordLength(word: String?): Int {
return word!!.length
## }
fun calculate(doubleIt: (Int) -> Int ): Int
## {
val result = doubleIt (num)
return result
## }
## }

What will this print?
class MainActivity : ComponentActivity() {
override fun onCreate(savedInstanceState: Bundle?) {
super.onCreate(savedInstanceState)
//creating an instance of Calculation class
val calculator = Calculation(7)
//calling its functions and printing them to Logcat
val result = calculator.calculate { it * 2 }
println("lambda double function: $result")
val result2 = calculator.changeToUpperCase("hello")
println("Change to uppercase function: $result2")
val result3 = calculator.wordLength("hello")
println("Word length function: $result3")
val result4 = calculator.echoThis(5)
println("Counter function: $result4")
## ...
## }