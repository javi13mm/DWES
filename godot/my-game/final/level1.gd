extends Node2D


# Called when the node enters the scene tree for the first time.
func _ready():
	for hijo in get_children():
		if hijo.name == "Elevator":
			hijo.find_child("Interruptor").move_up = true
			hijo.find_child("Interruptor").up_limit = 442
			hijo.find_child("Interruptor").down_limit = hijo.position.y
			hijo.find_child("Interruptor").speed = 5


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
