package com.example.myothercatalog;

import org.json.JSONException;
import org.json.JSONObject;

public class Tenista {
    private String name;
    private String description;
    private String imageUrl;

    public String getName() {return this.name;}
    public String getDescription() {return this.description;}
    public String getImageUrl() {return this.imageUrl;}

    public Tenista(String name, String description, String imageUrl) {
        this.name = name;
        this.description = description;
        this.imageUrl = imageUrl;
    }

    public Tenista(JSONObject json){
        try{
            this.name = json.getString("name");
            this.description = json.getString("description");
            this.imageUrl = json.getString("image_url");
        }catch (JSONException e){ e.printStackTrace(); }
    }
}
