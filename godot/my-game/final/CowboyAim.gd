extends RayCast2D

var other_arm_already_shot = true
var other_arm_finished_reload = true
var finished_shot = true
var finished_reload = true
var bullets = 6

signal reloading

func _ready():
	pass


func _process(delta):
	
	target_position = get_local_mouse_position() * 1000
	
	$Pointer.position = get_local_mouse_position()
	

	if finished_shot and (bullets < 1 or Input.is_action_just_pressed("reload") and bullets < 6):
		finished_reload = false
		$Arm.play("reload")
		bullets = 6
		if not $ReloadSound.is_playing():
			$ReloadSound.play()
			emit_signal("reloading")
	
	if finished_reload:
		var angle = get_angle_to(get_local_mouse_position() + (get_parent().position) + position*get_parent().scale)*180/PI
		$Arm.rotation_degrees = angle
		
		if Input.is_action_just_pressed("mouse_left") and finished_shot and bullets > 0:
			if other_arm_already_shot or not other_arm_finished_reload:
				bullets -= 1
				$Arm.play("shooting")
				$ShotSound.play()
				other_arm_already_shot = false
				finished_shot = false
				if is_colliding() and get_collider().name.begins_with("Zombie"):
					var placement = (get_collision_point() - get_collider().position)/get_parent().scale
					get_collider().place_blood(placement)
					get_collider().death()

func _on_arm_2_shot_already():
	other_arm_already_shot = true


func _on_arm_shot():
	finished_shot = true


func _on_arm_reloaded():
	finished_shot = true
	finished_reload = true


func _on_arm_2_reloaded():
	other_arm_finished_reload = true


func _on_cowboy_aim_2_reloading():
	other_arm_finished_reload = false
