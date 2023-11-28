extends AnimatedSprite2D


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	if animation == "kick" and frame > 2 and frame < 7:
		if get_parent().get_parent():
			if  $KickAim.is_colliding() and $KickAim.get_collider().name.begins_with("Zombie"):
				$KickAim.get_collider().kicked()
