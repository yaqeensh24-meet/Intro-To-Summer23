def creat_youtube_video(title,description):
	video={
	"title":title,
	"description":description,
	"likes":0,
	"dislike":0,
	"comments":{},
	}
	return video

def like (video):
	if "likes" in video:
		video["likes"] += 1
		return video

def dislike (video):
	if "dislike" in video:
		video["dislike"]+=1
	return video

def add_comment (video,username,comment_text):
	video['comments'][username] = comment_text
	return video

x=creat_youtube_video("how to cook pasta","learning video")
i=1
while i<=495:
	like(x)
	i+=1

print(x)






