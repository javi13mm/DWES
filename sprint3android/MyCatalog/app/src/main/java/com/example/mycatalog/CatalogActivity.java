package com.example.mycatalog;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class CatalogActivity extends AppCompatActivity {
    private Button button;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_catalog);

        button = findViewById(R.id.buttonGoToDetail);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // Intent y startActivity que inicializan la actividad de DetailActivity,
                // al pulsar el botón de la pantalla CatalogActivity.
                Intent intentDetailActivity = new Intent(CatalogActivity.this,DetailActivity.class);
                startActivity(intentDetailActivity);
            }
        });
    }
}