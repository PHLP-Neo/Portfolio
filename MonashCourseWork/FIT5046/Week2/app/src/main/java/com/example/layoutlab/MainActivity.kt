package com.example.layoutlab

import android.os.Bundle
import android.provider.CalendarContract
import android.widget.Toast
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.ElevatedButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.blur
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.Shape
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.style.LineHeightStyle
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.example.layoutlab.ui.theme.LayoutLabTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            LayoutLabTheme {
                Scaffold(modifier = Modifier.fillMaxSize()) { innerPadding ->
//                    ColumnLayoutComposable(
//                        modifier = Modifier.padding(innerPadding)
//                    )
                    LeafCompose(
                        modifier = Modifier.padding(innerPadding)
                    )


                }
            }
        }
    }
}

@Composable
fun Greeting(name: String, modifier: Modifier = Modifier) {
    Text(
        text = "Hello $name!",
        modifier = modifier
    )
}

@Composable
fun ColumnLayoutComposable(modifier: Modifier = Modifier){
    Surface (color = MaterialTheme.colorScheme.primary){
        Column(modifier = modifier.padding(24.dp)) {
            Text(text = "Spring")
            Text(text = "Summer")
            Text(text = "Autumn")
            Text(text = "Winter")
        }
    }
}

@Composable
fun ButtonCompose(modifier: Modifier){
    val context = LocalContext.current
    Box(Modifier.fillMaxSize(),
        contentAlignment = Alignment.Center) {
        Surface(color = MaterialTheme.colorScheme.primary) {
            Column(modifier = modifier.padding(24.dp),
                horizontalAlignment = Alignment.CenterHorizontally) {
                Text(text = "Spring")
                Text(text = "Summer")
                Text(text = "Autumn")
                Text(text = "Winter")
                Spacer(modifier = Modifier.height(20.dp))
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

@Composable
fun LeafCompose(modifier: Modifier){
    val context = LocalContext.current
    val seasons = listOf("Spring", "Summer", "Autumn", "Winter")
    Box(Modifier.fillMaxSize(),
        contentAlignment = Alignment.Center) {
        //Surface(color = MaterialTheme.colorScheme.primary) {
            Column(modifier = modifier.padding(24.dp),
                horizontalAlignment = Alignment.CenterHorizontally) {
//
//                Text(
//                    text = "Seasons and Months",
//                    modifier = Modifier
//                        .background(Color.Blue)
//                        .border(
//                            width = 1.dp,
//                            shape = RoundedCornerShape(12.dp, 12.dp, 12.dp, 12.dp),
//                            color = Color.Red
//                        ),
//                )

                Text(
                    text = "Seasons and Months",
                    color = Color.White,
                    modifier = Modifier
                        .background(
                            color = Color.Blue,
                            shape = RoundedCornerShape(12.dp)
                        )
                        .padding(horizontal = 16.dp, vertical = 8.dp)
                )
                Spacer(modifier = Modifier.height(20.dp))
                //I need to add picture here?
                Image(
                    painter = painterResource(R.drawable.seasons),
                    contentDescription = "My image",
                    modifier = Modifier.fillMaxWidth(0.8f),
                    contentScale = ContentScale.FillWidth
                )
                // I need to add a row of button here
                Spacer(modifier = Modifier.height(20.dp))
                Row(modifier = modifier.fillMaxWidth(),
                    horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                    seasons.forEach { season ->
                        ElevatedButton(
                            onClick = {
                                Toast.makeText(
                                    context,
                                    season,
                                    Toast.LENGTH_SHORT
                                ).show()
                            },
                            modifier = Modifier
                                .weight(1f)
                                .height(48.dp),
                            contentPadding = PaddingValues(horizontal = 4.dp)
                        ) {
                            Text(
                                text = season,
                                fontSize = 12.sp,
                                maxLines = 1
                            )
                        }
                    }
                }

                //
//                Text(text = "Summer")
//                Text(text = "Autumn")
//                Text(text = "Winter")
//                Spacer(modifier = Modifier.height(20.dp))
//                ElevatedButton(
//                    onClick = {
//                        Toast.makeText(
//                            context,
//                            "This is a Toast",
//                            Toast.LENGTH_SHORT
//                        ).show()
//                    }
//                ) {
//                    Text("Click")
//                }
            }
        //}
    }
}

@Composable
fun RowLayoutComposable(modifier: Modifier = Modifier){
    Surface (color = MaterialTheme.colorScheme.primary){
        Row(modifier = modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.SpaceBetween) {
            Text(text = "Spring")
            Text(text = "Summer")
            Text(text = "Autumn")
            Text(text = "Winter")
            
        }
    }
}

@Preview(showBackground = true)
@Composable
fun GreetingPreview() {
    LayoutLabTheme {
        Scaffold(modifier = Modifier.fillMaxSize()) { innerPadding ->
            ColumnLayoutComposable(
                modifier = Modifier.padding(innerPadding)
            )
        }
    }
}