extends AnimatedSprite2D

signal shot_already
signal shot
signal reloaded

var emited = false

# Called when the node enters the scene tree for the first time.
func _ready():
	animation = "shooting"
	frame = 0


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	if animation == "shooting" and 2 <= frame and frame <= 4 and not emited:
		emited = true
		emit_signal("shot_already")
	elif animation == "reload":
		if not flip_v:
			if frame == 1:
				rotation_degrees = 30
			elif frame == 2:
				rotation_degrees = 60
			elif frame == 3:
				rotation_degrees = 90
			elif frame == 4:
				rotation_degrees = 120
			elif frame == 9:
				rotation_degrees = 90
			elif frame == 10:
				rotation_degrees = 60
			elif frame == 11:
				rotation_degrees = 30
			elif frame == 12:
				rotation_degrees = 0
		else:
			if frame == 1:
				rotation_degrees = 150
			elif frame == 2:
				rotation_degrees = 120
			elif frame == 3:
				rotation_degrees = 90
			elif frame == 4:
				rotation_degrees = 60
			elif frame == 9:
				rotation_degrees = 90
			elif frame == 10:
				rotation_degrees = 120
			elif frame == 11:
				rotation_degrees = 150
			elif frame == 12:
				rotation_degrees = 180


func _on_animation_finished():
	if animation == "shooting":
		emited = false
		play("recoil")
	elif animation == "recoil":
		emit_signal("shot")
	elif animation == "reload":
		emit_signal("reloaded")
		animation = "shooting"
		frame = 0
