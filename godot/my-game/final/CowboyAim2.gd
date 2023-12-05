extends RayCast2D

var other_arm_already_shot = false
var other_arm_finished_reload = true
var finished_shot = true
var finished_reload = true
var bullets = 6

signal reloading

func _ready():
	pass


func _process(delta):
	target_position = get_local_mouse_position() * 1000

	if not get_parent().dead:
		if finished_shot and (bullets < 1 or Input.is_action_just_pressed("reload") and bullets < 6):
			finished_reload = false
			$Arm2.play("reload")
			bullets = 6
			if not $ReloadSound2.is_playing():
				$ReloadSound2.play()
				emit_signal("reloading")
		
		if finished_reload:
			var angle = get_angle_to(get_local_mouse_position() + (get_parent().position) + position*get_parent().scale)*180/PI
			$Arm2.rotation_degrees = angle
			if Input.is_action_just_pressed("mouse_left") and finished_shot and bullets > 0:
				if other_arm_already_shot or not other_arm_finished_reload:
					bullets -= 1
					$Arm2.play("shooting")
					$ShotSound2.play()
					other_arm_already_shot = false
					finished_shot = false
					if is_colliding() and get_collider().name.begins_with("Zombie"):
						var placement = (get_collision_point() - get_collider().position)/get_parent().scale
						get_collider().place_blood(placement, get_parent().position.x)
						get_collider().death()


func _on_arm_1_shot_already():
	other_arm_already_shot = true


func _on_arm_2_shot():
	finished_shot = true


func _on_arm_2_reloaded():
	finished_shot = true
	finished_reload = true


func _on_arm_reloaded():
	other_arm_finished_reload = true


func _on_cowboy_aim_reloading():
	other_arm_finished_reload = false
