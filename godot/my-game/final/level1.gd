extends Node2D

var scale_relation = 1.5

# Called when the node enters the scene tree for the first time.
func _ready():
	$Cowboy.scale *= scale_relation
	$Zombie.scale *= scale_relation
	$Zombie2.scale *= scale_relation


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass

func relation():
	return scale_relation
