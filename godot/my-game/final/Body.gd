extends AnimatedSprite2D

var kick_power_up = false

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	kick_power_up = get_parent().kick_power_up
	if animation == "kick" and frame > 2 and frame < 7:
		if get_parent().get_parent():
			if  $KickAim.is_colliding() and $KickAim.get_collider().name.begins_with("Zombie"):
				$KickAim.get_collider().kicked(kick_power_up)
			elif $KickAim.is_colliding() and $KickAim.get_collider().name.begins_with("Interruptor"):
				$KickAim.get_collider().kicked()
			elif $KickAim.is_colliding() and $KickAim.get_collider().name.begins_with("Door"):
				$KickAim.get_collider().kicked()
	elif animation == "run" and (frame == 4 or frame == 9) and not $FootstepSound.is_playing():
		$FootstepSound.play()
