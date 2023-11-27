package com.example.myothercatalog;

import android.app.Activity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class RecyclerViewAdapter extends RecyclerView.Adapter<ViewHolder> {
    private List<Tenista> listaTenistas;
    private Activity activity;

    public RecyclerViewAdapter(List<Tenista> dataSet, Activity activity) {
        this.listaTenistas = dataSet;
        this.activity = activity;
    }

    //Método para inflar los ViewHolders o celdas
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.view_holder, parent, false);
        return new ViewHolder(view);
    }

    //Método que asigna datos a las celdas
    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
        Tenista dataPositionToBeRendered = listaTenistas.get(position);
        holder.showData(dataPositionToBeRendered, activity);
    }

    //Método que indica el número de celdas
    public int getItemCount() {
        return listaTenistas.size();
    }
}
