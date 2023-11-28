extends CharacterBody2D


var SPEED = 170
var GRAVITY = 980

var direction = 0
var last_direction = 0
var dead = false
var detection_distance = 400
var detected_cowboy = false

var health = 3
var goto = 0
var reached_goto = false

func _ready():
	SPEED *= abs(scale.x)
	GRAVITY *= scale.y
	goto = position.x

func _physics_process(delta):
	if not is_on_floor():
		velocity.y += GRAVITY * delta

	if not dead:
		var cowboy_relative_pos = 0
		if get_parent().find_child("Cowboy"):
			cowboy_relative_pos = get_parent().find_child("Cowboy").position - position
			if (cowboy_relative_pos.x > 10 or cowboy_relative_pos.x < -10) and cowboy_relative_pos.length() <= detection_distance:
				$ZombieBodyAim.target_position = cowboy_relative_pos
			if $ZombieBodyAim.is_colliding() and $ZombieBodyAim.get_collider().name.begins_with("Cowboy"):
				goto = get_parent().find_child("Cowboy").position.x
			if goto < position.x-50:
				detected_cowboy = true
				direction = -1
				last_direction = direction
				reached_goto = false
				if is_on_wall():
					goto = position.x
			elif goto > position.x+50:
				detected_cowboy = true
				direction = 1
				last_direction = direction
				reached_goto = false
				if is_on_wall():
					goto = position.x
			else:
				detected_cowboy = false
				direction = 0
				reached_goto = true

		if detected_cowboy:
			if is_on_floor():
				velocity.x = move_toward(velocity.x, SPEED * direction, SPEED * delta)
			if is_on_floor() and (sign(direction) != sign(velocity.x)) or reached_goto:
				velocity.x = move_toward(velocity.x, 0, SPEED * delta)

		# ANIMACIONES
			if direction == -1:
				$Body.speed_scale = move_toward(0.4, 1, abs(velocity.x / SPEED))
				$Body.set_flip_h(true)
				$ZombieAim.set_draw_behind_parent(true)
				$ZombieAim/ZombieArm1.set_flip_v(true)
				$ZombieAim2.set_draw_behind_parent(false)
				$ZombieAim2/ZombieArm2.set_flip_v(true)
				$Body.play("run")
			elif direction == 1:
				$Body.speed_scale = move_toward(0.4, 1, abs(velocity.x / SPEED))
				$Body.set_flip_h(false)
				$ZombieAim.set_draw_behind_parent(false)
				$ZombieAim/ZombieArm1.set_flip_v(false)
				$ZombieAim2.set_draw_behind_parent(true)
				$ZombieAim2/ZombieArm2.set_flip_v(false)
				$Body.play("run")
			else:
				$Body.play("stand")
				velocity.x = move_toward(velocity.x, 0, SPEED * delta)
		else:
			$Body.play("stand")
			velocity.x = move_toward(velocity.x, 0, SPEED * delta)
	else:
		velocity.x = move_toward(velocity.x, 0, SPEED * delta)
		set_collision_layer_value(3, false)
		set_collision_mask_value(2, false)
	
	move_and_slide()

func place_blood(pos):
	$Blood.position.y = pos.y
	if pos.x > 0:
		$Blood.set_flip_h(false)
		$Blood.position.x = -5
	else:
		$Blood.set_flip_h(true)
		$Blood.position.x = 5

func kicked():
	print(true)
	velocity.x = -250 * last_direction

func death():
	health -= 1
	$Blood.stop()
	$Blood.play("blood")
	if health == 0:
		$ZombieAim/ZombieArm1.hide()
		$ZombieAim2/ZombieArm2.hide()
		dead = true
		if last_direction == -1:
			$Body.play("death")
			$Body.set_flip_h(false)
		else:
			$Body.play("death")
			$Body.set_flip_h(true)
