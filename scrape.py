from youtube_comment_downloader import YoutubeCommentDownloader

# Initialize the downloader
downloader = YoutubeCommentDownloader()

def scrape_comments(youtube_id):
    comments = downloader.get_comments(youtube_id)
    
    store_comments = []
    total_comments=0
    for comment in comments:
        store_comments.append(comment['text'])
        print(comment['text'])
        total_comments+=1
    
    print("Total comments: ", total_comments)
    return store_comments

if __name__ == "__main__":
    youtube_id = input("Enter the YouTube video ID: ")
    comments = scrape_comments(youtube_id)
    with open('comments.txt', 'w', encoding='utf-8') as f:
        for comment in comments:
            f.write(comment + "\n")
