package com.example.mycatalog;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class DetailActivity extends AppCompatActivity {
    private Button button;
    private int like_count;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detail);

        button = findViewById(R.id.buttonLike);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                like_count += 1;
                button.setText(String.valueOf(like_count)+"🤍");
            }
        });
    }
}