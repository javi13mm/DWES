extends Area2D

var finish_level = false

# Called when the node enters the scene tree for the first time.
func _ready():
	pass

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass 


func _on_body_entered(body):
	finish_level = true