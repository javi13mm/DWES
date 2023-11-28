extends RayCast2D

var angle = 0

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	if not get_parent().dead:
		if get_parent().get_parent():
			var cowboy_pos = get_parent().get_parent().find_child("Cowboy").position
			target_position = cowboy_pos - get_parent().position
			if target_position.x > 25:
				target_position.x = 25
			elif target_position.x < -25:
				target_position.x = -25
			if target_position.y < -18:
				target_position.y = -18
			elif target_position.y > 18:
				target_position.y = 18
			target_position *= target_position.normalized()
			
			if is_colliding() and get_collider().name.begins_with("Cowboy"):
				angle = get_angle_to(cowboy_pos + position*get_parent().scale)*180/PI
				$ZombieArm2.rotation_degrees = angle
				$ZombieArm2.angle_rotation()
			else:
				if get_parent().find_child("Body").animation == "stand":
					angle = 90
				else:
					angle = get_angle_to(cowboy_pos + position*get_parent().scale)*180/PI
				$ZombieArm2.rotation_degrees = angle
