extends Control

var file_dir = "save/score.json"
var nick = ""

# Called when the node enters the scene tree for the first time.
func _ready():
	$EditNick.grab_focus()
	


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass

func set_initial_score():
	var file = FileAccess.open(file_dir, 2)
	var file_content = FileAccess.get_file_as_string(file_dir)
	file.store_line("{\"name\":\""+nick+"\",\"score\":0}")
	file.close()


func _on_accept_pressed():
	if $EditNick.text.length() > 0:
		nick = $EditNick.text
		set_initial_score()
		get_tree().change_scene_to_file("res://Level1.tscn")
