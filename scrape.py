from youtube_comment_downloader import YoutubeCommentDownloader

# Initialize the downloader
downloader = YoutubeCommentDownloader()

# Get comments for the specified YouTube video ID
youtube_id = input("Enter the YouTube video ID: ")
comments = downloader.get_comments(youtube_id)

# Print each comment text

store_comments = []
for comment in comments:
    store_comments.append(comment.text)
    print(comment.text)
