extends Node2D

var file_dir = "save/settings.json"
var difficulty = JSON.parse_string(FileAccess.get_file_as_string(file_dir)).difficulty

# Called when the node enters the scene tree for the first time.
func _ready():
	for hijo in get_children():
		if hijo.name == "Elevator":
			hijo.find_child("Interruptor").move_up = true
			hijo.find_child("Interruptor").up_limit = 442
			hijo.find_child("Interruptor").down_limit = hijo.position.y
			hijo.find_child("Interruptor").speed = 5
		if difficulty == 1:
			if hijo.name.begins_with("Zombie"):
				hijo.SPEED = 390
				hijo.health = 30


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	$Camera.position = $Cowboy.position
	if $Meta.finish_level:
		get_tree().change_scene_to_file("res://menu.tscn")
