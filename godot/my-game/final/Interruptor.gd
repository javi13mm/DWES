extends AnimatableBody2D

var move_up = false

var speed = 0

var up_limit = 0
var down_limit = 0

var kick = false

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	if kick:
		if move_up:
			if get_parent().position.y <= up_limit:
				move_up = false
				kick = false
				get_parent().get_child(1).hide()
			else:
				get_parent().position.y -= speed
				position.y -= speed
				get_parent().get_child(1).show()
		else:
			if get_parent().position.y >= down_limit:
				move_up = true
				kick = false
				get_parent().get_child(1).hide()
			else:
				get_parent().position.y += speed
				position.y += speed
				get_parent().get_child(1).show()

func kicked():
	if not kick:
		kick = true
