package com.example.myothercatalog;

import android.app.Activity;
import android.content.Intent;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;

public class ViewHolder extends RecyclerView.ViewHolder {
    private final TextView name;
    private final ImageView image;
    private Button button;

    //ViewHolder que adquiere los elementos de view_holder.xml y actúa como celda
    public ViewHolder(@NonNull View itemView) {
        super(itemView);
        name = (TextView) itemView.findViewById(R.id.tenista_text_view);
        image = (ImageView) itemView.findViewById(R.id.tenista_image_view);
        button = (Button) itemView.findViewById(R.id.tenista_button);
    }

    //Función que asigna datos a las celdas ViewHolder
    public void showData(Tenista data, Activity activity) {
        name.setText(data.getName());
        Glide.with(itemView.getContext())
                .load(data.getImageUrl())
                //Placeholder que muestra una imagen mientras cargan las imágenes del json
                .placeholder(R.drawable.ic_launcher_background)
                //Error que muestra una imágen ante un error en la carga de las imágenes del json
                .error(R.drawable.ic_launcher_foreground)
                .circleCrop()
                .into(image);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                //Al clickar el botón, se lanza la DetailActivity
                Intent intentDetailActivity = new Intent(view.getContext(), DetailActivity.class);
                view.getContext().startActivity(intentDetailActivity);
            }
        });
    }
}
