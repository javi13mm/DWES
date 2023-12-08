extends Node2D

var score_dir = "save/score.json"
var nick = ""
var score = 0

var file_dir = "save/settings.json"
var difficulty = JSON.parse_string(FileAccess.get_file_as_string(file_dir)).difficulty

# Called when the node enters the scene tree for the first time.
func _ready():
	for hijo in get_children():
		if hijo.name == "Elevator":
			hijo.find_child("Interruptor").move_up = true
			hijo.find_child("Interruptor").up_limit = 442
			hijo.find_child("Interruptor").down_limit = hijo.position.y
			hijo.find_child("Interruptor").speed = 5
		if difficulty == 1:
			if hijo.name.begins_with("Zombie"):
				hijo.SPEED = 390
				hijo.health = 30


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	$Camera.position = $Cowboy.position
	if find_child("Cowboy").dead and $DeathTimer.is_stopped():
		$DeathTimer.start()
	elif $Meta.finish_level:
		save_score()
		get_tree().change_scene_to_file("res://level_2.tscn")


func _on_death_timer_timeout():
	get_tree().change_scene_to_file("res://you_lose.tscn")

func save_score():
	var file = FileAccess.open(score_dir, 1)
	var file_content = FileAccess.get_file_as_string(score_dir)
	var json = JSON.parse_string(file_content)
	nick = json.name
	score += json.score
	file.close()
	
	if difficulty == 1:
		score += find_child("Cowboy").health * 2
	else:
		score += find_child("Cowboy").health
	
	file = FileAccess.open(score_dir, 2)
	file.store_line("{\"name\":\""+nick+"\",\"score\":"+str(score)+"}")
	file.close()
