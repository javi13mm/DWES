extends CharacterBody2D

var SPEED = 250
var JUMP_VELOCITY = -400
var GRAVITY = 950

var already_kicked = true
var direction

var health = 1000
var dead = false

var scale_relation = 1

func _ready():
	Input.set_mouse_mode(Input.MOUSE_MODE_HIDDEN)
	$Body.play("stand")
	
	scale = Vector2(1.5,1.5)
	
	SPEED *= scale.x
	JUMP_VELOCITY *= scale.x
	GRAVITY *= scale.x


func _physics_process(delta):
	if $HurtTimer.is_stopped():
		$HurtSound.stop()
# FÍSICAS
	velocity.y += GRAVITY * delta
	if not dead:
		direction = Input.get_axis("left", "right")
		if is_on_floor():
			velocity.x = move_toward(velocity.x, SPEED * direction, SPEED * delta)
		else:
			velocity.x = move_toward(velocity.x, SPEED * direction, SPEED * 0.6 * delta)
		
		if is_on_floor():
			if direction != 0 and (sign(direction) != sign(velocity.x)):
				velocity.x = move_toward(velocity.x, 0, SPEED * 4 * delta)
			elif direction == 0:
				velocity.x = move_toward(velocity.x, 0, SPEED * 2 * delta)
		else:
			if (sign(direction) != sign(velocity.x)):
				velocity.x = move_toward(velocity.x, 0, SPEED * 0.25 * delta)

		if Input.is_action_just_pressed("jump") and is_on_floor():
			velocity.y = JUMP_VELOCITY

# ANIMACIONES
		if (get_local_mouse_position().x) < 0:
			$CowboyAim.set_draw_behind_parent(true)
			$CowboyAim/Arm.set_flip_v(true)
			$CowboyAim2.set_draw_behind_parent(false)
			$CowboyAim2/Arm2.set_flip_v(true)
			$Body.set_flip_h(true)
			$Body/KickAim.target_position.x = -20
		else:
			$CowboyAim.set_draw_behind_parent(false)
			$CowboyAim/Arm.set_flip_v(false)
			$CowboyAim2.set_draw_behind_parent(true)
			$CowboyAim2/Arm2.set_flip_v(false)
			$Body.set_flip_h(false)
			$Body/KickAim.target_position.x = 20

		if is_on_floor() and Input.is_action_just_pressed("kick"):
			$Body.play("kick")
			already_kicked = false
		if already_kicked:
			if direction == -1:
				if (get_local_mouse_position().x) > 0:
					if is_on_floor():
						$Body.play_backwards("run")
					else:
						$Body.play_backwards("jump")
				else:
					if is_on_floor():
						$Body.play("run")
					else:
						$Body.play("jump")
			elif direction == 1:
				if (get_local_mouse_position().x) < 0:
					if is_on_floor():
						$Body.play_backwards("run")
					else:
						$Body.play_backwards("jump")
				else:
					if is_on_floor():
						$Body.play("run")
					else:
						$Body.play("jump")
			else:
				if is_on_floor():
					$Body.play("stand")
				else:
					$Body.play("jump")
			
			if $Body.animation == "jump":
				if velocity.x >= 0 and (get_local_mouse_position().x) > 0:
					if velocity.y < 0:
						$Body.set_frame(0)
					else:
						$Body.set_frame(1)
				elif velocity.x >= 0 and (get_local_mouse_position().x) < 0:
					if velocity.y < 0:
						$Body.set_frame(1)
					else:
						$Body.set_frame(0)
				elif velocity.x <= 0 and (get_local_mouse_position().x) > 0:
					if velocity.y < 0:
						$Body.set_frame(1)
					else:
						$Body.set_frame(0)
				else:
					if velocity.y < 0:
						$Body.set_frame(0)
					else:
						$Body.set_frame(1)
			elif $Body.animation == "run":
				$Body.speed_scale = move_toward(0.4, 1, abs(velocity.x / SPEED))
	else:
		velocity.x = move_toward(velocity.x, 0, SPEED * delta)
		set_collision_layer_value(2, false)
		set_collision_mask_value(3, false)
	move_and_slide()

func death():
	if health > 0:
		health -= 1
		if not $HurtSound.is_playing():
			#var secs = randi_range()
			var secs = 1.0 + 2.5 * randi_range(0, 6)
			$HurtSound.play(secs)
			$HurtTimer.start()
	if health == 0:
		$HurtSound.stop()
		$DeathSound.play()
		$Body.play("death")
		$CowboyAim/Arm.hide()
		$CowboyAim2/Arm2.hide()
		dead = true

func _on_body_animation_finished():
	if $Body.animation == "kick":
		already_kicked = true
