extends Control

var score_dir = "save/score.json"
var nick = ""
var score = 0
# Called when the node enters the scene tree for the first time.
func _ready():
	set_score()
	$WinLabel.text += "\nNICK: "+nick+"\nSCORE: "+str(score)
	send_post_new_score()
	$BackToMenu.grab_focus()


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass


func _on_back_to_menu_pressed():
	get_tree().change_scene_to_file("res://menu.tscn")

func set_score():
	var file = FileAccess.open(score_dir, 1)
	var file_content = FileAccess.get_file_as_string(score_dir)
	var json = JSON.parse_string(file_content)
	nick = json.name
	score = json.score
	file.close()

func send_post_new_score():
	var http_request = HTTPRequest.new()
	add_child(http_request)
	http_request.request_completed
	http_request.connect("request_completed",_on_server_has_responded)
	var body = {"name":nick,"score":score}
	body = JSON.stringify(body)
	http_request.request("http://127.0.0.1:8000/scorecza",
						PackedStringArray(["Content-Type: application/json", "Client-Secret: abc"]),
						HTTPClient.METHOD_POST,
						body)

func _on_server_has_responded(result, response_code, headers, body):
	var response = JSON.parse_string(body.get_string_from_utf8())
