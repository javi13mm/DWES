package com.example.myothercatalog;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;

import com.bumptech.glide.Glide;

public class DetailActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detail);

        Intent intent = getIntent();

        String name = intent.getStringExtra("name");
        String descripcion = intent.getStringExtra("description");
        String url = intent.getStringExtra("image_url");

        TextView title = findViewById(R.id.title);
        title.setText(name);
        ImageView image = findViewById(R.id.image);
        TextView description = findViewById(R.id.description);
        description.setText(descripcion);

        Glide.with(this)
                .load(url)
                //Placeholder que muestra una imagen mientras cargan las imágenes del json
                .placeholder(R.drawable.ic_launcher_background)
                //Error que muestra una imágen ante un error en la carga de las imágenes del json
                .error(R.drawable.ic_launcher_foreground)
                .into(image);
    }
}