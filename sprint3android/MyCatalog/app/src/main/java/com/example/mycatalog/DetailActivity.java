package com.example.mycatalog;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.res.Configuration;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class DetailActivity extends AppCompatActivity {
    private Button button;
    private int likeCount;
    private Bundle bundle = new Bundle();
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        // Recogemos los datos del Bundle asociado al iniciar la DetailActivity
        // en un Bundle privado.
        bundle = getIntent().getExtras();

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detail);

        button = findViewById(R.id.buttonLike);
        // Guardamos el número de likes del Bundle en una variable privada
        likeCount = Integer.parseInt(String.valueOf(bundle.get("likes")));
        // Si ya se le dió un like al menos anteriormente, debemos actualizarlo en el botón:
        if(likeCount != 0)
            button.setText(likeCount+"🤍");

        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // Y con cada click, un like más:
                likeCount += 1;
                // Actualizamos el Bundle de likes privado
                bundle.putInt("likes",likeCount);
                // Actualizamos los likes que muestra el botón
                button.setText(likeCount+"🤍");
            }
        });
    }

    // Ante cambios en la orientación de la pantalla, manejamos el reinicio de la DetailActivity
    // manualmente para que siga mostrando correctamente el número de likes, enviándole
    // un Bundle de cada vez.
    @Override
    public void onConfigurationChanged(@NonNull Configuration newConfig) {
        super.onConfigurationChanged(newConfig);

        // Reinicio de la DetailActivity desde sí misma
        Intent intentDetailActivity = new Intent(DetailActivity.this, DetailActivity.class);
        // Volvemos a enviarle el Bundle de likes actualizado cada vez que se reinicia la actividad
        intentDetailActivity.putExtras(bundle);
        // Finalizamos la actividad para volver a abrirla
        finish();
        startActivity(intentDetailActivity);
    }
}